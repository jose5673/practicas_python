# -*- coding: utf-8 -*-

# =================================================================================================
# 📋 FASE 2: HERRAMIENTAS ESENCIALES
# Módulo 2.1: Manejo de Archivos y Excepciones
# =================================================================================================
#
# Python para Automatización Industrial y Desarrollo Web
#
# Autor: GitHub Copilot
# Fecha: 30 de junio de 2025
#
# -------------------------------------------------------------------------------------------------
#
# **ACERCA DE ESTE SCRIPT:**
#
# Este archivo define la secuencia de aprendizaje y los conceptos clave para el Módulo 2.1.
# Sirve como una guía estructurada para entender cómo Python interactúa con el sistema de
# archivos y cómo gestiona los errores en tiempo de ejecución. Dominar estos conceptos es
# esencial para crear aplicaciones robustas y fiables en cualquier campo, especialmente en la
# automatización industrial, donde la integridad de los datos y la estabilidad del
# software son críticas.
#
# -------------------------------------------------------------------------------------------------
#
# **SECUENCIA DE ENSEÑANZA DETALLADA:**
#
# ---
#
# ### PARTE 1: MANEJO DE EXCEPCIONES (LA RED DE SEGURIDAD)
#
# **Concepto Clave:** Los errores ocurren. En lugar de dejar que el programa se caiga,
# los "atrapamos" y decidimos qué hacer.
#
# 1.  **¿Qué es una Excepción?**
#     -   Introducción a los errores en tiempo de ejecución (ej. `ZeroDivisionError`, `FileNotFoundError`).
#     -   Diferencia entre errores de sintaxis (que impiden que el programa corra) y excepciones.
#
# 2.  **El Bloque `try...except`:**
#     -   Sintaxis básica para "intentar" ejecutar un código que podría fallar.
#     -   Atrapar excepciones específicas para manejar diferentes tipos de errores.
#     -   Uso de `as` para obtener el objeto de la excepción y ver el mensaje de error.
#     -   Atrapar múltiples excepciones en un solo bloque `except`.
#
# 3.  **Los Bloques `else` y `finally`:**
#     -   `else`: Código que se ejecuta solo si el bloque `try` **no** lanzó ninguna excepción.
#     -   `finally`: Código que se ejecuta **siempre**, haya habido un error o no. Ideal para
#       acciones de limpieza, como cerrar archivos o conexiones de red.
#
# 4.  **Lanzar Excepciones (`raise`):**
#     -   Cómo y por qué lanzar nuestras propias excepciones para señalar condiciones de
#       error específicas en nuestro código (ej. `raise ValueError("La presión no puede ser negativa")`).
#
# ---
#
# ### PARTE 2: MANEJO DE ARCHIVOS (LA MEMORIA PERSISTENTE)
#
# **Concepto Clave:** Los programas necesitan leer y escribir información que perdure
# más allá de su ejecución.
#
# 1.  **Lectura de Archivos de Texto (`.txt`):**
#     -   La forma moderna y segura: `with open('archivo.txt', 'r') as f:`.
#     -   Explicación de por qué `with` es preferible (cierra el archivo automáticamente).
#     -   Métodos: `.read()`, `.readline()`, `.readlines()`.
#
# 2.  **Escritura en Archivos de Texto:**
#     -   Modo escritura (`'w'`): Sobrescribe el archivo si existe.
#     -   Modo añadir (`'a'`): Agrega contenido al final del archivo.
#     -   Creación de archivos que no existen.
#
# 3.  **Trabajando con Rutas de Archivos:**
#     -   Uso de la librería `pathlib` (el enfoque moderno) para manejar rutas de forma
#       independiente del sistema operativo.
#     -   Diferencia entre rutas relativas y absolutas.
#
# ---
#
# ### PARTE 3: DATOS ESTRUCTURADOS (JSON Y CSV)
#
# **Concepto Clave:** No todos los datos son texto plano. JSON y CSV son estándares para
# intercambiar información de forma estructurada.
#
# 1.  **Módulo `json`:**
#     -   ¿Qué es JSON? (JavaScript Object Notation). Su similitud con los diccionarios de Python.
#     -   `json.dump()`: Escribir un objeto Python (diccionario, lista) a un archivo JSON.
#     -   `json.load()`: Leer un archivo JSON y convertirlo en un objeto Python.
#     -   **Caso de uso industrial:** Guardar la configuración de un dispositivo o los parámetros de un proceso.
#
# 2.  **Módulo `csv`:**
#     -   ¿Qué es CSV? (Comma-Separated Values). Formato tabular ideal para hojas de cálculo.
#     -   `csv.writer`: Escribir datos (listas de listas) en un archivo CSV.
#     -   `csv.reader`: Leer datos de un archivo CSV.
#     -   `csv.DictWriter` y `csv.DictReader`: Trabajar con CSV usando diccionarios.
#     -   **Caso de uso industrial:** Exportar lecturas de sensores tomadas a lo largo del tiempo.
#
# ---
#
# ### PARTE 4: LOGGING (LA CAJA NEGRA DE TU APLICACIÓN)
#
# **Concepto Clave:** En lugar de usar `print()` para depurar, el logging ofrece un sistema
# robusto, configurable y estándar para registrar eventos.
#
# 1.  **Módulo `logging`:**
#     -   Configuración básica: `logging.basicConfig()`.
#     -   Niveles de severidad: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
#     -   Cómo registrar mensajes a cada nivel.
#     -   **Caso de uso industrial:** Registrar un `INFO` cuando se establece conexión con un PLC,
#       un `WARNING` si un valor de sensor está fuera del rango normal, y un `ERROR` si la
#       conexión se pierde.
#     -   Configurar el logging para que escriba a un archivo en lugar de la consola.
#
# -------------------------------------------------------------------------------------------------
#
# **PROYECTO INTEGRADOR DEL MÓDULO:**
#
# Crearemos un script que simule la lectura de datos de varios sensores.
# 1.  La configuración de los sensores (IDs, tipo, rangos) se leerá de un archivo `config.json`.
# 2.  El script intentará leer los valores de cada sensor. Si un sensor da un error (simulado),
#     se manejará la excepción.
# 3.  Todas las lecturas exitosas se guardarán en un archivo `data.csv` con timestamp.
# 4.  Todos los eventos (lecturas correctas, errores, inicio/fin del script) se registrarán
#     en un archivo `log.txt` usando el módulo `logging`.
#
# =================================================================================================

