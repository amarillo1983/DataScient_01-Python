import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score 
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

#Cargar datos
fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\housing.csv'
datos = pd.read_csv(fichero)
print(datos.head())

# Realizamos un primer análisis exploratorio.
## Vamos a graficar en una matriz la relación entre todas las variables (correlación).
matriz_correlacion = datos.corr().round(2)
plt.figure(figsize=(12,8))
sns.heatmap(data=matriz_correlacion, annot=True, cmap='coolwarm')
plt.title('Correlación entre características')
#plt.show()

#Definimos variables predictoras y variable objetivo.
X = datos.drop('MEDV', axis=1)
y = datos['MEDV']

#El escalado puede ayudar a evitar que ciertas variables dominen el modelo 
# debido a su mayor magnitud. Sin embargo, es importante tener en cuenta 
# que el escalado no es un requisito para la regresión lineal y su necesidad 
# depende de los datos y los objetivos específicos del análisis.
escala = StandardScaler()
X_escaladas = escala.fit_transform(X)

# Separamos los datos de entrenamiento y pruebas.
X_train, X_test, y_train, y_test = train_test_split(X_escaladas, y, test_size=0.2, random_state=42)

# Creamos modelo Regresión Lineal
modeloLR = LinearRegression()

#Entrenamiento modelo
modeloLR.fit(X_train, y_train)

#Prediccion
y_pred = modeloLR.predict(X_test)

#Evaluación de modelo
MSE = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Error cuadrático medio:{MSE}')
print(f'R2:{r2}')

#Guardar el modelo en disco para no tener que realizar el entrenamiento cada vez que se quiera usar.
joblib.dump(modeloLR, 'python-workspace\\DataScient_01-Python\\13_Regresion lineal_4\\regresion_lineal.pkl')

#Cargar el modelo ya guardado.
carga_modelo = joblib.load('python-workspace\\DataScient_01-Python\\13_Regresion lineal_4\\regresion_lineal.pkl')
