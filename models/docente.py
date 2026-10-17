from models.persona import Persona

class Docente(Persona):
    def __init__(self, identificacion, nombre, correo, num_empleado, facultad, tipo_contrato, horas_semanales):
        super().__init__(identificacion, nombre, correo)
        self.__num_empleado = num_empleado
        self.__facultad = facultad
        self.__tipo_contrato = tipo_contrato
        self.__horas_semanales = horas_semanales

    def get_num_empleado(self):
        return self.__num_empleado

    def get_facultad(self):
        return self.__facultad

    def get_tipo_contrato(self):
        return self.__tipo_contrato

    def get_horas_semanales(self):
        return self.__horas_semanales

    def set_horas_semanales(self, horas):
        if horas <= 0:
            return False
        self.__horas_semanales = horas
        return True

    def mostrar_informacion(self):
        texto = "--- DOCENTE ---\n"
        texto += super().mostrar_informacion() + "\n"
        texto += "Número de empleado: " + self.__num_empleado + "\n"
        texto += "Facultad: " + self.__facultad + "\n"
        texto += "Tipo de contratación: " + self.__tipo_contrato + "\n"
        texto += "Horas semanales: " + str(self.__horas_semanales)
        return texto

    def realizar_actividad_principal(self):
        return self.get_nombre() + " orienta clases en la facultad de " + self.__facultad
