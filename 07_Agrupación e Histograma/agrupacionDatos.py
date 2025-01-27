import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\precios_coches.csv'

datos = pd.read_csv(fichero)

print(datos.head())
print(datos.columns)
print(datos.dtypes)


titulos_cabecera = ['indice', 'nombre', 'localización', 'año', 'kilometros recorridos', 'combustible', 
                    'transmision', 'tipo propietario', 'kilometraje', 'motor', 'potencia', 'asientos', 'precio nuevo', 'precio']

datos.columns = titulos_cabecera

print(datos.head(5))
print(datos.columns)

intervalo = np.linspace(min(datos['kilometros recorridos']), max(datos['kilometros recorridos']), 4)
nombre_grupos = ['pocos', 'normal', 'muchos']
datos['kilometros agrupados'] = pd.cut(datos['kilometros recorridos'], intervalo, labels=nombre_grupos, include_lowest=True)

plt.hist(datos['kilometros recorridos'], bins=intervalo, rwidth=0.9, color='#991')
plt.title('Histograma kilometros recorridos')
plt.xlabel('Kilometros')
plt.ylabel('Frecuencia')
plt.show()

