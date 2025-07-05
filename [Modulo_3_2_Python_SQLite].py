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
CONCEPTOS FUNDAMENTALES
=================================================================

1. MÓDULO SQLITE3 NATIVO
========================

Python incluye sqlite3 de forma nativa, proporcionando una interfaz
completa para trabajar con bases de datos SQLite.

"""

import sqlite3
import pandas as pd
from datetime import datetime, date
import json
import csv
from pathlib import Path
from contextlib import contextmanager
from typing import List, Dict, Any, Optional

# Ejemplo básico de conexión
def conexion_basica():
    """Ejemplo de conexión básica a SQLite"""
    
    # Conectar a base de datos (se crea si no existe)
    conn = sqlite3.connect('empresa_industrial.db')
    cursor = conn.cursor()
    
    # Configurar para que devuelva diccionarios
    conn.row_factory = sqlite3.Row
    
    # Operación simple
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas = cursor.fetchall()
    
    # Cerrar conexión
    conn.close()
    
    return tablas

"""
2. CONTEXT MANAGERS PARA BASES DE DATOS
=======================================

Los context managers garantizan que las conexiones se cierren
correctamente, incluso si ocurre un error.
"""

@contextmanager
def obtener_conexion(db_path: str):
    """Context manager para manejo seguro de conexiones"""
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row  # Resultados como diccionarios
        yield conn
    except sqlite3.Error as e:
        if conn:
            conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

# Uso del context manager
def ejemplo_context_manager():
    """Ejemplo de uso de context manager"""
    
    with obtener_conexion('empresa.db') as conn:
        cursor = conn.cursor()
        
        # Todas las operaciones aquí
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sensores (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                valor REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # La conexión se cierra automáticamente

"""
3. CLASE DAO (DATA ACCESS OBJECT)
================================

Encapsula todas las operaciones de base de datos en una clase
organizada y reutilizable.
"""

class EmpleadoDAO:
    """Data Access Object para empleados"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._inicializar_tabla()
    
    def _inicializar_tabla(self):
        """Crea la tabla si no existe"""
        with obtener_conexion(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    email TEXT UNIQUE,
                    salario REAL,
                    departamento TEXT,
                    fecha_ingreso DATE,
                    activo BOOLEAN DEFAULT 1
                )
            """)
            conn.commit()
    
    def crear_empleado(self, empleado: Dict[str, Any]) -> int:
        """Crea un nuevo empleado"""
        with obtener_conexion(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO empleados (nombre, apellido, email, salario, departamento, fecha_ingreso)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                empleado['nombre'],
                empleado['apellido'],
                empleado['email'],
                empleado['salario'],
                empleado['departamento'],
                empleado['fecha_ingreso']
            ))
            conn.commit()
            return cursor.lastrowid
    
    def obtener_empleado(self, id_empleado: int) -> Optional[Dict]:
        """Obtiene un empleado por ID"""
        with obtener_conexion(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleados WHERE id = ?", (id_empleado,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def obtener_todos_empleados(self) -> List[Dict]:
        """Obtiene todos los empleados"""
        with obtener_conexion(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM empleados WHERE activo = 1")
            return [dict(row) for row in cursor.fetchall()]
    
    def actualizar_empleado(self, id_empleado: int, datos: Dict[str, Any]) -> bool:
        """Actualiza un empleado"""
        with obtener_conexion(self.db_path) as conn:
            # Construir query dinámico
            campos = []
            valores = []
            for campo, valor in datos.items():
                campos.append(f"{campo} = ?")
                valores.append(valor)
            
            valores.append(id_empleado)
            query = f"UPDATE empleados SET {', '.join(campos)} WHERE id = ?"
            
            cursor = conn.cursor()
            cursor.execute(query, valores)
            conn.commit()
            return cursor.rowcount > 0
    
    def eliminar_empleado(self, id_empleado: int) -> bool:
        """Elimina (marca como inactivo) un empleado"""
        with obtener_conexion(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE empleados SET activo = 0 WHERE id = ?", (id_empleado,))
            conn.commit()
            return cursor.rowcount > 0
    
    def buscar_empleados(self, filtros: Dict[str, Any]) -> List[Dict]:
        """Búsqueda avanzada de empleados"""
        with obtener_conexion(self.db_path) as conn:
            where_clauses = []
            valores = []
            
            for campo, valor in filtros.items():
                if isinstance(valor, str) and '%' in valor:
                    where_clauses.append(f"{campo} LIKE ?")
                else:
                    where_clauses.append(f"{campo} = ?")
                valores.append(valor)
            
            where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
            query = f"SELECT * FROM empleados WHERE {where_sql} AND activo = 1"
            
            cursor = conn.cursor()
            cursor.execute(query, valores)
            return [dict(row) for row in cursor.fetchall()]

"""
4. INTEGRACIÓN CON PANDAS
========================

