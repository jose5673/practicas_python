# -*- coding: utf-8 -*-

# =================================================================================================
# 📋 FASE 2: HERRAMIENTAS ESENCIALES
# Módulo 2.2: Librerías Fundamentales
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
# Este archivo desarrolla la teoría, ejemplos y buenas prácticas para el uso de librerías
# fundamentales en la automatización industrial con Python. Cada sección incluye contexto
# industrial, advertencias, analogías, errores comunes y preguntas de reflexión.
#
# -------------------------------------------------------------------------------------------------
#
# **SECUENCIA DE ENSEÑANZA DETALLADA:**
#
# ---
#
# ### PARTE 1: datetime — Fechas y Tiempos en la Industria
#
# - ¿Por qué es vital registrar timestamps en procesos industriales?
# - Ejemplo: registrar la hora exacta de una alarma o evento.
# - Uso de datetime.now(), strftime(), timedelta.
# - Buenas prácticas: siempre usa formato ISO o explícito para fechas.
# - Errores comunes: confundir formatos, zonas horarias.
# - Pregunta: ¿Por qué es importante la trazabilidad temporal en auditoría industrial?
#
# ---
#
# ### PARTE 2: os y pathlib — Interacción con el Sistema de Archivos
#
# - ¿Por qué automatizar tareas de archivos y carpetas?
# - Ejemplo: crear backups automáticos, listar logs, mover archivos históricos.
# - Uso de os.listdir(), os.makedirs(), pathlib.Path, Path.glob().
# - Buenas prácticas: rutas relativas vs absolutas, manejo multiplataforma.
# - Advertencia: nunca borres archivos críticos sin confirmación.
# - Pregunta: ¿Cómo garantizarías que tus scripts funcionen en Windows y Linux?
#
# ---
#
# ### PARTE 3: requests — Comunicación con APIs y Dispositivos
#
# - ¿Por qué es clave en la industria moderna?
# - Ejemplo: consultar una API de clima para ajustar procesos, comunicarte con un PLC vía REST.
# - Uso de requests.get(), requests.post(), manejo de respuestas y errores.
# - Buenas prácticas: manejo de timeouts, validación de respuestas, logging de peticiones.
# - Errores comunes: no validar status_code, no manejar excepciones de red.
# - Pregunta: ¿Qué riesgos hay si tu sistema depende de una API externa?
#
# ---
#
# ### PARTE 4: threading — Concurrencia Básica
#
# - ¿Por qué ejecutar tareas en paralelo?
# - Ejemplo: leer sensores y registrar datos mientras se monitorea una alarma.
# - Uso de threading.Thread, start(), join().
# - Buenas prácticas: evitar condiciones de carrera, usar locks si es necesario.
# - Advertencia: la concurrencia puede complicar el debug y la trazabilidad.
# - Pregunta: ¿Cuándo es mejor usar procesos en vez de hilos?
#
# -------------------------------------------------------------------------------------------------
#
# **PROYECTO INTEGRADOR DEL MÓDULO:**
#
# Desarrolla un script que:
# 1. Obtenga datos de una API (simulada o real) y los registre con timestamp.
# 2. Guarde los datos en archivos organizados por fecha usando pathlib/os.
# 3. Ejecute la recolección de datos en paralelo con el monitoreo de un archivo de logs.
# 4. Registre todos los eventos y errores usando logging.
#
# =================================================================================================
#
# """
# ================================================================================================
# SECCIÓN EXTRA: OTRAS LIBRERÍAS FUNDAMENTALES PARA AUTOMATIZACIÓN
# ================================================================================================
# """

# =============================
# 5. sys — Interacción con el sistema y argumentos de línea de comandos
# =============================
# - Permite acceder a argumentos, información del sistema y terminar scripts de forma controlada.
# - Ejemplo: recibir parámetros de configuración al ejecutar un script industrial.
# - sys.argv, sys.exit(), sys.platform
# - Advertencia: valida siempre los argumentos antes de usarlos.
# - Pregunta: ¿Cómo harías un script que reciba el nombre de un archivo de configuración por línea de comandos?

# =============================
# 6. time — Esperas, medición y temporización
# =============================
# - time.sleep() para pausar procesos (ej: muestreo periódico de sensores).
# - time.time() para medir duración de procesos.
# - Ejemplo: esperar 5 segundos entre lecturas de sensores.
# - Advertencia: no abuses de sleep en sistemas críticos de tiempo real.
# - Pregunta: ¿Por qué es importante medir el tiempo de ejecución de tareas industriales?

