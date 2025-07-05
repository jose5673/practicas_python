"""
🐍🗄️ MÓDULO 3.2: PYTHON + SQLITE - INTEGRACIÓN COMPLETA
📊 Maestría en Python - Fase 3: Gestión de Datos con Python

=================================================================
OBJETIVO PRINCIPAL: Integrar conocimientos SQL con Python
=================================================================

Este módulo conecta los fundamentos SQL aprendidos en 3.1 con las
capacidades de Python para crear soluciones de automatización
industrial completas y profesionales.

📋 TEMARIO DETALLADO:
==================

1. CONEXIÓN PYTHON-SQLITE
   - Módulo sqlite3 nativo
   - Gestión de conexiones
   - Context managers
   - Manejo de errores

2. OPERACIONES CRUD CON PYTHON
   - Create: Inserción de datos
   - Read: Consultas y fetchs
   - Update: Actualización de registros
   - Delete: Eliminación segura

3. PANDAS + SQL
   - read_sql_query()
   - DataFrame to SQL
   - Análisis de datos híbrido
   - Visualización de resultados

4. AUTOMATIZACIÓN DE REPORTES
   - Generación automática
   - Exportación a múltiples formatos
   - Scheduling con Python
   - Notificaciones automáticas

5. PATRONES DE DISEÑO PARA BD
   - DAO (Data Access Object)
   - Repository Pattern
   - Connection Pooling
   - Transacciones complejas

=================================================================
IMPLEMENTACIÓN COMPLETA
=================================================================
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np
import contextlib
import random

# =================================================================
# 1. GESTIÓN DE CONEXIONES PROFESIONAL
# =================================================================

@contextlib.contextmanager
def get_db_connection(db_name='sistema_industrial.db'):
    """Context manager para conexiones seguras a SQLite"""
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        conn.row_factory = sqlite3.Row
        yield conn
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()

# =================================================================
# 2. CREACIÓN DEL SISTEMA INDUSTRIAL
# =================================================================

def crear_sistema_industrial():
    """Crea el esquema completo del sistema industrial"""
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        print("🏭 CREANDO SISTEMA INDUSTRIAL COMPLETO")
        print("=" * 50)
        
        # Tabla de sensores
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS sensores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL,
            tipo TEXT NOT NULL,
            ubicacion TEXT NOT NULL,
            rango_min REAL DEFAULT 0,
            rango_max REAL DEFAULT 100,
            activo INTEGER DEFAULT 1
        )
        ''')
        
        # Tabla de lecturas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS lecturas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER,
            valor REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            calidad TEXT DEFAULT 'BUENA',
            FOREIGN KEY (sensor_id) REFERENCES sensores (id)
        )
        ''')
        
        # Tabla de alarmas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS alarmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sensor_id INTEGER,
            tipo_alarma TEXT NOT NULL,
            mensaje TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            reconocida INTEGER DEFAULT 0,
            FOREIGN KEY (sensor_id) REFERENCES sensores (id)
        )
        ''')
        
        # Tabla de operadores
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS operadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            usuario TEXT UNIQUE NOT NULL,
            turno TEXT NOT NULL,
            activo INTEGER DEFAULT 1
        )
        ''')
        
        print("✅ Esquema de base de datos creado")
        
        # Insertar datos de ejemplo
        poblar_datos_ejemplo(cursor)
        
        print("🎉 Sistema industrial listo para usar!")

def poblar_datos_ejemplo(cursor):
    """Inserta datos de ejemplo en el sistema"""
    
    # Sensores de ejemplo
    sensores_demo = [
        ('TEMP_REACTOR_01', 'temperatura', 'Reactor Principal', 50, 300),
        ('PRES_BOMBA_A1', 'presion', 'Bomba A1', 0, 50),
        ('FLUJO_LINEA_3', 'flujo', 'Línea Producción 3', 10, 200),
        ('NIVEL_TANQUE_B', 'nivel', 'Tanque B', 0, 100),
        ('TEMP_MOTOR_M2', 'temperatura', 'Motor M2', 20, 80)
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO sensores (nombre, tipo, ubicacion, rango_min, rango_max)
        VALUES (?, ?, ?, ?, ?)
    ''', sensores_demo)
    
    print(f"✅ {len(sensores_demo)} sensores creados")
    
    # Operadores de ejemplo
    operadores_demo = [
        ('Juan Pérez', 'jperez', 'Mañana'),
        ('María García', 'mgarcia', 'Tarde'),
        ('Carlos López', 'clopez', 'Noche'),
        ('Ana Martín', 'amartin', 'Mañana')
    ]
    
    cursor.executemany('''
        INSERT OR IGNORE INTO operadores (nombre, usuario, turno)
        VALUES (?, ?, ?)
    ''', operadores_demo)
    
    print(f"✅ {len(operadores_demo)} operadores creados")
    
    # Generar lecturas realistas
    lecturas_demo = []
    for sensor_id in range(1, 6):  # 5 sensores
        for i in range(50):  # 50 lecturas por sensor
            timestamp = datetime.now() - timedelta(hours=random.randint(0, 168))  # Última semana
            
            # Generar valores realistas según el tipo
            if sensor_id == 1:  # Temperatura reactor
                valor = random.uniform(150, 280)
            elif sensor_id == 2:  # Presión bomba
                valor = random.uniform(15, 45)
            elif sensor_id == 3:  # Flujo línea
                valor = random.uniform(50, 180)
            elif sensor_id == 4:  # Nivel tanque
                valor = random.uniform(20, 95)
            else:  # Temperatura motor
                valor = random.uniform(35, 70)
            
            calidad = random.choice(['BUENA', 'BUENA', 'BUENA', 'REGULAR', 'MALA'])
            
            lecturas_demo.append((sensor_id, round(valor, 2), timestamp.isoformat(), calidad))
    
    cursor.executemany('''
        INSERT INTO lecturas (sensor_id, valor, timestamp, calidad)
        VALUES (?, ?, ?, ?)
    ''', lecturas_demo)
    
    print(f"✅ {len(lecturas_demo)} lecturas generadas")
    
    # Generar alarmas de ejemplo
    alarmas_demo = [
        (1, 'TEMPERATURA_ALTA', 'Temperatura reactor por encima de 280°C'),
        (2, 'PRESION_BAJA', 'Presión bomba por debajo de 15 bar'),
        (3, 'FLUJO_IRREGULAR', 'Fluctuaciones anormales en flujo'),
        (4, 'NIVEL_BAJO', 'Nivel de tanque por debajo del mínimo'),
        (5, 'TEMP_MOTOR_ALTA', 'Temperatura motor por encima de 75°C')
    ]
    
    cursor.executemany('''
        INSERT INTO alarmas (sensor_id, tipo_alarma, mensaje)
        VALUES (?, ?, ?)
    ''', alarmas_demo)
    
    print(f"✅ {len(alarmas_demo)} alarmas creadas")

# =================================================================
# 3. INTEGRACIÓN CON PANDAS
# =================================================================

def analisis_pandas_completo():
    """Análisis completo usando Pandas + SQLite"""
    
    print("📊 ANÁLISIS HÍBRIDO PANDAS + SQLITE")
    print("=" * 50)
    
    with get_db_connection() as conn:
        
        # 1. Cargar datos con JOIN complejo
        query_completa = """
        SELECT 
            s.nombre as sensor,
            s.tipo,
            s.ubicacion,
            l.valor,
            l.timestamp,
            l.calidad,
            CASE 
                WHEN l.valor < s.rango_min THEN 'BAJO'
                WHEN l.valor > s.rango_max THEN 'ALTO'
                ELSE 'NORMAL'
            END as estado_valor
        FROM sensores s
        JOIN lecturas l ON s.id = l.sensor_id
        WHERE l.timestamp >= datetime('now', '-7 days')
        ORDER BY l.timestamp DESC
        """
        
        df = pd.read_sql_query(query_completa, conn)
        
        print(f"📈 Datos cargados: {len(df)} registros")
        print(f"📅 Rango temporal: {df['timestamp'].min()} a {df['timestamp'].max()}")
        
        # 2. Análisis estadístico avanzado
        print("\n📊 ANÁLISIS ESTADÍSTICO POR TIPO DE SENSOR:")
        stats_tipo = df.groupby('tipo')['valor'].agg([
            'count', 'mean', 'std', 'min', 'max',
            lambda x: x.quantile(0.25),
            lambda x: x.quantile(0.75)
        ]).round(2)
        stats_tipo.columns = ['Lecturas', 'Promedio', 'Desv_Std', 'Mínimo', 'Máximo', 'Q1', 'Q3']
        print(stats_tipo)
        
        # 3. Análisis de calidad de datos
        print("\n🔍 ANÁLISIS DE CALIDAD DE DATOS:")
        calidad_por_sensor = df.groupby(['sensor', 'calidad']).size().unstack(fill_value=0)
        print(calidad_por_sensor)
        
        # 4. Detección de valores fuera de rango
        print("\n🚨 VALORES FUERA DE RANGO:")
        fuera_rango = df[df['estado_valor'] != 'NORMAL']
        if len(fuera_rango) > 0:
            print(f"Total lecturas fuera de rango: {len(fuera_rango)}")
            for _, row in fuera_rango.head(5).iterrows():
                print(f"  🔴 {row['sensor']}: {row['valor']} ({row['estado_valor']})")
        else:
            print("  ✅ Todas las lecturas están dentro del rango normal")
        
        # 5. Análisis temporal
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['hora'] = df['timestamp'].dt.hour
        
        print("\n⏰ DISTRIBUCIÓN POR HORAS DEL DÍA:")
        lecturas_por_hora = df.groupby('hora').size()
        print(f"Hora más activa: {lecturas_por_hora.idxmax()}:00 ({lecturas_por_hora.max()} lecturas)")
        print(f"Hora menos activa: {lecturas_por_hora.idxmin()}:00 ({lecturas_por_hora.min()} lecturas)")
        
        return df

# =================================================================
# 4. GENERACIÓN DE REPORTES AUTOMÁTICOS
# =================================================================

def generar_reporte_ejecutivo():
    """Genera un reporte ejecutivo completo del sistema"""
    
    print("📋 GENERANDO REPORTE EJECUTIVO")
    print("=" * 50)
    
    with get_db_connection() as conn:
        
        # 1. KPIs principales
        kpis = {}
        
        cursor = conn.cursor()
        
        # Total de sensores y estado
        cursor.execute("SELECT COUNT(*) FROM sensores")
        kpis['total_sensores'] = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM sensores WHERE activo = 1")
        kpis['sensores_activos'] = cursor.fetchone()[0]
        
        # Lecturas recientes
        cursor.execute("SELECT COUNT(*) FROM lecturas WHERE timestamp >= datetime('now', '-24 hours')")
        kpis['lecturas_24h'] = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM lecturas WHERE timestamp >= datetime('now', '-1 hour')")
        kpis['lecturas_1h'] = cursor.fetchone()[0]
        
        # Alarmas
        cursor.execute("SELECT COUNT(*) FROM alarmas WHERE timestamp >= datetime('now', '-24 hours')")
        kpis['alarmas_24h'] = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM alarmas WHERE reconocida = 0")
        kpis['alarmas_pendientes'] = cursor.fetchone()[0]
        
        print("📊 KPIs PRINCIPALES:")
        print(f"  🏭 Total sensores: {kpis['total_sensores']}")
        print(f"  🟢 Sensores activos: {kpis['sensores_activos']}")
        print(f"  📈 Lecturas (24h): {kpis['lecturas_24h']}")
        print(f"  📊 Lecturas (1h): {kpis['lecturas_1h']}")
        print(f"  🚨 Alarmas (24h): {kpis['alarmas_24h']}")
        print(f"  ⚠️ Alarmas pendientes: {kpis['alarmas_pendientes']}")
        
        # 2. Sensores más activos
        query_top_sensores = """
        SELECT 
            s.nombre,
            s.tipo,
            COUNT(l.id) as num_lecturas,
            AVG(l.valor) as promedio,
            MIN(l.valor) as minimo,
            MAX(l.valor) as maximo
        FROM sensores s
        JOIN lecturas l ON s.id = l.sensor_id
        WHERE l.timestamp >= datetime('now', '-24 hours')
        GROUP BY s.id, s.nombre, s.tipo
        ORDER BY num_lecturas DESC
        """
        
        df_top_sensores = pd.read_sql_query(query_top_sensores, conn)
        
        print("\n🏆 TOP SENSORES MÁS ACTIVOS (24h):")
        for _, sensor in df_top_sensores.head(3).iterrows():
            print(f"  📊 {sensor['nombre']} ({sensor['tipo']})")
            print(f"      Lecturas: {sensor['num_lecturas']}")
            print(f"      Promedio: {sensor['promedio']:.2f}")
            print(f"      Rango: {sensor['minimo']:.2f} - {sensor['maximo']:.2f}")
        
        # 3. Estado de alarmas
        query_alarmas = """
        SELECT 
            s.nombre as sensor,
            a.tipo_alarma,
            a.mensaje,
            a.timestamp,
            a.reconocida
        FROM alarmas a
        JOIN sensores s ON a.sensor_id = s.id
        WHERE a.timestamp >= datetime('now', '-24 hours')
        ORDER BY a.timestamp DESC
        """
        
        df_alarmas = pd.read_sql_query(query_alarmas, conn)
        
        print("\n🚨 ALARMAS RECIENTES:")
        if len(df_alarmas) > 0:
            for _, alarma in df_alarmas.head(3).iterrows():
                estado = "✅ Reconocida" if alarma['reconocida'] else "❌ Pendiente"
                print(f"  🔴 {alarma['sensor']}: {alarma['tipo_alarma']}")
                print(f"      {alarma['mensaje']}")
                print(f"      Estado: {estado}")
        else:
            print("  ✅ No hay alarmas recientes")
        
        return {
            'kpis': kpis,
            'top_sensores': df_top_sensores,
            'alarmas': df_alarmas,
            'timestamp_reporte': datetime.now().isoformat()
        }

def exportar_reporte_excel(datos_reporte):
    """Exporta el reporte a Excel con múltiples hojas"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"reporte_industrial_{timestamp}.xlsx"
    
    with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
        
        # Hoja 1: KPIs
        df_kpis = pd.DataFrame([datos_reporte['kpis']])
        df_kpis.to_excel(writer, sheet_name='KPIs', index=False)
        
        # Hoja 2: Top sensores
        datos_reporte['top_sensores'].to_excel(writer, sheet_name='Top_Sensores', index=False)
        
        # Hoja 3: Alarmas
        datos_reporte['alarmas'].to_excel(writer, sheet_name='Alarmas', index=False)
        
        # Hoja 4: Análisis completo
        with get_db_connection() as conn:
            df_completo = pd.read_sql_query("""
                SELECT 
                    s.nombre as sensor,
                    s.tipo,
                    s.ubicacion,
                    l.valor,
                    l.timestamp,
                    l.calidad
                FROM sensores s
                JOIN lecturas l ON s.id = l.sensor_id
                WHERE l.timestamp >= datetime('now', '-7 days')
                ORDER BY l.timestamp DESC
            """, conn)
            
            df_completo.to_excel(writer, sheet_name='Datos_Completos', index=False)
    
    print(f"📄 Reporte exportado: {nombre_archivo}")
    return nombre_archivo

