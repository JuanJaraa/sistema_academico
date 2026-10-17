class ProgramaAcademico:
    def __init__(self, codigo, nombre, facultad, num_semestres):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__facultad = facultad
        self.__num_semestres = num_semestres

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_facultad(self):
        return self.__facultad

    def get_num_semestres(self):
        return self.__num_semestres

    
    def set_nombre(self, nombre):
        if nombre.strip() == "":
            return False
        self.__nombre = nombre
        return True

    def set_facultad(self, facultad):
        if facultad.strip() == "":
            return False
        self.__facultad = facultad
        return True

    def set_num_semestres(self, num_semestres):
        if num_semestres <= 0:
            return False
        self.__num_semestres = num_semestres
        return True

    # Devuelve el texto con los datos (la vista se encarga de imprimirlo)
    def mostrar_informacion(self):
        texto = "Programa: " + self.__nombre + "\n"
        texto += "  Código: " + self.__codigo + "\n"
        texto += "  Facultad: " + self.__facultad + "\n"
        texto += "  Semestres: " + str(self.__num_semestres)