import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_iris

#Carga de datos
datos = load_iris() #Cargamos los datos directamente de Iris.

X = datos.data
#print(X)
y = datos.target
#print(y)
y = (datos.target != 0) * 1 # Convertir a 1 o 0
#print(y)

#Entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Creación y entrenamiento del modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

#Realizamos predicciones y evaluamos el modelo.
y_pred = modelo.predict(X_test)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))


