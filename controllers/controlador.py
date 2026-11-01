from models.programa import ProgramaAcademico
from models.asignatura import Asignatura
from models.estudiante import Estudiante
from models.docente import Docente
from models.administrativo import Administrativo
from view.vista import Vista
# [AC2 - NUEVO] imports de las nuevas clases
from models.persona import Persona
from models.grupo import GrupoAcademico
from models.excepciones import (EstudianteYaMatriculadoError, GrupoLlenoError,
                                EstudianteNoMatriculadoError, AsignaturaNoEncontradaError,
                                ProgramaNoEncontradoError)

class Controlador:
    def __init__(self):
        self.vista = Vista()
        self.programas = []
        self.asignaturas = []
        self.personas = []  # una sola lista con estudiantes, docentes y administrativos
        self.grupos = []  # [AC2 - NUEVO] lista de grupos académicos

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
        for p in self.personas:
            self.vista.mensaje(p.mostrar_informacion())
            self.vista.mensaje(p.realizar_actividad_principal())
            self.vista.mensaje("")

    # [AC2] A partir de aquí: métodos agregados en la Actividad 2
  

    # [AC2 - NUEVO] Búsquedas que lanzan excepción (Fase 4)
    def buscar_asignatura(self, codigo):
        for a in self.asignaturas:
            if a.get_codigo() == codigo:
                return a
        raise AsignaturaNoEncontradaError(codigo)

    def buscar_programa(self, codigo):
        for p in self.programas:
            if p.get_codigo() == codigo:
                return p
        raise ProgramaNoEncontradoError(codigo)

    # [AC2 - NUEVO] Fase 1: Persona ya no se puede instanciar
    def probar_persona_abstracta(self):
        self.vista.titulo("8. PERSONA ES UNA CLASE ABSTRACTA")
        try:
            Persona("9999", "Persona Genérica", "generica@umanizales.edu.co")
        except TypeError:
            self.vista.error("no se puede crear una Persona directamente porque es una clase abstracta. Debe ser Estudiante, Docente o Administrativo.")
        self.vista.mensaje("El programa continúa su ejecución.")

    # [AC2 - NUEVO] Fase 2 y 3: grupos con su horario
    def crear_grupos(self):
        self.vista.titulo("9. CREACIÓN DE GRUPOS ACADÉMICOS Y HORARIOS")
        asig1 = self.asignaturas[0]
        asig2 = self.asignaturas[1]
        doc1 = self.personas[2]
        doc2 = self.personas[3]

   
        g1 = GrupoAcademico("G01", asig1, doc1, 2, "Lunes", "08:00", "10:00", "B-201")
        g2 = GrupoAcademico("G02", asig1, doc2, 3, "Martes", "10:00", "12:00", "B-305")
        g3 = GrupoAcademico("G03", asig2, doc2, 30, "Jueves", "14:00", "16:00", "A-102")
        self.grupos = [g1, g2, g3]

        for g in self.grupos:
            self.vista.mostrar(g.mostrar_informacion_grupo())

    # [AC2 - NUEVO] Matrículas correctas, duplicada y grupo lleno
    def probar_matriculas(self):
        self.vista.titulo("10. MATRÍCULA DE ESTUDIANTES")
        g1 = self.grupos[0]  # capacidad máxima: 2
        est1 = self.personas[0]
        est2 = self.personas[1]
        est3 = Estudiante("1003", "Valentina Rojas", "valentina@umanizales.edu.co", "E003",
                          self.programas[0], 2, 4.5)
        self.personas.append(est3)

        # Matrículas correctas
        self.vista.mensaje(g1.matricular_estudiante(est1))
        self.vista.mensaje(g1.matricular_estudiante(est2))

        # Matrícula duplicada
        try:
            g1.matricular_estudiante(est1)
        except EstudianteYaMatriculadoError as e:
            self.vista.error(str(e))
        self.vista.mensaje("El programa continúa su ejecución.")

        # Superar la capacidad del grupo
        try:
            g1.matricular_estudiante(est3)
        except GrupoLlenoError as e:
            self.vista.error(str(e))
        self.vista.mensaje("El programa continúa su ejecución.")

        self.vista.mostrar("\n" + g1.mostrar_estudiantes())

    # [AC2 - NUEVO] Retiro correcto y retiro de un estudiante inexistente
    def probar_retiros(self):
        self.vista.titulo("11. RETIRO DE ESTUDIANTES")
        g1 = self.grupos[0]

        self.vista.mensaje(g1.retirar_estudiante("E002"))

        try:
            g1.retirar_estudiante("E002")  # ya fue retirado
        except EstudianteNoMatriculadoError as e:
            self.vista.error(str(e))
        self.vista.mensaje("El programa continúa su ejecución.")

        # Con el cupo liberado, ahora sí se puede matricular al tercer estudiante
        self.vista.mensaje(g1.matricular_estudiante(self.personas[6]))
        self.vista.mostrar("\n" + g1.mostrar_estudiantes())

    # [AC2 - NUEVO] Búsquedas de asignatura y programa inexistentes
    def probar_busquedas(self):
        self.vista.titulo("12. BÚSQUEDAS DE ASIGNATURAS Y PROGRAMAS")
        self.vista.mensaje("Asignatura encontrada: " + self.buscar_asignatura("PROG1").get_nombre())
        self.vista.mensaje("Programa encontrado: " + self.buscar_programa("ISI01").get_nombre())

        try:
            self.buscar_asignatura("XYZ99")
        except AsignaturaNoEncontradaError as e:
            self.vista.error(str(e))
        self.vista.mensaje("El programa continúa su ejecución.")

        try:
            self.buscar_programa("NOEXISTE")
        except ProgramaNoEncontradoError as e:
            self.vista.error(str(e))
        self.vista.mensaje("El programa continúa su ejecución.")

        self.vista.titulo("FIN: el programa terminó con normalidad")

    def ejecutar(self):
        self.crear_programas_y_asignaturas()
        self.crear_personas()
        self.consultar_datos()
        self.modificar_datos_validos()
        self.probar_valores_invalidos()
        self.mostrar_cada_tipo()
        self.recorrido_polimorfico()
        # [AC2 - NUEVO] nuevas fases de la Actividad 2
        self.probar_persona_abstracta()
        self.crear_grupos()
        self.probar_matriculas()
        self.probar_retiros()
        self.probar_busquedas()
