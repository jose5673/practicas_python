"""
📚 TEMARIO: LISTAS Y TUPLAS EN PYTHON
=====================================

🎯 OBJETIVO DE APRENDIZAJE:
Dominar las estructuras de datos fundamentales (listas y tuplas) para almacenar y 
manipular colecciones de información, preparándote para manejar datos de sensores,
configuraciones de dispositivos y procesamiento de información industrial.

📖 BASADO EN: "Curso Intensivo de Python" - Eric Matthes (Capítulos 3-4)

🗓️ FECHA: 30 de junio de 2025
👨‍🏫 TUTOR: GitHub Copilot (Experto en Python)
👨‍🎓 ESTUDIANTE: José

═══════════════════════════════════════════════════════════════════════════════
SECUENCIA DE ENSEÑANZA DETALLADA
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 1: INTRODUCCIÓN A LAS LISTAS - COLECCIONES DINÁMICAS
# ═══════════════════════════════════════════════════════════════════════════════

def paso_1_introduccion_listas():
    """
    🎯 OBJETIVO: Entender qué son las listas y por qué son fundamentales
    
    💡 ANALOGÍA INDUSTRIAL: Las listas son como "arrays de sensores" donde puedes
    almacenar múltiples lecturas, agregar nuevos valores, y procesar datos en conjunto.
    
    🏭 APLICACIONES CRÍTICAS:
    - Lecturas de múltiples sensores
    - Configuraciones de dispositivos PyModbus
    - Datos históricos para análisis
    - Listas de parámetros para APIs Flask
    """
    print("=" * 70)
    print("PASO 1: INTRODUCCIÓN A LAS LISTAS")
    print("=" * 70)
    
    # CREAR LISTAS - SINTAXIS BÁSICA
    print("\n📋 CREACIÓN DE LISTAS:")
    
    # Lista de temperaturas de sensores
    temperaturas_sensores = [23.5, 25.1, 22.8, 24.7, 26.2]
    print(f"Temperaturas: {temperaturas_sensores}")
    print(f"Tipo: {type(temperaturas_sensores)}")
    print(f"Cantidad de sensores: {len(temperaturas_sensores)}")
    
    # Lista de identificadores de dispositivos (strings)
    dispositivos_modbus = ["Sensor_Temp_01", "Bomba_Principal", "Valvula_A1", "Motor_Ventilador"]
    print(f"\nDispositivos Modbus: {dispositivos_modbus}")
    
    # Lista mixta (diferentes tipos de datos)
    info_reactor = ["Reactor_Principal", 101, 78.5, True, "Operativo"]
    print(f"Info Reactor: {info_reactor}")
    
    # ACCESO A ELEMENTOS - INDEXACIÓN
    print(f"\n🔍 ACCESO A ELEMENTOS:")
    print(f"Primera temperatura: {temperaturas_sensores[0]}°C")
    print(f"Última temperatura: {temperaturas_sensores[-1]}°C")
    print(f"Segundo dispositivo: {dispositivos_modbus[1]}")
    
    # ÍNDICES NEGATIVOS (desde el final)
    print(f"Penúltima temperatura: {temperaturas_sensores[-2]}°C")
    
    # CARACTERÍSTICAS FUNDAMENTALES
    print(f"\n✅ CARACTERÍSTICAS CLAVE DE LAS LISTAS:")
    print("• Son MUTABLES (se pueden modificar)")
    print("• Permiten elementos DUPLICADOS")
    print("• Mantienen el ORDEN de inserción")
    print("• Pueden contener DIFERENTES tipos de datos")
    print("• Se accede por ÍNDICE (posición)")

def paso_2_operaciones_listas():
    """
    🎯 OBJETIVO: Dominar las operaciones esenciales con listas
    
    🔧 APLICACIONES PARA PyModbus/Flask:
    - Agregar nuevas lecturas de sensores
    - Modificar configuraciones de dispositivos
    - Filtrar datos por criterios específicos
    - Procesar lotes de información
    """
    print("\n" + "=" * 70)
    print("PASO 2: OPERACIONES FUNDAMENTALES CON LISTAS")
    print("=" * 70)
    
    # LISTA INICIAL DE TRABAJO
    lecturas_presion = [2.1, 2.3, 2.0, 2.4]
    print(f"📊 Lista inicial: {lecturas_presion}")
    
    # AGREGAR ELEMENTOS
    print(f"\n➕ AGREGAR ELEMENTOS:")
    
    # append() - agregar al final
    lecturas_presion.append(2.2)
    print(f"Después de append(2.2): {lecturas_presion}")
    
    # insert() - agregar en posición específica
    lecturas_presion.insert(2, 1.9)
    print(f"Después de insert(2, 1.9): {lecturas_presion}")
    
    # extend() - agregar múltiples elementos
    nuevas_lecturas = [2.5, 2.6, 2.3]
    lecturas_presion.extend(nuevas_lecturas)
    print(f"Después de extend([2.5, 2.6, 2.3]): {lecturas_presion}")
    
    # MODIFICAR ELEMENTOS
    print(f"\n🔧 MODIFICAR ELEMENTOS:")
    print(f"Antes: {lecturas_presion}")
    lecturas_presion[0] = 2.15  # Calibración del primer sensor
    print(f"Después de calibrar sensor 0: {lecturas_presion}")
    
    # ELIMINAR ELEMENTOS
    print(f"\n❌ ELIMINAR ELEMENTOS:")
    
    # remove() - eliminar por valor
    lecturas_presion.remove(1.9)  # Eliminar lectura errónea
    print(f"Después de remove(1.9): {lecturas_presion}")
    
    # pop() - eliminar por índice y obtener el valor
    ultimo_valor = lecturas_presion.pop()
    print(f"Valor eliminado: {ultimo_valor}")
    print(f"Lista después de pop(): {lecturas_presion}")
    
    # del - eliminar por índice sin obtener valor
    del lecturas_presion[1]
    print(f"Después de del lecturas_presion[1]: {lecturas_presion}")
    
    # MÉTODOS DE BÚSQUEDA Y ANÁLISIS
    print(f"\n🔍 BÚSQUEDA Y ANÁLISIS:")
    
    # Agregar algunos datos para el análisis
    lecturas_presion.extend([2.4, 2.2, 2.4, 2.1])
    print(f"Lista para análisis: {lecturas_presion}")
    
    print(f"Índice de valor 2.4: {lecturas_presion.index(2.4)}")
    print(f"Contar ocurrencias de 2.4: {lecturas_presion.count(2.4)}")
    print(f"Valor máximo: {max(lecturas_presion)} bar")
    print(f"Valor mínimo: {min(lecturas_presion)} bar")
    print(f"Promedio: {sum(lecturas_presion)/len(lecturas_presion):.2f} bar")

def paso_3_slicing_listas():
    """
    🎯 OBJETIVO: Dominar el slicing para extraer subsecciones de datos
    
    🏭 APLICACIONES INDUSTRIALES:
    - Extraer últimas N lecturas de sensores
    - Obtener datos de un período específico
    - Procesar datos en lotes
    - Crear ventanas de análisis temporal
    """
    print("\n" + "=" * 70)
    print("PASO 3: SLICING - EXTRAER SUBSECCIONES")
    print("=" * 70)
    
    # DATOS DE EJEMPLO: 24 HORAS DE LECTURAS DE TEMPERATURA
    temperaturas_24h = [
        20.1, 20.3, 20.0, 19.8, 19.5, 19.3,  # 00:00-05:00
        19.8, 21.2, 23.5, 25.8, 28.1, 30.2,  # 06:00-11:00
        32.1, 33.5, 34.2, 33.8, 32.1, 30.5,  # 12:00-17:00
        28.9, 26.7, 24.3, 22.8, 21.5, 20.8   # 18:00-23:00
    ]
    
    print(f"📊 Temperaturas 24h (24 lecturas): {len(temperaturas_24h)} valores")
    
    # SLICING BÁSICO: [inicio:fin]
    print(f"\n✂️ SLICING BÁSICO:")
    print(f"Primeras 6 horas: {temperaturas_24h[0:6]}")
    print(f"Horas laborales (8-17): {temperaturas_24h[8:18]}")
    print(f"Últimas 6 horas: {temperaturas_24h[18:24]}")
    
    # SLICING CON PASOS: [inicio:fin:paso]
    print(f"\n⚡ SLICING CON PASOS:")
    print(f"Cada 2 horas: {temperaturas_24h[::2]}")
    print(f"Cada 4 horas: {temperaturas_24h[::4]}")
    print(f"Temperaturas inversas: {temperaturas_24h[::-1][:5]}...")  # Últimas 5 al revés
    
    # SLICING AVANZADO
    print(f"\n🔬 ANÁLISIS CON SLICING:")
    temp_matutinas = temperaturas_24h[6:12]   # 06:00-11:00
    temp_vespertinas = temperaturas_24h[12:18] # 12:00-17:00
    temp_nocturnas = temperaturas_24h[18:] + temperaturas_24h[:6]  # 18:00-05:00
    
    print(f"Promedio matutino: {sum(temp_matutinas)/len(temp_matutinas):.1f}°C")
    print(f"Promedio vespertino: {sum(temp_vespertinas)/len(temp_vespertinas):.1f}°C")
    print(f"Promedio nocturno: {sum(temp_nocturnas)/len(temp_nocturnas):.1f}°C")
    
    # CASOS PRÁCTICOS PARA AUTOMATIZACIÓN
    print(f"\n🏭 CASOS PRÁCTICOS:")
    
    # Últimas 3 lecturas para análisis de tendencia
    ultimas_3 = temperaturas_24h[-3:]
    print(f"Últimas 3 lecturas: {ultimas_3}")
    
    # Detectar período de mayor temperatura
    temp_max = max(temperaturas_24h)
    indice_max = temperaturas_24h.index(temp_max)
    print(f"Temperatura máxima: {temp_max}°C a las {indice_max}:00")

def paso_4_introduccion_tuplas():
    """
    🎯 OBJETIVO: Entender las tuplas como estructuras inmutables
    
    🔒 APLICACIONES EN AUTOMATIZACIÓN:
    - Coordenadas de dispositivos (x, y, z)
    - Configuraciones que no deben cambiar
    - Parámetros de calibración de sensores
    - Constantes del sistema
    """
    print("\n" + "=" * 70)
    print("PASO 4: INTRODUCCIÓN A LAS TUPLAS")
    print("=" * 70)
    
    # CREAR TUPLAS
    print("\n🔒 CREACIÓN DE TUPLAS:")
    
    # Coordenadas de sensor (x, y, z)
    posicion_sensor = (10.5, 25.3, 5.0)
    print(f"Posición sensor: {posicion_sensor}")
    print(f"Tipo: {type(posicion_sensor)}")
    
    # Configuración de calibración (ganancia, offset, unidad)
    calibracion_temp = (0.1, -2.5, "°C")
    print(f"Calibración: {calibracion_temp}")
    
    # Rango de operación (mínimo, máximo)
    rango_presion = (0.0, 5.0)
    print(f"Rango presión: {rango_presion}")
    
    # Tupla con un solo elemento (nota la coma)
    puerto_modbus = (502,)
    print(f"Puerto Modbus: {puerto_modbus}")
    
    # ACCESO A ELEMENTOS
    print(f"\n🔍 ACCESO A ELEMENTOS:")
    x, y, z = posicion_sensor  # Desempaquetado
    print(f"Coordenada X: {x}")
    print(f"Coordenada Y: {y}")
    print(f"Coordenada Z: {z}")
    
    print(f"Primera coordenada: {posicion_sensor[0]}")
    print(f"Última coordenada: {posicion_sensor[-1]}")
    
    # CARACTERÍSTICAS FUNDAMENTALES
    print(f"\n✅ CARACTERÍSTICAS CLAVE DE LAS TUPLAS:")
    print("• Son INMUTABLES (no se pueden modificar)")
    print("• Permiten elementos DUPLICADOS")
    print("• Mantienen el ORDEN de inserción")
    print("• Pueden contener DIFERENTES tipos de datos")
    print("• Se accede por ÍNDICE (posición)")
    print("• Son más RÁPIDAS que las listas")
    print("• Ideales para datos que NO deben cambiar")

def paso_5_comparacion_listas_tuplas():
    """
    🎯 OBJETIVO: Entender cuándo usar listas vs tuplas
    
    🤔 DECISIÓN CRÍTICA:
    - ¿Los datos cambiarán? → Lista
    - ¿Los datos son constantes? → Tupla
    - ¿Necesitas métodos de modificación? → Lista
    - ¿Necesitas máxima velocidad? → Tupla
    """
    print("\n" + "=" * 70)
    print("PASO 5: LISTAS vs TUPLAS - ¿CUÁNDO USAR QUÉ?")
    print("=" * 70)
    
    print(f"\n🔄 MUTABILIDAD:")
    
    # LISTA - MUTABLE
    sensores_activos = ["temp_01", "presion_02", "nivel_03"]
    print(f"Lista original: {sensores_activos}")
    sensores_activos.append("flujo_04")  # ✅ FUNCIONA
    print(f"Después de agregar: {sensores_activos}")
    
    # TUPLA - INMUTABLE
    config_sistema = ("192.168.1.100", 502, "TCP")
    print(f"Tupla original: {config_sistema}")
    try:
        config_sistema.append("nuevo")  # ❌ ERROR
    except AttributeError as e:
        print(f"Error al modificar tupla: {e}")
    
    print(f"\n⚡ RENDIMIENTO:")
    import time
    
    # Comparación de velocidad
    lista_grande = list(range(1000000))
    tupla_grande = tuple(range(1000000))
    
    # Acceso por índice
    start = time.time()
    _ = lista_grande[500000]
    tiempo_lista = time.time() - start
    
    start = time.time()
    _ = tupla_grande[500000]
    tiempo_tupla = time.time() - start
    
    print(f"Acceso a lista: {tiempo_lista:.8f} segundos")
    print(f"Acceso a tupla: {tiempo_tupla:.8f} segundos")
    print(f"Tupla es {tiempo_lista/tiempo_tupla:.1f}x más rápida")
    
    print(f"\n📋 GUÍA DE DECISIÓN:")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                    USA LISTAS CUANDO:                   ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║ • Necesites agregar/eliminar elementos                  ║")
    print("║ • Los datos cambien durante la ejecución                ║")
    print("║ • Proceses datos de sensores en tiempo real             ║")
    print("║ • Implementes colas o pilas de datos                    ║")
    print("╚══════════════════════════════════════════════════════════╝")
    
    print("╔══════════════════════════════════════════════════════════╗")
    print("║                    USA TUPLAS CUANDO:                   ║")
    print("╠══════════════════════════════════════════════════════════╣")
    print("║ • Los datos no cambien (configuraciones)                ║")
    print("║ • Necesites máximo rendimiento                          ║")
    print("║ • Representes coordenadas o puntos                      ║")
    print("║ • Devuelvas múltiples valores de funciones              ║")
    print("╚══════════════════════════════════════════════════════════╝")

def paso_6_casos_practicos_industriales():
    """
    🎯 OBJETIVO: Aplicar listas y tuplas en contextos industriales reales
    
    🏭 ESCENARIOS REALES:
    - Gestión de múltiples sensores
    - Configuraciones de dispositivos PyModbus
    - Datos para APIs Flask
    - Información para interfaces Tkinter
    """
    print("\n" + "=" * 70)
    print("PASO 6: CASOS PRÁCTICOS INDUSTRIALES")
    print("=" * 70)
    
    # CASO 1: SISTEMA DE SENSORES CON LISTAS
    print(f"\n🌡️ CASO 1: GESTIÓN DE SENSORES DE TEMPERATURA")
    
    # Lista de lecturas que cambia constantemente
    temperaturas_reactores = []
    reactores = ["Reactor_A", "Reactor_B", "Reactor_C"]
    
    # Simular lecturas de sensores
    import random
    for reactor in reactores:
        temp = round(random.uniform(70.0, 90.0), 1)
        temperaturas_reactores.append(temp)
        print(f"📊 {reactor}: {temp}°C")
    
    # Procesamiento de datos
    temp_promedio = sum(temperaturas_reactores) / len(temperaturas_reactores)
    temp_maxima = max(temperaturas_reactores)
    reactor_critico = reactores[temperaturas_reactores.index(temp_maxima)]
    
    print(f"🔍 Análisis:")
    print(f"   Temperatura promedio: {temp_promedio:.1f}°C")
    print(f"   Reactor más caliente: {reactor_critico} ({temp_maxima}°C)")
    
    # CASO 2: CONFIGURACIONES CON TUPLAS
    print(f"\n🔧 CASO 2: CONFIGURACIONES DE DISPOSITIVOS MODBUS")
    
    # Configuraciones que NO deben cambiar
    config_dispositivos = [
        ("Sensor_Temp_01", "192.168.1.101", 502, 1),
        ("Bomba_Principal", "192.168.1.102", 502, 2),
        ("Valvula_Control", "192.168.1.103", 502, 3),
    ]
    
    print(f"📋 Dispositivos configurados:")
    for nombre, ip, puerto, slave_id in config_dispositivos:
        print(f"   {nombre}: {ip}:{puerto} (Slave ID: {slave_id})")
    
    # CASO 3: DATOS PARA API FLASK
    print(f"\n🌐 CASO 3: ESTRUCTURA DE DATOS PARA API")
    
    # Lista de endpoints de API (puede crecer)
    endpoints_api = [
        "/api/sensores/temperatura",
        "/api/dispositivos/estado",
        "/api/reportes/diario"
    ]
    
    # Tuplas para respuestas estructuradas
    respuesta_sensor = ("temp_01", 75.3, "OK", "2025-06-30 15:30:00")
    codigo, valor, estado, timestamp = respuesta_sensor
    
    print(f"📡 Endpoints disponibles:")
    for endpoint in endpoints_api:
        print(f"   {endpoint}")
    
    print(f"📊 Respuesta típica: {respuesta_sensor}")
    print(f"   Código: {codigo}")
    print(f"   Valor: {valor}°C")
    print(f"   Estado: {estado}")
    print(f"   Timestamp: {timestamp}")

def paso_7_ejemplo_integrador():
    """
    🎯 OBJETIVO: Proyecto completo combinando listas y tuplas
    
    🏭 PROYECTO: Sistema de Monitoreo Multi-Sensor
    Simula un sistema real que monitorea múltiples sensores,
    almacena configuraciones y genera reportes.
    """
    print("\n" + "=" * 70)
    print("PASO 7: PROYECTO INTEGRADOR - SISTEMA DE MONITOREO")
    print("=" * 70)
    
    # CONFIGURACIONES FIJAS (TUPLAS)
    print(f"\n🔧 CONFIGURACIONES DEL SISTEMA:")
    
    # Configuración de sensores (inmutable)
    sensores_config = [
        ("TEMP_01", "Temperatura Reactor A", 0.0, 100.0, "°C"),
        ("PRES_02", "Presión Sistema", 0.0, 5.0, "bar"),
        ("NIVEL_03", "Nivel Tanque Principal", 0.0, 100.0, "%"),
        ("FLUJO_04", "Flujo Bomba Principal", 0.0, 50.0, "L/min"),
    ]
    
    # Límites de alarma (inmutables)
    limites_alarma = {
        "TEMP_01": (75.0, 85.0),    # (warning, critical)
        "PRES_02": (3.5, 4.0),
        "NIVEL_03": (20.0, 10.0),
        "FLUJO_04": (5.0, 2.0),
    }
    
    for config in sensores_config:
        sensor_id, descripcion, min_val, max_val, unidad = config
        warning, critical = limites_alarma[sensor_id]
        print(f"📊 {sensor_id}: {descripcion}")
        print(f"   Rango: {min_val}-{max_val} {unidad}")
        print(f"   Alarmas: Warning>{warning} Critical>{critical}")
    
    # DATOS DINÁMICOS (LISTAS)
    print(f"\n📈 LECTURAS EN TIEMPO REAL:")
    
    # Listas para almacenar lecturas (pueden crecer)
    lecturas_actuales = []
    timestamps = []
    estados_sensores = []
    
    import random
    import datetime
    
    # Simular 5 ciclos de lectura
    for ciclo in range(5):
        ciclo_lecturas = []
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        timestamps.append(timestamp)
        
        print(f"\n⏰ Ciclo {ciclo + 1} - {timestamp}")
        
        for config in sensores_config:
            sensor_id, _, min_val, max_val, unidad = config
            
            # Generar lectura aleatoria
            lectura = round(random.uniform(min_val * 0.8, max_val * 0.9), 1)
            ciclo_lecturas.append((sensor_id, lectura, unidad))
            
            # Evaluar estado
            warning, critical = limites_alarma[sensor_id]
            if lectura >= critical:
                estado = "CRÍTICO"
            elif lectura >= warning:
                estado = "WARNING"
            else:
                estado = "OK"
            
            print(f"   {sensor_id}: {lectura} {unidad} - {estado}")
        
        lecturas_actuales.append(ciclo_lecturas)
        
        # Contar estados por ciclo
        estados_ciclo = [
            "CRÍTICO" if l[1] >= limites_alarma[l[0]][1] else
            "WARNING" if l[1] >= limites_alarma[l[0]][0] else "OK"
            for l in ciclo_lecturas
        ]
        estados_sensores.append(estados_ciclo)
    
    # ANÁLISIS FINAL
    print(f"\n📊 ANÁLISIS DEL SISTEMA:")
    print(f"{'='*50}")
    
    # Estadísticas generales
    total_lecturas = len(lecturas_actuales) * len(sensores_config)
    sensores_ok = sum(estado.count("OK") for estado in estados_sensores)
    sensores_warning = sum(estado.count("WARNING") for estado in estados_sensores)
    sensores_criticos = sum(estado.count("CRÍTICO") for estado in estados_sensores)
    
    print(f"Total de lecturas: {total_lecturas}")
    print(f"Estados OK: {sensores_ok} ({sensores_ok/total_lecturas*100:.1f}%)")
    print(f"Estados WARNING: {sensores_warning} ({sensores_warning/total_lecturas*100:.1f}%)")
    print(f"Estados CRÍTICOS: {sensores_criticos} ({sensores_criticos/total_lecturas*100:.1f}%)")
    
    # Últimas lecturas
    print(f"\n📋 ÚLTIMAS LECTURAS:")
    if lecturas_actuales:
        for sensor_id, valor, unidad in lecturas_actuales[-1]:
            print(f"   {sensor_id}: {valor} {unidad}")
    
    eficiencia_sistema = sensores_ok / total_lecturas * 100
    estado_general = (
        "OPERATIVO" if eficiencia_sistema >= 80 else
        "ADVERTENCIA" if eficiencia_sistema >= 60 else
        "CRÍTICO"
    )
    
    print(f"\n🎯 ESTADO GENERAL DEL SISTEMA: {estado_general}")
    print(f"   Eficiencia operacional: {eficiencia_sistema:.1f}%")

# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL - EJECUTA TODA LA SECUENCIA DE ENSEÑANZA
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """
    🚀 FUNCIÓN PRINCIPAL
    Ejecuta toda la secuencia de enseñanza paso a paso
    """
    print("🐍 BIENVENIDO AL TEMARIO: LISTAS Y TUPLAS")
    print("📚 Curso Intensivo de Python - Aplicado a Automatización Industrial")
    print("👨‍🏫 Tutor: GitHub Copilot | 👨‍🎓 Estudiante: José")
    print("\n🎯 Este temario te preparará para manejar colecciones de datos")
    print("   fundamentales para PyModbus, Flask, SQL y análisis con NumPy\n")
    
    # Ejecutar cada paso secuencialmente
    paso_1_introduccion_listas()
    paso_2_operaciones_listas()
    paso_3_slicing_listas()
    paso_4_introduccion_tuplas()
    paso_5_comparacion_listas_tuplas()
    paso_6_casos_practicos_industriales()
    paso_7_ejemplo_integrador()
    
    print("\n" + "=" * 70)
    print("🎉 ¡TEMARIO LISTAS Y TUPLAS COMPLETADO!")
    print("=" * 70)
    print("✅ Dominas la creación y manipulación de listas")
    print("✅ Entiendes el uso apropiado de tuplas")
    print("✅ Puedes manejar colecciones de datos industriales")
    print("✅ Conoces las mejores prácticas para cada tipo")
    print("\n🚀 PRÓXIMO PASO: Practicar con ejercicios industriales")
    print("📋 RECORDATORIO: Solo avanza cuando confirmes consolidación")
    print("\n💡 CONEXIÓN CON TUS METAS:")
    print("   • PyModbus: Listas de dispositivos y configuraciones")
    print("   • Flask: Arrays de datos para APIs JSON")
    print("   • SQL: Preparar datos para inserción en bases de datos")
    print("   • NumPy: Base para arrays numéricos avanzados")
    print("   • Tkinter: Llenar listas de elementos en interfaces")

if __name__ == "__main__":
    main()