"""
================================================================================
PARTE 1: MANEJO DE EXCEPCIONES (LA RED DE SEGURIDAD)
================================================================================
"""

# ¿Qué es una excepción?
# ----------------------------------------------------------------------------
# Una excepción es un evento que ocurre durante la ejecución de un programa y que
# interrumpe el flujo normal de las instrucciones. Por ejemplo, intentar dividir
# por cero, acceder a un archivo que no existe, o convertir una cadena no numérica
# a entero.

# Ejemplo de excepción:
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"❌ Error: {e}")

# Diferencia entre error de sintaxis y excepción:
# - Error de sintaxis: impide que el programa se ejecute (ej: print('Hola)
# - Excepción: ocurre durante la ejecución (ej: 1/0)

# ----------------------------------------------------------------------------
# El bloque try...except
# ----------------------------------------------------------------------------
try:
    archivo = open('no_existe.txt', 'r')
except FileNotFoundError as e:
    print(f"❌ Archivo no encontrado: {e}")
else:
    print("✅ Archivo abierto correctamente")
    archivo.close()
finally:
    print("🔔 Fin del intento de abrir archivo")

# Puedes capturar varias excepciones:
try:
    x = int(input("Introduce un número: "))
    y = 10 / x
except ValueError:
    print("❌ Debes introducir un número válido.")
except ZeroDivisionError:
    print("❌ No se puede dividir por cero.")

# Lanzar tus propias excepciones:
def leer_presion(valor):
    if valor < 0:
        raise ValueError("La presión no puede ser negativa")
    return valor

