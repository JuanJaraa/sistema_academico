from models.persona import Persona

class Estudiante(Persona):
        
    def __init__(self, identificacion, nombre, correo, codigo, programa, semestre, promedio):
        super().__init__(identificacion, nombre, correo)
        self.__codigo = codigo
        self.__programa = programa  
        self.__semestre = semestre
        self.__promedio = promedio

    def get_codigo(self):
        return self.__codigo

    def get_programa(self):
        return self.__programa

    def get_semestre(self):
        return self.__semestre

    def get_promedio(self):
        return self.__promedio

    def set_semestre(self, semestre):
        if semestre <= 0 or semestre > self.__programa.get_num_semestres():
            return False
        self.__semestre = semestre
        return True

    def set_promedio(self, promedio):
        if promedio < 0 or promedio > 5:
            return False
        self.__promedio = promedio
        return True

    # Sobrescritura: datos de Persona + datos del estudiante
    def mostrar_informacion(self):
        texto = "--- ESTUDIANTE ---\n"
        texto += super().mostrar_informacion() + "\n"
        texto += "Codigo estudiantil: " + self.__codigo + "\n"
        texto += "Programa: " + self.__programa.get_nombre() + "\n"
        texto += "Semestre: " + str(self.__semestre) + "\n"
        texto += "Promedio acumulado: " + str(self.__promedio)
        return texto

    def realizar_actividad_principal(self):
        return (self.get_nombre() + " cursa el programa de " + self.__programa.get_nombre()
                + " y esta en el semestre " + str(self.__semestre))
