"""
🐍🔗 MÓDULO 3.3: ORM CON SQLALCHEMY - PARTE 2
📊 Maestría en Python - Fase 3: CONFIGURACIÓN PRÁCTICA DE SQLALCHEMY

=================================================================
OBJETIVO: Configuración práctica y primeros modelos con SQLAlchemy
=================================================================

Esta parte 2 se enfoca en la implementación práctica de SQLAlchemy,
desde la instalación hasta los primeros modelos industriales
funcionales y operaciones CRUD básicas.

📋 CONTENIDO DE ESTA PARTE:
==========================

1. INSTALACIÓN Y CONFIGURACIÓN
   - Instalación de SQLAlchemy
   - Configuración del Engine
   - Setup de sesiones
   - Configuración de logging

2. PRIMER MODELO INDUSTRIAL
   - Definición de modelos declarativos
   - Mapeo de tablas
   - Tipos de datos industriales
   - Validaciones básicas

3. OPERACIONES CRUD BÁSICAS
   - Create: Inserción con ORM
   - Read: Consultas básicas
   - Update: Actualización de objetos
   - Delete: Eliminación segura

4. CONFIGURACIÓN PROFESIONAL
   - Connection pooling
   - Configuración de producción
   - Manejo de errores
   - Best practices

=================================================================
1. INSTALACIÓN Y CONFIGURACIÓN DE SQLALCHEMY
=================================================================

SQLAlchemy es el ORM más potente y flexible de Python. Proporciona
tanto un ORM de alto nivel como herramientas de bajo nivel para
trabajar con bases de datos.
"""

# Primero verificamos e instalamos las dependencias necesarias
import sys
import subprocess
from pathlib import Path

