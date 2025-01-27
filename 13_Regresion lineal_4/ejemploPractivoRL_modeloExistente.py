import numpy as np
from sklearn.preprocessing import StandardScaler 
import joblib


#Cargar el modelo ya guardado.
carga_modelo = joblib.load('python-workspace\\DataScient_01-Python\\13_Regresion lineal_4\\regresion_lineal.pkl')

nuevos_datos = np.array([[0.00632, 18.0, 2.31, 0, 0.538, 6.575, 65.2, 4.0900, 1, 296.0, 15.3, 396.90, 4.98]])
escala = StandardScaler()
nuevos_datos_escalados = escala.fit_transform(nuevos_datos)
prediccion = carga_modelo.predict(nuevos_datos_escalados)
print("Precios prediccion: ", prediccion)