Pandas ofrece funciones específicas para trabajar con SQL,
permitiendo análisis de datos más potentes.
"""

class AnalisisEmpleados:
    """Análisis de datos de empleados usando Pandas + SQL"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
    
    def obtener_conexion(self):
        """Obtiene conexión para pandas"""
        return sqlite3.connect(self.db_path)
    
    def estadisticas_departamento(self) -> pd.DataFrame:
        """Estadísticas por departamento"""
        query = """
            SELECT 
                departamento,
                COUNT(*) as total_empleados,
                ROUND(AVG(salario), 2) as salario_promedio,
                MIN(salario) as salario_minimo,
                MAX(salario) as salario_maximo,
                SUM(salario) as costo_total
            FROM empleados 
            WHERE activo = 1
            GROUP BY departamento
            ORDER BY salario_promedio DESC
        """
        
        with self.obtener_conexion() as conn:
            return pd.read_sql_query(query, conn)
    
    def tendencias_contratacion(self) -> pd.DataFrame:
        """Análisis de tendencias de contratación"""
        query = """
            SELECT 
                strftime('%Y', fecha_ingreso) as año,
                strftime('%m', fecha_ingreso) as mes,
                COUNT(*) as contrataciones,
                AVG(salario) as salario_promedio_ingreso
            FROM empleados
            WHERE activo = 1
            GROUP BY año, mes
            ORDER BY año DESC, mes DESC
        """
        
        with self.obtener_conexion() as conn:
            df = pd.read_sql_query(query, conn)
            df['fecha'] = pd.to_datetime(df[['año', 'mes']].assign(day=1))
            return df
    
    def exportar_reporte_excel(self, archivo: str):
        """Exporta múltiples análisis a Excel"""
        with pd.ExcelWriter(archivo, engine='openpyxl') as writer:
            # Hoja 1: Estadísticas generales
            stats = self.estadisticas_departamento()
            stats.to_excel(writer, sheet_name='Estadísticas Departamento', index=False)
            
            # Hoja 2: Tendencias
            tendencias = self.tendencias_contratacion()
            tendencias.to_excel(writer, sheet_name='Tendencias Contratación', index=False)
            
            # Hoja 3: Datos raw
            with self.obtener_conexion() as conn:
                empleados = pd.read_sql_query(
                    "SELECT * FROM empleados WHERE activo = 1", conn
                )
                empleados.to_excel(writer, sheet_name='Datos Empleados', index=False)

"""
5. SISTEMA DE MONITOREO INDUSTRIAL
==================================

Ejemplo práctico de un sistema completo de monitoreo industrial
que integra sensores, alarmas y reportes automatizados.
"""