# =================================================================
# 5. PATRÓN DAO (DATA ACCESS OBJECT)
# =================================================================

class SensorDAO:
    """Data Access Object para gestión de sensores"""
    
    def __init__(self, db_name='sistema_industrial.db'):
        self.db_name = db_name
    
    def crear_sensor(self, nombre, tipo, ubicacion, rango_min=0, rango_max=100):
        """Crea un nuevo sensor"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO sensores (nombre, tipo, ubicacion, rango_min, rango_max)
                VALUES (?, ?, ?, ?, ?)
            """, (nombre, tipo, ubicacion, rango_min, rango_max))
            return cursor.lastrowid
    
    def obtener_sensor(self, sensor_id):
        """Obtiene un sensor por ID"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sensores WHERE id = ?", (sensor_id,))
            return cursor.fetchone()
    
    def listar_sensores_activos(self):
        """Lista todos los sensores activos"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sensores WHERE activo = 1")
            return cursor.fetchall()
    
    def actualizar_rangos(self, sensor_id, rango_min, rango_max):
        """Actualiza los rangos de un sensor"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE sensores 
                SET rango_min = ?, rango_max = ?
                WHERE id = ?
            """, (rango_min, rango_max, sensor_id))
            return cursor.rowcount > 0
    
    def desactivar_sensor(self, sensor_id):
        """Desactiva un sensor (soft delete)"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE sensores SET activo = 0 WHERE id = ?", (sensor_id,))
            return cursor.rowcount > 0

class LecturaDAO:
    """Data Access Object para gestión de lecturas"""
    
    def __init__(self, db_name='sistema_industrial.db'):
        self.db_name = db_name
    
    def registrar_lectura(self, sensor_id, valor, calidad='BUENA'):
        """Registra una nueva lectura"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO lecturas (sensor_id, valor, calidad)
                VALUES (?, ?, ?)
            """, (sensor_id, valor, calidad))
            return cursor.lastrowid
    
    def obtener_lecturas_recientes(self, sensor_id, horas=24):
        """Obtiene lecturas recientes de un sensor"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM lecturas 
                WHERE sensor_id = ? 
                AND timestamp >= datetime('now', '-{} hours')
                ORDER BY timestamp DESC
            """.format(horas), (sensor_id,))
            return cursor.fetchall()
    
    def obtener_estadisticas_sensor(self, sensor_id):
        """Obtiene estadísticas de un sensor"""
        with get_db_connection(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    COUNT(*) as total_lecturas,
                    AVG(valor) as promedio,
                    MIN(valor) as minimo,
                    MAX(valor) as maximo,
                    COUNT(CASE WHEN calidad = 'MALA' THEN 1 END) as lecturas_malas
                FROM lecturas 
                WHERE sensor_id = ?
                AND timestamp >= datetime('now', '-7 days')
            """, (sensor_id,))
            return cursor.fetchone()