def verificar_dependencias():
    """Verifica e instala las dependencias necesarias para SQLAlchemy"""
    
    print("🔍 VERIFICANDO DEPENDENCIAS DE SQLALCHEMY...")
    
    dependencias = [
        'sqlalchemy>=2.0.0',
        'pandas>=1.5.0', 
        'alembic>=1.8.0',  # Para migraciones
        'python-dotenv>=0.19.0'  # Para configuración
    ]
    
    for dep in dependencias:
        try:
            # Intentar importar el paquete base
            package_name = dep.split('>=')[0].replace('-', '_')
            __import__(package_name)
            print(f"✅ {dep} - YA INSTALADO")
        except ImportError:
            print(f"📦 INSTALANDO: {dep}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"✅ {dep} - INSTALADO CORRECTAMENTE")
    
    print("🎉 TODAS LAS DEPENDENCIAS LISTAS")

# Ejecutar verificación
verificar_dependencias()

# Ahora importamos SQLAlchemy y dependencias
from sqlalchemy import (
    create_engine, 
    Column, 
    Integer, 
    String, 
    Float, 
    DateTime, 
    Boolean,
    ForeignKey,
    Text,
    func
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from datetime import datetime, timedelta
import pandas as pd
from typing import Optional, List, Dict, Any
import logging
from dotenv import load_dotenv
import os

"""
2. CONFIGURACIÓN DEL ENGINE Y SESIONES
======================================

El Engine es el corazón de SQLAlchemy. Maneja la conexión con la
base de datos y el pool de conexiones.
"""

class ConfiguracionSQLAlchemy:
    """Configuración profesional de SQLAlchemy para entornos industriales"""
    
    def __init__(self, db_path: str = "empresa_industrial_orm.db"):
        self.db_path = db_path
        self.engine = None
        self.SessionLocal = None
        self._configurar_logging()
        self._crear_engine()
        self._configurar_sesiones()
    
    def _configurar_logging(self):
        """Configura logging para SQLAlchemy"""
        logging.basicConfig(level=logging.INFO)
        
        # Logger específico para SQLAlchemy
        self.logger = logging.getLogger('sqlalchemy.engine')
        self.logger.setLevel(logging.INFO)
        
        # Configurar para mostrar SQL queries (útil para desarrollo)
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    
    def _crear_engine(self):
        """Crea y configura el engine de SQLAlchemy"""
        
        # URL de conexión para SQLite
        database_url = f"sqlite:///{self.db_path}"
        
        # Configuración del engine con opciones de producción
        self.engine = create_engine(
            database_url,
            # Configuración de pool de conexiones
            pool_size=5,                    # Número de conexiones en el pool
            max_overflow=10,                # Conexiones adicionales permitidas
            pool_timeout=30,                # Timeout para obtener conexión
            pool_recycle=3600,              # Reciclar conexiones cada hora
            
            # Configuración de SQLite específica
            connect_args={
                "check_same_thread": False,  # Permitir múltiples threads
                "timeout": 20               # Timeout de conexión
            },
            
            # Para desarrollo: mostrar SQL queries
            echo=False,  # Cambiar a True para ver las queries
            
            # Configuración de rendimiento
            future=True  # Usar SQLAlchemy 2.0 style
        )
        
        print(f"🔗 Engine configurado: {database_url}")
        print(f"📊 Pool size: 5, Max overflow: 10")
    
    def _configurar_sesiones(self):
        """Configura el factory de sesiones"""
        
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autocommit=False,    # Transacciones manuales
            autoflush=False,     # Flush manual para mejor control
            expire_on_commit=False  # Los objetos permanecen válidos después del commit
        )
        
        print("🔄 Sesiones configuradas correctamente")
    
    def get_session(self) -> Session:
        """Obtiene una nueva sesión de base de datos"""
        return self.SessionLocal()
    
    def probar_conexion(self):
        """Prueba la conexión a la base de datos"""
        try:
            with self.engine.connect() as conn:
                result = conn.execute("SELECT 1")
                print("✅ Conexión a base de datos exitosa")
                return True
        except Exception as e:
            print(f"❌ Error de conexión: {e}")
            return False
    
    def obtener_info_motor(self):
        """Obtiene información del motor de base de datos"""
        info = {
            'url': str(self.engine.url),
            'driver': self.engine.driver,
            'pool_size': self.engine.pool.size(),
            'checked_in': self.engine.pool.checkedin(),
            'checked_out': self.engine.pool.checkedout(),
            'overflow': self.engine.pool.overflow(),
        }
        
        print("📋 INFORMACIÓN DEL MOTOR:")
        for key, value in info.items():
            print(f"    {key}: {value}")
        
        return info

# Crear instancia global de configuración
config_db = ConfiguracionSQLAlchemy()

"""
3. DEFINICIÓN DE MODELOS DECLARATIVOS
====================================

Los modelos declarativos son clases Python que se mapean directamente
a tablas de base de datos. SQLAlchemy maneja automáticamente la
conversión entre objetos Python y registros de base de datos.
"""

# Base declarativa - todas las clases modelo heredan de aquí
Base = declarative_base()

class SensorIndustrial(Base):
    """Modelo para sensores industriales - Ejemplo básico"""
    
    __tablename__ = 'sensores_industriales'
    
    # Campos básicos
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    tipo = Column(String(50), nullable=False)
    ubicacion = Column(String(200), nullable=False)
    
    # Campos técnicos
    unidad_medida = Column(String(20), nullable=False)
    valor_minimo = Column(Float, nullable=False)
    valor_maximo = Column(Float, nullable=False)
    precision_decimal = Column(Integer, default=2)
    
    # Campos de estado
    activo = Column(Boolean, default=True)
    fecha_instalacion = Column(DateTime, default=datetime.utcnow)
    fecha_ultima_calibracion = Column(DateTime)
    
    # Campos de auditoría
    creado_en = Column(DateTime, default=datetime.utcnow)
    actualizado_en = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relación con lecturas (se definirá más adelante)
    # lecturas = relationship("LecturasSensor", back_populates="sensor")
    
    def __repr__(self):
        return f"<SensorIndustrial(id={self.id}, nombre='{self.nombre}', tipo='{self.tipo}')>"
    
    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.ubicacion}"
    
    def validar_valor(self, valor: float) -> bool:
        """Valida si un valor está dentro del rango del sensor"""
        return self.valor_minimo <= valor <= self.valor_maximo
    
    def calcular_porcentaje_rango(self, valor: float) -> float:
        """Calcula el porcentaje del valor dentro del rango del sensor"""
        if not self.validar_valor(valor):
            return -1  # Valor fuera de rango
        
        rango_total = self.valor_maximo - self.valor_minimo
        return ((valor - self.valor_minimo) / rango_total) * 100
    
    def requiere_calibracion(self, dias_limite: int = 90) -> bool:
        """Determina si el sensor requiere calibración"""
        if not self.fecha_ultima_calibracion:
            return True
        
        dias_desde_calibracion = (datetime.utcnow() - self.fecha_ultima_calibracion).days
        return dias_desde_calibracion > dias_limite

