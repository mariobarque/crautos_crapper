import requests
from bs4 import BeautifulSoup
from car import Car
from constants import Constants
from helper import Helper


class CarParser:

    @staticmethod
    def get_attribute_value(content, index, colspan = 1):
        attribute = ''
        if colspan > 1:
            if len(content) > index and len(content[index]) > 1 and len(content[index].contents[1]) > 0:
                attribute = content[index].contents[1].contents[0]
        else:
            if len(content) > index and len(content[index]) > 3 and len(content[index].contents[3]) > 0:
                attribute = content[index].contents[3].contents[0]

        return attribute.strip().replace('"', '').replace("'", "")


    @staticmethod
    def categorize_kilometraje(kilometraje):
        if kilometraje < 20000:
            return "<20K"
        elif kilometraje < 50000:
            return "20K-50K"
        elif kilometraje < 100000:
            return "50K-100K"
        elif kilometraje < 200000:
            return "100K-200K"
        elif kilometraje < 500000:
            return "200K-500K"
        else:
            return ">500K"

    @staticmethod
    def categorize_anno(anno):
        if anno > 2018:
            return "Como Nuevo"
        elif anno > 2010:
            return "Moderno"
        elif anno > 2000:
            return "Regular"
        elif anno > 1900:
            return "Viejo"
        else:
            return "Muy viejo"


    def has_image(soup):
        images_table = soup.find_all('table', attrs={'class':'table-responsive table-striped table-bordered'})
        no_image = '/rimages/nopiclg.jpg'
        first_image = images_table[0].contents[3].contents[1].contents[1].attrs['src']
        if no_image == first_image:
            return "No"
        else:
            return "Si"

    @staticmethod
    def parse_car(car_id):
        try:
            url = Constants.base_car_url + str(car_id)
            response = requests.request("GET", url)
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find_all('table', attrs={'class':'technical table-striped'})
            contents = table[0].contents[3].contents

            cilindrada = CarParser.get_attribute_value(contents, 1)
            estilo = CarParser.get_attribute_value(contents, 3)
            combustible = CarParser.get_attribute_value(contents, 5)
            transmision = CarParser.get_attribute_value(contents, 7)
            estado = CarParser.get_attribute_value(contents, 9)
            kilometraje = CarParser.get_attribute_value(contents, 11)
            puertas = CarParser.get_attribute_value(contents, 19)
            pagoImpuesto = CarParser.get_attribute_value(contents, 21)
            negociable = CarParser.get_attribute_value(contents, 23)
            recibeVehiculo = CarParser.get_attribute_value(contents, 25)
            fechaIngreso = CarParser.get_attribute_value(contents, 29)
            vecesVisto = CarParser.get_attribute_value(contents, 31, colspan=2)
            comentario = CarParser.get_attribute_value(contents, 33, colspan=2)

            price_div = soup.find('div', attrs={'class':'col-lg-4 col-md-4 col-sm-4 text-right'})
            price = price_div.contents[1].contents[0]
            price = price.strip()

            marca_modelo_anno_dif = soup.find('div', attrs={'class': 'col-lg-8 col-md-8 col-sm-8 col-xs-12'})
            marca_modelo = marca_modelo_anno_dif.contents[1].contents[0].strip()
            anno = marca_modelo_anno_dif.contents[1].contents[2].strip()

            marca = marca_modelo.partition(' ')[0].strip()
            modelo = marca_modelo.replace(marca, '').strip()

            kilometraje = Helper.remove_non_numeric_values(kilometraje)
            vecesVisto = Helper.remove_non_numeric_values(vecesVisto)
            anno = Helper.remove_non_numeric_values(anno)

            price = Helper.remove_non_numeric_values(price)
            if price == "":
                return None
            elif price < 200000:
                return None
            
            if modelo is None:
                return None

            if kilometraje == "":
                return None

            kilometraje = CarParser.categorize_kilometraje(kilometraje)
            anno_categoria = CarParser.categorize_anno(anno)

            tiene_imagen = CarParser.has_image(soup)

            car = Car(car_id, marca, modelo, anno, anno_categoria, cilindrada, estilo, combustible, transmision, estado, kilometraje,
                      puertas, pagoImpuesto, negociable, recibeVehiculo, fechaIngreso, vecesVisto, comentario, tiene_imagen, price)

            return car

        except:
            print("Error processing car id: ", car_id)
            return None