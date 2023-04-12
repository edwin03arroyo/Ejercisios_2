#EJERCICIOS DE TUPLAS
#Crear una tupla de números enteros y calcular su suma y promedio.
numeros = (4, 7, 10, 12, 15)
suma = sum(numeros)
promedio = suma / len(numeros)
print("La suma de los números es:", suma)
print("El promedio de los números es:", promedio)

#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
tupla1 = (2, 4, 6, 8, 10)
tupla2 = (1, 3, 5, 7, 9)
suma_tuplas = tuple(map(sum, zip(tupla1, tupla2)))
print("La nueva tupla con la suma de las tuplas es:", suma_tuplas)

#Crear una tupla de nombres y ordenarla alfabéticamente.
nombres = ("Juan", "Ana", "Pedro", "Luisa", "Sofía")
nombres_ordenados = sorted(nombres)
print("La tupla ordenada alfabéticamente es:", nombres_ordenados)

#Crear una tupla de números y encontrar el valor mínimo y máximo.
numeros = (4, 7, 10, 12, 15)
minimo = min(numeros)
maximo = max(numeros)
print("El valor mínimo es:", minimo)
print("El valor máximo es:", maximo)

#Crear una tupla de números y convertirla en una lista.
numeros_tupla = (4, 7, 10, 12, 15)
numeros_lista = list(numeros_tupla)
print("La tupla convertida en lista es:", numeros_lista)

#Crear una tupla con los días de la semana y mostrar el tercer elemento.
dias_semana = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
tercer_dia = dias_semana[2]
print("El tercer día de la semana es:", tercer_dia)

#Crear una tupla con números enteros y mostrar aquellos que son pares.
numeros = (4, 7, 10, 12, 15)
pares = [num for num in numeros if num % 2 == 0]
print("Los números pares son:", pares)

#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
meses_mas_cinco = [mes for mes in meses if len(mes) > 5]
print("Los meses con más de cinco letras son:", meses_mas_cinco)

#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
edades = (12, 18, 25, 36, 42, 14, 21, 30, 17)
mayores_edad = len([edad for edad in edades if edad > 18])
print("La cantidad de personas mayores de 18 años es:", mayores_edad)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
libros = (
    ("Viaje al fin de la noche", "Louis-Ferdinand Céline"),
    ("Don Quijote de la Mancha", "Miguel de Cervantes"),
    ("Los cuentos de Canterbury", "Geoffrey Chaucer"),
)
print(libros[2][0])