class LecturasSensor(Base):
    """Modelo para lecturas de sensores industriales"""
    
    __tablename__ = 'lecturas_sensores'
    
    # Campos básicos
    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(Integer, ForeignKey('sensores_industriales.id'), nullable=False)
    valor = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Campos de calidad de datos
    calidad = Column(String(20), default='BUENA')  # BUENA, REGULAR, MALA
    confiabilidad = Column(Float, default=100.0)  # Porcentaje de confiabilidad
    
    # Campos de contexto
    temperatura_ambiente = Column(Float)
    humedad_ambiente = Column(Float)
    presion_atmosferica = Column(Float)
    
    # Estado de la lectura
    anomalia_detectada = Column(Boolean, default=False)
    procesada = Column(Boolean, default=False)
    
    # Relación con sensor
    sensor = relationship("SensorIndustrial")
    
    def __repr__(self):
        return f"<LecturasSensor(id={self.id}, sensor_id={self.sensor_id}, valor={self.valor})>"
    
    def es_valor_normal(self) -> bool:
        """Determina si la lectura está dentro de rangos normales"""
        if self.sensor:
            return self.sensor.validar_valor(self.valor)
        return True
    
    def calcular_desviacion_promedio(self, session: Session, ventana_horas: int = 24) -> float:
        """Calcula la desviación respecto al promedio de las últimas N horas"""
        
        # Timestamp de hace N horas
        timestamp_limite = self.timestamp - timedelta(hours=ventana_horas)
        
        # Consulta promedio de lecturas recientes
        promedio = session.query(func.avg(LecturasSensor.valor)).filter(
            LecturasSensor.sensor_id == self.sensor_id,
            LecturasSensor.timestamp >= timestamp_limite,
            LecturasSensor.id != self.id  # Excluir la lectura actual
        ).scalar()
        
        if promedio is None:
            return 0.0
        
        return abs(self.valor - promedio)

"""
4. CREACIÓN DE TABLAS Y CONFIGURACIÓN INICIAL
=============================================

Antes de usar los modelos, necesitamos crear las tablas en la base
de datos y configurar algunos datos de ejemplo.
"""

def crear_tablas_base_datos():
    """Crea todas las tablas definidas en los modelos"""
    
    print("🏗️ CREANDO ESTRUCTURA DE BASE DE DATOS...")
    
    try:
        # Crear todas las tablas
        Base.metadata.create_all(bind=config_db.engine)
        print("✅ Tablas creadas exitosamente")
        
        # Mostrar tablas creadas
        inspector = config_db.engine.dialect.get_table_names(config_db.engine.connect())
        print(f"📋 Tablas en la base de datos: {inspector}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creando tablas: {e}")
        return False

def configurar_datos_iniciales():
    """Configura datos iniciales para demostración"""
    
    print("📊 CONFIGURANDO DATOS INICIALES...")
    
    session = config_db.get_session()
    
    try:
        # Verificar si ya existen datos
        count_sensores = session.query(SensorIndustrial).count()
        
        if count_sensores > 0:
            print(f"📋 Ya existen {count_sensores} sensores. Saltando inicialización.")
            return True
        
        # Crear sensores de ejemplo
        sensores_ejemplo = [
            {
                'nombre': 'TEMP_HORNO_01',
                'tipo': 'Temperatura',
                'ubicacion': 'Horno Principal - Zona A',
                'unidad_medida': '°C',
                'valor_minimo': 200.0,
                'valor_maximo': 800.0,
                'precision_decimal': 1
            },
            {
                'nombre': 'PRES_TURBINA_02',
                'tipo': 'Presión',
                'ubicacion': 'Turbina de Vapor - Entrada',
                'unidad_medida': 'PSI',
                'valor_minimo': 0.0,
                'valor_maximo': 150.0,
                'precision_decimal': 2
            },
            {
                'nombre': 'VIB_MOTOR_03',
                'tipo': 'Vibración',
                'ubicacion': 'Motor Principal - Cojinete A',
                'unidad_medida': 'mm/s',
                'valor_minimo': 0.0,
                'valor_maximo': 25.0,
                'precision_decimal': 3
            },
            {
                'nombre': 'FLUJO_AGUA_04',
                'tipo': 'Flujo',
                'ubicacion': 'Sistema de Refrigeración',
                'unidad_medida': 'L/min',
                'valor_minimo': 10.0,
                'valor_maximo': 500.0,
                'precision_decimal': 1
            }
        ]
        
        # Insertar sensores
        for sensor_data in sensores_ejemplo:
            sensor = SensorIndustrial(**sensor_data)
            session.add(sensor)
        
        # Commit de los sensores
        session.commit()
        
        # Obtener IDs de sensores creados
        sensores_creados = session.query(SensorIndustrial).all()
        
        print(f"✅ {len(sensores_creados)} sensores creados:")
        for sensor in sensores_creados:
            print(f"    {sensor.id}: {sensor.nombre} ({sensor.tipo})")
        
        # Crear algunas lecturas de ejemplo
        import random
        
        print("📈 Generando lecturas de ejemplo...")
        
        for sensor in sensores_creados:
            # Generar 10 lecturas por sensor
            for i in range(10):
                # Valor aleatorio dentro del rango del sensor
                valor = random.uniform(sensor.valor_minimo, sensor.valor_maximo)
                
                # Timestamp aleatorio de las últimas 24 horas
                timestamp_base = datetime.utcnow() - timedelta(hours=random.randint(0, 24))
                
                lectura = LecturasSensor(
                    sensor_id=sensor.id,
                    valor=round(valor, sensor.precision_decimal),
                    timestamp=timestamp_base,
                    calidad='BUENA',
                    confiabilidad=random.uniform(95.0, 100.0),
                    temperatura_ambiente=random.uniform(18.0, 25.0),
                    humedad_ambiente=random.uniform(40.0, 60.0)
                )
                
                session.add(lectura)
        
        # Commit de las lecturas
        session.commit()
        
        # Verificar lecturas creadas
        count_lecturas = session.query(LecturasSensor).count()
        print(f"✅ {count_lecturas} lecturas generadas")
        
        return True
        
    except Exception as e:
        session.rollback()
        print(f"❌ Error configurando datos iniciales: {e}")
        return False
        
    finally:
        session.close()

