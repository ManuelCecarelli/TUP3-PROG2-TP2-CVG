import os
import estudiante as est
import profesor as prof
import curso as cur

#listas para almacenar profesores, estudiantes y cursos
registroProfesores = []
registroEstudiantes = []
registroCursos = []

#instanciamos algunos estudiantes 
estudianteUno = est.Estudiante(53019,2023,"Manuel","Cecarelli","manuelcecarelli@gmail.com","35750423")
estudianteDos = est.Estudiante(53041,2023,"Danisa","Gomez","danisagomez86@gmail.com","33105762")
estudianteTres = est.Estudiante(53289,2023,"Jeremias","Zagaglia","jeremiaszagaglia@gmail.com","44995290")

#los agregamos a la lista
registroEstudiantes.append(estudianteUno)
registroEstudiantes.append(estudianteDos)
registroEstudiantes.append(estudianteTres)

#instanciamos algunos profesores
profesorUno = prof.Profesor("Ingeniería en Sistemas",2020,"Ricardo","Ruben","ricardoruben@gmail.com","11223344")
profesorDos = prof.Profesor("Profesorado en matemáticas",2005,"Monica","Perez","moniperez@gmail.com","11111111")
profesorTres = prof.Profesor("Profesorado en Inglés",1998,"Martina","Gonzalez","martinagonzalez@gmail.com","22222222")

#los agregamos a la lista
registroProfesores.append(profesorUno)
registroProfesores.append(profesorDos)
registroProfesores.append(profesorTres)

respuesta = ""

def menu_principal():
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")

'''APLICACION PRINCIPAL'''
#---------------------------------------------------------

print("Bienvenido!\n")

while respuesta != "salir":
    menu_principal()

    opt = input("\nIngrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla

    if opt.isnumeric():
        if int(opt) == 1:
            pass
        elif int(opt) == 2:
            pass
        elif int(opt) == 3:
            pass
        elif int(opt) == 4:
            respuesta = "salir"
        else:
            print("Ingrese una opción válida")
    else: 
        print("Ingrese una opción numérica")
    
    os.system ("cls") #Limpiar pantalla

print("Hasta luego!")