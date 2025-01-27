import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
datos_normales = np.random.normal(loc=50, scale=10, size=100)

#print(datos_normales)

valores_atipicos = [20, 80, 90, 100, 120]
datos_completos = np.concat([datos_normales, valores_atipicos])

print(datos_completos)

def identificar_valores_atipicos(datos):
    cuartil_1 = np.percentile(datos, 25)
    cuartil_3 = np.percentile(datos, 75)
    IQR = cuartil_3 - cuartil_1
    limite_inferior = cuartil_1 - 1.5*IQR
    limite_superior = cuartil_3 + 1.5*IQR

    valores_atipicos_identificados = datos[(datos<limite_inferior) | (datos>limite_superior)]
    return valores_atipicos_identificados

valores_atipicos = identificar_valores_atipicos(datos_completos)

print("Valores atípicos identificados: ", valores_atipicos)

plt.figure(figsize=(8,6))
plt.boxplot(datos_completos, vert=False)
plt.title("Diagrama de caja")
plt.xlabel("Valores")
#plt.show()

#Vamos a eliminar los valores atipicos del conjunto.
datos_sin_atipico = datos_completos[~np.isin(datos_completos,valores_atipicos)]

print("Datos sin valores atípicos: ", datos_sin_atipico)