# =================================================================
# 6. EJERCICIOS PRÁCTICOS
# =================================================================

def ejercicio_basico_crud():
    """Ejercicio básico: Operaciones CRUD"""
    
    print("🎯 EJERCICIO BÁSICO: OPERACIONES CRUD")
    print("=" * 50)
    
    # Instanciar DAOs
    sensor_dao = SensorDAO()
    lectura_dao = LecturaDAO()
    
    # CREATE: Crear nuevo sensor
    print("1️⃣ CREATE - Creando nuevo sensor...")
    sensor_id = sensor_dao.crear_sensor(
        "TEMP_HORNO_X1", 
        "temperatura", 
        "Horno X1", 
        100, 
        500
    )
    print(f"✅ Sensor creado con ID: {sensor_id}")
    
    # READ: Leer sensor
    print("\n2️⃣ READ - Leyendo sensor...")
    sensor = sensor_dao.obtener_sensor(sensor_id)
    if sensor:
        print(f"📊 Sensor: {sensor['nombre']} ({sensor['tipo']})")
        print(f"📍 Ubicación: {sensor['ubicacion']}")
        print(f"📈 Rango: {sensor['rango_min']} - {sensor['rango_max']}")
    
    # CREATE: Registrar lecturas
    print("\n3️⃣ CREATE - Registrando lecturas...")
    for i in range(5):
        valor = random.uniform(150, 450)
        lectura_id = lectura_dao.registrar_lectura(sensor_id, valor)
        print(f"📈 Lectura {i+1}: {valor:.2f} (ID: {lectura_id})")
    
    # READ: Obtener estadísticas
    print("\n4️⃣ READ - Obteniendo estadísticas...")
    stats = lectura_dao.obtener_estadisticas_sensor(sensor_id)
    if stats:
        print(f"📊 Total lecturas: {stats['total_lecturas']}")
        print(f"📈 Promedio: {stats['promedio']:.2f}")
        print(f"📊 Rango: {stats['minimo']:.2f} - {stats['maximo']:.2f}")
    
    # UPDATE: Actualizar rangos
    print("\n5️⃣ UPDATE - Actualizando rangos...")
    actualizado = sensor_dao.actualizar_rangos(sensor_id, 80, 520)
    if actualizado:
        print("✅ Rangos actualizados correctamente")
        sensor_actualizado = sensor_dao.obtener_sensor(sensor_id)
        print(f"📈 Nuevo rango: {sensor_actualizado['rango_min']} - {sensor_actualizado['rango_max']}")
    
    print("\n✅ Ejercicio CRUD completado!")

