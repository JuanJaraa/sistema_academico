class Persona:
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

    # Cada hijo lo sobrescribe con su propia versión
    def realizar_actividad_principal(self):
        return self.__nombre + " es una persona de la universidad."
