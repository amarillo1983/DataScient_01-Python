import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

#Cargar datos
fichero = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
datos = pd.read_csv(fichero, header=None)
print("Dimensiones del conjunto de datos: ", datos.shape)
print("Primeras finlas del conjunto de datos: ")
print(datos.head())

print("PREPOCESAMIENTO")
print("*Cantidad de valores nulos por columnas: *")
print(datos.isnull().sum())


# Si hubiera valores null datos.dropna(inplace=True)

X = datos.iloc[:, :-1] # hasta la penultima columna
y = datos.iloc[:, -1] # La última columna - variable objetivo

X.columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']

X['ca'] = X['ca'].replace('?', 0.0)
X['thal'] = X['thal'].replace('?', 0.0)
X['ca'] = X['ca'].astype('float64')
X['thal'] = X['thal'].astype('float64')
print(X.dtypes)

print(X.head())
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# joblib.dump(modelo, 'modelos_entrenados/arbol_de_decision.pkl')

modelo_cargado = joblib.load ('modelos_entrenados/arbol_de_decision.pkl')

y_predicciones = modelo_cargado.predict(X_test)

X_test_con_prediccion = X_test.copy()
X_test_con_prediccion['prediccion'] = y_predicciones
X_test_con_prediccion['valor real'] = y_test

print('Predicciones vs variable objetivo')
print(X_test_con_prediccion.head())

print('Evaluamos el modelo en base a las metricas')
metrica = accuracy_score(y_test, y_predicciones)
print('Metrica: ', metrica)

clasificacion = classification_report(y_test, y_predicciones)
print('Clasificación:')
print(clasificacion)

plt.figure(figsize=(8,6))
plt.scatter(X_test_con_prediccion['valor real'], X_test_con_prediccion['prediccion'])
plt.xlabel('Valor Real')
plt.ylabel('Predicción')
plt.title('Valores reales vs predicciones')
plt.show()

