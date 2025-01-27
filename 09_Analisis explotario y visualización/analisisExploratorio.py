import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Carga de datos.
fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\precios_coches02.csv'
datos = pd.read_csv(fichero, sep=';')
#print(datos.head())

#columna indice
datos.set_index('Unnamed: 0', inplace=True)
datos.index.name = 'indice'
#print(datos.head())

#print(datos.columns)
titulos_cabecera = ['nombre', 'localización', 'año', 'kilometros recorridos', 'combustible', 
                    'transmision', 'tipo propietario', 'kilometraje', 'motor', 'potencia', 'asientos', 'precio nuevo', 'precio']
datos.columns = titulos_cabecera
#print(datos.head(5))

#Estadisticoas básicos
#print(datos.describe())
#print('**'*15)
#print(datos.describe(include='all'))

##Reemplazar valores nulos - detectados en columna asientos.
media = datos['asientos'].mean()
datos['asientos'].replace(np.nan, media, inplace=True)
#print(datos.describe())
#cambio tipo
#print(datos['motor'])
#print(datos['potencia'])
#datos['potencia'] = datos['potencia'].astype('float64')
datos['potencia'] = pd.to_numeric(datos['potencia'], errors='coerce')
#print(datos['potencia'])
#reemplazar los NaN de potencia por la media
media = datos['potencia'].mean()
datos['potencia'].replace(np.nan, media, inplace=True)
#print(datos['potencia'])

#Contar cuantas veces aparece un nombre
#print(datos['nombre'].value_counts())
#Contar cuantas aparece un año
#print(datos['año'].value_counts())

#Visualización datos
#plt.boxplot(datos['precio'])
#plt.title('Precios')
#plt.show()

#Grafico de dispersión - relación entre variables
y = datos['precio']
x = datos['potencia']
plt.scatter(x, y)
plt.title('Relación Potencia / Precio')
plt.xlabel('Potencia')
#plt.xlim(datos['potencia'].min()-100, datos['potencia'].max()+100)
plt.ylabel('Precio')
#plt.show()

y = datos['precio']
x = datos['motor']
plt.scatter(x, y)
plt.title('Relación motor / Precio')
plt.xlabel('motor')
plt.ylabel('Precio')
#plt.show()

#Coeficiente de Correlación y p-valor
# -----Coeficiente de Correlación-----
# Si prox a 1 relación positiva
# Si prox a -1 relación negativa
# Si prox a 0 sin relación
# -----p-valor-----
# Si <0.001 fuerte certeza en el resultado de correlación.
# Si <0.05 moderada certeza en el resultado de correlación
# Si <0.1 baja o debil certeza en el resultado de correlación
# Si >0.1 sin certeza de correlación

from scipy import stats

media = datos['motor'].mean()
datos['motor'].replace(np.nan, media, inplace=True)
media = datos['precio'].mean()
datos['precio'].replace(np.nan, media, inplace=True)

pearson_coef, p_valor = stats.pearsonr(datos['motor'], datos['precio'])
print(f"El coeficiente de correlación de Pearon es: {pearson_coef}")
print(f"El p-valor es: {p_valor}")

columnas_nuevas = ['año', 'kilometros recorridos', 'motor', 'potencia', 'precio']

datos_nuevo = datos[columnas_nuevas]
datos_agrupados = datos_nuevo.groupby(['año'], as_index=False)
print(datos_agrupados.head())

#Guardar datos
fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\datosModificados.csv'
datos.to_csv(fichero)



