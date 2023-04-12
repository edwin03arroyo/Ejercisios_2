#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: "clave": valor
dic={}
dic["alumno"]={"Juan Bravo":18}
dic["alumno"]={"Kevin Santos":19}
dic["alumno"]={"Karla Vintimilla":19}

#2.Dado el siguiente diccionario:
personas = {"Juan": 28, "María": 20, "Pedro": 32, "Ana": 25}
#a) Imprime la edad de Juan.
print(personas.get("Juan"))

#b) Agrega un nuevo elemento al diccionario con la clave "Luis" y la edad 18.
personas["Luis"]=18

#c) Elimina el elemento con la clave "Pedro".
personas.pop("Pedro")
print(personas)

#3.Dado el siguiente diccionario:
ventas = {"manzanas": 10, "naranjas": 5, "peras": 8}
#a) Imprime la cantidad de manzanas vendidas.
#print(ventas("manzanas"))

#b) Agrega 3 elementos más al diccionario: "limones": 12, "sandías": 3, "melones": 5.
ventas["limones"]=12
ventas["sandias"]=3
ventas["melones"]=5

#c) Imprime las claves del diccionario.
print(ventas.keys())

#4. Dado el siguiente diccionario:
alumnos = {"Juan": {"edad": 22, "promedio": 8.5}, "María": {"edad": 20, "promedio": 9.0}, "Pedro": {"edad": 25, "promedio": 7.5}}
#a) Imprime la edad de Juan.
print(alumnos["Juan"]["edad"])
for e in alumnos:
    print(e)
for c,v in alumnos.items():
    print(c,v)



#b) Imprime el promedio de María.
print(alumnos["María"]["promedio"])

#c) Agrega un nuevo elemento al diccionario con la clave "Ana" y los valores "edad": 19 y "promedio": 8.0.
alumnos["Ana"]={"edad":19,"promedio":8.0}

for e in alumnos:
    if e == 20 and 22:
        print("Edades que tienen 20 y 22",e)
#5. Dado el siguiente diccionario:
empleados = {"Juan": {"departamento": "Ventas", "sueldo": 1500}, "María": {"departamento": "Contabilidad", "sueldo": 1800}, "Pedro": {"departamento": "Ventas", "sueldo": 1700}, "Ana": {"departamento": "Recursos Humanos", "sueldo": 1900}}
#a) Imprime el sueldo de Pedro.
#b) Cambia el sueldo de Ana a 2000.
#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.
#6.Dado el siguiente diccionario:
#a) Imprime las materias en las que está inscrito Pedro.
#b) Agrega una materia más a la lista de materias de María: "Programación".
#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
#7. Dado el siguiente diccionario:
#a) Imprime el precio de las naranjas.
#b) Cambia el stock de peras a 12.
#c) Crea una función que calcule el valor total de los productos en el diccionario.