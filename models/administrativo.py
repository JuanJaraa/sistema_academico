from models.persona import Persona

class Administrativo(Persona):
    def __init__(self, identificacion, nombre, correo, num_empleado, dependencia, cargo, jornada):
        super().__init__(identificacion, nombre, correo)
        self.__num_empleado = num_empleado
        self.__dependencia = dependencia
        self.__cargo = cargo
        self.__jornada = jornada

    def get_num_empleado(self):
        return self.__num_empleado

    def get_dependencia(self):
        return self.__dependencia

    def get_cargo(self):
        return self.__cargo

    def get_jornada(self):
        return self.__jornada

    def set_cargo(self, cargo):
        if cargo.strip() == "":
            return False
        self.__cargo = cargo
        return True

    def mostrar_informacion(self):
        texto = "--- ADMINISTRATIVO ---\n"
        texto += super().mostrar_informacion() + "\n"
        texto += "Número de empleado: " + self.__num_empleado + "\n"
        texto += "Dependencia: " + self.__dependencia + "\n"
        texto += "Cargo: " + self.__cargo + "\n"
        texto += "Jornada: " + self.__jornada
        return texto

    def realizar_actividad_principal(self):
        return (self.get_nombre() + " trabaja como " + self.__cargo
                + " en la dependencia de " + self.__dependencia)
