# Sistema de Gestión Académica

Actividad colaborativa N.º 1

## Integrantes
- Juan Sebastián Jaramillo

## Descripción general
Programa en Python que representa la información básica de una universidad: programas académicos, asignaturas y tres tipos de personas (estudiantes, docentes y administrativos). Se hizo con programación orientada a objetos: clases, constructores, encapsulamiento, herencia, sobreescritura y polimorfismo.

## Estructura de los archivos
El proyecto usa el patrón Modelo-Vista-Controlador (MVC):

```
main.py                      -> archivo principal, solo arranca el programa
modelo/
    persona.py               -> clase Persona (clase padre)
    estudiante.py            -> clase Estudiante (hija de Persona)
    docente.py               -> clase Docente (hija de Persona)
    administrativo.py        -> clase Administrativo (hija de Persona)
    programa.py              -> clase ProgramaAcademico
    asignatura.py            -> clase Asignatura
vista/
    vista.py                 -> clase Vista, se encarga de mostrar todo en pantalla
controlador/
    controlador.py           -> clase Controlador, crea los objetos y hace las pruebas
```

- **Modelo:** las clases con los datos y las validaciones. No imprimen nada: los métodos `mostrar_informacion()` y `realizar_actividad_principal()` devuelven el texto, y los setters devuelven `True` o `False`.
- **Vista:** solo imprime los mensajes en pantalla.
- **Controlador:** une las dos partes. Crea los objetos del modelo, ejecuta las pruebas y le pasa los resultados a la vista.

## Cómo ejecutar
Se necesita Python 3. Desde la carpeta del proyecto:

```
python main.py
```

## Herencia, sobreescritura y polimorfismo
- Herencia: `Estudiante`, `Docente` y `Administrativo` heredan de `Persona`, así que no repiten la identificación, el nombre y el correo. Cada hija usa `super().__init__()` para pasarle esos datos a la clase padre y solo agrega sus propios atributos.
- Sobreescritura: los métodos `mostrar_informacion()` y `realizar_actividad_principal()` están en `Persona`, pero cada clase hija los vuelve a escribir con su propia versión. En `mostrar_informacion()` se llama a `super()` para mostrar los datos generales y luego se agregan los datos propios.
- Polimorfismo: en `controlador/controlador.py` hay una sola lista con los 6 objetos y un solo ciclo `for`. En cada vuelta se llaman los dos métodos y Python ejecuta la versión que corresponde al tipo real del objeto, sin usar `if` para preguntar de qué clase es.

## Encapsulamiento
Todos los atributos son privados y se consultan o cambian con métodos `get_` y `set_`. Los setters validan que el correo no sea vacío, que los semestres y créditos sean mayores que cero, y que el promedio esté entre 0 y 5.

## Uso de inteligencia artificial
Se usó una herramienta de IA (Claude) como apoyo para verificar y complementar el código base del proyecto. El código fue revisado y modificado para adaptarlo y comprenderlo.
