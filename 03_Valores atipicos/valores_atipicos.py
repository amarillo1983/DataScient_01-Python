import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos = np.array([10,12,12,13,12,11,14,13,15,64,12,14,15,12,78,13,59])

plt.boxplot(datos, vert=False) # vert es para indicar que la representación sea vertical u horizontal
plt.title('BoxPlot de datos con outliers')
plt.xlabel('Valores')
plt.show()

Q1 = np.percentile(datos, 25)
Q3 = np.percentile(datos, 75)
#Rango intercuarticulos - Q3 - Q1 Lo que midre la cajita
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5*IQR
limite_superior = Q3 + 1.5*IQR
print(limite_inferior)
print(limite_superior)
datos_filtrado = datos[(datos >= limite_inferior) & (datos<=limite_superior)]
print(datos_filtrado)

plt.boxplot(datos_filtrado, vert=False)
plt.title('Boxplot de datos in outliers')
plt.xlabel('Valores')
plt.show()
