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

#Instanciamos algunos cursos
cursoUno = cur.Curso("Ingles I")
cursoDos = cur.Curso("Ingles II")
cursoTres = cur.Curso("Laboratorio I")
cursoCuatro = cur.Curso("Laboratorio II")
cursoCinco = cur.Curso("Programación I")
cursoSeis = cur.Curso("Programación II")

#los agregamos a la lista
registroCursos.append(cursoUno)
registroCursos.append(cursoDos)
registroCursos.append(cursoTres)
registroCursos.append(cursoCuatro)
registroCursos.append(cursoCinco)
registroCursos.append(cursoSeis)

respuesta = ""

def menu_principal():
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")
def submenu_alumno():
    print("1. Matricularse a un curso")
    print("2. Ver curso")
    print("3. Volver al menu principal")
   

'''APLICACION PRINCIPAL'''
#---------------------------------------------------------

print("Bienvenido!\n")

while respuesta != "salir":
    menu_principal()

    opt = input("\nIngrese la opción de menú: ")
    os.system ("cls") #Limpiar pantalla

    if opt.isnumeric():
        if int(opt) == 1:
            emailIngresado = input("Ingrese su email")
            contraseniaIngresada = input("Ingrese su contraseña")
            i=0
            banderaEmail=False
            while (banderaEmail==False and i <len(registroEstudiantes)):
                auxalumnos= registroEstudiantes[i]
                if (emailIngresado == auxalumnos.email):
                    banderaEmail=True
                
                
                    
            
                    if (auxalumnos.validarCredenciales(emailIngresado, contraseniaIngresada)):
                        option = ""
                        while(option !="3"):
                            submenu_alumno()
                            option = input("\nIngrese la opción de menú: ")
                            os.system ("cls") #Limpiar pantalla
                            if opt.isnumeric():
                                if int(option) == 1:
                                    for i in range(len(registroCursos)):
                                        auxcur=registroCursos[i]
                                        print(f"{i+1}. {auxcur.nombre}")
                                
                                    opcion=input("Seleccione el curso")
                                    if int(opcion) in [1,2,3,4,5,6]:
                                        if registroCursos[int(opcion)] not in auxalumnos.misCursos:
                                            auxalumnos.matricularEnCurso(registroCursos[int(opcion)])
                                            print("Alumno matriculado correctamente")
                                        else:
                                            print("El alumno ya fue antiguamente matriculado")
                                            input("")



                                
                                
                i=i+1




                
               
            if (banderaEmail == False):
                input("email inexistente, Debe darse de alta en alumnado")

           

    
      
            

            
        
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