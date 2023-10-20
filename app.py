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

carrera = "Tecnicatura Universitaria en Programación"
respuesta = ""

def menu_principal():
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")

def submenuAlumno():
    print("1. Matricularse a un curso")
    print("2. Ver curso")
    print("3. Volver al menu principal")

def submenuProfesor():
    print("1. Dictar Curso")
    print("2. Ver curso")
    print("3. Volver al menu principal")
   
'''APLICACION PRINCIPAL'''
#---------------------------------------------------------

print("Bienvenido!\n")

while respuesta != "salir":
    menu_principal()

    opt1 = input("\nIngrese la opción de menú: ")

    if opt1.isnumeric():
        if int(opt1) == 1:
            os.system ("cls") #Limpiar pantalla
            emailIngresado = input("Ingrese su email: ")
            contraseniaIngresada = input("Ingrese su contraseña: ")
            i=0
            banderaEmail=False
            while (banderaEmail==False and i <len(registroEstudiantes)):
                auxAlumno= registroEstudiantes[i]
                if (emailIngresado == auxAlumno.email):
                    banderaEmail=True
                    if (auxAlumno.validarCredenciales(emailIngresado, contraseniaIngresada)):
                        opt2 = ""
                        while(opt2 !="3"):
                            os.system ("cls") #Limpiar pantalla
                            print(f"Alumno: {auxAlumno.nombre} {auxAlumno.apellido}\n")
                            submenuAlumno()
                            opt2 = input("\nIngrese la opción de menú: ")
                            os.system ("cls") #Limpiar pantalla
                            if opt2.isnumeric():
                                if int(opt2) == 1:
                                    for i in range(len(registroCursos)):
                                        auxCurso = registroCursos[i]
                                        print(f"{i+1}. {auxCurso.nombre}")
                                    opt3=input("\nSeleccione el curso: ")
                                    if opt3.isnumeric():
                                        if int(opt3) in [1,2,3,4,5,6]:
                                            if registroCursos[int(opt3)-1] not in auxAlumno.misCursos:
                                                auxCurso = registroCursos[int(opt3)-1]
                                                contrasenia = input("\nIngrese la contraseña de matriculación: ")
                                                if auxCurso.contraseniaMatriculacion == contrasenia:
                                                    auxAlumno.matricularEnCurso(registroCursos[int(opt3)-1])
                                                    print("\nUsted se ha matriculado correctamente")
                                                    input("\nPresione una tecla para continuar")
                                                else:
                                                    print("\nLa contraseña ingresada es incorrecta")
                                                    input("\nPresione una tecla para continuar")
                                            else:
                                                print("\nUsted ya se encuentra matriculado en ese curso")
                                                input("\nPresione una tecla para continuar")
                                        else:
                                            print("\nDebe ingresar una opción válida")
                                            input("\nPresione una tecla para continuar")
                                    else:
                                        print("\nDebe ingresar una opción válida")
                                        input("\nPresione una tecla para continuar")
                                elif int(opt2) == 2:
                                    if len(auxAlumno.misCursos) > 0:
                                        listaAuxiliar = []
                                        print("Usted se encuentra matriculado en los siguientes cursos:\n")
                                        for i in range(len(auxAlumno.misCursos)):
                                            auxInscripto = auxAlumno.misCursos[i]
                                            listaAuxiliar.append(i+1)
                                            print(f"{i+1}. {auxInscripto.nombre}")
                                        opt4 = input("\nIngrese el curso para detalle: ")
                                        if opt4.isnumeric():
                                            if int(opt4) in listaAuxiliar:
                                                auxInscripto = auxAlumno.misCursos[int(opt4)-1]
                                                print(f"\nNombre: {auxInscripto.nombre}")
                                                input("\nPresione una tecla para continuar")
                                            else:
                                                print("\nDebe ingresar una opción válida")
                                                input("\nPresione una tecla para continuar")
                                        else:
                                            print("\nDebe ingresar una opción válida")
                                            input("\nPresione una tecla para continuar")
                                    else:
                                        print("\nUsted aun no se encuentra matriculado en ningún curso")
                                        input("\nPresione una tecla para continuar")
                                elif int(opt2) == 3:
                                    print(f"\nAdiós {auxAlumno.nombre} {auxAlumno.apellido}")
                                    input("\nPresione cualquier tecla para continuar...")
                                    os.system ("cls") #Limpiar pantalla
                                else:
                                    print("\nDebe ingresar una opción válida")
                                    input("\nPresione una tecla para continuar")
                            else:
                                print("\nDebe ingresar una opción válida")
                                input("\nPresione una tecla para continuar")
                    else:
                        print("\nError de ingreso")
                        input("\nPresione una tecla para continuar")  
                i=i+1
            if (banderaEmail == False):
                input("\nE-mail inexistente, debe darse de alta en alumnado")

        elif int(opt1) == 2:
            os.system ("cls") #Limpiar pantalla
            emailIngresado = input("Ingrese su email: ")
            contraseniaIngresada = input("Ingrese su contraseña: ")
            i=0
            banderaEmail=False
            while (banderaEmail==False and i <len(registroProfesores)):
                auxProfesor= registroProfesores[i]
                if (emailIngresado == auxProfesor.email):
                    banderaEmail=True
                    if (auxProfesor.validarCredenciales(emailIngresado, contraseniaIngresada)):
                        opt2 = ""
                        while(opt2 !="3"):
                            os.system ("cls") #Limpiar pantalla
                            print(f"Profesor: {auxProfesor.nombre} {auxProfesor.apellido}\n")
                            submenuProfesor()
                            opt2 = input("\nIngrese la opción de menú: ")
                            os.system ("cls") #Limpiar pantalla
                            if opt2.isnumeric():
                                if int(opt2) == 1:
                                    nombreCurso = input("Ingrese el nombre del nuevo curso: ")
                                    nuevoCurso = cur.Curso(nombreCurso)
                                    auxProfesor.dictarCurso(nuevoCurso)
                                    registroCursos.append(nuevoCurso)
                                    print("\nEl nuevo curso ha sido creado con éxito")
                                    print(f"\nDatos del nuevo curso:\nNombre: {nuevoCurso.nombre}\nContraseña: {nuevoCurso.contraseniaMatriculacion}")
                                    input("\nPresione una tecla para continuar")
                                elif int(opt2) == 2:
                                    if len(auxProfesor.misCursos) > 0:
                                        listaAuxiliar = []
                                        print("Usted dicta los siguientes cursos:\n")
                                        for i in range(len(auxProfesor.misCursos)):
                                            auxInscripto = auxProfesor.misCursos[i]
                                            listaAuxiliar.append(i+1)
                                            print(f"{i+1}. {auxInscripto.nombre}")
                                        opt4 = input("\nIngrese el curso para detalle: ")
                                        if opt4.isnumeric():
                                            if int(opt4) in listaAuxiliar:
                                                auxInscripto = auxProfesor.misCursos[int(opt4)-1]
                                                print(f"\nNombre: {auxInscripto.nombre}")
                                                print(f"Contraseña: {auxInscripto.contraseniaMatriculacion}")
                                                input("\nPresione una tecla para continuar")
                                            else:
                                                print("\nDebe ingresar una opción válida")
                                                input("\nPresione una tecla para continuar")
                                        else:
                                            print("\nDebe ingresar una opción válida")
                                            input("\nPresione una tecla para continuar")
                                    else:
                                        print("\nUsted aun no dicta ningún curso")
                                        input("\nPresione una tecla para continuar")
                                elif int(opt2) == 3:
                                    print(f"\nAdiós {auxProfesor.nombre} {auxProfesor.apellido}")
                                    input("\nPresione cualquier tecla para continuar...")
                                    os.system ("cls") #Limpiar pantalla
                                else:
                                    print("\nDebe ingresar una opción válida")
                                    input("\nPresione una tecla para continuar")
                            else:
                                print("\nDebe ingresar una opción válida")
                                input("\nPresione una tecla para continuar")
                    else:
                        print("\nError de ingreso")
                        input("\nPresione una tecla para continuar")  
                i=i+1
            if (banderaEmail == False):
                input("\nE-mail inexistente, debe darse de alta en administración")

        elif int(opt1) == 3:
            if len(registroCursos) > 0:
                #Para poder ordenar alfabéticamente los objetos de la lista de cursos tomando como criterio el atributo 'nombre', investigamos un poco en la documentación oficial de python :)
                nuevaLista = sorted(registroCursos, key=lambda Curso: Curso.nombre)
                os.system ("cls") #Limpiar pantalla
                print("Los cursos disponibles son los siguientes:\n")
                for i in range(len(nuevaLista)):
                    auxCurso = nuevaLista[i]
                    #como el curso 'Programación II' tiene un nombre más largo que el resto, no nos coincidían las tbulaciones, así que ideamos la siguiente línea para solucionarlo :)
                    tabulacion = "\t" if len(auxCurso.nombre)>=15 else "\t\t"
                    print(f"Materia: {auxCurso.nombre}{tabulacion}Carrera: {carrera}")
                input("\nPresione cualquier tecla para continuar...")
            else:
                print("\nDisculpe, actualmente no hay cursos disponibles")
                input("\nPresione cualquier tecla para continuar...")
        elif int(opt1) == 4:
            respuesta = "salir"
        else:
            print("\nDebe ingresar una opción válida")
            input("\nPresione una tecla para continuar")
            os.system ("cls") #Limpiar pantalla
    else: 
        print("\nDebe ingresar una opción válida")
        input("\nPresione una tecla para continuar")
        os.system ("cls") #Limpiar pantalla
    
    os.system ("cls") #Limpiar pantalla

print("Hasta luego!")