import numpy as np
import pandas as pd

df = pd.read_csv('csv_practicos/precios_cochesCopia.csv')

#print(df.isnull())

#Borrar filas con na
df_sin_nulos = df.dropna()

#Borrar columnas con na
#df_sin_nulos = df.dropna(axis=1)

#Rellenar valores na con valor 0
#df.fillna(value=0, inplace=True)


#Rellenar valores na con siguiente valor
#df.fillna(method='ffill', inplace=True)
#print(df)

#Rellenar valores na con anterior valor
#df.fillna(method='bfill', inplace=True)
#print(df)

#Rellenar valores na con la media de la columna (Si todos los datos son numericos)
#df.fillna(df.mean(), inplace=True)
#print(df)

#Rellenar valores na mediante interpolación (Si todos los datos son numericos)
#df.interpolate(inplace=True)
#print(df)