"""
5. OPERACIONES CRUD BÁSICAS CON ORM
===================================

Ahora implementamos las operaciones CRUD usando el ORM de SQLAlchemy.
Esto demuestra la potencia y simplicidad del mapeo objeto-relacional.
"""

class GestorSensoresORM:
    """Gestor de sensores usando SQLAlchemy ORM"""
    
    def __init__(self):
        self.config_db = config_db
    
    def crear_sensor(self, datos_sensor: Dict[str, Any]) -> Optional[SensorIndustrial]:
        """Crea un nuevo sensor usando ORM"""
        
        session = self.config_db.get_session()
        
        try:
            # Crear objeto sensor
            sensor = SensorIndustrial(**datos_sensor)
            
            # Agregar a la sesión
            session.add(sensor)
            
            # Commit para persistir
            session.commit()
            
            # Refrescar para obtener el ID generado
            session.refresh(sensor)
            
            print(f"✅ Sensor creado: {sensor.id} - {sensor.nombre}")
            return sensor
            
        except Exception as e:
            session.rollback()
            print(f"❌ Error creando sensor: {e}")
            return None
            
        finally:
            session.close()
    
    def obtener_sensor(self, sensor_id: int) -> Optional[SensorIndustrial]:
        """Obtiene un sensor por ID"""
        
        session = self.config_db.get_session()
        
        try:
            sensor = session.query(SensorIndustrial).filter(
                SensorIndustrial.id == sensor_id
            ).first()
            
            if sensor:
                print(f"📊 Sensor encontrado: {sensor}")
                return sensor
            else:
                print(f"❌ Sensor {sensor_id} no encontrado")
                return None
                
        finally:
            session.close()
    
    def listar_sensores(self, activos_solo: bool = True) -> List[SensorIndustrial]:
        """Lista todos los sensores"""
        
        session = self.config_db.get_session()
        
        try:
            query = session.query(SensorIndustrial)
            
            if activos_solo:
                query = query.filter(SensorIndustrial.activo == True)
            
            sensores = query.all()
            
            print(f"📋 {len(sensores)} sensores encontrados")
            for sensor in sensores:
                print(f"    {sensor.id}: {sensor.nombre} ({sensor.tipo})")
            
            return sensores
            
        finally:
            session.close()
    
    def actualizar_sensor(self, sensor_id: int, nuevos_datos: Dict[str, Any]) -> bool:
        """Actualiza un sensor existente"""
        
        session = self.config_db.get_session()
        
        try:
            # Obtener el sensor
            sensor = session.query(SensorIndustrial).filter(
                SensorIndustrial.id == sensor_id
            ).first()
            
            if not sensor:
                print(f"❌ Sensor {sensor_id} no encontrado")
                return False
            
            # Actualizar campos
            for campo, valor in nuevos_datos.items():
                if hasattr(sensor, campo):
                    setattr(sensor, campo, valor)
                else:
                    print(f"⚠️ Campo '{campo}' no válido para sensor")
            
            # El campo actualizado_en se actualiza automáticamente por onupdate
            session.commit()
            
            print(f"✅ Sensor {sensor_id} actualizado correctamente")
            return True
            
        except Exception as e:
            session.rollback()
            print(f"❌ Error actualizando sensor: {e}")
            return False
            
        finally:
            session.close()
    
    def eliminar_sensor(self, sensor_id: int, eliminar_fisico: bool = False) -> bool:
        """Elimina un sensor (lógico o físico)"""
        
        session = self.config_db.get_session()
        
        try:
            sensor = session.query(SensorIndustrial).filter(
                SensorIndustrial.id == sensor_id
            ).first()
            
            if not sensor:
                print(f"❌ Sensor {sensor_id} no encontrado")
                return False
            
            if eliminar_fisico:
                # Eliminación física
                session.delete(sensor)
                print(f"🗑️ Sensor {sensor_id} eliminado físicamente")
            else:
                # Eliminación lógica
                sensor.activo = False
                print(f"📝 Sensor {sensor_id} marcado como inactivo")
            
            session.commit()
            return True
            
        except Exception as e:
            session.rollback()
            print(f"❌ Error eliminando sensor: {e}")
            return False
            
        finally:
            session.close()
    
    def buscar_sensores(self, filtros: Dict[str, Any]) -> List[SensorIndustrial]:
        """Búsqueda avanzada de sensores con filtros"""
        
        session = self.config_db.get_session()
        
        try:
            query = session.query(SensorIndustrial)
            
            # Aplicar filtros dinámicamente
            for campo, valor in filtros.items():
                if hasattr(SensorIndustrial, campo):
                    column = getattr(SensorIndustrial, campo)
                    
                    if isinstance(valor, str) and valor.startswith('%') and valor.endswith('%'):
                        # Búsqueda con LIKE
                        query = query.filter(column.like(valor))
                    else:
                        # Búsqueda exacta
                        query = query.filter(column == valor)
            
            sensores = query.all()
            
            print(f"🔍 Búsqueda completada: {len(sensores)} sensores encontrados")
            return sensores
            
        finally:
            session.close()

