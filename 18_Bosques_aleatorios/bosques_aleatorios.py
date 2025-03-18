import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

datos = sns.load_dataset('iris')

#print(datos.head())
#print(datos.describe())

#print(datos.isnull().sum())
#print(datos.dtypes)

matriz_correlacion = datos.corr(numeric_only=True)
# print(matriz_correlacion)

sns.heatmap(matriz_correlacion, annot=True, cmap='coolwarm')

#plt.title('Matriz de correlacion')
#plt.show()

X = datos.drop('species', axis=1)
y = datos['species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
# modelo_rf.fit(X_train, y_train)

#joblib.dump(modelo_rf, 'modelos_entrenados/modelo_random_forest.pkl')

modelo_cargado: RandomForestClassifier = joblib.load('modelos_entrenados/modelo_random_forest.pkl')

nuevos_datos= [[5.1, 3.5, 1.4, 0.2]]

prediccion = modelo_cargado.predict(nuevos_datos)
print('Predicción: ', prediccion)

y_pred_test = modelo_cargado.predict(X_test)
precision = accuracy_score(y_test, y_pred_test)
print('Precisión del modelo: ', precision)

reporte_clasificacion = classification_report(y_test, y_pred_test)
print('Reporte de clasificación: \n', reporte_clasificacion)

