import pandas as pd
import os

data_path = os.path.join(os.getcwd(), 'data')
os.chdir(data_path)

df = pd.read_csv('cars.csv')


analysis_df = df[['marca','modelo','año','estilo','combustible','kilometraje','puertas','pago impuesto','precio']].groupby(['marca','modelo','año','estilo','combustible','kilometraje','puertas','pago impuesto']).mean().reset_index()
def get_suggested_price(marca, modelo, anno, estilo, combustible, puertas, pagoImpuesto, kilometraje):
  try:
    result_df = analysis_df[(analysis_df['marca'] == marca) & 
                            (analysis_df['modelo'] == modelo) &
                            (analysis_df['año'] == anno) &
                            (analysis_df['estilo'] == estilo) &
                            (analysis_df['combustible'] == combustible) &
                            (analysis_df['kilometraje'] == kilometraje) &
                            (analysis_df['puertas'] == puertas) &
                            (analysis_df['pago impuesto'] == pagoImpuesto)]
    return int(result_df['precio'])
  except:
    print('Issue with:', marca, modelo, anno, estilo, combustible, puertas, pagoImpuesto, kilometraje)

generic_analysis_df = df[['marca','moderno','estilo','combustible','kilometraje','precio']].groupby(['marca','moderno','estilo','combustible','kilometraje']).mean().reset_index()
def get_generic_suggested_price(marca, moderno, estilo, combustible, kilometraje):
  try:
    result_df = generic_analysis_df[(generic_analysis_df['marca'] == marca) & 
                            (generic_analysis_df['moderno'] == moderno) &
                            (generic_analysis_df['estilo'] == estilo) &
                            (generic_analysis_df['combustible'] == combustible) &
                            (generic_analysis_df['kilometraje'] == kilometraje)]
    return int(result_df['precio'])
  except:
    print('Issue with:', marca, moderno, estilo, combustible, kilometraje)

df['precio_sugerido'] = 0
df['precio_sugerido_generico'] = 0

for i, row in df.iterrows():
    #suggested_price = get_suggested_price(row['marca'], row['modelo'], row['año'], row['estilo'], row['combustible'], row['kilometraje'], row['puertas'], row['pago impuesto'])
    suggested_generic_price = get_generic_suggested_price(row['marca'], row['moderno'], row['estilo'], row['combustible'], row['kilometraje'])
    #df.at[i,'precio_sugerido'] = suggested_price
    df.at[i,'precio_sugerido_generico'] = suggested_generic_price

#df['difrencia'] = (df['precio_sugerido'] - df['precio'])/df['precio_sugerido']
df['difrencia generica'] = (df['precio_sugerido_generico'] - df['precio'])/df['precio_sugerido_generico']


df.to_csv('analysis.csv', encoding='utf-8-sig', index=False)