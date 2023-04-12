#EJERCICIOS DE CONJUNTOS
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
numeros = set(range(1, 11))
print(numeros)

#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ellos.
numeros_pares = set(range(2, 11, 2))
numeros_impares = set(range(1, 10, 2))
print("Conjunto de números pares:", numeros_pares)
print("Conjunto de números impares:", numeros_impares)
interseccion = numeros_pares.intersection(numeros_impares)
print("Intersección:", interseccion)

#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas = {"manzana", "banana", "naranja"}
elemento = input("Ingrese un elemento: ")
if elemento in frutas:
    print("El elemento", elemento, "se encuentra en el conjunto.")
else:
    print("El elemento", elemento, "no se encuentra en el conjunto.")

#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
numeros_1 = set(range(1, 6))
numeros_2 = set(range(4, 9))
union = numeros_1.union(numeros_2)
print("Unión de los conjuntos:", union)

#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.
compras = {"leche", "pan", "huevos", "azúcar"}
compras.remove("azúcar")
compras.add("harina")
print("Elementos de la lista de compras:", compras)

#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.
nombres = {"Juan", "María", "Pedro", "Luisa"}
print("Número de elementos del conjunto:", len(nombres))

#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.
numeros_1 = set(range(1, 6))
numeros_2 = set(range(4, 9))
print("Conjunto 1:", numeros_1)
print("Conjunto 2:", numeros_2)
diferencia_simetrica = numeros_1.symmetric_difference(numeros_2)
print("Diferencia simétrica:", diferencia_simetrica)

#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.
conjunto1 = set(range(1, 11))
conjunto2 = set(range(5, 16))
print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
print("Unión:", union)

#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.
frutas = {"manzana", "banana", "naranja", "pera"}
for fruta in sorted(frutas):
    print(fruta)

#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.
conjunto3 = set(range(1, 11))
conjunto4= set(range(6, 16))
print("Conjunto 1:", conjunto3)
print("Conjunto 2:", conjunto4)
interseccion = conjunto3.intersection(conjunto4)
print("Intersección:", interseccion)