class Asignatura:
    def __init__(self, codigo, nombre, creditos, programa):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__creditos = creditos
        self.__programa = programa  # es un objeto ProgramaAcademico

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_creditos(self):
        return self.__creditos

    def get_programa(self):
        return self.__programa

    def set_nombre(self, nombre):
        if nombre.strip() == "":
            return False
        self.__nombre = nombre
        return True

    def set_creditos(self, creditos):
        if creditos <= 0:
            return False
        self.__creditos = creditos
        return True

    def mostrar_informacion(self):
        texto = "Asignatura: " + self.__nombre + "\n"
        texto += "  Código: " + self.__codigo + "\n"
        texto += "  Créditos: " + str(self.__creditos) + "\n"
        texto += "  Programa: " + self.__programa.get_nombre()
        return texto
