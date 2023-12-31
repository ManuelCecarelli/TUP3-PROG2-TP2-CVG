from abc import ABC, abstractclassmethod

class Usuario(ABC):
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia
        self._misCursos = []

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def apellido(self):
        return self._apellido

    @property
    def email(self):
        return self._email
    
    @property
    def misCursos(self):
        return self._misCursos
    
    @abstractclassmethod
    def __str__(self) -> str:
        pass

    def validarCredenciales(self, email: str, contrasenia: str) -> bool:
        if (self._email == email and self._contrasenia == contrasenia):
            return True
        else:
            return False