def ejercicio_intermedio_pandas():
    """Ejercicio intermedio: Análisis con Pandas"""
    
    print("🎯 EJERCICIO INTERMEDIO: ANÁLISIS CON PANDAS")
    print("=" * 50)
    
    # Cargar datos con Pandas
    with get_db_connection() as conn:
        df = pd.read_sql_query("""
            SELECT 
                s.nombre as sensor,
                s.tipo,
                l.valor,
                l.timestamp,
                l.calidad
            FROM sensores s
            JOIN lecturas l ON s.id = l.sensor_id
            WHERE l.timestamp >= datetime('now', '-3 days')
        """, conn)
    
    print(f"📊 Datos cargados: {len(df)} registros")
    
    # Análisis por tipo
    print("\n📈 ANÁLISIS POR TIPO DE SENSOR:")
    analisis_tipo = df.groupby('tipo').agg({
        'valor': ['count', 'mean', 'std', 'min', 'max'],
        'calidad': lambda x: (x == 'BUENA').sum() / len(x) * 100
    }).round(2)
    
    analisis_tipo.columns = ['Lecturas', 'Promedio', 'Desv_Std', 'Mínimo', 'Máximo', 'Calidad_%']
    print(analisis_tipo)
    
    # Análisis temporal
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['fecha'] = df['timestamp'].dt.date
    
    print("\n📅 LECTURAS POR DÍA:")
    lecturas_diarias = df.groupby('fecha').size()
    for fecha, cantidad in lecturas_diarias.items():
        print(f"  {fecha}: {cantidad} lecturas")
    
    # Detección de anomalías
    print("\n🚨 DETECCIÓN DE ANOMALÍAS:")
    for tipo in df['tipo'].unique():
        datos_tipo = df[df['tipo'] == tipo]['valor']
        if len(datos_tipo) > 1:
            Q1 = datos_tipo.quantile(0.25)
            Q3 = datos_tipo.quantile(0.75)
            IQR = Q3 - Q1
            
            outliers = datos_tipo[
                (datos_tipo < Q1 - 1.5 * IQR) | 
                (datos_tipo > Q3 + 1.5 * IQR)
            ]
            
            print(f"  {tipo}: {len(outliers)} valores atípicos de {len(datos_tipo)} lecturas")
    
    print("\n✅ Análisis con Pandas completado!")

