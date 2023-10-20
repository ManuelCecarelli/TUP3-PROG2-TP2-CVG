from abc import ABC, abstractclassmethod

class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
        self._misCursos = []
    

    @abstractclassmethod
    def __str__(self) -> str:
        pass

    def validarCredenciales(self, email: str, contrasenia: str) -> bool:
        if (self._email == email and self._contrasenia == contrasenia):
            return True
        else:
            return False
