import pandas as pd
from datetime import datetime

#Cargar csv en un dataFrame
df_ventas = pd.read_csv('csv_practicos/ventas_.csv', sep=';')

#Reemplazar los valores na por ceros.
df_ventas.fillna(0, inplace=True)

#Añadir una nueva columna Total con la multiplicación de Cantidad y precio unitario
df_ventas['Ingresos'] = df_ventas['Cantidad'] * df_ventas['Precio_Unitario']
print(df_ventas)

#Agrupar los datos por Tienda y producto y 
# calculos los ingresos totales por producto en cada tienda
ingresos_por_tienda_producto = df_ventas.groupby(['Tienda', 'Producto'])['Ingresos'].sum().reset_index()
#print(ingresos_por_tienda_producto)

#Encontrar el producto con mayores ingresos en cada tienda.
producto_top_por_tienda = ingresos_por_tienda_producto.sort_values(['Tienda', 'Ingresos'], ascending=[True, False]).groupby('Tienda').first().reset_index
#print(producto_top_por_tienda)


#Resumen cantidad total de productos vendidos a lo largo del mes
hoy = pd.to_datetime(datetime.now())
ultimo_mes = hoy - pd.DateOffset(months=1)
print(ultimo_mes)
#resumen_cantidad = df_ventas.filter(lambda x: x['Fecha'].sum())
#groupby('Producto')['Cantidad'].sum().reset_index

#print(resumen_cantidad)
resumenCantidad = df_ventas.groupby('Producto')['Cantidad'].sum().reset_index()
print(resumenCantidad)
resumenCantidad.to_csv('csv_practicos/resumenVentas.csv', index=False)


