import pandas as pd
import numpy as np

def cargaDatos(ruta, fichero):
    datos = pd.read_csv(ruta + fichero)
    return datos

def dameColumnas(datos):
    return datos.columns

def cambiaColumnas(datos, columnas):
    datos.columns = columnas
    return datos

def renombrarColumna(datos, cambio):
    datos.rename(columns=cambio, inplace=True)
    return datos

def guardaDatos(datos, ruta, fichero):
    datos.to_csv(ruta+fichero)
    return True

def dameEstadisticos(datos, tipo='numerico'):
    if tipo=='numerico':
        return datos.describe()
    else:
        return datos.describe(include='all')
    
def reemplazarNulos(datos, columna):
    media = datos[columna].mean()
    datos[columna].replace(np.nan, media, inplace=True)
    return datos

def cambiaTipoDato(columna, tipo='float64'):
    columna = columna.astype(tipo)
    return columna

def normalizaColumna(datos, columna):
    datos[columna] = datos[columna] / datos[columna].max()
    return datos