"""
6. GESTIÓN DE LECTURAS CON ORM
==============================

Implementación de operaciones CRUD para lecturas de sensores,
demostrando relaciones entre objetos.
"""

class GestorLecturasORM:
    """Gestor de lecturas usando SQLAlchemy ORM"""
    
    def __init__(self):
        self.config_db = config_db
    
    def registrar_lectura(self, sensor_id: int, valor: float, **kwargs) -> Optional[LecturasSensor]:
        """Registra una nueva lectura para un sensor"""
        
        session = self.config_db.get_session()
        
        try:
            # Verificar que el sensor existe
            sensor = session.query(SensorIndustrial).filter(
                SensorIndustrial.id == sensor_id
            ).first()
            
            if not sensor:
                print(f"❌ Sensor {sensor_id} no encontrado")
                return None
            
            # Validar que el valor está en rango
            if not sensor.validar_valor(valor):
                print(f"⚠️ Valor {valor} fuera del rango del sensor ({sensor.valor_minimo}-{sensor.valor_maximo})")
                kwargs['anomalia_detectada'] = True
                kwargs['calidad'] = 'MALA'
            
            # Crear lectura
            lectura = LecturasSensor(
                sensor_id=sensor_id,
                valor=valor,
                **kwargs
            )
            
            session.add(lectura)
            session.commit()
            session.refresh(lectura)
            
            print(f"📊 Lectura registrada: {lectura.id} - {valor} {sensor.unidad_medida}")
            return lectura
            
        except Exception as e:
            session.rollback()
            print(f"❌ Error registrando lectura: {e}")
            return None
            
        finally:
            session.close()
    
    def obtener_lecturas_sensor(self, sensor_id: int, limit: int = 100) -> List[LecturasSensor]:
        """Obtiene las últimas lecturas de un sensor"""
        
        session = self.config_db.get_session()
        
        try:
            lecturas = session.query(LecturasSensor).filter(
                LecturasSensor.sensor_id == sensor_id
            ).order_by(LecturasSensor.timestamp.desc()).limit(limit).all()
            
            print(f"📈 {len(lecturas)} lecturas obtenidas para sensor {sensor_id}")
            return lecturas
            
        finally:
            session.close()
    
    def obtener_estadisticas_sensor(self, sensor_id: int, horas: int = 24) -> Dict[str, Any]:
        """Obtiene estadísticas de un sensor en las últimas N horas"""
        
        session = self.config_db.get_session()
        
        try:
            # Timestamp límite
            timestamp_limite = datetime.utcnow() - timedelta(hours=horas)
            
            # Consultar lecturas en el período
            lecturas = session.query(LecturasSensor).filter(
                LecturasSensor.sensor_id == sensor_id,
                LecturasSensor.timestamp >= timestamp_limite
            ).all()
            
            if not lecturas:
                return {'error': 'No hay lecturas en el período especificado'}
            
            # Calcular estadísticas
            valores = [l.valor for l in lecturas]
            
            estadisticas = {
                'sensor_id': sensor_id,
                'periodo_horas': horas,
                'total_lecturas': len(lecturas),
                'valor_minimo': min(valores),
                'valor_maximo': max(valores),
                'valor_promedio': sum(valores) / len(valores),
                'primera_lectura': min(l.timestamp for l in lecturas),
                'ultima_lectura': max(l.timestamp for l in lecturas),
                'anomalias_detectadas': sum(1 for l in lecturas if l.anomalia_detectada),
                'calidad_promedio': sum(1 for l in lecturas if l.calidad == 'BUENA') / len(lecturas) * 100
            }
            
            print(f"📊 Estadísticas calculadas para sensor {sensor_id}:")
            for key, value in estadisticas.items():
                if isinstance(value, float):
                    print(f"    {key}: {value:.2f}")
                else:
                    print(f"    {key}: {value}")
            
            return estadisticas
            
        finally:
            session.close()

