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
6. PATRONES AVANZADOS
====================

Implementación de patrones de diseño profesionales para
aplicaciones industriales robustas.
"""

class ConnectionPool:
    """Pool de conexiones para alta concurrencia"""
    
    def __init__(self, db_path: str, max_connections: int = 10):
        self.db_path = db_path
        self.max_connections = max_connections
        self._pool = []
        self._in_use = set()
    
    def get_connection(self):
        """Obtiene conexión del pool"""
        if self._pool:
            conn = self._pool.pop()
        else:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
        
        self._in_use.add(conn)
        return conn
    
    def return_connection(self, conn):
        """Devuelve conexión al pool"""
        if conn in self._in_use:
            self._in_use.remove(conn)
            if len(self._pool) < self.max_connections:
                self._pool.append(conn)
            else:
                conn.close()
    
    def close_all(self):
        """Cierra todas las conexiones"""
        for conn in self._pool + list(self._in_use):
            conn.close()
        self._pool.clear()
        self._in_use.clear()

"""
7. AUTOMATIZACIÓN Y SCHEDULING
==============================

Herramientas para automatizar tareas de base de datos
y generar reportes programados.
"""

class AutomacionReportes:
    """Sistema de automatización de reportes"""
    
    def __init__(self, sistema_monitoreo: SistemaMonitoreoIndustrial):
        self.sistema = sistema_monitoreo
    
    def backup_diario(self, directorio_backup: str):
        """Realiza backup diario de la base de datos"""
        from shutil import copy2
        fecha = datetime.now().strftime('%Y%m%d')
        backup_path = Path(directorio_backup) / f"backup_{fecha}.db"
        copy2(self.sistema.db_path, backup_path)
        return backup_path
    
    def limpieza_datos_antiguos(self, dias_retention: int = 90):
        """Limpia datos antiguos para optimizar rendimiento"""
        with obtener_conexion(self.sistema.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM lecturas 
                WHERE timestamp < date('now', '-{} days')
            """.format(dias_retention))
            
            registros_eliminados = cursor.rowcount
            conn.commit()
            return registros_eliminados
    
    def generar_reporte_semanal(self) -> Dict[str, Any]:
        """Genera reporte semanal consolidado"""
        # Implementación del reporte semanal
        pass
    
    def enviar_notificacion_email(self, destinatarios: List[str], reporte: Dict):
        """Envía reporte por email (simulado)"""
        # En implementación real usarías smtplib
        print(f"📧 Enviando reporte a {destinatarios}")
        print(f"📊 Datos del reporte: {len(reporte)} elementos")

"""
8. MEJORES PRÁCTICAS Y PATRONES
===============================

Implementación de mejores prácticas para aplicaciones
industriales de misión crítica.
"""

# Configuración de logging
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

class SeguridadBaseDatos:
    """Implementa medidas de seguridad para BD industriales"""
    
    @staticmethod
    def validar_sql_injection(query: str) -> bool:
        """Valida contra inyección SQL básica"""
        palabras_peligrosas = ['DROP', 'DELETE', 'UPDATE', 'INSERT', 'ALTER']
        query_upper = query.upper()
        return not any(palabra in query_upper for palabra in palabras_peligrosas)
    
    @staticmethod
    def encriptar_datos_sensibles(data: str) -> str:
        """Encripta datos sensibles (implementación básica)"""
        import base64
        return base64.b64encode(data.encode()).decode()
    
    @staticmethod
    def audit_log(usuario: str, accion: str, tabla: str):
        """Registra auditoría de operaciones"""
        logging.info(f"AUDIT: {usuario} realizó {accion} en {tabla}")

"""
=================================================================
RESUMEN DEL MÓDULO 3.2
=================================================================

✅ CONCEPTOS DOMINADOS:
- Conexión Python-SQLite con sqlite3
- Context managers para manejo seguro
- Patrones DAO y Repository
- Integración Pandas + SQL
- Automatización de reportes
- Pool de conexiones
- Seguridad básica de BD
- Monitoreo industrial en tiempo real

🎯 PRÓXIMO MÓDULO 3.3: CONSULTAS AVANZADAS Y OPTIMIZACIÓN
- Stored procedures en SQLite
- Triggers para automatización
- Views complejas y materializadas
- Optimización avanzada de consultas
- Análisis de performance
- Índices especializados

💡 APLICACIONES INDUSTRIALES DESARROLLADAS:
- Sistema de monitoreo de sensores
- Dashboard en tiempo real
- Automatización de reportes
- Gestión de empleados con DAO
- Pool de conexiones para alta concurrencia
"""

# Ejemplo de uso completo del sistema
if __name__ == "__main__":
    # Configuración del sistema
    sistema = SistemaMonitoreoIndustrial("planta_industrial.db")
    
    # Registro de sensores
    sensor_temp = {
        'nombre': 'Temperatura Reactor 1',
        'tipo': 'Temperatura',
        'ubicacion': 'Planta Principal - Reactor 1',
        'unidad_medida': '°C',
        'valor_min': 20.0,
        'valor_max': 80.0
    }
    
    sensor_id = sistema.registrar_sensor(sensor_temp)
    
    # Simulación de lecturas
    import random
    for _ in range(10):
        valor = random.uniform(15, 85)  # Algunos valores fuera de rango
        sistema.registrar_lectura(sensor_id, valor)
    
    # Obtener dashboard
    dashboard = sistema.obtener_dashboard_data()
    print("📊 Dashboard actualizado:", dashboard)
    
    # Generar reporte
    reporte = sistema.generar_reporte_diario()
    print("📋 Reporte diario generado:", reporte)
