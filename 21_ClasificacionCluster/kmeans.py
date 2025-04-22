import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#Carga de datos
datos = load_iris()
X = pd.DataFrame(datos.data, columns=datos.feature_names)
#print(X.info)
#print(X.describe())
#print(X.head())

#Escalar los datos
scaler = StandardScaler()
X_escalado = scaler.fit_transform(X)

#Crear y entrenar el modelo
kmeans_model = KMeans(n_clusters=3, random_state=0)
kmeans_model.fit(X_escalado)

#Obtener etiquetas de cluster y asignarla a los datos
etiquetas= kmeans_model.labels_
X['cluster'] = etiquetas

#Visualización
#plt.scatter(X['sepal length (cm)'], X['sepal width (cm)'], c=X['cluster'], cmap='viridis')
plt.scatter(X['petal length (cm)'], X['petal width (cm)'], c=X['cluster'], cmap='viridis')
plt.xlabel('Longitud sepalo')
plt.ylabel('Ancho sepalo')
plt.title('Clasificación por cluster con K-means')
plt.show()