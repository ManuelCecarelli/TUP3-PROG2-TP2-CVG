import random
import string

class Curso:
    def __init__(self, nombre: str):
        self.__nombre =nombre
        self.__contraseniaMatriculacion = Curso.__generarContrasenia()

    def __str__(self) -> str:
        mensaje = f"\nNombre: {self.__nombre}\nContraseña: {self.__contraseniaMatriculacion}"
        return mensaje
    
    @classmethod
    def __generarContrasenia(cls) -> str:
        characters = string.ascii_letters + string.digits
        cod = ''.join(random.choice(characters) for i in range(8))
        return cod