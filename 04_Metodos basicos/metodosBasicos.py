import pandas as pd
import numpy as np

fichero = 'python-workspace\DataScient_01-Python\csv_practicos\precios_coches.csv'

datos = pd.read_csv(fichero)

#print(datos.dtypes)
#print(datos.describe())
#print(datos.describe(include='all'))
#print(datos.info())

#Preprocesamiento de datos.
print(datos['Seats'].head(5))
#datos['Seats'] = datos['Seats'] + 1

#Sustitución valores faltantes.
#datos.dropna(subset=['Seats'], axis= 0, inplace=True) # Borrado por fila los valores faltantes 
#datos.replace(np.nan, 'nulo')  # REeemplar los faltantes por el string nulo
 # Reemplazar los faltantes con la media de los valores
media_asientos = datos['Seats'].mean()
datos['Seats'].replace(np.nan, media_asientos, inplace=True)
print(datos.describe())