# =============================
# 7. shutil — Operaciones avanzadas con archivos y carpetas
# =============================
# - Copiar, mover, eliminar archivos y directorios de forma robusta.
# - Ejemplo: backup automático de logs o configuraciones.
# - shutil.copy(), shutil.move(), shutil.rmtree()
# - Advertencia: ¡Cuidado al borrar carpetas completas!
# - Pregunta: ¿Cómo automatizarías el backup diario de archivos críticos?

# =============================
# 8. subprocess — Ejecución de comandos externos
# =============================
# - Permite lanzar otros programas o scripts desde Python.
# - Ejemplo: ejecutar un script de diagnóstico externo o un comando del sistema.
# - subprocess.run(), subprocess.Popen()
# - Buenas prácticas: captura la salida y los errores, nunca ejecutes comandos inseguros.
# - Pregunta: ¿Cuándo es útil integrar Python con herramientas externas en la industria?

# =============================
# 9. math y statistics — Cálculos matemáticos y estadísticos
# =============================
# - math: operaciones matemáticas avanzadas (trigonometría, logaritmos, potencias).
# - statistics: media, mediana, desviación estándar, etc.
# - Ejemplo: calcular promedios y tendencias de sensores.
# - Advertencia: valida siempre los datos antes de calcular estadísticas.
# - Pregunta: ¿Por qué es útil analizar tendencias estadísticas en mantenimiento predictivo?

# =============================
# 10. enum — Enumeraciones para estados y modos
# =============================
# - Permite definir conjuntos de valores simbólicos (estados, modos de operación).
# - Ejemplo: estados de un motor (APAGADO, ENCENDIDO, FALLA).
# - from enum import Enum
# - Buenas prácticas: usa enums para evitar errores de escritura y mejorar la legibilidad.
# - Pregunta: ¿Cómo usarías enums para modelar los estados de una máquina?

# =============================
# 11. BONUS: logging avanzado
# =============================
# - Configuración de logs rotativos (logging.handlers.RotatingFileHandler).
# - Registro de logs en diferentes archivos según el nivel.
# - Ejemplo: logs de errores críticos separados de logs informativos.
# - Pregunta: ¿Por qué separar los logs por nivel puede facilitar el mantenimiento?

"""
================================================================================
DESARROLLO TEÓRICO COMPLETO CON EJEMPLOS Y CÓDIGO
================================================================================
"""

# =============================
# 1. DATETIME — LA CRONOLOGÍA INDUSTRIAL
# =============================

# ¿Por qué es VITAL en la industria?
# ----------------------------------------------------------------------------
# 🏭 En una planta química, cada evento debe tener timestamp preciso para auditorías.
# ⚠️ Un error de 1 segundo en el registro puede significar millones en seguros.
# 🔍 El análisis de tendencias temporales permite mantenimiento predictivo.

# Analogía: El datetime es como el reloj maestro de una orquesta industrial
print("📅 === EJEMPLOS DATETIME ===")

from datetime import datetime, timedelta
import time

# Ejemplo 1: Registro de eventos con timestamp
evento_inicio = datetime.now()
print(f"🕐 Proceso iniciado: {evento_inicio}")
print(f"🕐 Formato ISO: {evento_inicio.isoformat()}")
print(f"🕐 Formato personalizado: {evento_inicio.strftime('%d/%m/%Y %H:%M:%S')}")

# Ejemplo 2: Cálculo de duraciones (crucial para SLA industriales)
time.sleep(2)  # Simula proceso
evento_fin = datetime.now()
duracion = evento_fin - evento_inicio
print(f"⏱️ Duración del proceso: {duracion.total_seconds():.2f} segundos")

# Ejemplo 3: Programación de mantenimientos
proximo_mantenimiento = datetime.now() + timedelta(days=30, hours=8)
print(f"🔧 Próximo mantenimiento programado: {proximo_mantenimiento.strftime('%d/%m/%Y a las %H:%M')}")

# Buenas prácticas industriales:
# ✅ Siempre usa UTC para sistemas distribuidos
# ✅ Registra timezone si trabajas con múltiples ubicaciones
# ⚠️ NUNCA uses solo time.time() para logs críticos (difícil de leer)

print("\n" + "="*50)

