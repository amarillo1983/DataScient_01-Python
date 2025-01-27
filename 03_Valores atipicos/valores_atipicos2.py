import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Establece la semilla para generar números aleatorios y que al generarlo varias veces la secuencia generada
#siempre sea la misma
np.random.seed(0)

x = np.random.normal(0, 0.5, 100)
y = np.random.normal(0, 0.5, 100)

x[98:]= [3, -3]
y[98:]= [3, -3]

plt.scatter(x, y)
plt.title('Scater Plot con Outliers')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Eliminar Outlairs con la distancia al centro y la media
print('Vaores x')
#print(x)
print('Valores y')
#print(y)
print('Distancia Centro')
distancia_centro = np.sqrt(x**2+y**2)
#print(distancia_centro)
limite = np.percentile(distancia_centro, 95) #Umbral del 95%
x_filtrado = x[distancia_centro <= limite]
y_filtrado = y[distancia_centro <= limite]
print("-"*35)
print(distancia_centro)
print(limite)
print(x_filtrado)
print(y_filtrado)

plt.scatter(x_filtrado, y_filtrado)
plt.title('Scater Plot sin Outliers')
plt.xlabel('X_filtrado')
plt.ylabel('Y_filtrado')
plt.grid(True)
plt.show()