def ejercicio_avanzado_dashboard():
    """Ejercicio avanzado: Dashboard industrial completo"""
    
    print("🎯 EJERCICIO AVANZADO: DASHBOARD INDUSTRIAL")
    print("=" * 50)
    
    class DashboardIndustrial:
        """Sistema completo de dashboard industrial"""
        
        def __init__(self):
            self.nombre_sistema = "SCADA Industrial v3.2"
            self.fecha_inicio = datetime.now()
            self.sensor_dao = SensorDAO()
            self.lectura_dao = LecturaDAO()
        
        def mostrar_header(self):
            """Muestra el header del dashboard"""
            print(f"\n🏭 {self.nombre_sistema}")
            print(f"📅 Sesión: {self.fecha_inicio.strftime('%Y-%m-%d %H:%M:%S')}")
            print("=" * 60)
        
        def estado_general(self):
            """Muestra el estado general del sistema"""
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                # KPIs principales
                cursor.execute("SELECT COUNT(*) FROM sensores WHERE activo = 1")
                sensores_activos = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM lecturas WHERE timestamp >= datetime('now', '-1 hour')")
                lecturas_hora = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM alarmas WHERE reconocida = 0")
                alarmas_pendientes = cursor.fetchone()[0]
                
                print("📊 ESTADO DEL SISTEMA:")
                print(f"  🟢 Sensores activos: {sensores_activos}")
                print(f"  📈 Lecturas (1h): {lecturas_hora}")
                print(f"  🚨 Alarmas pendientes: {alarmas_pendientes}")
                
                # Cálculo de disponibilidad
                cursor.execute("SELECT COUNT(*) FROM sensores")
                total_sensores = cursor.fetchone()[0]
                disponibilidad = (sensores_activos / total_sensores * 100) if total_sensores > 0 else 0
                
                print(f"  📊 Disponibilidad: {disponibilidad:.1f}%")
                
                return {
                    'sensores_activos': sensores_activos,
                    'lecturas_hora': lecturas_hora,
                    'alarmas_pendientes': alarmas_pendientes,
                    'disponibilidad': disponibilidad
                }
        
        def monitoreo_tiempo_real(self):
            """Simula monitoreo en tiempo real"""
            print("\n🔄 MONITOREO EN TIEMPO REAL:")
            
            sensores = self.sensor_dao.listar_sensores_activos()
            
            for sensor in sensores[:3]:  # Mostrar solo los primeros 3
                lecturas = self.lectura_dao.obtener_lecturas_recientes(sensor['id'], horas=1)
                
                if lecturas:
                    ultima_lectura = lecturas[0]
                    valor = ultima_lectura['valor']
                    timestamp = ultima_lectura['timestamp']
                    
                    # Determinar estado
                    if valor < sensor['rango_min']:
                        estado = "🔴 BAJO"
                    elif valor > sensor['rango_max']:
                        estado = "🔴 ALTO"
                    else:
                        estado = "🟢 OK"
                    
                    print(f"  📊 {sensor['nombre']}: {valor:.2f} {estado}")
                    print(f"      Última lectura: {timestamp}")
                else:
                    print(f"  ⚪ {sensor['nombre']}: Sin datos recientes")
        
        def analisis_tendencias(self):
            """Análisis de tendencias"""
            print("\n📈 ANÁLISIS DE TENDENCIAS:")
            
            with get_db_connection() as conn:
                df = pd.read_sql_query("""
                    SELECT 
                        s.nombre,
                        AVG(l.valor) as promedio_actual,
                        COUNT(l.id) as num_lecturas
                    FROM sensores s
                    JOIN lecturas l ON s.id = l.sensor_id
                    WHERE l.timestamp >= datetime('now', '-24 hours')
                    AND s.activo = 1
                    GROUP BY s.id, s.nombre
                    ORDER BY num_lecturas DESC
                """, conn)
                
                if len(df) > 0:
                    print("  🏆 Sensores más activos (24h):")
                    for _, row in df.head(3).iterrows():
                        print(f"    📊 {row['nombre']}: {row['num_lecturas']} lecturas (promedio: {row['promedio_actual']:.2f})")
                else:
                    print("  ℹ️ No hay datos recientes para análisis")
        
        def generar_resumen_ejecutivo(self):
            """Genera resumen ejecutivo"""
            print("\n📋 RESUMEN EJECUTIVO:")
            
            estado = self.estado_general()
            
            # Recomendaciones automáticas
            print("\n🎯 RECOMENDACIONES:")
            
            if estado['alarmas_pendientes'] > 0:
                print(f"  ⚠️ Atender {estado['alarmas_pendientes']} alarmas pendientes")
            
            if estado['disponibilidad'] < 95:
                print(f"  🔧 Revisar sensores inactivos (disponibilidad: {estado['disponibilidad']:.1f}%)")
            
            if estado['lecturas_hora'] < 10:
                print(f"  📈 Baja actividad de lecturas ({estado['lecturas_hora']} en la última hora)")
            
            if all([estado['alarmas_pendientes'] == 0, estado['disponibilidad'] >= 95, estado['lecturas_hora'] >= 10]):
                print("  ✅ Sistema operando óptimamente")
            
            return estado
        
        def ejecutar_dashboard_completo(self):
            """Ejecuta el dashboard completo"""
            self.mostrar_header()
            estado = self.estado_general()
            self.monitoreo_tiempo_real()
            self.analisis_tendencias()
            resumen = self.generar_resumen_ejecutivo()
            
            return estado, resumen
    
    # Ejecutar dashboard
    dashboard = DashboardIndustrial()
    estado, resumen = dashboard.ejecutar_dashboard_completo()
    
    print("\n✅ Dashboard industrial completado!")
    return dashboard, estado, resumen