# =============================
# 2. OS Y PATHLIB — EL SISTEMA DE ARCHIVOS COMO ALMACÉN
# =============================

print("📁 === EJEMPLOS OS Y PATHLIB ===")

import os
from pathlib import Path

# ¿Por qué automatizar archivos en la industria?
# 🏭 Backups automáticos de configuraciones críticas
# 📊 Organización de logs por fecha/turno/línea de producción  
# 🗂️ Limpieza automática de archivos antiguos

# Ejemplo 1: Crear estructura de carpetas para logs diarios
fecha_hoy = datetime.now().strftime('%Y-%m-%d')
ruta_logs = Path(f"logs/{fecha_hoy}")
ruta_logs.mkdir(parents=True, exist_ok=True)
print(f"📂 Carpeta creada: {ruta_logs}")

# Ejemplo 2: Listar archivos con filtros (buscar logs de errores)
archivos_py = list(Path('.').glob('*.py'))
print(f"🐍 Archivos Python encontrados: {len(archivos_py)}")
for archivo in archivos_py[:3]:  # Mostrar solo los primeros 3
    print(f"   📄 {archivo.name}")

# Ejemplo 3: Información del sistema (crucial para diagnósticos)
print(f"💻 Sistema operativo: {os.name}")
print(f"📁 Directorio actual: {Path.cwd()}")
print(f"👤 Usuario actual: {os.getenv('USERNAME', 'Desconocido')}")

# Advertencias industriales:
# ⚠️ NUNCA borres archivos sin confirmar la existencia de backups
# ⚠️ Usa rutas absolutas para scripts críticos
# ✅ Siempre maneja excepciones al crear/mover archivos

print("\n" + "="*50)

# =============================
# 3. REQUESTS — EL PUENTE HACIA EL MUNDO EXTERIOR
# =============================

print("🌐 === EJEMPLOS REQUESTS (simulados) ===")

# ¿Por qué es clave en Industria 4.0?
# 🏭 APIs de proveedores de energía para optimizar consumo
# 🌡️ APIs meteorológicas para ajustar procesos según clima
# 📊 Comunicación con sistemas ERP/MES via REST

# Nota: Por ser un ejemplo didáctico, simularemos las respuestas
# En la práctica real, usarías APIs reales

try:
    # Simulación de consulta a API meteorológica
    print("🌤️ Consultando API del clima...")
    # respuesta = requests.get('https://api.clima.com/actual', timeout=5)
    # Simulamos la respuesta:
    temperatura_externa = 22.5
    print(f"🌡️ Temperatura externa: {temperatura_externa}°C")
    
    # Lógica de negocio basada en clima
    if temperatura_externa > 25:
        print("❄️ Activando sistema de refrigeración adicional")
    else:
        print("✅ Temperatura normal, sin acciones adicionales")
        
except Exception as e:
    print(f"❌ Error al consultar API: {e}")
    print("🔄 Usando valores por defecto para continuar operación")

# Buenas prácticas para APIs industriales:
# ✅ Siempre usa timeout para evitar bloqueos
# ✅ Valida el status_code antes de procesar respuesta
# ✅ Implementa reintentos con backoff exponencial
# ⚠️ Ten siempre un plan B si la API falla

print("\n" + "="*50)

# =============================
# 4. THREADING — PARALELISMO CONTROLADO
# =============================

print("⚡ === EJEMPLOS THREADING ===")

import threading
import time

# ¿Por qué paralelismo en la industria?
# 🏭 Monitorear sensores mientras se ejecutan procesos
# 📊 Procesar datos mientras se recolectan nuevos
# 🚨 Sistema de alarmas independiente del proceso principal

def monitorear_sensor(sensor_id, duracion=3):
    """Simula el monitoreo continuo de un sensor"""
    for i in range(duracion):
        valor = 20 + i * 2  # Simula lectura creciente
        print(f"📊 Sensor {sensor_id}: {valor}°C")
        time.sleep(1)
    print(f"✅ Monitoreo del sensor {sensor_id} completado")

def procesar_datos():
    """Simula procesamiento de datos en paralelo"""
    print("⚙️ Iniciando procesamiento de datos...")
    time.sleep(2)
    print("✅ Procesamiento completado")

# Ejecutar tareas en paralelo
print("🚀 Iniciando monitoreo paralelo...")
hilo_sensor1 = threading.Thread(target=monitorear_sensor, args=("TEMP-01", 3))
hilo_sensor2 = threading.Thread(target=monitorear_sensor, args=("TEMP-02", 3))
hilo_procesamiento = threading.Thread(target=procesar_datos)

