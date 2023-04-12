#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE LISTAS A RESOLVER
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
numeros=[1,2,3,4,5]
print(numeros)

#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
amigos=["pedro","aron","edwin","nilo","ariel","dayanna"]
print(amigos[0])
print(amigos[4])

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
lista=[1,2,3,4,5,6,7,8,9,10]
for e in lista:
    if e%2== 0:
        print("e")
else:
    print("No es par")

#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
print(amigos[-1])
print(amigos[len(amigos),-1])

#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
print(lista[-1])

#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
for e in lista:
    if e%2== 1:
        print("e")
else:
    print("No es par")

#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
amigos.insert(2,"joaquin")
print(amigos)

#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
amigos(len())

#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
suma=0
print(sum(lista))