try:
    leer_presion(-5)
except ValueError as e:
    print(f"❌ Excepción personalizada: {e}")

"""
================================================================================
PARTE 2: MANEJO DE ARCHIVOS (LA MEMORIA PERSISTENTE)
================================================================================
"""

# Lectura y escritura de archivos de texto
# ----------------------------------------------------------------------------
# Forma moderna y segura:
with open('ejemplo.txt', 'w') as f:
    f.write("Línea 1\nLínea 2\n")

with open('ejemplo.txt', 'r') as f:
    contenido = f.read()
    print(f"📄 Contenido del archivo:\n{contenido}")

# Añadir contenido:
with open('ejemplo.txt', 'a') as f:
    f.write("Línea 3\n")

# Leer línea por línea:
with open('ejemplo.txt', 'r') as f:
    for linea in f:
        print(f"➡️ {linea.strip()}")

# Uso de pathlib para rutas
from pathlib import Path
ruta = Path('ejemplo.txt')
print(f"📁 Ruta absoluta: {ruta.resolve()}")

"""
================================================================================
PARTE 3: DATOS ESTRUCTURADOS (JSON Y CSV)
================================================================================
"""

# JSON
import json
config = {"sensor": "temp1", "rango": [0, 100]}
with open('config.json', 'w') as f:
    json.dump(config, f)

with open('config.json', 'r') as f:
    datos = json.load(f)
    print(f"🔧 Configuración cargada: {datos}")

