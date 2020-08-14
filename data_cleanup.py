import pandas as pd
import os

months = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6,
          'Julio': 7, 'Agosto': 8, 'Setiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}

data_path = os.path.join(os.getcwd(), 'data')
os.chdir(data_path)
df = pd.read_csv('cars.csv', encoding='utf-8-sig', index_col=None, header=None)
df[1] = df[1].str.replace(",", "")
df[1] = df[1].str.replace(" cc", "")

df[9] = df[9].str.replace(",", "")
df[9] = df[9].str.replace(" km", "")

df[14] = '%d/%d/%d' % (months[df[14].str.split(' ')[2]], df[14].str[0:2], df[14].str[-4:])

df[15] = df[15].str.replace("Este vehículo ha sido visto ", "")
df[15] = df[15].str.replace(" veces", "")

df[17] = df[17].str.replace(",", "")
df[17] = df[17].str.replace("¢ ", "")

names = ["car", "marca","modelo","año","cilindrada","estilo","combustibile","transmision","estado","kilometraje","puertas","pagoImpuesto","negociable","recibeVehiculo","fechaIngreso","vecesVisto","comentarios","precio"]

df.columns = names

df.to_csv('cars_p.csv', encoding='utf-8-sig', index=False)