"""
7. DEMO PRÁCTICA COMPLETA
=========================

Demostración práctica que muestra todos los conceptos implementados
en esta parte del módulo.
"""

def demo_sqlalchemy_parte2():
    """Demostración completa de SQLAlchemy Parte 2"""
    
    print("🚀 DEMO PRÁCTICA - SQLALCHEMY PARTE 2")
    print("=" * 60)
    
    try:
        # 1. Verificar configuración
        print("\n1️⃣ VERIFICANDO CONFIGURACIÓN...")
        if not config_db.probar_conexion():
            return False
        
        config_db.obtener_info_motor()
        
        # 2. Crear estructura de base de datos
        print("\n2️⃣ CREANDO ESTRUCTURA DE BASE DE DATOS...")
        if not crear_tablas_base_datos():
            return False
        
        # 3. Configurar datos iniciales
        print("\n3️⃣ CONFIGURANDO DATOS INICIALES...")
        if not configurar_datos_iniciales():
            return False
        
        # 4. Demostrar operaciones CRUD con sensores
        print("\n4️⃣ DEMOSTRANDO CRUD DE SENSORES...")
        gestor_sensores = GestorSensoresORM()
        
        # Listar sensores existentes
        sensores = gestor_sensores.listar_sensores()
        
        # Crear un nuevo sensor
        nuevo_sensor_data = {
            'nombre': 'TEMP_COMPRESOR_05',
            'tipo': 'Temperatura',
            'ubicacion': 'Compresor Principal - Entrada',
            'unidad_medida': '°C',
            'valor_minimo': -10.0,
            'valor_maximo': 120.0,
            'precision_decimal': 1
        }
        
        nuevo_sensor = gestor_sensores.crear_sensor(nuevo_sensor_data)
        
        if nuevo_sensor:
            # Actualizar el sensor
            gestor_sensores.actualizar_sensor(
                nuevo_sensor.id,
                {'valor_maximo': 150.0, 'fecha_ultima_calibracion': datetime.utcnow()}
            )
            
            # Buscar sensores por tipo
            sensores_temp = gestor_sensores.buscar_sensores({'tipo': 'Temperatura'})
        
        # 5. Demostrar operaciones con lecturas
        print("\n5️⃣ DEMOSTRANDO OPERACIONES CON LECTURAS...")
        gestor_lecturas = GestorLecturasORM()
        
        if sensores:
            primer_sensor = sensores[0]
            
            # Registrar algunas lecturas
            import random
            for i in range(5):
                valor = random.uniform(primer_sensor.valor_minimo, primer_sensor.valor_maximo)
                lectura = gestor_lecturas.registrar_lectura(
                    primer_sensor.id,
                    valor,
                    calidad='BUENA',
                    temperatura_ambiente=random.uniform(20.0, 25.0)
                )
            
            # Obtener lecturas del sensor
            lecturas_recientes = gestor_lecturas.obtener_lecturas_sensor(primer_sensor.id, 10)
            
            # Obtener estadísticas
            stats = gestor_lecturas.obtener_estadisticas_sensor(primer_sensor.id, 24)
        
        # 6. Demostrar relaciones entre objetos
        print("\n6️⃣ DEMOSTRANDO RELACIONES ORM...")
        session = config_db.get_session()
        
        try:
            # Consulta con JOIN usando ORM
            lecturas_con_sensor = session.query(LecturasSensor).join(SensorIndustrial).filter(
                SensorIndustrial.tipo == 'Temperatura'
            ).limit(5).all()
            
            print(f"🔗 {len(lecturas_con_sensor)} lecturas de sensores de temperatura:")
            for lectura in lecturas_con_sensor:
                print(f"    {lectura.sensor.nombre}: {lectura.valor} {lectura.sensor.unidad_medida}")
        
        finally:
            session.close()
        
        print("\n" + "="*60)
        print("🎉 ¡DEMO PARTE 2 COMPLETADA EXITOSAMENTE!")
        print("="*60)
        print("✅ Configuración de SQLAlchemy funcionando")
        print("✅ Modelos declarativos implementados")
        print("✅ Operaciones CRUD funcionando")
        print("✅ Relaciones ORM operativas")
        print("\n🚀 Listo para avanzar a la Parte 3: Modelos Avanzados y Relaciones")
        
        return True
        
    except Exception as e:
        print(f"❌ Error en demo: {e}")
        return False

"""
8. EJERCICIOS PRÁCTICOS PROGRESIVOS
===================================

Ejercicios diseñados para consolidar el aprendizaje de la Parte 2.
"""

