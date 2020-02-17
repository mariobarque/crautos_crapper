import pandas as pd
import os


os.chdir(os.getcwd() + "/data")
df = pd.read_csv('cars.csv', encoding='utf-8-sig', index_col=None, header=None)
df[1] = df[1].str.replace(",", "")
df[1] = df[1].str.replace(" cc", "")

df[9] = df[9].str.replace(",", "")
df[9] = df[9].str.replace(" km", "")

df[17] = df[17].str.replace(",", "")
df[17] = df[17].str.replace("¢ ", "")

names = ["car", "marca","modelo","año","cilindrada","estilo","combustibile","transmision","estado","kilometraje","puertas","pagoImpuesto","negociable","recibeVehiculo","fechaIngreso","vecesVisto","comentarios","precio"]

df.columns = names

df.to_csv('cars_p.csv', encoding='utf-8-sig', index = False)

