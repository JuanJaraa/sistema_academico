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

    def crear_personas(self):
        self.vista.titulo("2. CREACIÓN DE PERSONAS")
        prog1 = self.programas[0]
        prog2 = self.programas[1]

        est1 = Estudiante("1001", "Laura Gómez", "laura@umanizales.edu.co", "E001", prog1, 3, 4.2)
        est2 = Estudiante("1002", "Andrés Ruiz", "andres@umanizales.edu.co", "E002", prog2, 5, 3.8)
        doc1 = Docente("2001", "Carlos Pérez", "carlos@umanizales.edu.co", "D001", "Ciencias e Ingenierías", "Tiempo completo", 40)
        doc2 = Docente("2002", "María Torres", "maria@umanizales.edu.co", "D002", "Ciencias e Ingenierías", "Cátedra", 12)
        adm1 = Administrativo("3001", "Sofía Díaz", "sofia@umanizales.edu.co", "A001", "Registro Académico", "Secretaria", "Diurna")
        adm2 = Administrativo("3002", "Juan Castro", "juan@umanizales.edu.co", "A002", "Bienestar Universitario", "Coordinador", "Mixta")

        self.personas = [est1, est2, doc1, doc2, adm1, adm2]
        self.vista.mensaje("Se crearon " + str(len(self.personas)) + " personas.")

    def consultar_datos(self):
        self.vista.titulo("3. CONSULTA DE INFORMACIÓN")
        est1 = self.personas[0]
        doc1 = self.personas[2]
        asig1 = self.asignaturas[0]
        self.vista.mensaje("Programa de Laura: " + est1.get_programa().get_nombre())
        self.vista.mensaje("Correo de Carlos: " + doc1.get_correo())
        self.vista.mensaje("Créditos de " + asig1.get_nombre() + ": " + str(asig1.get_creditos()))

    def modificar_datos_validos(self):
        self.vista.titulo("4. MODIFICACIONES VÁLIDAS")
        est1 = self.personas[0]
        prog1 = self.programas[0]
        asig1 = self.asignaturas[0]

        est1.set_correo("laura.gomez@umanizales.edu.co")
        prog1.set_num_semestres(9)
        asig1.set_creditos(4)

        self.vista.mensaje("Nuevo correo de Laura: " + est1.get_correo())
        self.vista.mensaje("Nuevos semestres de " + prog1.get_nombre() + ": " + str(prog1.get_num_semestres()))
        self.vista.mensaje("Nuevos créditos de " + asig1.get_nombre() + ": " + str(asig1.get_creditos()))

    def probar_valores_invalidos(self):
        self.vista.titulo("5. INTENTOS DE VALORES INVÁLIDOS")
        est1 = self.personas[0]
        est2 = self.personas[1]
        prog1 = self.programas[0]
        asig1 = self.asignaturas[0]

        # Los setters devuelven False cuando el valor no es válido
        if not est1.set_correo(""):
            self.vista.error("el correo no puede estar vacío.")
        if not prog1.set_num_semestres(0):
            self.vista.error("el número de semestres debe ser mayor que cero.")
        if not asig1.set_creditos(-2):
            self.vista.error("el número de créditos debe ser mayor que cero.")
        if not est2.set_promedio(7):
            self.vista.error("el promedio debe estar entre 0 y 5.")

        self.vista.mensaje("Los valores no cambiaron: " + est1.get_correo() + ", "
                           + str(prog1.get_num_semestres()) + ", " + str(asig1.get_creditos()))

    def mostrar_cada_tipo(self):
        self.vista.titulo("6. PRESENTACIÓN DE CADA TIPO DE PERSONA")
        self.vista.mostrar(self.personas[0].mostrar_informacion())
        self.vista.mostrar(self.personas[2].mostrar_informacion())
        self.vista.mostrar(self.personas[4].mostrar_informacion())

    def recorrido_polimorfico(self):
        self.vista.titulo("7. RECORRIDO POLIMÓRFICO")
        # Un solo ciclo, sin preguntar el tipo: Python usa la versión de cada clase
        for p in self.personas:
            self.vista.mensaje(p.mostrar_informacion())
            self.vista.mensaje(p.realizar_actividad_principal())
            self.vista.mensaje("")

    def ejecutar(self):
        self.crear_programas_y_asignaturas()
        self.crear_personas()
        self.consultar_datos()
        self.modificar_datos_validos()
        self.probar_valores_invalidos()
        self.mostrar_cada_tipo()
        self.recorrido_polimorfico()
