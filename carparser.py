import requests
from bs4 import BeautifulSoup
from car import Car
from constants import Constants


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
    def parse_car(car_id):
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

        car = Car(car_id, marca, modelo, anno, cilindrada, estilo, combustible, transmision, estado, kilometraje,
                  puertas, pagoImpuesto, negociable, recibeVehiculo, fechaIngreso, vecesVisto, comentario, price)

        return car

