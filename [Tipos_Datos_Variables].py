"""
📚 TEMARIO: TIPOS DE DATOS Y VARIABLES EN PYTHON
==================================================

🎯 OBJETIVO DE APRENDIZAJE:
Dominar completamente los tipos de datos fundamentales de Python y el manejo de variables,
estableciendo una base sólida para todo el desarrollo posterior.

📖 BASADO EN: "Curso Intensivo de Python" - Eric Matthes (Capítulos 2-3)

🗓️ FECHA: 30 de junio de 2025
👨‍🏫 TUTOR: GitHub Copilot (Experto en Python)
👨‍🎓 ESTUDIANTE: José

═══════════════════════════════════════════════════════════════════════════════
SECUENCIA DE ENSEÑANZA DETALLADA
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 1: FUNDAMENTOS - ¿QUÉ SON LAS VARIABLES?
# ═══════════════════════════════════════════════════════════════════════════════

def paso_1_introduccion_variables():
    """
    🎯 OBJETIVO: Entender qué son las variables y por qué son fundamentales
    
    💡 ANALOGÍA: Las variables son como "cajas etiquetadas" donde guardamos información
    que podemos usar más tarde en nuestro programa.
    """
    print("=" * 60)
    print("PASO 1: INTRODUCCIÓN A LAS VARIABLES")
    print("=" * 60)
    
    # Ejemplo básico de variable
    nombre = "José"
    edad = 30
    
    print(f"Mi nombre es {nombre} y tengo {edad} años")
    print(f"Tipo de 'nombre': {type(nombre)}")
    print(f"Tipo de 'edad': {type(edad)}")
    
    # ¿Por qué son importantes las variables?
    print("\n🔍 ANÁLISIS:")
    print("- Las variables nos permiten REUTILIZAR información")
    print("- Hacen nuestro código más LEGIBLE y MANTENIBLE")
    print("- Podemos MODIFICAR valores fácilmente")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 2: TIPOS DE DATOS NUMÉRICOS
# ═══════════════════════════════════════════════════════════════════════════════

def paso_2_tipos_numericos():
    """
    🎯 OBJETIVO: Dominar enteros (int) y decimales (float)
    
    📊 CASOS DE USO:
    - int: Contadores, edades, cantidades exactas
    - float: Mediciones, cálculos científicos, precios
    """
    print("\n" + "=" * 60)
    print("PASO 2: TIPOS DE DATOS NUMÉRICOS")
    print("=" * 60)
    
    # ENTEROS (int)
    print("\n🔢 ENTEROS (int):")
    cantidad_sensores = 5
    temperatura_maxima = 85
    presion_minima = -10
    
    print(f"Cantidad de sensores: {cantidad_sensores} (tipo: {type(cantidad_sensores)})")
    print(f"Temperatura máxima: {temperatura_maxima}°C")
    print(f"Presión mínima: {presion_minima} bar")
    
    # DECIMALES (float)
    print("\n🎯 DECIMALES (float):")
    voltaje_sensor = 3.3
    corriente_maxima = 2.5
    precision_medicion = 0.001
    
    print(f"Voltaje del sensor: {voltaje_sensor}V (tipo: {type(voltaje_sensor)})")
    print(f"Corriente máxima: {corriente_maxima}A")
    print(f"Precisión de medición: {precision_medicion}")
    
    # OPERACIONES MATEMÁTICAS FUNDAMENTALES
    print("\n➕ OPERACIONES BÁSICAS:")
    a = 15
    b = 4
    
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    print(f"División entera: {a} // {b} = {a // b}")
    print(f"Módulo (resto): {a} % {b} = {a % b}")
    print(f"Potencia: {a} ** {b} = {a ** b}")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 3: CADENAS DE TEXTO (STRINGS)
# ═══════════════════════════════════════════════════════════════════════════════

def paso_3_strings():
    """
    🎯 OBJETIVO: Manipular texto de forma profesional
    
    🔧 APLICACIONES EN AUTOMATIZACIÓN:
    - Nombres de dispositivos
    - Mensajes de estado
    - Reportes y logs
    - Interfaces de usuario
    """
    print("\n" + "=" * 60)
    print("PASO 3: CADENAS DE TEXTO (STRINGS)")
    print("=" * 60)
    
    # CREACIÓN DE STRINGS
    print("\n📝 CREACIÓN DE STRINGS:")
    dispositivo = "Sensor de Temperatura"
    estado = 'Operativo'
    mensaje_largo = """Este es un mensaje
    que puede ocupar
    múltiples líneas"""
    
    print(f"Dispositivo: {dispositivo}")
    print(f"Estado: {estado}")
    print(f"Mensaje largo:\n{mensaje_largo}")
    
    # MÉTODOS FUNDAMENTALES DE STRINGS
    print("\n🔧 MÉTODOS IMPORTANTES:")
    texto_ejemplo = "  PyModbus Industrial Control  "
    
    print(f"Original: '{texto_ejemplo}'")
    print(f"Mayúsculas: '{texto_ejemplo.upper()}'")
    print(f"Minúsculas: '{texto_ejemplo.lower()}'")
    print(f"Sin espacios: '{texto_ejemplo.strip()}'")
    print(f"Reemplazar: '{texto_ejemplo.replace('Industrial', 'Automation')}'")
    print(f"Longitud: {len(texto_ejemplo)} caracteres")
    
    # F-STRINGS: LA FORMA MODERNA Y PROFESIONAL
    print("\n🚀 F-STRINGS (FORMATEO MODERNO):")
    sensor_id = 101
    valor_leido = 23.7
    unidad = "°C"
    
    reporte = f"Sensor ID: {sensor_id} | Valor: {valor_leido}{unidad} | Estado: OK"
    print(f"Reporte: {reporte}")
    
    # Formateo avanzado
    precio = 1234.567
    print(f"Precio formateado: ${precio:.2f}")
    print(f"Porcentaje: {0.856:.1%}")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 4: VALORES BOOLEANOS (BOOL)
# ═══════════════════════════════════════════════════════════════════════════════

def paso_4_booleanos():
    """
    🎯 OBJETIVO: Entender los valores True/False para control de flujo
    
    ⚡ CRÍTICO PARA:
    - Condiciones (if/else)
    - Bucles (while)
    - Estados de sistema (on/off)
    - Validaciones
    """
    print("\n" + "=" * 60)
    print("PASO 4: VALORES BOOLEANOS (BOOL)")
    print("=" * 60)
    
    # VALORES BOOLEANOS BÁSICOS
    print("\n✅ VALORES BÁSICOS:")
    sistema_activo = True
    error_detectado = False
    
    print(f"Sistema activo: {sistema_activo} (tipo: {type(sistema_activo)})")
    print(f"Error detectado: {error_detectado}")
    
    # COMPARACIONES QUE GENERAN BOOLEANOS
    print("\n🔍 COMPARACIONES:")
    temperatura = 75
    limite_superior = 80
    limite_inferior = 20
    
    print(f"Temperatura actual: {temperatura}°C")
    print(f"¿Temperatura alta? {temperatura > limite_superior}")
    print(f"¿Temperatura baja? {temperatura < limite_inferior}")
    print(f"¿Temperatura normal? {limite_inferior <= temperatura <= limite_superior}")
    print(f"¿Temperatura exacta a 75? {temperatura == 75}")
    print(f"¿Temperatura diferente a 80? {temperatura != 80}")
    
    # OPERADORES LÓGICOS
    print("\n🧠 OPERADORES LÓGICOS:")
    presion_ok = True
    temperatura_ok = True
    nivel_ok = False
    
    print(f"Sistema operativo: {presion_ok and temperatura_ok and nivel_ok}")
    print(f"Al menos un parámetro OK: {presion_ok or temperatura_ok or nivel_ok}")
    print(f"Sistema NO operativo: {not (presion_ok and temperatura_ok and nivel_ok)}")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 5: CONVERSIONES ENTRE TIPOS (TYPE CASTING)
# ═══════════════════════════════════════════════════════════════════════════════

def paso_5_conversiones():
    """
    🎯 OBJETIVO: Convertir entre diferentes tipos de datos
    
    🛠️ ESENCIAL PARA:
    - Leer datos de sensores (strings a números)
    - Mostrar números como texto
    - Validar entradas de usuario
    - Procesar datos de archivos
    """
    print("\n" + "=" * 60)
    print("PASO 5: CONVERSIONES ENTRE TIPOS")
    print("=" * 60)
    
    # CONVERSIONES BÁSICAS
    print("\n🔄 CONVERSIONES COMUNES:")
    
    # String a número
    valor_texto = "42.5"
    valor_numero = float(valor_texto)
    print(f"De string a float: '{valor_texto}' → {valor_numero}")
    
    # Número a string
    temperatura_sensor = 23.7
    temp_texto = str(temperatura_sensor)
    print(f"De float a string: {temperatura_sensor} → '{temp_texto}'")
    
    # Float a int (¡CUIDADO! Se pierde la parte decimal)
    medicion = 23.8
    medicion_entera = int(medicion)
    print(f"De float a int: {medicion} → {medicion_entera} (se trunca)")
    
    # CONVERSIONES CON BOOLEANOS
    print("\n🔢 CONVERSIONES CON BOOLEANOS:")
    print(f"bool(1): {bool(1)}")
    print(f"bool(0): {bool(0)}")
    print(f"bool('texto'): {bool('texto')}")
    print(f"bool(''): {bool('')}")
    print(f"int(True): {int(True)}")
    print(f"int(False): {int(False)}")
    
    # EJEMPLO PRÁCTICO: PROCESANDO DATOS DE SENSOR
    print("\n🌡️ EJEMPLO PRÁCTICO - DATOS DE SENSOR:")
    datos_sensor = "25.3,78.1,23.9"  # Simula datos CSV
    valores = datos_sensor.split(',')
    print(f"Datos recibidos: {valores}")
    
    temperaturas = [float(temp) for temp in valores]
    print(f"Convertido a números: {temperaturas}")
    print(f"Temperatura promedio: {sum(temperaturas) / len(temperaturas):.1f}°C")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 6: BUENAS PRÁCTICAS Y CONVENCIONES
# ═══════════════════════════════════════════════════════════════════════════════

def paso_6_buenas_practicas():
    """
    🎯 OBJETIVO: Escribir código profesional y mantenible
    
    📋 ESTÁNDARES PEP 8:
    - Nombres descriptivos
    - snake_case para variables
    - CONSTANTES en MAYÚSCULAS
    - Comentarios útiles
    """
    print("\n" + "=" * 60)
    print("PASO 6: BUENAS PRÁCTICAS DE PROGRAMACIÓN")
    print("=" * 60)
    
    # NOMBRES DESCRIPTIVOS
    print("\n📝 NOMBRES DESCRIPTIVOS:")
    
    # ❌ MAL
    t = 25
    s = "ON"
    
    # ✅ BIEN
    temperatura_ambiente = 25
    estado_bomba = "ON"
    
    print("❌ Evitar: t = 25, s = 'ON'")
    print("✅ Mejor: temperatura_ambiente = 25, estado_bomba = 'ON'")
    
    # CONSTANTES
    print("\n🔒 CONSTANTES (valores que no cambian):")
    TEMPERATURA_MAXIMA = 85
    PRESION_MINIMA = 1.0
    PUERTO_MODBUS = 502
    
    print(f"Temperatura máxima permitida: {TEMPERATURA_MAXIMA}°C")
    print(f"Presión mínima: {PRESION_MINIMA} bar")
    print(f"Puerto Modbus: {PUERTO_MODBUS}")
    
    # COMENTARIOS ÚTILES
    print("\n💬 COMENTARIOS EXPLICATIVOS:")
    # Configuración del sensor de temperatura
    sensor_temp_id = 101  # ID único del sensor
    rango_operacion = (-40, 125)  # Rango en grados Celsius
    precision = 0.1  # Precisión en grados
    
    print(f"Sensor configurado - ID: {sensor_temp_id}")
    print(f"Rango de operación: {rango_operacion[0]}°C a {rango_operacion[1]}°C")
    print(f"Precisión: ±{precision}°C")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 7: EJEMPLO INTEGRADOR PRÁCTICO
# ═══════════════════════════════════════════════════════════════════════════════

def paso_7_ejemplo_integrador():
    """
    🎯 OBJETIVO: Aplicar todos los conceptos en un ejemplo real
    
    🏭 ESCENARIO: Sistema de monitoreo industrial básico
    Combina todos los tipos de datos aprendidos
    """
    print("\n" + "=" * 60)
    print("PASO 7: EJEMPLO INTEGRADOR - SISTEMA DE MONITOREO")
    print("=" * 60)
    
    # DATOS DEL SISTEMA
    print("\n🏭 CONFIGURACIÓN DEL SISTEMA:")
    
    # String: Información descriptiva
    nombre_planta = "Planta Industrial ABC"
    ubicacion = "Sector Norte"
    
    # Enteros: Identificadores y contadores
    numero_sensores = 8
    sensor_temperatura_id = 101
    sensor_presion_id = 102
    
    # Floats: Mediciones
    temperatura_actual = 73.5
    presion_actual = 2.3
    voltaje_alimentacion = 24.0
    
    # Booleanos: Estados
    sistema_operativo = True
    mantenimiento_programado = False
    alarma_activa = False
    
    # CONSTANTES DE CONFIGURACIÓN
    TEMPERATURA_MAXIMA = 80.0
    PRESION_MAXIMA = 3.0
    VOLTAJE_NOMINAL = 24.0
    
    print(f"Planta: {nombre_planta}")
    print(f"Ubicación: {ubicacion}")
    print(f"Sensores instalados: {numero_sensores}")
    
    # PROCESAMIENTO Y EVALUACIÓN
    print(f"\n📊 ESTADO ACTUAL:")
    print(f"Temperatura: {temperatura_actual}°C (Máx: {TEMPERATURA_MAXIMA}°C)")
    print(f"Presión: {presion_actual} bar (Máx: {PRESION_MAXIMA} bar)")
    print(f"Voltaje: {voltaje_alimentacion}V")
    
    # EVALUACIONES LÓGICAS
    temperatura_ok = temperatura_actual <= TEMPERATURA_MAXIMA
    presion_ok = presion_actual <= PRESION_MAXIMA
    voltaje_ok = abs(voltaje_alimentacion - VOLTAJE_NOMINAL) < 1.0
    
    sistema_seguro = temperatura_ok and presion_ok and voltaje_ok and not alarma_activa
    
    print(f"\n🔍 EVALUACIÓN DE SEGURIDAD:")
    print(f"✅ Temperatura OK: {temperatura_ok}")
    print(f"✅ Presión OK: {presion_ok}")
    print(f"✅ Voltaje OK: {voltaje_ok}")
    print(f"🎯 Sistema seguro: {sistema_seguro}")
    
    # REPORTE FINAL
    estado_general = "OPERATIVO" if sistema_seguro else "ADVERTENCIA"
    color_estado = "🟢" if sistema_seguro else "🟡"
    
    reporte = f"""
{color_estado} REPORTE DE ESTADO - {nombre_planta}
{'='*50}
Estado General: {estado_general}
Sensores Activos: {numero_sensores}
Temperatura: {temperatura_actual}°C
Presión: {presion_actual} bar
Sistema Operativo: {sistema_operativo}
Mantenimiento: {'Programado' if mantenimiento_programado else 'No requerido'}
    """
    
    print(reporte)

# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL - EJECUTA TODA LA SECUENCIA DE ENSEÑANZA
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """
    🚀 FUNCIÓN PRINCIPAL
    Ejecuta toda la secuencia de enseñanza paso a paso
    """
    print("🐍 BIENVENIDO AL TEMARIO: TIPOS DE DATOS Y VARIABLES")
    print("📚 Curso Intensivo de Python - Aplicado a Automatización Industrial")
    print("👨‍🏫 Tutor: GitHub Copilot | 👨‍🎓 Estudiante: José")
    print("\n🎯 Este programa te enseñará TODOS los fundamentos que necesitas")
    print("   para construir las aplicaciones industriales con PyModbus, Flask y SQL\n")
    
    # Ejecutar cada paso secuencialmente
    paso_1_introduccion_variables()
    paso_2_tipos_numericos()
    paso_3_strings()
    paso_4_booleanos()
    paso_5_conversiones()
    paso_6_buenas_practicas()
    paso_7_ejemplo_integrador()
    
    print("\n" + "=" * 60)
    print("🎉 ¡TEMARIO COMPLETADO!")
    print("=" * 60)
    print("✅ Has aprendido todos los tipos de datos fundamentales")
    print("✅ Puedes crear variables profesionales")
    print("✅ Entiendes las conversiones entre tipos")
    print("✅ Conoces las buenas prácticas")
    print("\n🚀 PRÓXIMO PASO: Practicar con ejercicios en el notebook de prácticas")
    print("📋 RECORDATORIO: Solo avanza cuando confirmes que este tema está consolidado")

if __name__ == "__main__":
    main()
