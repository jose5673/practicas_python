"""
📚 MÓDULO 1.3: PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
=========================================================

🎯 OBJETIVO DE APRENDIZAJE:
Dominar los conceptos fundamentales de la Programación Orientada a Objetos para crear
sistemas modulares, reutilizables y escalables que simulen dispositivos industriales,
sensores y sistemas de control. Preparación directa para PyModbus, Flask y arquitecturas
de software industrial.

📖 BASADO EN: "Curso Intensivo de Python" - Eric Matthes (Capítulos 9-10)

🗓️ FECHA: 30 de junio de 2025
👨‍🏫 TUTOR: GitHub Copilot (Experto en Python)
👨‍🎓 ESTUDIANTE: José

═══════════════════════════════════════════════════════════════════════════════
SECUENCIA DE ENSEÑANZA DETALLADA - PROGRAMACIÓN ORIENTADA A OBJETOS
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 1: INTRODUCCIÓN A CLASES Y OBJETOS - CONCEPTOS FUNDAMENTALES
# ═══════════════════════════════════════════════════════════════════════════════

def paso_1_conceptos_fundamentales():
    """
    🎯 OBJETIVO: Entender qué son las clases y objetos, y por qué son cruciales
    
    💡 ANALOGÍA INDUSTRIAL: Una clase es como un "plano de fabricación" de un dispositivo.
    Un objeto es el "dispositivo físico" creado a partir de ese plano.
    
    🏭 APLICACIONES CRÍTICAS:
    - Modelar sensores y actuadores industriales
    - Crear dispositivos PyModbus con comportamientos específicos
    - Estructurar APIs Flask con clases de recursos
    - Diseñar sistemas modulares y mantenibles
    """
    print("=" * 70)
    print("PASO 1: CONCEPTOS FUNDAMENTALES DE POO")
    print("=" * 70)
    
    print("🔍 ¿QUÉ ES UNA CLASE?")
    print("Una clase es un MOLDE o PLANTILLA que define:")
    print("• ATRIBUTOS (características del objeto)")
    print("• MÉTODOS (acciones que puede realizar)")
    print("\n🔍 ¿QUÉ ES UN OBJETO?")
    print("Un objeto es una INSTANCIA específica creada a partir de una clase")
    print("• Cada objeto tiene sus propios valores de atributos")
    print("• Todos comparten los mismos métodos definidos en la clase")

# PRIMERA CLASE: SENSOR INDUSTRIAL BÁSICO
class SensorTemperatura:
    """
    🌡️ Clase que representa un sensor de temperatura industrial
    
    Esta clase modela un sensor real que podrías encontrar en:
    - Reactores químicos
    - Sistemas HVAC
    - Procesos de manufactura
    - Redes de monitoreo PyModbus
    """
    
    def __init__(self, id_sensor, ubicacion, temperatura_inicial=20.0):
        """
        🔧 CONSTRUCTOR: Se ejecuta automáticamente al crear un objeto
        
        Args:
            id_sensor (str): Identificador único del sensor
            ubicacion (str): Dónde está instalado físicamente
            temperatura_inicial (float): Temperatura inicial en °C
        """
        # ATRIBUTOS DE INSTANCIA - Cada objeto tendrá sus propios valores
        self.id_sensor = id_sensor
        self.ubicacion = ubicacion
        self.temperatura_actual = temperatura_inicial
        self.estado = "operativo"
        self.alarmas_activas = []
        self.historial_lecturas = [temperatura_inicial]
        
        print(f"✅ Sensor {id_sensor} inicializado en {ubicacion}")
    
    def leer_temperatura(self):
        """
        📊 Método para obtener la temperatura actual
        
        Returns:
            float: Temperatura en grados Celsius
        """
        return self.temperatura_actual
    
    def actualizar_temperatura(self, nueva_temperatura):
        """
        🔄 Método para actualizar la lectura del sensor
        
        Args:
            nueva_temperatura (float): Nueva lectura en °C
        """
        self.temperatura_actual = nueva_temperatura
        self.historial_lecturas.append(nueva_temperatura)
        
        # Verificar alarmas
        self._verificar_alarmas()
        
        print(f"🌡️ {self.id_sensor}: {nueva_temperatura}°C")
    
    def _verificar_alarmas(self):
        """
        🚨 Método privado para verificar condiciones de alarma
        
        Convención: métodos que empiezan con _ son "privados"
        """
        temp = self.temperatura_actual
        
        # Limpiar alarmas previas
        self.alarmas_activas.clear()
        
        if temp > 80:
            self.alarmas_activas.append("TEMPERATURA_ALTA")
            self.estado = "alarma"
        elif temp < 0:
            self.alarmas_activas.append("TEMPERATURA_BAJA") 
            self.estado = "alarma"
        else:
            self.estado = "operativo"
    
    def obtener_estadisticas(self):
        """
        📈 Método para calcular estadísticas del historial
        
        Returns:
            dict: Diccionario con estadísticas calculadas
        """
        if not self.historial_lecturas:
            return {"error": "No hay lecturas disponibles"}
        
        return {
            "temperatura_promedio": sum(self.historial_lecturas) / len(self.historial_lecturas),
            "temperatura_maxima": max(self.historial_lecturas),
            "temperatura_minima": min(self.historial_lecturas),
            "total_lecturas": len(self.historial_lecturas),
            "ultima_lectura": self.historial_lecturas[-1]
        }
    
    def generar_reporte(self):
        """
        📋 Método para generar un reporte completo del sensor
        """
        stats = self.obtener_estadisticas()
        
        print(f"\n📊 REPORTE DEL SENSOR {self.id_sensor}")
        print(f"{'='*50}")
        print(f"📍 Ubicación: {self.ubicacion}")
        print(f"🌡️ Temperatura actual: {self.temperatura_actual}°C")
        print(f"📈 Estado: {self.estado.upper()}")
        print(f"🔥 Temp. máxima: {stats['temperatura_maxima']}°C")
        print(f"❄️ Temp. mínima: {stats['temperatura_minima']}°C")
        print(f"📊 Temp. promedio: {stats['temperatura_promedio']:.1f}°C")
        print(f"📚 Total lecturas: {stats['total_lecturas']}")
        
        if self.alarmas_activas:
            print(f"🚨 Alarmas activas: {', '.join(self.alarmas_activas)}")
        else:
            print(f"✅ Sin alarmas activas")

def paso_2_creacion_uso_objetos():
    """
    🎯 OBJETIVO: Aprender a crear y usar objetos de la clase
    
    🔧 APLICACIÓN PRÁCTICA:
    - Instanciar múltiples sensores
    - Simular lecturas en tiempo real
    - Gestionar una red de dispositivos
    """
    print("\n" + "=" * 70)
    print("PASO 2: CREACIÓN Y USO DE OBJETOS")
    print("=" * 70)
    
    # CREAR OBJETOS (INSTANCIAR LA CLASE)
    print("🏭 CREANDO RED DE SENSORES INDUSTRIALES:")
    
    # Cada objeto es independiente con sus propios datos
    sensor_reactor_a = SensorTemperatura("TEMP_001", "Reactor Principal A", 75.0)
    sensor_reactor_b = SensorTemperatura("TEMP_002", "Reactor Secundario B", 68.5)
    sensor_intercambiador = SensorTemperatura("TEMP_003", "Intercambiador de Calor", 45.0)
    
    # USAR MÉTODOS DE LOS OBJETOS
    print(f"\n📊 LECTURAS INICIALES:")
    print(f"Reactor A: {sensor_reactor_a.leer_temperatura()}°C")
    print(f"Reactor B: {sensor_reactor_b.leer_temperatura()}°C")
    print(f"Intercambiador: {sensor_intercambiador.leer_temperatura()}°C")
    
    # SIMULAR CAMBIOS EN EL PROCESO
    print(f"\n🔄 SIMULANDO PROCESO INDUSTRIAL:")
    
    # El reactor A se está calentando (proceso normal)
    sensor_reactor_a.actualizar_temperatura(78.5)
    sensor_reactor_a.actualizar_temperatura(82.1)  # Esto generará alarma
    sensor_reactor_a.actualizar_temperatura(85.5)
    
    # El reactor B está estable
    sensor_reactor_b.actualizar_temperatura(69.2)
    sensor_reactor_b.actualizar_temperatura(68.8)
    
    # El intercambiador está funcionando
    sensor_intercambiador.actualizar_temperatura(47.3)
    sensor_intercambiador.actualizar_temperatura(46.1)
    
    # GENERAR REPORTES
    print(f"\n📋 REPORTES DE SENSORES:")
    sensor_reactor_a.generar_reporte()
    sensor_reactor_b.generar_reporte()
    sensor_intercambiador.generar_reporte()

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 3: ATRIBUTOS DE CLASE VS ATRIBUTOS DE INSTANCIA
# ═══════════════════════════════════════════════════════════════════════════════

class DispositivoModbus:
    """
    🔧 Clase avanzada que demuestra atributos de clase vs instancia
    
    Simula un dispositivo conectado via protocolo Modbus
    """
    
    # ATRIBUTOS DE CLASE - Compartidos por todas las instancias
    protocolo = "Modbus TCP/IP"
    puerto_default = 502
    timeout_default = 5.0
    dispositivos_totales = 0  # Contador global
    
    def __init__(self, id_dispositivo, ip_address, tipo_dispositivo):
        """
        Constructor que demuestra la diferencia entre atributos de clase e instancia
        """
        # ATRIBUTOS DE INSTANCIA - Únicos para cada objeto
        self.id_dispositivo = id_dispositivo
        self.ip_address = ip_address
        self.tipo_dispositivo = tipo_dispositivo
        self.estado_conexion = "desconectado"
        self.registros_leidos = {}
        
        # Incrementar contador de clase
        DispositivoModbus.dispositivos_totales += 1
        
        print(f"🔧 Dispositivo {id_dispositivo} ({tipo_dispositivo}) creado")
        print(f"📡 IP: {ip_address} | Protocolo: {self.protocolo}")
    
    @classmethod
    def obtener_info_protocolo(cls):
        """
        📡 Método de clase - Opera sobre la clase, no sobre instancias
        
        Se usa para funcionalidades que afectan a toda la clase
        """
        return {
            "protocolo": cls.protocolo,
            "puerto_default": cls.puerto_default,
            "timeout_default": cls.timeout_default,
            "dispositivos_registrados": cls.dispositivos_totales
        }
    
    @staticmethod
    def validar_ip(ip_address):
        """
        🛡️ Método estático - No depende de la clase ni instancia
        
        Funciones utilitarias relacionadas con la clase
        """
        partes = ip_address.split('.')
        if len(partes) != 4:
            return False
        
        try:
            return all(0 <= int(parte) <= 255 for parte in partes)
        except ValueError:
            return False
    
    def conectar(self):
        """Simula conexión al dispositivo"""
        if self.validar_ip(self.ip_address):
            self.estado_conexion = "conectado"
            print(f"✅ {self.id_dispositivo} conectado en {self.ip_address}")
        else:
            print(f"❌ IP inválida para {self.id_dispositivo}")
    
    def leer_registro(self, direccion, cantidad=1):
        """Simula lectura de registros Modbus"""
        if self.estado_conexion != "conectado":
            print(f"❌ {self.id_dispositivo} no está conectado")
            return None
        
        # Simular datos
        import random
        valores = [random.randint(0, 1000) for _ in range(cantidad)]
        self.registros_leidos[direccion] = valores
        
        print(f"📊 {self.id_dispositivo} - Registro {direccion}: {valores}")
        return valores

def paso_3_atributos_clase_instancia():
    """
    🎯 OBJETIVO: Entender la diferencia entre atributos de clase e instancia
    """
    print("\n" + "=" * 70)
    print("PASO 3: ATRIBUTOS DE CLASE VS INSTANCIA")
    print("=" * 70)
    
    # Verificar información del protocolo antes de crear dispositivos
    print("📡 INFORMACIÓN DEL PROTOCOLO:")
    info = DispositivoModbus.obtener_info_protocolo()
    for clave, valor in info.items():
        print(f"  {clave}: {valor}")
    
    print(f"\n🔧 CREANDO DISPOSITIVOS MODBUS:")
    
    # Crear varios dispositivos
    plc_principal = DispositivoModbus("PLC_001", "192.168.1.100", "PLC")
    sensor_red = DispositivoModbus("SENSOR_002", "192.168.1.101", "Sensor")
    actuador_valvula = DispositivoModbus("VALVE_003", "192.168.1.102", "Válvula")
    
    # Verificar que el contador de clase se actualizó
    print(f"\n📊 DISPOSITIVOS REGISTRADOS: {DispositivoModbus.dispositivos_totales}")
    
    # Usar método estático para validar IPs
    print(f"\n🛡️ VALIDACIÓN DE IPs:")
    ips_prueba = ["192.168.1.100", "300.168.1.100", "192.168.1", "192.168.1.101"]
    for ip in ips_prueba:
        valida = DispositivoModbus.validar_ip(ip)
        print(f"  {ip}: {'✅ Válida' if valida else '❌ Inválida'}")
    
    # Conectar dispositivos y leer datos
    print(f"\n🔌 CONECTANDO DISPOSITIVOS:")
    for dispositivo in [plc_principal, sensor_red, actuador_valvula]:
        dispositivo.conectar()
        dispositivo.leer_registro(40001, 3)

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 4: HERENCIA - CREANDO JERARQUÍAS DE CLASES
# ═══════════════════════════════════════════════════════════════════════════════

class SensorIndustrial:
    """
    🏭 CLASE BASE: Funcionalidad común a todos los sensores industriales
    
    Esta será la clase padre de la que heredarán sensores específicos
    """
    
    def __init__(self, id_sensor, ubicacion, unidad_medida):
        self.id_sensor = id_sensor
        self.ubicacion = ubicacion
        self.unidad_medida = unidad_medida
        self.estado = "operativo"
        self.historial = []
        self.alarmas = []
        
        print(f"🏭 Sensor base {id_sensor} inicializado")
    
    def registrar_lectura(self, valor, timestamp=None):
        """Método común para registrar lecturas"""
        if timestamp is None:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.historial.append((timestamp, valor))
        self.verificar_alarmas(valor)
        
        print(f"📊 {self.id_sensor}: {valor} {self.unidad_medida} ({timestamp})")
    
    def verificar_alarmas(self, valor):
        """Método base para verificar alarmas - será sobrescrito por clases hijas"""
        pass
    
    def obtener_ultima_lectura(self):
        """Obtener la lectura más reciente"""
        if self.historial:
            return self.historial[-1]
        return None
    
    def generar_reporte_base(self):
        """Generar reporte básico común a todos los sensores"""
        print(f"\n📋 REPORTE SENSOR {self.id_sensor}")
        print(f"📍 Ubicación: {self.ubicacion}")
        print(f"📊 Estado: {self.estado}")
        print(f"📈 Total lecturas: {len(self.historial)}")
        
        if self.alarmas:
            print(f"🚨 Alarmas: {', '.join(self.alarmas)}")

class SensorTemperaturaAvanzado(SensorIndustrial):
    """
    🌡️ CLASE HIJA: Sensor de temperatura con funcionalidades específicas
    
    HEREDA de SensorIndustrial y AÑADE funcionalidad específica
    """
    
    def __init__(self, id_sensor, ubicacion, limite_min=-10, limite_max=100):
        # Llamar al constructor de la clase padre
        super().__init__(id_sensor, ubicacion, "°C")
        
        # Atributos específicos de temperatura
        self.limite_min = limite_min
        self.limite_max = limite_max
        self.tipo_sensor = "Temperatura"
        
        print(f"🌡️ Sensor de temperatura especializado creado")
        print(f"   Límites: {limite_min}°C a {limite_max}°C")
    
    def verificar_alarmas(self, temperatura):
        """
        SOBRESCRIBIR método padre con lógica específica de temperatura
        """
        self.alarmas.clear()
        
        if temperatura > self.limite_max:
            self.alarmas.append("TEMPERATURA_ALTA")
            self.estado = "alarma_alta"
        elif temperatura < self.limite_min:
            self.alarmas.append("TEMPERATURA_BAJA")
            self.estado = "alarma_baja"
        else:
            self.estado = "operativo"
    
    def calcular_eficiencia_termica(self):
        """
        MÉTODO ESPECÍFICO: Solo los sensores de temperatura lo tienen
        """
        if len(self.historial) < 2:
            return None
        
        # Calcular estabilidad térmica
        temperaturas = [lectura[1] for lectura in self.historial]
        variacion = max(temperaturas) - min(temperaturas)
        
        # Eficiencia basada en estabilidad (menos variación = más eficiente)
        eficiencia = max(0, 100 - (variacion * 2))
        
        return {
            "eficiencia_termica": eficiencia,
            "variacion_maxima": variacion,
            "temperatura_promedio": sum(temperaturas) / len(temperaturas)
        }
    
    def generar_reporte(self):
        """
        EXTENDER funcionalidad del método padre
        """
        # Llamar al reporte base del padre
        self.generar_reporte_base()
        
        # Agregar información específica de temperatura
        print(f"🌡️ Tipo: {self.tipo_sensor}")
        print(f"🔥 Límite máximo: {self.limite_max}°C")
        print(f"❄️ Límite mínimo: {self.limite_min}°C")
        
        eficiencia = self.calcular_eficiencia_termica()
        if eficiencia:
            print(f"⚡ Eficiencia térmica: {eficiencia['eficiencia_termica']:.1f}%")
            print(f"📊 Temp. promedio: {eficiencia['temperatura_promedio']:.1f}°C")

class SensorPresion(SensorIndustrial):
    """
    💨 CLASE HIJA: Sensor de presión con funcionalidades específicas
    """
    
    def __init__(self, id_sensor, ubicacion, presion_maxima=10.0):
        super().__init__(id_sensor, ubicacion, "bar")
        
        self.presion_maxima = presion_maxima
        self.tipo_sensor = "Presión"
        self.presion_critica = presion_maxima * 0.9  # 90% de la máxima
        
        print(f"💨 Sensor de presión especializado creado")
        print(f"   Presión máxima: {presion_maxima} bar")
    
    def verificar_alarmas(self, presion):
        """Verificar alarmas específicas de presión"""
        self.alarmas.clear()
        
        if presion > self.presion_maxima:
            self.alarmas.append("PRESION_CRITICA")
            self.estado = "emergencia"
        elif presion > self.presion_critica:
            self.alarmas.append("PRESION_ALTA")
            self.estado = "advertencia"
        elif presion < 0:
            self.alarmas.append("PRESION_NEGATIVA")
            self.estado = "error"
        else:
            self.estado = "operativo"
    
    def calcular_factor_seguridad(self):
        """Método específico para calcular factor de seguridad"""
        if not self.historial:
            return None
        
        ultima_presion = self.historial[-1][1]
        factor = self.presion_maxima / ultima_presion if ultima_presion > 0 else float('inf')
        
        return {
            "factor_seguridad": factor,
            "presion_actual": ultima_presion,
            "margen_seguridad": self.presion_maxima - ultima_presion
        }
    
    def generar_reporte(self):
        """Reporte específico de presión"""
        self.generar_reporte_base()
        
        print(f"💨 Tipo: {self.tipo_sensor}")
        print(f"🔴 Presión máxima: {self.presion_maxima} bar")
        print(f"🟡 Presión crítica: {self.presion_critica} bar")
        
        factor = self.calcular_factor_seguridad()
        if factor:
            print(f"🛡️ Factor de seguridad: {factor['factor_seguridad']:.2f}")
            print(f"📊 Margen seguridad: {factor['margen_seguridad']:.2f} bar")

def paso_4_herencia_practica():
    """
    🎯 OBJETIVO: Demostrar herencia con sensores especializados
    """
    print("\n" + "=" * 70)
    print("PASO 4: HERENCIA - SENSORES ESPECIALIZADOS")
    print("=" * 70)
    
    # Crear sensores especializados
    print("🏭 CREANDO RED DE SENSORES ESPECIALIZADOS:")
    
    sensor_temp_reactor = SensorTemperaturaAvanzado(
        "TEMP_REACTOR_001", 
        "Reactor Principal", 
        limite_min=60, 
        limite_max=120
    )
    
    sensor_presion_linea = SensorPresion(
        "PRES_LINEA_001", 
        "Línea Principal", 
        presion_maxima=8.0
    )
    
    # Simular operación durante varios ciclos
    print(f"\n🔄 SIMULACIÓN DE PROCESO INDUSTRIAL:")
    
    # Ciclo 1: Arranque del sistema
    print(f"\n⏰ CICLO 1 - ARRANQUE:")
    sensor_temp_reactor.registrar_lectura(65.5)
    sensor_presion_linea.registrar_lectura(2.1)
    
    # Ciclo 2: Operación normal
    print(f"\n⏰ CICLO 2 - OPERACIÓN NORMAL:")
    sensor_temp_reactor.registrar_lectura(85.2)
    sensor_presion_linea.registrar_lectura(4.5)
    
    # Ciclo 3: Condición de alarma
    print(f"\n⏰ CICLO 3 - CONDICIÓN DE ALARMA:")
    sensor_temp_reactor.registrar_lectura(125.8)  # Excede límite
    sensor_presion_linea.registrar_lectura(7.8)   # Presión alta
    
    # Ciclo 4: Normalización
    print(f"\n⏰ CICLO 4 - NORMALIZACIÓN:")
    sensor_temp_reactor.registrar_lectura(95.1)
    sensor_presion_linea.registrar_lectura(5.2)
    
    # Generar reportes especializados
    print(f"\n📋 REPORTES ESPECIALIZADOS:")
    sensor_temp_reactor.generar_reporte()
    sensor_presion_linea.generar_reporte()

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 5: POLIMORFISMO - DIFERENTES OBJETOS, MISMA INTERFAZ
# ═══════════════════════════════════════════════════════════════════════════════

def paso_5_polimorfismo():
    """
    🎯 OBJETIVO: Demostrar polimorfismo - tratar objetos diferentes de manera uniforme
    
    🔧 APLICACIÓN INDUSTRIAL:
    - Gestionar diferentes tipos de sensores con la misma interfaz
    - Crear sistemas escalables y mantenibles
    - Preparar para arquitecturas de microservicios
    """
    print("\n" + "=" * 70)
    print("PASO 5: POLIMORFISMO - INTERFAZ UNIFORME")
    print("=" * 70)
    
    # Crear una lista mixta de diferentes tipos de sensores
    red_sensores = [
        SensorTemperaturaAvanzado("TEMP_001", "Zona A", 50, 150),
        SensorPresion("PRES_001", "Zona A", 6.0),
        SensorTemperaturaAvanzado("TEMP_002", "Zona B", 40, 120),
        SensorPresion("PRES_002", "Zona B", 8.0),
        SensorTemperaturaAvanzado("TEMP_003", "Zona C", 70, 200)
    ]
    
    print(f"\n🌐 RED DE SENSORES CONFIGURADA: {len(red_sensores)} dispositivos")
    
    # POLIMORFISMO: Tratar todos los sensores igual, sin importar su tipo específico
    print(f"\n🔄 SIMULACIÓN MASIVA DE LECTURAS:")
    
    import random
    
    for ciclo in range(1, 4):
        print(f"\n⏰ CICLO DE MONITOREO {ciclo}:")
        
        for sensor in red_sensores:
            # POLIMORFISMO: Cada sensor responde según su tipo
            if isinstance(sensor, SensorTemperaturaAvanzado):
                # Simular temperatura entre límites +/- variación
                base = (sensor.limite_min + sensor.limite_max) / 2
                variacion = random.uniform(-20, 30)
                valor = base + variacion
                sensor.registrar_lectura(valor)
                
            elif isinstance(sensor, SensorPresion):
                # Simular presión entre 0 y máxima
                valor = random.uniform(0, sensor.presion_maxima * 1.1)
                sensor.registrar_lectura(valor)
    
    # GENERAR REPORTE UNIFICADO usando polimorfismo
    print(f"\n📊 REPORTE UNIFICADO DE TODA LA RED:")
    print(f"{'='*60}")
    
    sensores_operativos = 0
    sensores_alarma = 0
    total_lecturas = 0
    
    for i, sensor in enumerate(red_sensores, 1):
        print(f"\n🔸 SENSOR {i}: {sensor.id_sensor}")
        print(f"   📍 Ubicación: {sensor.ubicacion}")
        print(f"   📊 Estado: {sensor.estado}")
        print(f"   📈 Lecturas: {len(sensor.historial)}")
        
        # Polimorfismo: método existe en todas las clases hijas
        ultima = sensor.obtener_ultima_lectura()
        if ultima:
            print(f"   🕐 Última: {ultima[1]} {sensor.unidad_medida}")
        
        # Estadísticas
        if sensor.estado == "operativo":
            sensores_operativos += 1
        else:
            sensores_alarma += 1
        
        total_lecturas += len(sensor.historial)
    
    # RESUMEN EJECUTIVO
    print(f"\n📈 RESUMEN EJECUTIVO:")
    print(f"   🟢 Sensores operativos: {sensores_operativos}")
    print(f"   🔴 Sensores con alarma: {sensores_alarma}")
    print(f"   📊 Total de lecturas: {total_lecturas}")
    print(f"   💯 Disponibilidad: {(sensores_operativos/len(red_sensores)*100):.1f}%")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 6: MÉTODOS ESPECIALES (DUNDER METHODS)
# ═══════════════════════════════════════════════════════════════════════════════

class DispositivoIoT:
    """
    📡 Clase que demuestra métodos especiales (dunder methods)
    
    Estos métodos permiten que nuestros objetos se comporten como tipos nativos
    """
    
    def __init__(self, id_dispositivo, tipo, valor_inicial=0):
        self.id_dispositivo = id_dispositivo
        self.tipo = tipo
        self.valor = valor_inicial
        self.timestamp_creacion = self._obtener_timestamp()
    
    def _obtener_timestamp(self):
        """Método auxiliar para obtener timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        """
        🖨️ Representación amigable para usuarios (print)
        """
        return f"Dispositivo {self.id_dispositivo} ({self.tipo}): {self.valor}"
    
    def __repr__(self):
        """
        🔧 Representación técnica para desarrolladores
        """
        return f"DispositivoIoT('{self.id_dispositivo}', '{self.tipo}', {self.valor})"
    
    def __eq__(self, otro):
        """
        ⚖️ Comparación de igualdad (==)
        """
        if not isinstance(otro, DispositivoIoT):
            return False
        return self.id_dispositivo == otro.id_dispositivo
    
    def __lt__(self, otro):
        """
        📊 Comparación menor que (<) para ordenamiento
        """
        if not isinstance(otro, DispositivoIoT):
            return NotImplemented
        return self.valor < otro.valor
    
    def __add__(self, otro):
        """
        ➕ Operador suma para combinar valores
        """
        if isinstance(otro, DispositivoIoT):
            return self.valor + otro.valor
        elif isinstance(otro, (int, float)):
            return self.valor + otro
        return NotImplemented
    
    def __len__(self):
        """
        📏 Longitud del dispositivo (número de caracteres en ID)
        """
        return len(self.id_dispositivo)
    
    def __contains__(self, item):
        """
        🔍 Operador 'in' para verificar si algo está en el ID
        """
        return item in self.id_dispositivo
    
    def __getitem__(self, index):
        """
        📋 Acceso por índice como si fuera una lista
        """
        propiedades = [self.id_dispositivo, self.tipo, self.valor, self.timestamp_creacion]
        return propiedades[index]
    
    def actualizar_valor(self, nuevo_valor):
        """Actualizar el valor del dispositivo"""
        self.valor = nuevo_valor

