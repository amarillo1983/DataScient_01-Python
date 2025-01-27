
import numpy as np

lista = [1,2,3,4,5,6,3,2,8,9]
array = np.array(lista)
#print (lista)
#print (type(array))
#print (array)

lista2 = [[1,2,4], [2,5,3], [9,4,2]]
array2 = np.array(lista2)
#print (array2)

#arrays
array3 = np.arange(6)
#print(array3)

array3 = np.arange(2, 15, 2)
#print(array3)

matrizCeros = np.zeros ((4,5))
#print(matrizCeros)

matrizUnos = np.ones ((3,5))
#print(matrizUnos)

#Matriz de 40 elementos con valores del 2 - 6
matriz40 = np.linspace(2,6,40)
#print(matriz40)

#Matriz identidad
matrizIdentitad = np.eye(7)
#print(matrizIdentitad)

#Matriz de números aleatorios
matrizAleatoria = np.random.rand(3,4)
#print(matrizAleatoria)

matrizAleatoriaNormal = np.random.randn(4)
#print(matrizAleatoriaNormal)

matrizAleatoriaEnteros = np.random.randint(1,51, 20)
#print(matrizAleatoriaEnteros)

#Tamaño de los arrays
array = np.random. randint(1,201,30)
#print(array)
matriz = array.reshape(5,6)
#print(matriz)

#max y min
array = np.random.randint (1, 901, 200)
#print(array)
maximo = array.max()
#print(f"El valor maxiomo es {maximo}")
#print(array.argmax())

#Mostar elementos
array = np.arange(1,11)
#print(array)
#print(array[2])
#print(array[5:])
#print(array[:2])

#Copia de array
array2 = array.copy()
#print(array)
#print(array2)
array2[2] = 9999
#print(array)
#print(array2)

#Operaciones con la matriz
#print(matriz)
#print(matriz[0])
#print(matriz[:2])
#print(matriz[1][2])
#print(matriz[1, 2])
#print(matriz[:, :1])
#print(matriz[:, :2])
#print(matriz + 10)
#print(matriz + matriz)
#print(np.max(matriz))

condición = matriz > 50
#print(condición)
#print(matriz[condición])

#Ejercicio
lista = np.arange(5,41)
#print(lista)
#print(len(lista))
lista = lista.reshape(3,12)
#print(lista)
#print(lista[2,4])
#print(lista[:2,:4])
#print(lista[1][4])

#Combinación primitiva.
arrayPrimitiva = np.random.randint(1,50,6)
print(f"la combinación ganadora de la primitiva será {arrayPrimitiva}")