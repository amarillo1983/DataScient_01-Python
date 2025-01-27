import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 

#Cargar datos
fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\datosModificados.csv'
datos = pd.read_csv(fichero)
datos.set_index('indice', inplace=True)
print(datos.head())

# Creamos modelo Regresión Lineal
modeloLR = LinearRegression()

#Definimos variables predictoras y variable objetivo.
X = datos[['motor']]
y = datos['precio']
# Separamos los datos de entrenamiento y pruebas.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#Entrenamiento modelo
modeloLR.fit(X_train, y_train)

#Predicción
prediccion = modeloLR.predict(X_test)

a = modeloLR.intercept_
b = modeloLR.coef_

#Mostramos ecuación
print(f'y={a}+{b}*x')
print('Predicción')
print(prediccion)
print(y_test)
print('Valor que nos indica como se ajusta el modelo:', modeloLR.score(X_train,y_train)) #Lo ideal es que se ajuste a 1