def paso_6_metodos_especiales():
    """
    🎯 OBJETIVO: Demostrar métodos especiales para integración natural
    """
    print("\n" + "=" * 70)
    print("PASO 6: MÉTODOS ESPECIALES (DUNDER METHODS)")
    print("=" * 70)
    
    # Crear dispositivos IoT
    sensor_temp = DispositivoIoT("TEMP_SENSOR_01", "Temperatura", 25.5)
    sensor_hum = DispositivoIoT("HUM_SENSOR_01", "Humedad", 60.0)
    actuador_fan = DispositivoIoT("FAN_ACT_01", "Ventilador", 750)
    
    print("📡 DISPOSITIVOS IoT CREADOS:")
    
    # __str__ y __repr__ en acción
    print(f"Usuario ve: {sensor_temp}")  # Usa __str__
    print(f"Desarrollador ve: {repr(sensor_temp)}")  # Usa __repr__
    
    # Crear lista de dispositivos
    dispositivos = [sensor_temp, sensor_hum, actuador_fan]
    
    print(f"\n🔍 DEMOSTRANDO MÉTODOS ESPECIALES:")
    
    # __len__ en acción
    print(f"Longitud ID del sensor temp: {len(sensor_temp)} caracteres")
    
    # __contains__ en acción
    print(f"'TEMP' está en {sensor_temp.id_dispositivo}: {'TEMP' in sensor_temp}")
    print(f"'PRES' está en {sensor_temp.id_dispositivo}: {'PRES' in sensor_temp}")
    
    # __getitem__ en acción
    print(f"Acceso por índice - sensor_temp[0]: {sensor_temp[0]}")
    print(f"Acceso por índice - sensor_temp[1]: {sensor_temp[1]}")
    print(f"Acceso por índice - sensor_temp[2]: {sensor_temp[2]}")
    
    # __eq__ en acción
    sensor_temp_copia = DispositivoIoT("TEMP_SENSOR_01", "Temperatura", 30.0)
    print(f"\nComparación de igualdad:")
    print(f"sensor_temp == sensor_hum: {sensor_temp == sensor_hum}")
    print(f"sensor_temp == sensor_temp_copia: {sensor_temp == sensor_temp_copia}")
    
    # Actualizar valores para demostrar comparaciones
    sensor_hum.actualizar_valor(45.0)
    actuador_fan.actualizar_valor(800)
    
    print(f"\n📊 VALORES ACTUALIZADOS:")
    for dispositivo in dispositivos:
        print(f"  {dispositivo}")
    
    # __lt__ en acción - ordenamiento
    print(f"\n📈 ORDENAMIENTO POR VALOR:")
    dispositivos_ordenados = sorted(dispositivos)
    for dispositivo in dispositivos_ordenados:
        print(f"  {dispositivo}")
    
    # __add__ en acción
    print(f"\n➕ OPERACIONES MATEMÁTICAS:")
    suma_sensores = sensor_temp + sensor_hum
    suma_con_numero = sensor_temp + 10
    print(f"Suma sensores: {suma_sensores}")
    print(f"Suma con número: {suma_con_numero}")

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 7: PROYECTO INTEGRADOR - SISTEMA SCADA BÁSICO
# ═══════════════════════════════════════════════════════════════════════════════