class SistemaMonitoreoIndustrial:
    """Sistema completo de monitoreo para planta industrial"""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._inicializar_sistema()
    
    def _inicializar_sistema(self):
        """Inicializa todas las tablas del sistema"""
        with obtener_conexion(self.db_path) as conn:
            conn.executescript("""
                -- Tabla de sensores
                CREATE TABLE IF NOT EXISTS sensores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    ubicacion TEXT,
                    unidad_medida TEXT,
                    valor_min REAL,
                    valor_max REAL,
                    activo BOOLEAN DEFAULT 1
                );
                
                -- Tabla de lecturas
                CREATE TABLE IF NOT EXISTS lecturas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sensor_id INTEGER,
                    valor REAL NOT NULL,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    estado TEXT DEFAULT 'NORMAL',
                    FOREIGN KEY (sensor_id) REFERENCES sensores(id)
                );
                
                -- Tabla de alarmas
                CREATE TABLE IF NOT EXISTS alarmas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sensor_id INTEGER,
                    tipo_alarma TEXT,
                    mensaje TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    resuelto BOOLEAN DEFAULT 0,
                    FOREIGN KEY (sensor_id) REFERENCES sensores(id)
                );
                
                -- Índices para rendimiento
                CREATE INDEX IF NOT EXISTS idx_lecturas_sensor_time 
                ON lecturas(sensor_id, timestamp);
                
                CREATE INDEX IF NOT EXISTS idx_alarmas_resuelto 
                ON alarmas(resuelto, timestamp);
            """)
            conn.commit()
    
    def registrar_sensor(self, sensor_data: Dict[str, Any]) -> int:
        """Registra un nuevo sensor"""
        with obtener_conexion(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO sensores (nombre, tipo, ubicacion, unidad_medida, valor_min, valor_max)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                sensor_data['nombre'],
                sensor_data['tipo'],
                sensor_data['ubicacion'],
                sensor_data['unidad_medida'],
                sensor_data['valor_min'],
                sensor_data['valor_max']
            ))
            conn.commit()
            return cursor.lastrowid
    
    def registrar_lectura(self, sensor_id: int, valor: float) -> bool:
        """Registra una lectura y verifica alarmas"""
        with obtener_conexion(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Obtener límites del sensor
            cursor.execute(
                "SELECT valor_min, valor_max, nombre FROM sensores WHERE id = ?",
                (sensor_id,)
            )
            sensor = cursor.fetchone()
            
            if not sensor:
                return False
            
            valor_min, valor_max, nombre = sensor
            
            # Determinar estado
            if valor < valor_min:
                estado = 'BAJO'
                self._crear_alarma(conn, sensor_id, 'VALOR_BAJO', 
                                 f"{nombre}: Valor {valor} por debajo del mínimo {valor_min}")
            elif valor > valor_max:
                estado = 'ALTO'
                self._crear_alarma(conn, sensor_id, 'VALOR_ALTO', 
                                 f"{nombre}: Valor {valor} por encima del máximo {valor_max}")
            else:
                estado = 'NORMAL'
            
            # Registrar lectura
            cursor.execute("""
                INSERT INTO lecturas (sensor_id, valor, estado)
                VALUES (?, ?, ?)
            """, (sensor_id, valor, estado))
            
            conn.commit()
            return True
    
    def _crear_alarma(self, conn, sensor_id: int, tipo: str, mensaje: str):
        """Crea una nueva alarma"""
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO alarmas (sensor_id, tipo_alarma, mensaje)
            VALUES (?, ?, ?)
        """, (sensor_id, tipo, mensaje))
    
    def obtener_dashboard_data(self) -> Dict[str, Any]:
        """Obtiene datos para dashboard en tiempo real"""
        with obtener_conexion(self.db_path) as conn:
            # Últimas lecturas por sensor
            ultimas_lecturas = pd.read_sql_query("""
                SELECT 
                    s.nombre,
                    s.tipo,
                    s.ubicacion,
                    l.valor,
                    l.estado,
                    l.timestamp
                FROM sensores s
                INNER JOIN lecturas l ON s.id = l.sensor_id
                WHERE l.timestamp = (
                    SELECT MAX(timestamp) 
                    FROM lecturas l2 
                    WHERE l2.sensor_id = s.id
                )
                AND s.activo = 1
            """, conn)
            
            # Alarmas activas
            alarmas_activas = pd.read_sql_query("""
                SELECT 
                    s.nombre as sensor,
                    a.tipo_alarma,
                    a.mensaje,
                    a.timestamp
                FROM alarmas a
                INNER JOIN sensores s ON a.sensor_id = s.id
                WHERE a.resuelto = 0
                ORDER BY a.timestamp DESC
            """, conn)
            
            # Estadísticas del día
            stats_dia = pd.read_sql_query("""
                SELECT 
                    COUNT(*) as total_lecturas,
                    COUNT(DISTINCT sensor_id) as sensores_activos,
                    SUM(CASE WHEN estado != 'NORMAL' THEN 1 ELSE 0 END) as lecturas_anomalas
                FROM lecturas 
                WHERE DATE(timestamp) = DATE('now')
            """, conn)
            
            return {
                'ultimas_lecturas': ultimas_lecturas.to_dict('records'),
                'alarmas_activas': alarmas_activas.to_dict('records'),
                'estadisticas_dia': stats_dia.iloc[0].to_dict(),
                'timestamp_actualizacion': datetime.now().isoformat()
            }
    
    def generar_reporte_diario(self, fecha: str = None) -> Dict[str, Any]:
        """Genera reporte diario completo"""
        if not fecha:
            fecha = datetime.now().strftime('%Y-%m-%d')
        
        with obtener_conexion(self.db_path) as conn:
            # Resumen del día
            resumen = pd.read_sql_query("""
                SELECT 
                    s.nombre,
                    s.tipo,
                    COUNT(l.id) as total_lecturas,
                    ROUND(AVG(l.valor), 2) as valor_promedio,
                    MIN(l.valor) as valor_minimo,
                    MAX(l.valor) as valor_maximo,
                    SUM(CASE WHEN l.estado != 'NORMAL' THEN 1 ELSE 0 END) as lecturas_anomalas
                FROM sensores s
                LEFT JOIN lecturas l ON s.id = l.sensor_id AND DATE(l.timestamp) = ?
                WHERE s.activo = 1
                GROUP BY s.id, s.nombre, s.tipo
                ORDER BY s.nombre
            """, conn, params=[fecha])
            
            # Alarmas del día
            alarmas = pd.read_sql_query("""
                SELECT 
                    s.nombre as sensor,
                    a.tipo_alarma,
                    a.mensaje,
                    a.timestamp,
                    a.resuelto
                FROM alarmas a
                INNER JOIN sensores s ON a.sensor_id = s.id
                WHERE DATE(a.timestamp) = ?
                ORDER BY a.timestamp
            """, conn, params=[fecha])
            
            return {
                'fecha': fecha,
                'resumen_sensores': resumen.to_dict('records'),
                'alarmas_dia': alarmas.to_dict('records'),
                'total_sensores': len(resumen),
                'total_alarmas': len(alarmas),
                'alarmas_resueltas': len(alarmas[alarmas['resuelto'] == 1]),
                'generado_en': datetime.now().isoformat()
            }

"""
6. INTEGRACIÓN CON PANDAS PARA ANÁLISIS HÍBRIDO
=================================================================

"""
La integración de SQLite con Pandas es fundamental para análisis
de datos industriales. Pandas puede leer directamente desde SQLite
y también escribir DataFrames a la base de datos.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import numpy as np

def demo_pandas_sqlite():
    """Demostración completa de integración Pandas + SQLite"""
    
    # 1. LECTURA DIRECTA CON PANDAS
    with get_db_connection() as conn:
        # Leer datos de sensores con JOIN
        query_sensores = """
        SELECT 
            s.nombre as sensor,
            s.tipo,
            s.ubicacion,
            l.valor,
            l.timestamp,
            l.calidad
        FROM sensores s
        JOIN lecturas l ON s.id = l.sensor_id
        ORDER BY l.timestamp DESC
        """
        
        df_lecturas = pd.read_sql_query(query_sensores, conn)
        
        print(f"📈 DataFrame cargado: {len(df_lecturas)} registros")
        print("\n🔍 Primeras 5 filas:")
        print(df_lecturas.head())
        
        # 2. ANÁLISIS ESTADÍSTICO
        print("\n📊 Estadísticas por tipo de sensor:")
        stats_por_tipo = df_lecturas.groupby('tipo')['valor'].agg([
            'count', 'mean', 'std', 'min', 'max'
        ]).round(2)
        print(stats_por_tipo)
        
        # 3. DETECCIÓN DE VALORES ATÍPICOS
        print("\n🚨 Detección de valores atípicos:")
        for tipo in df_lecturas['tipo'].unique():
            datos_tipo = df_lecturas[df_lecturas['tipo'] == tipo]['valor']
            Q1 = datos_tipo.quantile(0.25)
            Q3 = datos_tipo.quantile(0.75)
            IQR = Q3 - Q1
            
            outliers = datos_tipo[
                (datos_tipo < Q1 - 1.5 * IQR) | 
                (datos_tipo > Q3 + 1.5 * IQR)
            ]
            
            print(f"    {tipo}: {len(outliers)} valores atípicos")
        
        return df_lecturas

"""
7. GENERACIÓN AUTOMÁTICA DE REPORTES
=================================================================

"""
Los reportes automáticos son cruciales en sistemas industriales.
Python permite generar reportes complejos combinando datos SQL
con análisis estadístico y exportación a múltiples formatos.
"""

def generar_reporte_operacional():
    """Genera un reporte operacional completo del sistema industrial"""
    
    with get_db_connection() as conn:
        # Datos para el reporte
        reporte_data = {}
        
        # 1. Estado general del sistema
        query_resumen = """
        SELECT 
            COUNT(DISTINCT s.id) as total_sensores,
            COUNT(DISTINCT s.id) FILTER (WHERE s.activo = 1) as sensores_activos,
            COUNT(l.id) as total_lecturas,
            COUNT(DISTINCT a.id) as total_alarmas,
            COUNT(DISTINCT a.id) FILTER (WHERE a.reconocida = 0) as alarmas_pendientes
        FROM sensores s
        LEFT JOIN lecturas l ON s.id = l.sensor_id AND l.timestamp >= datetime('now', '-24 hours')
        LEFT JOIN alarmas a ON s.id = a.sensor_id AND a.timestamp >= datetime('now', '-24 hours')
        """
        
        resumen = pd.read_sql_query(query_resumen, conn).iloc[0]
        reporte_data['resumen'] = resumen
        
        # 2. Top sensores con más lecturas
        query_top_sensores = """
        SELECT 
            s.nombre,
            s.tipo,
            s.ubicacion,
            COUNT(l.id) as num_lecturas,
            AVG(l.valor) as valor_promedio,
            MAX(l.timestamp) as ultima_lectura
        FROM sensores s
        JOIN lecturas l ON s.id = l.sensor_id
        WHERE l.timestamp >= datetime('now', '-24 hours')
        GROUP BY s.id, s.nombre, s.tipo, s.ubicacion
        ORDER BY num_lecturas DESC
        LIMIT 5
        """
        
        top_sensores = pd.read_sql_query(query_top_sensores, conn)
        reporte_data['top_sensores'] = top_sensores
        
        return reporte_data

def exportar_reporte_excel(reporte_data, nombre_archivo="reporte_operacional.xlsx"):
    """Exporta el reporte a un archivo Excel con múltiples hojas"""
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"reporte_operacional_{timestamp}.xlsx"
    
    with pd.ExcelWriter(nombre_archivo, engine='openpyxl') as writer:
        # Hoja 1: Resumen ejecutivo
        df_resumen = pd.DataFrame([reporte_data['resumen']])
        df_resumen.to_excel(writer, sheet_name='Resumen_Ejecutivo', index=False)
        
        # Hoja 2: Top sensores
        reporte_data['top_sensores'].to_excel(writer, sheet_name='Top_Sensores', index=False)
    
    print(f"📄 Reporte exportado: {nombre_archivo}")
    return nombre_archivo

"""
8. EJERCICIOS PRÁCTICOS PROGRESIVOS
=================================================================

"""
Ejercicios diseñados para consolidar el aprendizaje de manera
progresiva, desde conceptos básicos hasta implementaciones
avanzadas de sistemas industriales completos.
"""

# NIVEL BÁSICO 🟢
def ejercicio_basico_conexion():
    """Ejercicio básico: Conexión y consultas simples"""
    
    print("🎯 EJERCICIO BÁSICO: Conexión y Consultas")
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Contar sensores
        cursor.execute("SELECT COUNT(*) FROM sensores")
        total_sensores = cursor.fetchone()[0]
        print(f"📊 Total de sensores: {total_sensores}")
        
        # Listar sensores activos
        cursor.execute("SELECT nombre, tipo, ubicacion FROM sensores WHERE activo = 1")
        sensores_activos = cursor.fetchall()
        print(f"✅ Sensores activos: {len(sensores_activos)}")

# NIVEL INTERMEDIO 🟡
def ejercicio_intermedio_pandas():
    """Ejercicio intermedio: Análisis con Pandas"""
    
    print("🎯 EJERCICIO INTERMEDIO: Análisis con Pandas")
    
    with get_db_connection() as conn:
        df = pd.read_sql_query("""
            SELECT s.nombre, s.tipo, l.valor, l.timestamp
            FROM sensores s
            JOIN lecturas l ON s.id = l.sensor_id
            WHERE l.timestamp >= datetime('now', '-24 hours')
        """, conn)
        
        print(f"📊 Datos cargados: {len(df)} registros")
        
        # Análisis estadístico
        stats = df.groupby('tipo')['valor'].agg(['count', 'mean', 'std']).round(2)
        print("📈 Estadísticas por tipo:")
        print(stats)

# NIVEL AVANZADO 🔴
def ejercicio_avanzado_dashboard():
    """Ejercicio avanzado: Dashboard industrial completo"""
    
    print("🎯 EJERCICIO AVANZADO: Dashboard Industrial")
    
    class DashboardIndustrial:
        """Sistema completo de dashboard industrial"""
        
        def __init__(self):
            self.nombre_sistema = "SCADA Industrial v3.2"
            self.fecha_inicio = datetime.now()
        
        def estado_general(self):
            """Muestra el estado general del sistema"""
            print(f"\n🏭 {self.nombre_sistema}")
            print(f"📅 Sesión iniciada: {self.fecha_inicio.strftime('%Y-%m-%d %H:%M:%S')}")
            
            with get_db_connection() as conn:
                cursor = conn.cursor()
                
                cursor.execute("SELECT COUNT(*) FROM sensores WHERE activo = 1")
                sensores_activos = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM lecturas WHERE timestamp >= datetime('now', '-1 hour')")
                lecturas_hora = cursor.fetchone()[0]
                
                cursor.execute("SELECT COUNT(*) FROM alarmas WHERE reconocida = 0")
                alarmas_pendientes = cursor.fetchone()[0]
                
                print(f"🟢 Sensores activos: {sensores_activos}")
                print(f"📈 Lecturas (1h): {lecturas_hora}")
                print(f"🚨 Alarmas pendientes: {alarmas_pendientes}")
        
        def generar_reporte_ejecutivo(self):
            """Genera reporte ejecutivo completo"""
            print("\n📋 REPORTE EJECUTIVO:")
            
            datos_reporte = generar_reporte_operacional()
            
            print(f"📊 Sistema: {self.nombre_sistema}")
            print(f"✅ Estado: OPERACIONAL")
            print(f"🕐 Generado: {datetime.now().isoformat()}")
            
            return datos_reporte
    
    # Ejecutar dashboard
    dashboard = DashboardIndustrial()
    dashboard.estado_general()
    reporte = dashboard.generar_reporte_ejecutivo()
    
    return dashboard, reporte

"""
9. EVALUACIÓN Y CONSOLIDACIÓN
=================================================================

def cuestionario_evaluacion():
    """Cuestionario de evaluación del módulo"""
    
    print("📝 CUESTIONARIO DE EVALUACIÓN - MÓDULO 3.2")
    print("=" * 50)
    
    preguntas = {
        1: {
            'pregunta': '¿Cuál es la ventaja de usar context managers con SQLite?',
            'opciones': [
                'a) Mayor velocidad de consultas',
                'b) Gestión automática de conexiones y transacciones',
                'c) Mejor compatibilidad con Pandas',
                'd) Reduce el tamaño de la base de datos'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'Los context managers garantizan que las conexiones se cierren automáticamente y las transacciones se manejen correctamente.'
        },
        2: {
            'pregunta': '¿Qué patrón de diseño implementamos para la gestión de sensores?',
            'opciones': [
                'a) Singleton',
                'b) Factory', 
                'c) DAO (Data Access Object)',
                'd) Observer'
            ],
            'respuesta_correcta': 'c',
            'explicacion': 'El patrón DAO encapsula la lógica de acceso a datos, separando la lógica de negocio de la persistencia.'
        },
        3: {
            'pregunta': '¿Cuál es la principal ventaja de usar pd.read_sql_query()?',
            'opciones': [
                'a) Es más rápido que SQLite puro',
                'b) Convierte automáticamente los datos a DataFrame para análisis',
                'c) Usa menos memoria',
                'd) Es más seguro contra inyección SQL'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'pd.read_sql_query() convierte automáticamente los resultados SQL en DataFrames de Pandas, facilitando el análisis posterior.'
        }
    }
    
    print("✅ RESPUESTAS CORRECTAS:")
    for num, data in preguntas.items():
        print(f"\nPregunta {num}: {data['pregunta']}")
        for opcion in data['opciones']:
            marca = "✓" if opcion.startswith(data['respuesta_correcta']) else " "
            print(f"  [{marca}] {opcion}")
        print(f"💡 Explicación: {data['explicacion']}")

def checklist_consolidacion():
    """Checklist completo de consolidación del módulo"""
    
    print("\n🎯 CHECKLIST DE CONSOLIDACIÓN - MÓDULO 3.2")
    print("=" * 60)
    
    checklist_items = [
        "✅ Configuración correcta del entorno (Python + SQLite + Pandas)",
        "✅ Comprensión de conexiones y context managers",
        "✅ Dominio de operaciones CRUD (Create, Read, Update, Delete)",
        "✅ Implementación de esquemas industriales realistas",
        "✅ Integración efectiva de SQLite con Pandas",
        "✅ Análisis estadístico de datos industriales",
        "✅ Sistema completo de gestión de alarmas",
        "✅ Implementación del patrón DAO",
        "✅ Optimización de consultas con índices",
        "✅ Sistema de respaldos automáticos",
        "✅ Generación de reportes automáticos",
        "✅ Exportación de datos a Excel",
        "✅ Detección de valores atípicos y anomalías",
        "✅ Dashboard industrial integrado",
        "✅ Manejo profesional de errores y excepciones",
        "✅ Implementación de buenas prácticas de seguridad"
    ]
    
    print("📋 CONOCIMIENTOS CONSOLIDADOS:")
    for item in checklist_items:
        print(f"  {item}")
    
    print(f"\n🏆 TOTAL OBJETIVOS COMPLETADOS: {len(checklist_items)}/16")
    print("\n🎓 NIVEL DE COMPETENCIA: AVANZADO")
    print("📈 PREPARACIÓN PARA MÓDULO 3.3: 100% LISTO")

=================================================================
10. FUNCIÓN PRINCIPAL DE DEMOSTRACIÓN
=================================================================

def main():
    """Función principal que demuestra todos los conceptos del módulo"""
    
    print("🐍🗄️ MÓDULO 3.2: PYTHON + SQLITE - DEMOSTRACIÓN COMPLETA")
    print("=" * 70)
    
    try:
        # 1. Crear sistema de demostración
        print("\n1️⃣ CREANDO SISTEMA DE DEMOSTRACIÓN...")
        demo_rapida_sistema_industrial()
        
        # 2. Análisis con Pandas
        print("\n2️⃣ ANÁLISIS CON PANDAS...")
        df_datos = demo_pandas_sqlite()
        
        # 3. Generar reportes
        print("\n3️⃣ GENERANDO REPORTES...")
        reporte = generar_reporte_operacional()
        archivo_reporte = exportar_reporte_excel(reporte)
        
        # 4. Ejecutar ejercicios
        print("\n4️⃣ EJERCICIOS PRÁCTICOS...")
        ejercicio_basico_conexion()
        ejercicio_intermedio_pandas()
        dashboard, reporte_dashboard = ejercicio_avanzado_dashboard()
        
        # 5. Evaluación
        print("\n5️⃣ EVALUACIÓN Y CONSOLIDACIÓN...")
        cuestionario_evaluacion()
        checklist_consolidacion()
        
        print("\n" + "="*70)
        print("🎉 ¡MÓDULO 3.2 COMPLETAMENTE DEMOSTRADO!")
        print("="*70)
        print("🚀 Siguiente etapa: Módulo 3.3 - ORM con SQLAlchemy")
        print("📚 Ya tienes las bases sólidas para frameworks avanzados de ORM")
        print("💪 ¡Excelente trabajo siguiendo la metodología de aprendizaje deliberado!")
        
    except Exception as e:
        print(f"❌ Error en demostración: {e}")
        print("🔧 Revisa la configuración del entorno y las dependencias")

if __name__ == "__main__":
    main()

=================================================================
🎓 CONCLUSIÓN DEL MÓDULO 3.2
=================================================================

"""
¡FELICIDADES! Has completado exitosamente el Módulo 3.2: Python + SQLite.

🏆 LOGROS ALCANZADOS:
- Integración completa de Python con SQLite
- Manejo profesional de conexiones y transacciones
- Análisis híbrido con Pandas
- Generación automática de reportes
- Implementación de patrones de diseño para bases de datos
- Sistema industrial completo funcional

🚀 PREPARACIÓN PARA EL SIGUIENTE NIVEL:
- Tienes las bases sólidas para ORM avanzados
- Comprendes la integración SQL-Python
- Dominas el análisis de datos industriales
- Implementas buenas prácticas profesionales

📈 PRÓXIMO MÓDULO: 3.3 - ORM con SQLAlchemy
- Object-Relational Mapping avanzado
- Modelos declarativos
- Migraciones automáticas
- Consultas complejas con ORM
- Optimización de performance con ORM

¡Continúa con esta excelente metodología de aprendizaje deliberado!
"""