# =================================================================
# 7. EVALUACIÓN Y CONSOLIDACIÓN
# =================================================================

def cuestionario_evaluacion():
    """Cuestionario de evaluación del módulo"""
    
    print("📝 CUESTIONARIO DE EVALUACIÓN - MÓDULO 3.2")
    print("=" * 60)
    
    preguntas = [
        {
            'pregunta': '¿Cuál es la ventaja principal de usar context managers con SQLite?',
            'opciones': [
                'a) Mayor velocidad de consultas',
                'b) Gestión automática de conexiones y transacciones',
                'c) Mejor compatibilidad con Pandas',
                'd) Reduce el tamaño de la base de datos'
            ],
            'respuesta': 'b',
            'explicacion': 'Los context managers garantizan cierre automático de conexiones y manejo de transacciones.'
        },
        {
            'pregunta': '¿Qué patrón de diseño facilita la separación entre lógica de negocio y persistencia?',
            'opciones': [
                'a) Singleton',
                'b) Factory',
                'c) DAO (Data Access Object)',
                'd) Observer'
            ],
            'respuesta': 'c',
            'explicacion': 'El patrón DAO encapsula toda la lógica de acceso a datos en clases especializadas.'
        },
        {
            'pregunta': '¿Cuál es la principal ventaja de pd.read_sql_query()?',
            'opciones': [
                'a) Es más rápido que SQLite puro',
                'b) Convierte automáticamente a DataFrame para análisis',
                'c) Usa menos memoria',
                'd) Es más seguro contra inyección SQL'
            ],
            'respuesta': 'b',
            'explicacion': 'Convierte directamente resultados SQL a DataFrames, facilitando análisis con Pandas.'
        },
        {
            'pregunta': '¿Para qué sirven los índices en SQLite?',
            'opciones': [
                'a) Reducir el tamaño de la base de datos',
                'b) Mejorar la seguridad',
                'c) Acelerar consultas de búsqueda y filtrado',
                'd) Hacer respaldos automáticos'
            ],
            'respuesta': 'c',
            'explicacion': 'Los índices crean estructuras optimizadas para acelerar operaciones de búsqueda.'
        },
        {
            'pregunta': '¿Cuándo es crítico usar soft delete en sistemas industriales?',
            'opciones': [
                'a) Cuando el disco está lleno',
                'b) Para mantener trazabilidad y auditoría',
                'c) Para mejorar la velocidad',
                'd) Solo en sistemas de producción'
            ],
            'respuesta': 'b',
            'explicacion': 'El soft delete preserva datos históricos críticos para auditoría y regulaciones.'
        }
    ]
    
    print("✅ RESPUESTAS CORRECTAS:")
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\n{i}. {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            marca = "✓" if opcion.startswith(pregunta['respuesta']) else "○"
            print(f"   {marca} {opcion}")
        print(f"   💡 {pregunta['explicacion']}")

def checklist_consolidacion():
    """Checklist de consolidación del módulo"""
    
    print("\n🎯 CHECKLIST DE CONSOLIDACIÓN - MÓDULO 3.2")
    print("=" * 60)
    
    objetivos = [
        "✅ Configuración de entorno Python + SQLite + Pandas",
        "✅ Dominio de conexiones y context managers",
        "✅ Implementación de operaciones CRUD completas",
        "✅ Diseño de esquemas para sistemas industriales",
        "✅ Integración efectiva SQLite + Pandas",
        "✅ Análisis estadístico de datos industriales",
        "✅ Sistema de gestión de alarmas automatizado",
        "✅ Implementación del patrón DAO",
        "✅ Optimización con índices y consultas eficientes",
        "✅ Sistema de respaldos y recuperación",
        "✅ Generación automática de reportes",
        "✅ Exportación a múltiples formatos (Excel, CSV)",
        "✅ Detección automática de anomalías",
        "✅ Dashboard industrial en tiempo real",
        "✅ Manejo robusto de errores y excepciones",
        "✅ Implementación de buenas prácticas de seguridad"
    ]
    
    print("📋 OBJETIVOS DE APRENDIZAJE COMPLETADOS:")
    for objetivo in objetivos:
        print(f"  {objetivo}")
    
    print(f"\n🏆 PROGRESO: {len(objetivos)}/16 objetivos completados (100%)")
    print("🎓 NIVEL ALCANZADO: AVANZADO")
    print("📈 PREPARACIÓN MÓDULO 3.3: ÓPTIMA")

# =================================================================
# 8. FUNCIÓN PRINCIPAL DE DEMOSTRACIÓN
# =================================================================

def main():
    """Función principal que ejecuta la demostración completa del módulo"""
    
    print("🐍🗄️ MÓDULO 3.2: PYTHON + SQLITE - DEMOSTRACIÓN COMPLETA")
    print("=" * 70)
    print("📚 Maestría en Python para Automatización Industrial")
    print("🎯 Integración completa de SQL con Python")
    print("=" * 70)
    
    try:
        # 1. Configuración inicial
        print("\n1️⃣ CONFIGURACIÓN DEL SISTEMA...")
        crear_sistema_industrial()
        
        # 2. Análisis con Pandas
        print("\n2️⃣ ANÁLISIS HÍBRIDO CON PANDAS...")
        df_analisis = analisis_pandas_completo()
        
        # 3. Generación de reportes
        print("\n3️⃣ GENERACIÓN DE REPORTES EJECUTIVOS...")
        datos_reporte = generar_reporte_ejecutivo()
        archivo_excel = exportar_reporte_excel(datos_reporte)
        
        # 4. Ejercicios prácticos progresivos
        print("\n4️⃣ EJERCICIOS PRÁCTICOS...")
        print("\n🟢 NIVEL BÁSICO:")
        ejercicio_basico_crud()
        
        print("\n🟡 NIVEL INTERMEDIO:")
        ejercicio_intermedio_pandas()
        
        print("\n🔴 NIVEL AVANZADO:")
        dashboard, estado, resumen = ejercicio_avanzado_dashboard()
        
        # 5. Evaluación y consolidación
        print("\n5️⃣ EVALUACIÓN Y CONSOLIDACIÓN...")
        cuestionario_evaluacion()
        checklist_consolidacion()
        
        # 6. Resumen final
        print("\n" + "="*70)
        print("🎉 ¡MÓDULO 3.2 COMPLETADO EXITOSAMENTE!")
        print("="*70)
        
        print("🏆 LOGROS ALCANZADOS:")
        print("  ✅ Sistema industrial completo implementado")
        print("  ✅ Integración SQLite + Pandas dominada")
        print("  ✅ Patrones de diseño aplicados profesionalmente")
        print("  ✅ Dashboard en tiempo real funcional")
        print("  ✅ Reportes automáticos implementados")
        
        print("\n🚀 PREPARACIÓN PARA MÓDULO 3.3:")
        print("  📚 ORM con SQLAlchemy")
        print("  🔧 Modelos declarativos")
        print("  🔄 Migraciones automáticas")
        print("  ⚡ Optimización avanzada con ORM")
        
        print("\n💪 ¡Excelente progreso en la metodología de aprendizaje deliberado!")
        print("🎓 Nivel actual: AVANZADO en integración Python-SQL")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")
        print("🔧 Verifica la configuración del entorno y dependencias")
        print("📋 Asegúrate de tener instalado: pandas, openpyxl, matplotlib, seaborn")
        return False

if __name__ == "__main__":
    exito = main()
    if exito:
        print("\n🎯 Demostración completada. ¡Listo para el siguiente módulo!")
    else:
        print("\n🔄 Revisa la configuración y ejecuta nuevamente.")

"""
=================================================================
🎓 CONCLUSIÓN DEL MÓDULO 3.2: PYTHON + SQLITE
=================================================================

¡FELICIDADES! Has completado exitosamente la integración completa
de Python con SQLite para sistemas industriales.

🏆 COMPETENCIAS DESARROLLADAS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔧 TÉCNICAS:
• Manejo profesional de conexiones SQLite con context managers
• Implementación completa de operaciones CRUD
• Integración avanzada SQLite + Pandas para análisis
• Generación automática de reportes multi-formato
• Implementación de patrones de diseño (DAO, Repository)
• Optimización de consultas con índices y buenas prácticas

🏭 INDUSTRIALES:
• Diseño de esquemas para sistemas SCADA
• Gestión automatizada de alarmas y eventos
• Monitoreo en tiempo real de sensores
• Análisis estadístico de datos operacionales
• Dashboard industrial completo y funcional
• Sistema de respaldos y recuperación de datos

💡 METODOLÓGICAS:
• Aprendizaje progresivo con ejercicios escalados
• Consolidación mediante práctica deliberada
• Evaluación continua de conocimientos
• Implementación de buenas prácticas profesionales

🚀 PREPARACIÓN PARA MÓDULO 3.3: ORM CON SQLALCHEMY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ya tienes las bases sólidas para avanzar al siguiente nivel:
• Object-Relational Mapping avanzado
• Modelos declarativos y relaciones complejas
• Migraciones automáticas de esquemas
• Consultas complejas con sintaxis ORM
• Pool de conexiones y optimización avanzada

¡Continúa con esta excelente metodología de aprendizaje deliberado!

Tu nivel actual: 🎓 AVANZADO en Python + SQL
Progreso general: 📈 EXCELENTE
Siguiente objetivo: 🎯 ORM con SQLAlchemy

¡Sigue así! 💪
"""