class SistemaSCADA:
    """
    🏭 PROYECTO INTEGRADOR: Sistema SCADA que demuestra todos los conceptos POO
    
    Este sistema simula un SCADA real que:
    - Gestiona múltiples tipos de dispositivos
    - Procesa datos en tiempo real
    - Genera reportes y alarmas
    - Prepara datos para APIs (Flask) y bases de datos (SQL)
    """
    
    def __init__(self, nombre_planta):
        self.nombre_planta = nombre_planta
        self.dispositivos = {}
        self.historial_eventos = []
        self.alarmas_activas = []
        self.estado_sistema = "iniciando"
        
        print(f"🏭 Sistema SCADA '{nombre_planta}' inicializado")
    
    def registrar_dispositivo(self, dispositivo):
        """Registrar un nuevo dispositivo en el sistema"""
        self.dispositivos[dispositivo.id_sensor] = dispositivo
        evento = f"Dispositivo {dispositivo.id_sensor} registrado"
        self.historial_eventos.append(evento)
        print(f"✅ {evento}")
    
    def escanear_dispositivos(self):
        """Escanear todos los dispositivos y actualizar estados"""
        import random
        
        print(f"🔄 Escaneando {len(self.dispositivos)} dispositivos...")
        
        for id_dispositivo, dispositivo in self.dispositivos.items():
            # Simular lectura según tipo de dispositivo
            if isinstance(dispositivo, SensorTemperaturaAvanzado):
                # Temperatura aleatoria dentro de rangos
                rango = dispositivo.limite_max - dispositivo.limite_min
                valor = dispositivo.limite_min + random.uniform(0, rango * 1.2)
                dispositivo.registrar_lectura(valor)
                
            elif isinstance(dispositivo, SensorPresion):
                # Presión aleatoria
                valor = random.uniform(0, dispositivo.presion_maxima * 1.1)
                dispositivo.registrar_lectura(valor)
        
        self._actualizar_alarmas()
    
    def _actualizar_alarmas(self):
        """Actualizar lista de alarmas del sistema"""
        self.alarmas_activas.clear()
        
        for id_dispositivo, dispositivo in self.dispositivos.items():
            if dispositivo.alarmas:
                for alarma in dispositivo.alarmas:
                    self.alarmas_activas.append({
                        'dispositivo': id_dispositivo,
                        'tipo_alarma': alarma,
                        'ubicacion': dispositivo.ubicacion,
                        'estado': dispositivo.estado
                    })
    
    def generar_reporte_ejecutivo(self):
        """Generar reporte completo del sistema"""
        print(f"\n🏭 REPORTE EJECUTIVO - {self.nombre_planta}")
        print(f"{'='*70}")
        
        # Estadísticas generales
        total_dispositivos = len(self.dispositivos)
        dispositivos_operativos = sum(1 for d in self.dispositivos.values() 
                                    if d.estado == "operativo")
        
        print(f"📊 RESUMEN GENERAL:")
        print(f"   🔧 Total dispositivos: {total_dispositivos}")
        print(f"   ✅ Dispositivos operativos: {dispositivos_operativos}")
        print(f"   🚨 Alarmas activas: {len(self.alarmas_activas)}")
        print(f"   📈 Disponibilidad: {(dispositivos_operativos/total_dispositivos*100):.1f}%")
        
        # Detalle de alarmas
        if self.alarmas_activas:
            print(f"\n🚨 ALARMAS ACTIVAS:")
            for alarma in self.alarmas_activas:
                print(f"   ⚠️ {alarma['dispositivo']}: {alarma['tipo_alarma']}")
                print(f"      📍 {alarma['ubicacion']} | Estado: {alarma['estado']}")
        else:
            print(f"\n✅ Sin alarmas activas - Sistema operando normalmente")
        
        # Detalle por zonas
        zonas = {}
        for dispositivo in self.dispositivos.values():
            zona = dispositivo.ubicacion
            if zona not in zonas:
                zonas[zona] = {'dispositivos': 0, 'operativos': 0, 'alarmas': 0}
            
            zonas[zona]['dispositivos'] += 1
            if dispositivo.estado == "operativo":
                zonas[zona]['operativos'] += 1
            if dispositivo.alarmas:
                zonas[zona]['alarmas'] += len(dispositivo.alarmas)
        
        print(f"\n📍 ESTADO POR ZONAS:")
        for zona, stats in zonas.items():
            disponibilidad = (stats['operativos'] / stats['dispositivos'] * 100)
            print(f"   🏭 {zona}:")
            print(f"      📊 {stats['dispositivos']} dispositivos | "
                  f"✅ {stats['operativos']} operativos | "
                  f"🚨 {stats['alarmas']} alarmas | "
                  f"📈 {disponibilidad:.1f}% disponibilidad")
    
    def exportar_datos_json(self):
        """Preparar datos para API Flask (formato JSON)"""
        datos_exportacion = {
            'planta': self.nombre_planta,
            'timestamp': self._obtener_timestamp(),
            'dispositivos': [],
            'alarmas': self.alarmas_activas,
            'resumen': {
                'total_dispositivos': len(self.dispositivos),
                'dispositivos_operativos': sum(1 for d in self.dispositivos.values() 
                                             if d.estado == "operativo"),
                'total_alarmas': len(self.alarmas_activas)
            }
        }
        
        for id_dispositivo, dispositivo in self.dispositivos.items():
            ultima_lectura = dispositivo.obtener_ultima_lectura()
            datos_exportacion['dispositivos'].append({
                'id': id_dispositivo,
                'tipo': type(dispositivo).__name__,
                'ubicacion': dispositivo.ubicacion,
                'estado': dispositivo.estado,
                'unidad_medida': dispositivo.unidad_medida,
                'ultima_lectura': {
                    'timestamp': ultima_lectura[0] if ultima_lectura else None,
                    'valor': ultima_lectura[1] if ultima_lectura else None
                },
                'total_lecturas': len(dispositivo.historial)
            })
        
        return datos_exportacion
    
    def _obtener_timestamp(self):
        """Obtener timestamp actual"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def paso_7_proyecto_integrador():
    """
    🎯 OBJETIVO: Integrar todos los conceptos POO en un sistema completo
    """
    print("\n" + "=" * 70)
    print("PASO 7: PROYECTO INTEGRADOR - SISTEMA SCADA")
    print("=" * 70)
    
    # Crear sistema SCADA
    scada = SistemaSCADA("Planta Petroquímica Central")
    
    # Registrar dispositivos diversos
    print(f"\n🔧 REGISTRANDO DISPOSITIVOS EN EL SISTEMA:")
    
    dispositivos_planta = [
        SensorTemperaturaAvanzado("TEMP_REACTOR_A", "Reactor Principal A", 60, 150),
        SensorTemperaturaAvanzado("TEMP_REACTOR_B", "Reactor Secundario B", 50, 120),
        SensorPresion("PRES_LINEA_PRIN", "Línea Principal", 8.0),
        SensorPresion("PRES_SEPARADOR", "Separador Gas-Líquido", 5.0),
        SensorTemperaturaAvanzado("TEMP_INTERCAM", "Intercambiador Calor", 40, 100),
        SensorPresion("PRES_COMPRESOR", "Compresor Principal", 12.0)
    ]
    
    for dispositivo in dispositivos_planta:
        scada.registrar_dispositivo(dispositivo)
    
    # Simular operación durante varios ciclos
    print(f"\n🔄 SIMULANDO OPERACIÓN DE LA PLANTA:")
    
    for ciclo in range(1, 6):
        print(f"\n⏰ CICLO DE ESCANEO {ciclo}:")
        scada.escanear_dispositivos()
        
        if ciclo % 2 == 0:  # Cada 2 ciclos, generar reporte
            scada.generar_reporte_ejecutivo()
    
    # Exportar datos para Flask API
    print(f"\n🌐 EXPORTANDO DATOS PARA API FLASK:")
    datos_json = scada.exportar_datos_json()
    
    print(f"✅ Datos preparados para JSON:")
    print(f"   📊 Planta: {datos_json['planta']}")
    print(f"   🕐 Timestamp: {datos_json['timestamp']}")
    print(f"   🔧 Dispositivos: {len(datos_json['dispositivos'])}")
    print(f"   🚨 Alarmas: {len(datos_json['alarmas'])}")
    
    # Simular preparación para base de datos SQL
    print(f"\n💾 PREPARANDO DATOS PARA BASE DE DATOS SQL:")
    registros_sql = []
    
    for dispositivo_data in datos_json['dispositivos']:
        if dispositivo_data['ultima_lectura']['valor'] is not None:
            registro = (
                dispositivo_data['id'],
                dispositivo_data['ubicacion'],
                dispositivo_data['ultima_lectura']['valor'],
                dispositivo_data['unidad_medida'],
                dispositivo_data['estado'],
                dispositivo_data['ultima_lectura']['timestamp']
            )
            registros_sql.append(registro)
    
    print(f"✅ {len(registros_sql)} registros preparados para INSERT en SQL")
    print(f"   Formato: (id, ubicacion, valor, unidad, estado, timestamp)")

# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL - EJECUTA TODA LA SECUENCIA DE ENSEÑANZA
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """
    🎯 FUNCIÓN PRINCIPAL: Ejecuta todos los pasos del temario
    
    Esta función coordina todo el aprendizaje de POO paso a paso,
    siguiendo nuestra metodología de enseñanza estructurada.
    """
    print("🐍 TEMARIO COMPLETO: PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("🎯 Objetivo: Dominar POO para automatización industrial")
    print("📖 Basado en: Curso Intensivo de Python - Eric Matthes")
    print("👨‍🏫 Tutor: GitHub Copilot | 👨‍🎓 Estudiante: José")
    
    # Ejecutar todos los pasos en secuencia
    paso_1_conceptos_fundamentales()
    paso_2_creacion_uso_objetos()
    paso_3_atributos_clase_instancia()
    paso_4_herencia_practica()
    paso_5_polimorfismo()
    paso_6_metodos_especiales()
    paso_7_proyecto_integrador()
    
    # Resumen final
    print("\n" + "🎉" * 70)
    print("TEMARIO POO COMPLETADO EXITOSAMENTE")
    print("🎉" * 70)
    
    print(f"\n✅ CONCEPTOS DOMINADOS:")
    print("   🔸 Clases y objetos")
    print("   🔸 Atributos de instancia y clase")
    print("   🔸 Métodos de instancia, clase y estáticos")
    print("   🔸 Herencia y especialización")
    print("   🔸 Polimorfismo")
    print("   🔸 Métodos especiales (dunder methods)")
    print("   🔸 Integración en sistemas industriales")
    
    print(f"\n🚀 PREPARADO PARA:")
    print("   🏭 Modelar dispositivos PyModbus")
    print("   🌐 Crear clases para APIs Flask")
    print("   💾 Diseñar modelos para bases de datos")
    print("   🖥️ Estructurar aplicaciones Tkinter")
    print("   📊 Integrar con NumPy y Matplotlib")
    
    print(f"\n📋 SIGUIENTE PASO:")
    print("   🎯 Completar prácticas en [Modulo_1_3_POO_Practicas].ipynb")
    print("   ✍️ Confirmar dominio antes de avanzar al Módulo 2.1")

if __name__ == "__main__":
    main()