# Iniciar todos los hilos
hilo_sensor1.start()
hilo_sensor2.start()
hilo_procesamiento.start()

# Esperar a que terminen todos
hilo_sensor1.join()
hilo_sensor2.join()
hilo_procesamiento.join()

print("🎯 Todas las tareas paralelas completadas")

# Advertencias sobre threading:
# ⚠️ La concurrencia complica el debugging
# ⚠️ Cuidado con recursos compartidos (usa locks si es necesario)
# ✅ Úsalo para I/O bound tasks, no CPU intensive

print("\n" + "="*50)

# =============================
# 5. MATH Y STATISTICS — INTELIGENCIA DE DATOS
# =============================

print("📈 === EJEMPLOS MATH Y STATISTICS ===")

import math
import statistics

# ¿Por qué matemáticas en la industria?
# 📊 Análisis de tendencias para mantenimiento predictivo
# 🔢 Cálculos de eficiencia energética
# 📈 Control estadístico de procesos

# Simulación: lecturas de un sensor de vibración
lecturas_vibracion = [2.1, 2.3, 2.0, 2.4, 2.2, 2.8, 2.1, 2.5, 2.3, 2.6]

# Análisis estadístico básico
media = statistics.mean(lecturas_vibracion)
mediana = statistics.median(lecturas_vibracion)
desviacion = statistics.stdev(lecturas_vibracion)

print(f"📊 Análisis de vibraciones:")
print(f"   📈 Media: {media:.2f} mm/s")
print(f"   📊 Mediana: {mediana:.2f} mm/s")
print(f"   📉 Desviación estándar: {desviacion:.2f} mm/s")

# Detección de anomalías (regla 3-sigma)
limite_superior = media + 3 * desviacion
limite_inferior = media - 3 * desviacion

anomalias = [x for x in lecturas_vibracion if x > limite_superior or x < limite_inferior]
if anomalias:
    print(f"🚨 ALARMA: Vibraciones anómalas detectadas: {anomalias}")
else:
    print("✅ Todas las lecturas dentro de parámetros normales")

# Cálculos avanzados con math
print(f"📐 Cálculos adicionales:")
print(f"   🔢 Raíz cuadrada de la media: {math.sqrt(media):.2f}")
print(f"   📊 Logaritmo natural de la media: {math.log(media):.2f}")

print("\n" + "="*50)

# =============================
# 6. ENUM — ESTADOS INDUSTRIALES BIEN DEFINIDOS
# =============================

print("🏷️ === EJEMPLOS ENUM ===")

from enum import Enum, auto

# ¿Por qué enums en la industria?
# 🏭 Estados claros y sin ambigüedad
# 🔧 Modos de operación bien definidos
# ⚠️ Prevención de errores por valores incorrectos

class EstadoMotor(Enum):
    APAGADO = 0
    ENCENDIDO = 1
    FALLA = 2
    MANTENIMIENTO = 3

class ModoOperacion(Enum):
    AUTOMATICO = auto()
    MANUAL = auto()
    EMERGENCIA = auto()

# Ejemplo de uso en lógica industrial
def evaluar_motor(estado_actual):
    if estado_actual == EstadoMotor.APAGADO:
        return "⚫ Motor detenido - Seguro para mantenimiento"
    elif estado_actual == EstadoMotor.ENCENDIDO:
        return "🟢 Motor funcionando - Operación normal"
    elif estado_actual == EstadoMotor.FALLA:
        return "🔴 Motor en falla - Revisar inmediatamente"
    elif estado_actual == EstadoMotor.MANTENIMIENTO:
        return "🟡 Motor en mantenimiento - No operar"

# Simulación de estados
motor_principal = EstadoMotor.ENCENDIDO
modo_actual = ModoOperacion.AUTOMATICO

print(f"🏭 Estado del sistema:")
print(f"   🔧 Motor: {evaluar_motor(motor_principal)}")
print(f"   ⚙️ Modo: {modo_actual.name}")

# Ventajas de usar enums:
# ✅ Código más legible y mantenible
# ✅ Autocompletado en IDEs
# ✅ Imposible usar valores incorrectos

print("\n" + "="*80)
print("🎯 FIN DE EJEMPLOS TEÓRICOS - LISTOS PARA LAS PRÁCTICAS")
