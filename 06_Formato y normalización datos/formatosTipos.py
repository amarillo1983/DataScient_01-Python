import pandas as pd
import numpy as np

fichero = 'python-workspace\DataScient_01-Python\csv_practicos\precios_coches.csv'

datos = pd.read_csv(fichero)

#print(datos.head())
#print(datos.dtypes)

#Cambiar el tipo de dato de la columa Unnamed a float6
datos['Unnamed: 0'] = datos['Unnamed: 0'].astype('float64')
#print(datos.dtypes)

#Realizar calculos y añadir a otra columna.

#millas = kilometros * 0.6211371
datos['millas_driven']= datos['Kilometers_Driven'] * 0.6211371
print(datos.head())

datos.rename(columns={'millas_driven': 'Millas'}, inplace=True)
print(datos.head())

# Normalizar datos.
# min y valor anterior
print(datos[['Millas', 'Kilometers_Driven']])
datos['Millas_nor'] = datos['Millas'] / datos['Millas'].max()
datos['Kilometros_nor'] = datos['Kilometers_Driven'] / datos['Kilometers_Driven'].max()
print(datos[['Millas_nor', 'Kilometros_nor']])

# min y max
print(datos[['Millas', 'Kilometers_Driven']])
datos['Millas_nor'] = (datos['Millas'] - datos['Millas'].min()) / (datos['Millas'].max() - datos['Millas'].min())
datos['Kilometros_nor'] = (datos['Kilometers_Driven'] - datos['Kilometers_Driven'].min()) / (datos['Kilometers_Driven'].max() - datos['Kilometers_Driven'].min())
print(datos[['Millas_nor', 'Kilometros_nor']])