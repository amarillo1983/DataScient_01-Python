import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Creamos conjunto de datos con gastos en publicidad y ventas.
datos = {
    'Gasto_publicidad': [100,200,300,400,500,200,300,400,500,200,300,400,500],
    'Ventas': [800,900,700,600,500,900,700,600,500,900,700,600,500]
}

# Creamos el dataframe a partir de los datos anteriores.
df = pd.DataFrame(data= datos)

# Separamos variables en predictoras y objetivo.
x = df[['Gasto_publicidad']]
y = df['Ventas']

# Datos de entrenamiento y pruebas. Tenemos que separar los datos con los que se va a
# entrenar el modelo y los datos con los que vamos a probar dicho modelo.
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Modelo
model = LinearRegression()

# Entrenamos al modelo
model.fit(X_train, y_train)

# Predicción
y_pred = model.predict(X_test)

# Coeficientes, pendiente e interseccion
print('Coeficientes:', model.coef_)
print('Pendiente:', model.coef_[0])
print('Interseccion:', model.intercept_)

#Evaluar el modelo
print('Error cuadrático medio (MSE):', mean_squared_error(y_test, y_pred))
print('Coeficiente de determinación (R^2):', r2_score(y_test, y_pred))

#Visualizamos
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('Regresión lineal: Gastos en publicidad Vs Ventas')
plt.xlabel('Gastos en publicidad')
plt.ylabel('Ventas')
plt.show()




