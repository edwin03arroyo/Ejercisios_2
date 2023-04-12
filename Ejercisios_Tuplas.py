#EJERCICIOS DE TUPLAS
#Crear una tupla vacía:
tupla = ()

#Crear una tupla con algunos elementos:
elementos = (1, 2, 3, 'cuatro', 'cinco')

#Acceder a un elemento de la tupla:
print(elementos[3])

#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):
elementos[2] = 5

#Concatenar dos tuplas:
tupla_1 = (1, 2, 3)
tupla_2 = ('cuatro', 'cinco')
concatenada = tupla_1 + tupla_2
print(concatenada)

#Obtener la longitud de una tupla:
print(len(elementos))

#Convertir una tupla en una lista:
tupla_convertir = (1, 2, 3)
lista = list(tupla)
print(lista)

#Convertir una lista en una tupla:
lista_convertir = ['cuatro', 'cinco', 'seis']
tupla_convertida = tuple(lista)
print(tupla_convertida)

