# [AC2 - NUEVO] excepciones personalizadas del sistema (Fase 4)

class SistemaAcademicoError(Exception):
    pass


class EstudianteYaMatriculadoError(SistemaAcademicoError):
    #Salta en GrupoAcademico.matricular_estudiante() cuando el estudiante ya está en el grupo.
    def __init__(self, codigo_estudiantil, codigo_grupo):
        self.codigo_estudiantil = codigo_estudiantil
        self.codigo_grupo = codigo_grupo
        super().__init__("El estudiante con código " + codigo_estudiantil
                         + " ya está matriculado en el grupo " + codigo_grupo + ".")


class GrupoLlenoError(SistemaAcademicoError):
    #Salta en GrupoAcademico.matricular_estudiante() cuando el grupo alcanzó su capacidad máxima.
    def __init__(self, codigo_grupo, capacidad_maxima):
        self.codigo_grupo = codigo_grupo
        self.capacidad_maxima = capacidad_maxima
        super().__init__("El grupo " + codigo_grupo + " alcanzó su capacidad máxima de "
                         + str(capacidad_maxima) + " estudiantes.")


class EstudianteNoMatriculadoError(SistemaAcademicoError):
    #Salta en GrupoAcademico.retirar_estudiante() cuando el estudiante no está en el grupo.
    def __init__(self, codigo_estudiantil, codigo_grupo):
        self.codigo_estudiantil = codigo_estudiantil
        self.codigo_grupo = codigo_grupo
        super().__init__("El estudiante con código " + codigo_estudiantil
                         + " no está matriculado en el grupo " + codigo_grupo + ".")


class AsignaturaNoEncontradaError(SistemaAcademicoError):
    #Salta en Controlador.buscar_asignatura() cuando el código no existe.
    def __init__(self, codigo_asignatura):
        self.codigo_asignatura = codigo_asignatura
        super().__init__("No existe una asignatura con el código " + codigo_asignatura + ".")


class ProgramaNoEncontradoError(SistemaAcademicoError):
    #Salta en Controlador.buscar_programa() cuando el código no existe.
    def __init__(self, codigo_programa):
        self.codigo_programa = codigo_programa
        super().__init__("No existe un programa académico con el código " + codigo_programa + ".")
