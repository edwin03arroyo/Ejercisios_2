instituto={"carreras":["Desarrollo","Siverseguridad","Audiovisual","Enfermeria","Grafico","Cocina"],
          "materias":["Sistemas","Programacion","Optica","Rinoplastia","Sombreados","Especias"],
          "profesores":["Fanny Reinoso","Belen Toledo","Carlos Guaman","Karla Lopez","Carlos Yunga","Dayanna Guaman"],
          "notas":["80.5","90.0","78.8","72.6","80.5","68.0"]}
print(instituto["carreras"])
print(instituto["materias"])
print(instituto["profesores"])
print(instituto["notas"])

promedio=0
for e in(instituto["notas"]):
    promedio+=float(e)
print(promedio/len(instituto["notas"]))
print(round(promedio/len(instituto["notas"]),2))
valor_maximo=max(instituto["notas"])
valor_minimo=min(instituto["notas"])

posicion=(instituto["notas"]).index(valor_maximo)
print("La nota minima es: ",valor_maximo)
print("De la carrera: ",instituto["carreras"][posicion])
print("Asignatura: ",instituto["materias"][posicion])
print("Profesor: ",instituto["profesores"][posicion])