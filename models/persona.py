# [AC2 - NUEVO] Se importa ABC y abstractmethod para volver abstracta a Persona
from abc import ABC, abstractmethod

# [AC2 - MODIFICADO] Antes: class Persona:  ->  Ahora hereda de ABC (clase abstracta)
class Persona(ABC):
    def __init__(self, identificacion, nombre, correo):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo


    def get_identificacion(self):
        return self.__identificacion

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    # Setters
    def set_nombre(self, nombre):
        if nombre.strip() == "":
            return False
        self.__nombre = nombre
        return True

    def set_correo(self, correo):
        if correo.strip() == "":
            return False
        self.__correo = correo
        return True

    def mostrar_informacion(self):
        texto = "Identificacion: " + self.__identificacion + "\n"
        texto += "Nombre: " + self.__nombre + "\n"
        texto += "Correo: " + self.__correo
        return texto

    # [AC2 - MODIFICADO] Ahora es un método abstracto: Persona ya no lo implementa.
    # Cada hijo (Estudiante, Docente, Administrativo) está obligado a escribir su versión.
    @abstractmethod
    def realizar_actividad_principal(self):
        pass
