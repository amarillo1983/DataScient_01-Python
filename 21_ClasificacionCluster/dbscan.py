import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons

#Datos
X, _ = make_moons(n_samples=1000, noise=0.05)

#Entrenar modelo
dbscan_model = DBSCAN(eps=0.2, min_samples=5)
dbscan_model.fit(X)

# Visualizar los resultados del clustering
labels = dbscan_model.labels_
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.title('DBSCAN Clustering')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()