def ejercicio_basico_modelos():
    """Ejercicio básico: Creación y manipulación de modelos"""
    
    print("🎯 EJERCICIO BÁSICO: Modelos y CRUD")
    print("-" * 40)
    
    # TODO para el estudiante:
    print("📝 TAREAS A COMPLETAR:")
    print("1. Crear un nuevo sensor de tipo 'Humedad'")
    print("2. Registrar 3 lecturas para ese sensor")
    print("3. Actualizar la ubicación del sensor")
    print("4. Obtener estadísticas de 1 hora")
    
    # Implementación ejemplo
    gestor_sensores = GestorSensoresORM()
    gestor_lecturas = GestorLecturasORM()
    
    # 1. Crear sensor de humedad
    sensor_humedad = gestor_sensores.crear_sensor({
        'nombre': 'HUM_AMBIENTE_01',
        'tipo': 'Humedad',
        'ubicacion': 'Sala de Control',
        'unidad_medida': '%',
        'valor_minimo': 0.0,
        'valor_maximo': 100.0,
        'precision_decimal': 1
    })
    
    if sensor_humedad:
        # 2. Registrar lecturas
        import random
        for i in range(3):
            valor = random.uniform(30.0, 70.0)
            gestor_lecturas.registrar_lectura(sensor_humedad.id, valor)
        
        # 3. Actualizar ubicación
        gestor_sensores.actualizar_sensor(
            sensor_humedad.id,
            {'ubicacion': 'Sala de Control - Zona Norte'}
        )
        
        # 4. Obtener estadísticas
        stats = gestor_lecturas.obtener_estadisticas_sensor(sensor_humedad.id, 1)
    
    print("✅ Ejercicio básico completado")

def ejercicio_intermedio_consultas():
    """Ejercicio intermedio: Consultas avanzadas con ORM"""
    
    print("🎯 EJERCICIO INTERMEDIO: Consultas Avanzadas")
    print("-" * 45)
    
    session = config_db.get_session()
    
    try:
        # Consulta 1: Sensores que requieren calibración
        print("\n1. Sensores que requieren calibración:")
        sensores = session.query(SensorIndustrial).all()
        for sensor in sensores:
            if sensor.requiere_calibracion(30):  # 30 días
                print(f"    ⚠️ {sensor.nombre} - Última calibración: {sensor.fecha_ultima_calibracion}")
        
        # Consulta 2: Promedio de lecturas por tipo de sensor
        print("\n2. Promedio de lecturas por tipo:")
        from sqlalchemy import func
        
        resultado = session.query(
            SensorIndustrial.tipo,
            func.avg(LecturasSensor.valor).label('promedio'),
            func.count(LecturasSensor.id).label('total_lecturas')
        ).join(LecturasSensor).group_by(SensorIndustrial.tipo).all()
        
        for tipo, promedio, total in resultado:
            print(f"    {tipo}: {promedio:.2f} ({total} lecturas)")
        
        # Consulta 3: Lecturas con anomalías
        print("\n3. Lecturas con anomalías detectadas:")
        lecturas_anomalas = session.query(LecturasSensor).filter(
            LecturasSensor.anomalia_detectada == True
        ).join(SensorIndustrial).all()
        
        for lectura in lecturas_anomalas:
            print(f"    🚨 {lectura.sensor.nombre}: {lectura.valor} (calidad: {lectura.calidad})")
    
    finally:
        session.close()
    
    print("✅ Ejercicio intermedio completado")

