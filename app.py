import os
import estudiante as est
import profesor as prof
import curso as cur

#listas para almacenar profesores, estudiantes y cursos
registroProfesores = []
registroEstudiantes = []
registroCursos = []

#instanciamos algunos estudiantes 
#estudianteUno = est.Estudiante()
#estudianteDos = est.Estudiante()
#estudianteTres = est.Estudiante()

#los agregamos a la lista
#registroEstudiantes.append(estudianteUno)
#registroEstudiantes.append(estudianteDos)
#registroEstudiantes.append(estudianteTres)

#instanciamos algunos profesores
#profesorUno = prof.Profesor()
#profesorDos = prof.Profesor()
#profesorTres = prof.Profesor()

#los agregamos a la lista
#registroProfesores.append(profesorUno)
#registroProfesores.append(profesorDos)
#registroProfesores.append(profesorTres)

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