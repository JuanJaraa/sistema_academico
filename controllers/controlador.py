from models.programa import ProgramaAcademico
from models.asignatura import Asignatura
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo
from view.vista import Vista

class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.programas = []
        self.asignaturas = []
        self.personas = []  # una sola lista con estudiantes, docentes y administrativos

    def crear_programas_y_asignaturas(self):
        self.vista.titulo("1. CREACIÓN DE PROGRAMAS Y ASIGNATURAS")
        prog1 = ProgramaAcademico("ISI01", "Ingeniería de Sistemas", "Ciencias e Ingenierías", 10)
        prog2 = ProgramaAcademico("IND01", "Ingeniería Industrial", "Ciencias e Ingenierías", 10)
        self.programas = [prog1, prog2]

        asig1 = Asignatura("PROG1", "Programación Orientada a Objetos", 3, prog1)
        asig2 = Asignatura("CAL1", "Cálculo Diferencial", 4, prog2)
        self.asignaturas = [asig1, asig2]

        for p in self.programas:
            self.vista.mostrar(p.mostrar_informacion())
        for a in self.asignaturas:
            self.vista.mostrar(a.mostrar_informacion())