"""
9. CUESTIONARIO DE CONSOLIDACIÓN PARTE 2
========================================

def cuestionario_parte2():
    \"\"\"Cuestionario de evaluación para la Parte 2\"\"\"
    
    print("📝 CUESTIONARIO - PARTE 2: CONFIGURACIÓN PRÁCTICA")
    print("=" * 55)
    
    preguntas = {
        1: {
            'pregunta': '¿Qué ventaja principal ofrece declarative_base() de SQLAlchemy?',
            'opciones': [
                'a) Mayor velocidad de consultas',
                'b) Mapeo automático entre clases Python y tablas SQL',
                'c) Mejor seguridad contra inyección SQL',
                'd) Reducción del tamaño de la base de datos'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'declarative_base() permite definir modelos como clases Python que se mapean automáticamente a tablas SQL.'
        },
        2: {
            'pregunta': '¿Cuál es el propósito del sessionmaker() en SQLAlchemy?',
            'opciones': [
                'a) Crear conexiones directas a la base de datos',
                'b) Factory para crear objetos Session configurados',
                'c) Manejar migraciones de esquema',
                'd) Optimizar consultas SQL'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'sessionmaker() es un factory que crea objetos Session con configuración predefinida.'
        },
        3: {
            'pregunta': '¿Qué diferencia hay entre eliminar un objeto con session.delete() vs marcarlo como inactivo?',
            'opciones': [
                'a) No hay diferencia, ambos hacen lo mismo',
                'b) delete() elimina físicamente, marcar inactivo es eliminación lógica',
                'c) delete() es más rápido',
                'd) Marcar inactivo consume más espacio'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'session.delete() elimina físicamente el registro, mientras que marcar como inactivo preserva los datos históricos.'
        }
    }
    
    print("✅ RESPUESTAS CORRECTAS:")
    for num, data in preguntas.items():
        print(f"\nPregunta {num}: {data['pregunta']}")
        for opcion in data['opciones']:
            marca = "✓" if opcion.startswith(data['respuesta_correcta']) else " "
            print(f"  [{marca}] {opcion}")
        print(f"💡 Explicación: {data['explicacion']}")

def checklist_parte2():
    \"\"\"Checklist de consolidación para la Parte 2\"\"\"
    
    print("\n🎯 CHECKLIST DE CONSOLIDACIÓN - PARTE 2")
    print("=" * 50)
    
    items_parte2 = [
        "✅ SQLAlchemy instalado y configurado correctamente",
        "✅ Engine configurado con parámetros de producción",
        "✅ SessionLocal configurado adecuadamente",
        "✅ Modelos declarativos funcionando (SensorIndustrial, LecturasSensor)",
        "✅ Relaciones entre modelos definidas correctamente",
        "✅ Operaciones CRUD básicas implementadas",
        "✅ Validaciones de negocio en los modelos",
        "✅ Manejo de errores y rollback de transacciones",
        "✅ Consultas con filtros y ordenamiento",
        "✅ Estadísticas básicas con funciones agregadas",
        "✅ Context managers para gestión de sesiones",
        "✅ Logging configurado para debugging",
        "✅ Datos de demostración generados",
        "✅ Ejercicios prácticos completados"
    ]
    
    print("📋 CONOCIMIENTOS CONSOLIDADOS:")
    for item in items_parte2:
        print(f"  {item}")
    
    print(f"\n🏆 TOTAL OBJETIVOS PARTE 2: {len(items_parte2)}/14")
    print("🎓 NIVEL: CONFIGURACIÓN PRÁCTICA COMPLETADA")
    print("📈 PREPARACIÓN PARA PARTE 3: 100% LISTO")

=================================================================
10. FUNCIÓN PRINCIPAL DE DEMOSTRACIÓN
=================================================================

def main():
    \"\"\"Función principal que ejecuta toda la demostración de la Parte 2\"\"\"
    
    print("🐍🔗 MÓDULO 3.3 PARTE 2: CONFIGURACIÓN PRÁCTICA DE SQLALCHEMY")
    print("=" * 70)
    
    try:
        # Ejecutar demostración completa
        if demo_sqlalchemy_parte2():
            
            # Ejecutar ejercicios
            print("\n📚 EJECUTANDO EJERCICIOS PRÁCTICOS...")
            ejercicio_basico_modelos()
            ejercicio_intermedio_consultas()
            
            # Evaluación
            print("\n📝 EVALUACIÓN Y CONSOLIDACIÓN...")
            cuestionario_parte2()
            checklist_parte2()
            
            print("\n" + "="*70)
            print("🎉 ¡PARTE 2 COMPLETADA EXITOSAMENTE!")
            print("="*70)
            print("🚀 Siguiente etapa: Parte 3 - Modelos Avanzados y Relaciones")
            print("📚 Has dominado la configuración práctica de SQLAlchemy")
            print("💪 ¡Excelente progreso en el aprendizaje deliberado!")
            
        else:
            print("\n❌ Error en la demostración. Revisa la configuración.")
    
    except Exception as e:
        print(f"\n❌ Error ejecutando Parte 2: {e}")
        print("🔧 Verifica las dependencias y configuración")

if __name__ == "__main__":
    main()

=================================================================
🎓 CONCLUSIÓN DE LA PARTE 2
=================================================================

\"\"\"
¡EXCELENTE TRABAJO! Has completado la Parte 2 del Módulo 3.3.

🏆 LOGROS DE ESTA PARTE:
- Configuración profesional de SQLAlchemy
- Modelos declarativos industriales funcionando
- Operaciones CRUD completas con ORM
- Relaciones básicas entre entidades
- Validaciones de negocio implementadas
- Manejo de sesiones y transacciones

🚀 PREPARACIÓN PARA PARTE 3:
- Tienes la base sólida de SQLAlchemy ORM
- Comprendes el mapeo objeto-relacional
- Dominas las operaciones básicas
- Estás listo para relaciones complejas

📈 PRÓXIMA PARTE: 3.3.3 - Modelos Avanzados y Relaciones
- Relaciones One-to-Many, Many-to-Many
- Modelos industriales complejos
- Herencia de modelos
- Consultas avanzadas con joins
- Optimización de rendimiento

¡Continúa con esta metodología de aprendizaje deliberado!
\"\"\"
"""
