import pandas as pd

fichero = 'python-workspace\\DataScient_01-Python\\csv_practicos\\precios_coches.csv'

datos = pd.read_csv(fichero)

print(datos.columns)
print(datos['Fuel_Type'])

#Transformar variabl categoricas en dummies (ficticias)
columna_dummies = pd.get_dummies(datos['Fuel_Type'])
print(columna_dummies)

datos_dummies = pd.get_dummies(datos, columns=['Fuel_Type'])
print(datos.head())
print('*'*10)
print(datos_dummies.head())