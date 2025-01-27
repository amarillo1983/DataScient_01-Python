import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics 
import matplotlib.pyplot as plt

#Cargar datos
fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\datosModificados.csv'
datos = pd.read_csv(fichero)
datos.set_index('indice', inplace=True)
#print(datos.head())

#Columnas con nulos, detectar si las columnas que usaremos en el modelo tienen valores nulos para reemplazarlos.
columnas_nulos = [col for col in datos.columns if datos[col].isnull().any()]
#print(columnas_nulos) # Las columnas con valores nulos no las vamos a usar en el modelo

# Creamos modelo Regresión Lineal
modeloLR = LinearRegression()

#Hot encoding
datos_dummies_combustible = pd.get_dummies(datos['combustible'], dtype=int)
#print(datos_dummies_combustible)
datos = pd.concat([datos, datos_dummies_combustible], axis=1)

#Normalización columnas Motor y Potencia
datos['motor'] = datos['motor'] / datos['motor'].max()
datos['potencia'] = datos['potencia'] / datos['potencia'].max()

#Definimos variables predictoras y variable objetivo.
X = datos[['motor', 'potencia', 'asientos', 
           'CNG', 'Diesel', 'Electric', 'LPG', 'Petrol']]
#print(X)
#La columna  combustible tiene un valor categorico, hay que cambiar a valores, ver comentario Hot encoding
y = datos['precio']

# Separamos los datos de entrenamiento y pruebas.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Entrenamiento modelo
modeloLR.fit(X_train, y_train)

#Predicción
prediccion = modeloLR.predict(X_test)

a = modeloLR.intercept_
b = modeloLR.coef_

#Mostramos ecuación
#print(f'y={a}+{b}*x1 + b2*x2 + b3*x3')
#print('***'*20)
#print('Predicción: ', prediccion)
#print(y_test)
#print('Valor que nos indica como se ajusta el modelo:', modeloLR.score(X_train,y_train)) #Lo ideal es que se ajuste a 1

# Comparativa Dato Real Vs predicción modelo RL
resultado = {
    'Real': y_test,
    'Prediccion': prediccion 
}
dataFrameResultado = pd.DataFrame(data=resultado)
print(dataFrameResultado.head())

# Vamos a ver las métricas de nuestro modelo
ECM = metrics.mean_squared_error(y_test, prediccion)
#print(f"El error cuadrático medio es: {ECM}")
r_cuadrado = metrics.r2_score(y_test, prediccion)
#print(r_cuadrado)

#Graficamos los resultados
plt.scatter(X_test['motor'], prediccion, c='red', label='Predicción')
plt.scatter(X_test['motor'], y_test, label='Datos')
plt.title('Regresion lineal')
plt.xlabel('Motor')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()

