import usuario as usu
import curso as cur

class Estudiante(usu.Usuario):
    def __init__(self, legajo: int, anioIncripcionCarrera: int, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__legajo = legajo
        self.__anioIncripcionCarrera = anioIncripcionCarrera

    def __str__(self) -> str:
        mensaje = f"\nLegajo: {self.__legajo}\nAño Inscripción a Carrera: {self.__anioIncripcionCarrera}\nNombre: {self._nombre}\nApellido: {self._apellido}\nE-mail: {self._email}"
        return mensaje
    
    def matricularEnCurso(self, curso: cur.Curso):
        self._misCursos.append(curso)

    #def __str__(self) -> str:
    #    return super().__str__()