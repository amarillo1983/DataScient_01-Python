import numpy as np
import pandas as pd

fichero = 'python-workspace\DataScient_01-Python\csv_practicos\precios_coches.csv'

datos = pd.read_csv(fichero)

#print(datos)
#print(datos.head(5))
#print(datos.tail(5))

#print(datos.columns)

titulos_cabecera = ['Indice', 'Nombre', 'Localización', 'Año', 'Kilometros recorridos', 'Combustible', 
'Transmision', 'Tipo propietario', 'Kilometraje', 'Motor', 'Potencia', 'Asientos', 'Precio nuevo', 'Precio']

datos.columns = titulos_cabecera
print(datos.head(5))

#Export datos
datos.to_csv('csv_practicos/precios_cochesCopia.csv')

#Otros formatos de archivos
#datos.to_json()
#datos.to_excel()
#datos.to_sql()


