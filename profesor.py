import usuario as usu
import curso as cur

class Profesor(usu.Usuario):
    def __init__(self, titulo: str, anioEgreso: int, nombre: str, apellido: str, email: str, contrasenia: str):
        super().__init__(nombre, apellido, email, contrasenia)
        self.__titulo = titulo
        self.__anioEgreso = anioEgreso

    def __str__(self) -> str:
        mensaje = f"\nTítulo: {self.__titulo}\nAño Egreso: {self.__anioEgreso}\nNombre: {self._nombre}\nApellido: {self._apellido}\nE-mail: {self._email}"
        return mensaje
    
    def dictarCurso(self, curso: cur.Curso):
        self._misCursos.append(curso)