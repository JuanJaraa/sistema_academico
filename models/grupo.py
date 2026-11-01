# [AC2 - NUEVO] clase GrupoAcademico (Fases 2, 3 y 4)

from models.horario import Horario
from models.excepciones import (EstudianteYaMatriculadoError, GrupoLlenoError,
                                EstudianteNoMatriculadoError)


class GrupoAcademico:
    def __init__(self, codigo, asignatura, docente, capacidad_maxima,
                 dia, hora_inicio, hora_fin, salon):
        self.__codigo = codigo
        self.__asignatura = asignatura          # objeto Asignatura ya creado 
        self.__docente = docente                # objeto Docente ya creado 
        self.__capacidad_maxima = capacidad_maxima
        self.__estudiantes = []                 # lista de objetos Estudiante matriculados
        
        self.__horario = Horario(dia, hora_inicio, hora_fin, salon)

    def get_codigo(self):
        return self.__codigo

    def get_asignatura(self):
        return self.__asignatura

    def get_docente(self):
        return self.__docente

    def get_capacidad_maxima(self):
        return self.__capacidad_maxima

    def get_horario(self):
        return self.__horario

    def get_estudiantes(self):
        return list(self.__estudiantes)  # copia, para no exponer la lista privada

    def mostrar_informacion_grupo(self):
        texto = "Grupo: " + self.__codigo + "\n"
        texto += "  Asignatura: " + self.__asignatura.get_nombre() + " (" + self.__asignatura.get_codigo() + ")\n"
        texto += "  Docente: " + self.__docente.get_nombre() + "\n"
        texto += "  Horario: " + self.__horario.mostrar_informacion() + "\n"
        texto += "  Matriculados: " + str(len(self.__estudiantes)) + "/" + str(self.__capacidad_maxima)
        return texto

    def matricular_estudiante(self, estudiante):
        for e in self.__estudiantes:
            if e.get_codigo() == estudiante.get_codigo():
                raise EstudianteYaMatriculadoError(estudiante.get_codigo(), self.__codigo)
        if len(self.__estudiantes) >= self.__capacidad_maxima:
            raise GrupoLlenoError(self.__codigo, self.__capacidad_maxima)
        self.__estudiantes.append(estudiante)
        return estudiante.get_nombre() + " fue matriculado(a) en el grupo " + self.__codigo + "."

    def retirar_estudiante(self, codigo_estudiantil):
        for e in self.__estudiantes:
            if e.get_codigo() == codigo_estudiantil:
                self.__estudiantes.remove(e)
                return e.get_nombre() + " fue retirado(a) del grupo " + self.__codigo + "."
        raise EstudianteNoMatriculadoError(codigo_estudiantil, self.__codigo)

    def mostrar_estudiantes(self):
        texto = "Estudiantes del grupo " + self.__codigo + ":"
        if len(self.__estudiantes) == 0:
            return texto + "\n  (sin estudiantes matriculados)"
        for e in self.__estudiantes:
            texto += "\n  - " + e.get_codigo() + " | " + e.get_nombre()
        return texto
