import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_absolute_error

#Cargar datos
fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\melb_data.csv'
datos = pd.read_csv(fichero)
#print(datos.describe())
#print(datos.columns)
#print(datos.head())
datos.drop('Unnamed: 0', axis=1, inplace=True)
#print(datos.describe())
#print(datos.columns)
print(datos.head())

#Variable predictora o dependendiente
y = datos['Price']

#Variables dependientes
columnas_seleccionadas= ['Rooms', 'Bathroom', 'Landsize', 'Lattitude','Longtitude']
X = datos[columnas_seleccionadas]

#Borrar valores perdidos o nulos
#datos = datos.dropna(axis=0) Borra las filas que contengan valores nulos (está como recordatorio)
#Imputación a los faltantes
print(X.describe())
imputer = SimpleImputer()
X = pd.DataFrame(imputer.fit_transform(X))
#Con la operación anterior, se pueden borrar el nombre de las columnas. Se lo volvemos asignasr
X.columns = columnas_seleccionadas
print(X.describe())

#Vamos a ver si tenemos alguna variable categorica
object = (X.dtypes=='object')
print(object)

#Separación entrenamiento y pruebas
train_X, test_X, train_y, test_y = train_test_split(X, y, random_state=0)

#Definimos el modelo
modelo = DecisionTreeRegressor(random_state=0)
modelo.fit(train_X, train_y)

#Predicciones para las siguientes casas
print('Predicciones para las casas')
print(test_X)
prediccion = modelo.predict(test_X)
print('la prediccion es ', prediccion)

#Añadimos la columna de precición y el valor real
#test_X ['Prediccion'] = prediccion
#test_X ['Real'] = test_y
#print(test_X.head())

#Validación del modelo
print(mean_absolute_error(test_y, prediccion))

#Función obtener error medio
def dame_mae(maximo_nodos, train_x, test_x, train_y, test_y):
    modelo = DecisionTreeRegressor(max_leaf_nodes=maximo_nodos, random_state=1)
    modelo.fit(train_X, train_y)
    prediccion = modelo.predict(test_X)
    mae = mean_absolute_error(test_y, prediccion)
    return mae

# Comparamos el error en base a diferentes profundidades.
for maximo_nodo in [10, 15, 30, 100, 200, 1000, 5000]:
    mae = dame_mae(maximo_nodo, train_X, test_X, train_y, test_y)
    print ("Para {} \t MAE: {}".format(maximo_nodo, mae))


