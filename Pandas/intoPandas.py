import pandas as pd
import numpy as np

etiquetas = ['a', 'b', 'c', 'd', 'e']
datos = np.arange(4, 9)
serie = pd.Series(datos, index=etiquetas)

#print(serie)

#acceder a valor
#print(serie['c'])

#datos de distinto tipo
datos = ['Jose', 49, 'Mar', 46, True]
serie = pd.Series(datos)
#print(serie)


#datos directos
serie = pd.Series([1000, 500, 1200, 700], ['Emp01', 'Emp02', 'Emp03', 'Emp04'])
#print(serie)

#Operación suma
etiquetasEmpleados = ['Empleado', 'Productividad', 'Edad', 'Sexo']
datosEmpleado1 = ['Antonio', 92, 34, 'Masculino']
datosEmpleado2 = ['Ismael', 81, 24, 'Masculino']

serieEmpleado1 = pd.Series(datosEmpleado1, etiquetasEmpleados)
#print(serieEmpleado1)

serieEmpleado2 = pd.Series(datosEmpleado2, etiquetasEmpleados)
#print(serieEmpleado2)

#print(serieEmpleado1 + serieEmpleado2)

#dataFrames

AreaDesarrollo = ['Java', 'Drupal', 'TypeScrit', 'Liferay']
Provincias = ['Sevilla', 'Madrid', 'Barcelona']
datosProductividad = [[np.nan, 72, 12], [42, np.nan, 60], [26, 37, 88], [45, 9, np.nan]]

dataFrameProductividad = pd.DataFrame(datosProductividad, index=AreaDesarrollo, columns=Provincias)
#print(dataFrameProductividad)

#Selección de fila
#print(dataFrameProductividad.loc[['Drupal']])
#print(dataFrameProductividad.loc['Drupal'])
#print(dataFrameProductividad.loc[['Drupal', 'Liferay']])

#Selección de columna
#print(dataFrameProductividad['Sevilla'])
#print(dataFrameProductividad[['Sevilla']])

#Selección valor concreto
#print(dataFrameProductividad.loc['Java', 'Madrid'])

#Añadir nueva columna
dataFrameProductividad['Almeria'] = [0, 1, 2, 3]
#dataFrameProductividad['Almeria'] = 0
#print(dataFrameProductividad)

#print(dataFrameProductividad)

dataFrameProductividad['total'] = dataFrameProductividad['Sevilla'] + dataFrameProductividad['Madrid'] + \
    dataFrameProductividad['Barcelona'] + dataFrameProductividad['Almeria']

#print(dataFrameProductividad)

#Eliminar columna
#dataFrameProductividad = dataFrameProductividad.drop(['total'], axis=1) #xaxi 1 es para indicarle que es una colunma
dataFrameProductividad.drop(['total'], axis=1, inplace=True) # inplace true es para indicarle que persita la acción en el objeto
#print(dataFrameProductividad)

#condición = dataFrameProductividad > 50 
#print(dataFrameProductividad[condición])

#condicion = (dataFrameProductividad['Sevilla'] > 85) & (dataFrameProductividad['Madrid'] < 90)
#print(dataFrameProductividad[condicion])

dataFrameProductividad['Indices'] = [1,2,3,4]
print(dataFrameProductividad)
#print(dataFrameProductividad)
dataFrameProductividad = dataFrameProductividad.set_index('Indices')


#Borrado valores nulos
#dataFrameProductividad.dropna(axis=1, inplace=True)
#Rellenar los valores nulos
#dataFrameProductividad.fillna(value=69, inplace=True)

#print(dataFrameProductividad)

media = dataFrameProductividad.mean()
#print(media)

dataFrameProductividad.fillna(value=media, inplace=True)
#print(dataFrameProductividad)

#Unión de dataFrame
dataFrame1 = dataFrameProductividad.copy()
dataFrame2 = dataFrameProductividad.copy()

#dataFrameTotal = pd.concat([dataFrame1, dataFrame2], axis=1)
dataFrameTotal = pd.concat([dataFrame1, dataFrame2])
#print(dataFrameTotal)
#print(dataFrameTotal['Barcelona'].unique())
#print(dataFrameTotal['Barcelona'].value_counts())

dataFrameTotal = dataFrameTotal.apply(lambda y: y*10)
dataFrameTotal = dataFrameTotal.apply(lambda y: round(y))
print(dataFrameTotal)

#print(dataFrameTotal.columns)
#print(dataFrameTotal.index)
#print(dataFrameTotal.sort_values(['Madrid']))
#print(dataFrameTotal.describe())

#dataFrameTotal.to_csv('dataFrameTotal.csv')
dataFrameRead = pd.read_csv('dataFrameTotal.csv', index_col=0)
print(dataFrameRead)