# CSV
import csv
datos = [["sensor", "valor"], ["temp1", 23.5], ["pres1", 1.2]]
with open('datos.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(datos)

with open('datos.csv', 'r') as f:
    reader = csv.reader(f)
    for fila in reader:
        print(f"📊 {fila}")

"""
================================================================================
PARTE 4: LOGGING (LA CAJA NEGRA DE TU APLICACIÓN)
================================================================================
"""

import logging
logging.basicConfig(filename='log.txt', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')
logging.info('✅ Inicio del script')
logging.warning('⚠️ Valor fuera de rango')
logging.error('❌ Error de conexión con PLC')

print("Consulta el archivo log.txt para ver los eventos registrados.")

"""
================================================================================
SECCIÓN EXTRA: REFUERZO TEÓRICO Y PRÁCTICO
================================================================================
"""

# =============================
# 1. MANEJO DE EXCEPCIONES
# =============================

# ¿Por qué es vital en la industria?
# ----------------------------------------------------------------------------
# Imagina un sistema de monitoreo de presión en una caldera industrial. Si ocurre un error
# (por ejemplo, un sensor desconectado), el sistema debe registrar el evento, notificar y
# continuar funcionando de forma segura, no simplemente detenerse.

# Analogía: El try...except es como el paracaídas de emergencia de un avión: no lo usas siempre,
# pero si algo falla, puede salvar tu misión (¡y tu vida!).

# Buenas prácticas:
# - Captura solo las excepciones que esperas y puedes manejar.
# - No uses except sin especificar el tipo de excepción, salvo en scripts de depuración.
# - Usa finally para liberar recursos (cerrar archivos, conexiones, etc.).
# - Documenta por qué capturas cada excepción.

# Errores comunes:
# - Olvidar cerrar archivos (usa with siempre que puedas).
# - Capturar Exception sin control (puede ocultar bugs graves).
# - No registrar el error (usa logging, no solo print).

# Ejemplo industrial:
try:
    # Simulación: lectura de sensor
    valor = float(input("Introduce la presión del tanque (bar): "))
    if valor < 0:
        raise ValueError("Presión negativa detectada. ¡Revisar sensor!")
    print(f"Presión registrada: {valor} bar")
except ValueError as e:
    logging.error(f"Lectura inválida de presión: {e}")
    print(f"⚠️ Error en la lectura: {e}")
else:
    print("✅ Lectura exitosa.")
finally:
    print("🔔 Fin del ciclo de lectura de presión.")

# Preguntas de reflexión:
# 1. ¿Qué pasaría si no capturamos la excepción ValueError?
# 2. ¿Por qué es mejor registrar el error que solo mostrarlo por pantalla?

# =============================
# 2. MANEJO DE ARCHIVOS
# =============================

# Advertencia: En sistemas industriales, nunca sobrescribas archivos críticos sin backup.
# Usa siempre modos de apertura seguros y verifica la existencia del archivo antes de escribir.

# Ejemplo industrial:
# Guardar logs de temperatura cada minuto en un archivo CSV, añadiendo una nueva línea cada vez.
import time
from datetime import datetime

def registrar_temperatura(valor):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('registro_temp.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, valor])
    logging.info(f"Temperatura registrada: {valor} °C a las {timestamp}")

# Simulación de registro periódico (descomenta para probar en entorno real):
# for i in range(3):
#     temp = 20 + i  # Simulación de lectura
#     registrar_temperatura(temp)
#     time.sleep(1)

# Pregunta de reflexión:
# ¿Por qué es importante registrar la fecha y hora junto con el valor?

# =============================
# 3. JSON Y CSV EN AUTOMATIZACIÓN
# =============================

# Caso real: Configuración de sensores desde un archivo JSON
configuracion = {
    "sensores": [
        {"id": "T1", "tipo": "temperatura", "rango": [0, 100]},
        {"id": "P1", "tipo": "presion", "rango": [0, 10]}
    ]
}
with open('config_sensores.json', 'w') as f:
    json.dump(configuracion, f, indent=4)

with open('config_sensores.json', 'r') as f:
    conf = json.load(f)
    for sensor in conf["sensores"]:
        print(f"🔎 Sensor {sensor['id']} ({sensor['tipo']}), rango: {sensor['rango']}")

# Errores comunes:
# - Olvidar el indent en json.dump (dificulta la lectura humana).
# - No manejar excepciones al leer archivos corruptos o inexistentes.

# =============================
# 4. LOGGING AVANZADO
# =============================

# Buenas prácticas:
# - Usa diferentes niveles según la gravedad (INFO, WARNING, ERROR, CRITICAL).
# - Incluye siempre timestamp y contexto en los logs.
# - No uses print para eventos importantes en producción.

# Ejemplo de logging con contexto:
def log_evento_sensor(sensor_id, valor, estado):
    mensaje = f"Sensor {sensor_id}: valor={valor}, estado={estado}"
    if estado == "OK":
        logging.info(mensaje)
    elif estado == "FUERA DE RANGO":
        logging.warning(mensaje)
    else:
        logging.error(mensaje)

# log_evento_sensor("T1", 105, "FUERA DE RANGO")
# log_evento_sensor("P1", 5, "OK")

# Pregunta de reflexión:
# ¿Por qué es útil diferenciar los niveles de logging?

# =============================
# 5. ERRORES FRECUENTES Y CÓMO EVITARLOS
# =============================

# - No validar datos antes de procesarlos (usa try/except y validaciones previas).
# - No cerrar archivos (usa with siempre).
# - No registrar eventos críticos (usa logging).
# - Sobrescribir archivos importantes accidentalmente (verifica antes de escribir).

# =============================
# 6. AUTOEVALUACIÓN RÁPIDA
# =============================

# 1. ¿Qué diferencia hay entre except Exception y except ValueError?
# 2. ¿Por qué es preferible usar with para abrir archivos?
# 3. ¿Cómo registrarías un error crítico en el log?
# 4. ¿Qué ventajas tiene usar JSON frente a TXT plano para configuraciones?
# 5. ¿Qué ocurre si abres un archivo en modo 'w' y ya existe?

# =============================
# 7. RESUMEN VISUAL
# =============================

# ⚠️ try/except/finally = Red de seguridad
# 📄 with open(...) = Lectura/escritura segura
# 🔧 json/csv = Datos estructurados y portables
# 📝 logging = Bitácora profesional
# 🚨 Valida, documenta y registra todo
