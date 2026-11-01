# [AC2 - NUEVO] clase Horario (Fases 2 y 3)

class Horario:

    def __init__(self, dia, hora_inicio, hora_fin, salon):
        self.__dia = dia
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin
        self.__salon = salon

    def get_dia(self):
        return self.__dia

    def get_hora_inicio(self):
        return self.__hora_inicio

    def get_hora_fin(self):
        return self.__hora_fin

    def get_salon(self):
        return self.__salon

    def set_salon(self, salon):
        if salon.strip() == "":
            return False
        self.__salon = salon
        return True

    def mostrar_informacion(self):
        return (self.__dia + " de " + self.__hora_inicio + " a " + self.__hora_fin
                + ", salón " + self.__salon)
