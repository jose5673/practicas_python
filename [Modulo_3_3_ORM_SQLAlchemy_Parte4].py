"""
🐍🗄️ MÓDULO 3.3: ORM CON SQLALCHEMY - PARTE 4
🔧 MIGRACIONES, TESTING Y CONFIGURACIÓN PARA PRODUCCIÓN
📈 Maestría en Python - Fase 3: Gestión Avanzada de Datos

=================================================================
OBJETIVO PRINCIPAL: Preparar aplicaciones SQLAlchemy para producción
=================================================================

Esta parte final del módulo 3.3 cubre los aspectos críticos para llevar
aplicaciones SQLAlchemy a producción industrial:
- Migraciones automáticas con Alembic
- Testing exhaustivo de modelos ORM
- Configuración robusta para producción
- Monitoreo y logging avanzado
- Deployment y mantenimiento

📋 CONTENIDO DE LA PARTE 4:
=========================

1. MIGRACIONES CON ALEMBIC
   - Configuración de Alembic
   - Creación de migraciones automáticas
   - Aplicación y rollback de migraciones
   - Estrategias de deployment

2. TESTING DE MODELOS ORM
   - Unit tests para modelos
   - Integration tests con base de datos
   - Fixtures y factories
   - Testing de relaciones complejas

3. CONFIGURACIÓN PARA PRODUCCIÓN
   - Variables de entorno
   - Connection pooling avanzado
   - Configuración por ambientes
   - Secrets management

4. MONITOREO Y LOGGING
   - Logging de queries SQL
   - Métricas de performance
   - Alertas y monitoreo
   - Debugging en producción

5. DEPLOYMENT Y MANTENIMIENTO
   - Containerización con Docker
   - CI/CD pipelines
   - Backup y recovery
   - Escalabilidad horizontal

=================================================================
1. MIGRACIONES CON ALEMBIC
=================================================================

🔄 ¿QUÉ SON LAS MIGRACIONES?
===========================

Las migraciones son scripts que modifican el esquema de la base de datos
de manera controlada y versionada. Permiten:

✅ VENTAJAS:
- Evolución controlada del esquema
- Sincronización entre entornos (dev, test, prod)
- Rollback seguro de cambios
- Trabajo colaborativo sin conflictos
- Deployment automatizado

🛠️ ALEMBIC: EL GESTOR DE MIGRACIONES DE SQLALCHEMY
==================================================

Alembic es la herramienta oficial para migraciones de SQLAlchemy:
- Autogeneración de migraciones
- Soporte para múltiples cabezas (branches)
- Migraciones online y offline
- Integración completa con SQLAlchemy

=================================================================
CONFIGURACIÓN INICIAL DE ALEMBIC
=================================================================
"""

import os
import sys
from pathlib import Path
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
from typing import Optional
import logging

# Configuración base
Base = declarative_base()

class ConfiguracionProduccion:
    """Configuración centralizada para diferentes ambientes"""
    
    def __init__(self, ambiente: str = "development"):
        self.ambiente = ambiente
        self._configurar_ambiente()
    
    def _configurar_ambiente(self):
        """Configura variables según el ambiente"""
        
        if self.ambiente == "development":
            self.database_url = "sqlite:///desarrollo_industrial.db"
            self.echo_sql = True
            self.pool_size = 5
            self.max_overflow = 10
            
        elif self.ambiente == "testing":
            self.database_url = "sqlite:///:memory:"
            self.echo_sql = False
            self.pool_size = 1
            self.max_overflow = 0
            
        elif self.ambiente == "production":
            # En producción, usar variables de entorno
            self.database_url = os.getenv(
                'DATABASE_URL', 
                'postgresql://user:password@localhost:5432/industrial_prod'
            )
            self.echo_sql = False
            self.pool_size = 20
            self.max_overflow = 30
            
        # Configuración de logging
        self.log_level = logging.DEBUG if self.ambiente == "development" else logging.INFO

def obtener_engine(config: ConfiguracionProduccion):
    """Factory para crear engines según configuración"""
    
    return create_engine(
        config.database_url,
        echo=config.echo_sql,
        pool_size=config.pool_size,
        max_overflow=config.max_overflow,
        # Configuraciones adicionales para producción
        pool_pre_ping=True,  # Verificar conexiones antes de usar
        pool_recycle=3600,   # Reciclar conexiones cada hora
    )

"""
=================================================================
MODELOS PARA DEMOSTRACIÓN DE MIGRACIONES
=================================================================

Vamos a partir de un esquema básico y evolucionarlo a través de migraciones.
"""

# VERSIÓN INICIAL DE LOS MODELOS (para primera migración)
class DispositivoIndustrial(Base):
    """Modelo base para dispositivos industriales"""
    __tablename__ = 'dispositivos_industriales'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    modelo = Column(String(100))
    fabricante = Column(String(100))
    numero_serie = Column(String(100), unique=True)
    fecha_instalacion = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<DispositivoIndustrial(nombre='{self.nombre}', tipo='{self.tipo}')>"

class LecturaDispositivo(Base):
    """Lecturas de dispositivos industriales"""
    __tablename__ = 'lecturas_dispositivos'
    
    id = Column(Integer, primary_key=True)
    dispositivo_id = Column(Integer, ForeignKey('dispositivos_industriales.id'), nullable=False)
    valor = Column(Float, nullable=False)
    unidad = Column(String(20))
    timestamp = Column(DateTime, default=datetime.utcnow)
    calidad = Column(String(20), default='GOOD')
    
    # Relación
    dispositivo = relationship("DispositivoIndustrial", backref="lecturas")
    
    def __repr__(self):
        return f"<LecturaDispositivo(dispositivo_id={self.dispositivo_id}, valor={self.valor})>"

"""
=================================================================
CONFIGURACIÓN PASO A PASO DE ALEMBIC
=================================================================

📋 PASO 1: INSTALACIÓN Y CONFIGURACIÓN INICIAL
===============================================
"""

def setup_alembic_paso_a_paso():
    """Guía paso a paso para configurar Alembic"""
    
    print("🔧 CONFIGURACIÓN DE ALEMBIC - PASO A PASO")
    print("=" * 50)
    
    print("\n1️⃣ INSTALACIÓN:")
    print("pip install alembic")
    
    print("\n2️⃣ INICIALIZACIÓN DEL PROYECTO:")
    print("alembic init alembic")
    print("   - Crea directorio 'alembic/' con configuración")
    print("   - Crea archivo 'alembic.ini' de configuración")
    
    print("\n3️⃣ ESTRUCTURA CREADA:")
    print("""
    proyecto/
    ├── alembic/
    │   ├── env.py              # Configuración del entorno
    │   ├── script.py.mako      # Template para migraciones
    │   └── versions/           # Directorio de migraciones
    ├── alembic.ini             # Configuración principal
    └── models.py               # Tus modelos SQLAlchemy
    """)
    
    return True

"""
=================================================================
CONFIGURACIÓN DEL ARCHIVO env.py
=================================================================

El archivo env.py es el corazón de la configuración de Alembic.
Aquí está una configuración robusta para producción:
"""

def generar_env_py_produccion():
    """Genera un env.py optimizado para producción"""
    
    env_py_content = '''
import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Agregar el directorio del proyecto al path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar modelos y configuración
from models import Base  # Ajustar según tu estructura
from config import ConfiguracionProduccion, obtener_engine

# Configuración de Alembic
config = context.config

# Configurar logging si existe
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# MetaData target para autogeneración
target_metadata = Base.metadata

def get_url():
    """Obtiene la URL de la base de datos según el ambiente"""
    ambiente = os.getenv('AMBIENTE', 'development')
    config_obj = ConfiguracionProduccion(ambiente)
    return config_obj.database_url

def run_migrations_offline():
    """Ejecuta migraciones en modo offline"""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Ejecuta migraciones en modo online"""
    
    # Configurar engine
    configuration = config.get_section(config.config_ini_section)
    configuration['sqlalchemy.url'] = get_url()
    
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
'''
    
    return env_py_content

"""
=================================================================
CREACIÓN DE MIGRACIONES AUTOMÁTICAS
=================================================================
"""

class GestorMigraciones:
    """Gestor para crear y aplicar migraciones"""
    
    def __init__(self, directorio_alembic: str = "alembic"):
        self.directorio_alembic = directorio_alembic
    
    def crear_migracion_inicial(self):
        """Crea la migración inicial del esquema"""
        
        print("\n🚀 CREANDO MIGRACIÓN INICIAL")
        print("=" * 40)
        
        # Comando para crear migración inicial
        comando = "alembic revision --autogenerate -m 'Migración inicial: dispositivos y lecturas'"
        
        print(f"💻 Comando: {comando}")
        print("\n📋 Esta migración incluirá:")
        print("   - Tabla dispositivos_industriales")
        print("   - Tabla lecturas_dispositivos")
        print("   - Relación Foreign Key entre ambas")
        print("   - Índices automáticos")
        
        return comando
    
    def crear_migracion_evolutiva(self, descripcion: str):
        """Crea una migración para evolucionar el esquema"""
        
        print(f"\n🔄 CREANDO MIGRACIÓN: {descripcion}")
        print("=" * 50)
        
        comando = f"alembic revision --autogenerate -m '{descripcion}'"
        
        print(f"💻 Comando: {comando}")
        print("\n⚡ Alembic detectará automáticamente:")
        print("   - Tablas nuevas")
        print("   - Columnas agregadas/eliminadas")
        print("   - Índices modificados")
        print("   - Constraints cambiados")
        
        return comando
    
    def aplicar_migraciones(self, revision: str = "head"):
        """Aplica migraciones hasta la revisión especificada"""
        
        print(f"\n✅ APLICANDO MIGRACIONES HASTA: {revision}")
        print("=" * 45)
        
        comando = f"alembic upgrade {revision}"
        
        print(f"💻 Comando: {comando}")
        print("\n🔍 Verificaciones que hace Alembic:")
        print("   - Estado actual de la BD")
        print("   - Migraciones pendientes")
        print("   - Validación de integridad")
        print("   - Aplicación en orden correcto")
        
        return comando
    
    def rollback_migracion(self, revision: str = "-1"):
        """Hace rollback a una revisión anterior"""
        
        print(f"\n⬅️ ROLLBACK A REVISIÓN: {revision}")
        print("=" * 40)
        
        comando = f"alembic downgrade {revision}"
        
        print(f"💻 Comando: {comando}")
        print("\n⚠️ IMPORTANTE:")
        print("   - Rollback puede perder datos")
        print("   - Siempre hacer backup antes")
        print("   - Verificar scripts de downgrade")
        
        return comando

# ========================== PUNTO DE PARADA 1 ==========================
print("""
🛑 PUNTO DE PAUSA 1 - CONFIGURACIÓN DE ALEMBIC
==============================================

He cubierto hasta aquí:
✅ Configuración inicial de Alembic
✅ Setup del archivo env.py para producción
✅ Gestor de migraciones básico
✅ Comandos fundamentales

📋 PRÓXIMO BLOQUE INCLUIRÁ:
- Ejemplos prácticos de migraciones
- Testing exhaustivo de modelos ORM
- Configuración robusta para producción
- Estrategias de deployment

💬 ¿Continúo con la siguiente sección de Testing y ejemplos prácticos?
""")

def continuar_con_testing():
    """Función placeholder para continuar con testing"""
    return "Listo para continuar con Testing de modelos ORM"

if __name__ == "__main__":
    print("🐍🔧 MÓDULO 3.3 PARTE 4: MIGRACIONES Y PRODUCCIÓN")
    print("=" * 60)
    print("📋 Configuración de Alembic completada")
    print("🛑 Esperando confirmación para continuar...")

# ========================== CONTINUACIÓN PARTE 4 ==========================

"""
=================================================================
2. TESTING EXHAUSTIVO DE MODELOS ORM
=================================================================

🧪 IMPORTANCIA DEL TESTING EN ORM
=================================

Testing de modelos ORM es crítico porque:
- Valida integridad de relaciones complejas
- Detecta problemas de performance temprano
- Asegura comportamiento correcto en producción
- Facilita refactoring seguro
- Cumple estándares de calidad industrial

📋 TIPOS DE TESTING PARA ORM:
============================
1. Unit Tests: Modelos individuales
2. Integration Tests: Relaciones entre modelos
3. Performance Tests: Optimización de queries
4. Migration Tests: Validación de migraciones
"""

import unittest
import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import tempfile
import os
from datetime import datetime, timedelta
import random

# Configuración para testing
class TestConfig:
    """Configuración específica para testing"""
    
    @staticmethod
    def get_test_engine():
        """Engine en memoria para tests rápidos"""
        return create_engine(
            'sqlite:///:memory:',
            echo=False,  # Silencioso durante tests
            poolclass=StaticPool,
            connect_args={
                'check_same_thread': False,
            }
        )
    
    @staticmethod
    def get_test_session(engine):
        """Sesión para tests"""
        Session = sessionmaker(bind=engine)
        return Session()

"""
=================================================================
UNIT TESTS PARA MODELOS INDIVIDUALES
=================================================================
"""

class TestDispositivoIndustrial(unittest.TestCase):
    """Tests unitarios para el modelo DispositivoIndustrial"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.engine = TestConfig.get_test_engine()
        Base.metadata.create_all(self.engine)
        self.session = TestConfig.get_test_session(self.engine)
    
    def tearDown(self):
        """Limpieza después de cada test"""
        self.session.close()
        Base.metadata.drop_all(self.engine)
    
    def test_crear_dispositivo_basico(self):
        """Test: Crear dispositivo con datos básicos"""
        dispositivo = DispositivoIndustrial(
            nombre="SENSOR_TEST_01",
            tipo="temperatura",
            modelo="TH100",
            fabricante="IndustrialTech"
        )
        
        self.session.add(dispositivo)
        self.session.commit()
        
        # Verificaciones
        self.assertIsNotNone(dispositivo.id)
        self.assertEqual(dispositivo.nombre, "SENSOR_TEST_01")
        self.assertTrue(dispositivo.activo)  # Default True
        self.assertIsNotNone(dispositivo.fecha_instalacion)
    
    def test_dispositivo_con_numero_serie_unico(self):
        """Test: Número de serie debe ser único"""
        dispositivo1 = DispositivoIndustrial(
            nombre="SENSOR_01",
            tipo="presion",
            numero_serie="SN123456"
        )
        
        dispositivo2 = DispositivoIndustrial(
            nombre="SENSOR_02",
            tipo="temperatura",
            numero_serie="SN123456"  # Mismo número de serie
        )
        
        self.session.add(dispositivo1)
        self.session.commit()
        
        self.session.add(dispositivo2)
        
        # Debe fallar por constraint de unicidad
        with self.assertRaises(Exception):
            self.session.commit()
    
    def test_representacion_string(self):
        """Test: Representación string del modelo"""
        dispositivo = DispositivoIndustrial(
            nombre="MOTOR_X1",
            tipo="motor"
        )
        
        expected = "<DispositivoIndustrial(nombre='MOTOR_X1', tipo='motor')>"
        self.assertEqual(str(dispositivo), expected)

class TestLecturaDispositivo(unittest.TestCase):
    """Tests unitarios para el modelo LecturaDispositivo"""
    
    def setUp(self):
        """Configuración antes de cada test"""
        self.engine = TestConfig.get_test_engine()
        Base.metadata.create_all(self.engine)
        self.session = TestConfig.get_test_session(self.engine)
        
        # Crear dispositivo de prueba
        self.dispositivo_test = DispositivoIndustrial(
            nombre="DISPOSITIVO_TEST",
            tipo="temperatura"
        )
        self.session.add(self.dispositivo_test)
        self.session.commit()
    
    def tearDown(self):
        """Limpieza después de cada test"""
        self.session.close()
        Base.metadata.drop_all(self.engine)
    
    def test_crear_lectura_basica(self):
        """Test: Crear lectura básica"""
        lectura = LecturaDispositivo(
            dispositivo_id=self.dispositivo_test.id,
            valor=25.5,
            unidad="°C"
        )
        
        self.session.add(lectura)
        self.session.commit()
        
        # Verificaciones
        self.assertIsNotNone(lectura.id)
        self.assertEqual(lectura.valor, 25.5)
        self.assertEqual(lectura.calidad, 'GOOD')  # Default
        self.assertIsNotNone(lectura.timestamp)
    
    def test_relacion_con_dispositivo(self):
        """Test: Relación correcta con dispositivo"""
        lectura = LecturaDispositivo(
            dispositivo_id=self.dispositivo_test.id,
            valor=100.0
        )
        
        self.session.add(lectura)
        self.session.commit()
        
        # Verificar relación
        self.assertEqual(lectura.dispositivo.nombre, "DISPOSITIVO_TEST")
        self.assertEqual(len(self.dispositivo_test.lecturas), 1)
        self.assertEqual(self.dispositivo_test.lecturas[0].valor, 100.0)
    
    def test_lectura_sin_dispositivo_falla(self):
        """Test: Lectura sin dispositivo válido debe fallar"""
        lectura = LecturaDispositivo(
            dispositivo_id=99999,  # ID inexistente
            valor=50.0
        )
        
        self.session.add(lectura)
        
        # Debe fallar por foreign key constraint
        with self.assertRaises(Exception):
            self.session.commit()

"""
=================================================================
INTEGRATION TESTS PARA RELACIONES COMPLEJAS
=================================================================
"""

class TestRelacionesComplejas(unittest.TestCase):
    """Tests de integración para relaciones entre modelos"""
    
    def setUp(self):
        """Configuración para tests de integración"""
        self.engine = TestConfig.get_test_engine()
        Base.metadata.create_all(self.engine)
        self.session = TestConfig.get_test_session(self.engine)
    
    def tearDown(self):
        """Limpieza después de cada test"""
        self.session.close()
        Base.metadata.drop_all(self.engine)
    
    def test_cascada_eliminacion(self):
        """Test: Eliminación en cascada funciona correctamente"""
        # Crear dispositivo con lecturas
        dispositivo = DispositivoIndustrial(
            nombre="DEVICE_CASCADE",
            tipo="sensor"
        )
        self.session.add(dispositivo)
        self.session.flush()  # Para obtener ID
        
        # Crear múltiples lecturas
        for i in range(5):
            lectura = LecturaDispositivo(
                dispositivo_id=dispositivo.id,
                valor=i * 10.0
            )
            self.session.add(lectura)
        
        self.session.commit()
        
        # Verificar que se crearon las lecturas
        self.assertEqual(len(dispositivo.lecturas), 5)
        
        # Eliminar dispositivo
        self.session.delete(dispositivo)
        self.session.commit()
        
        # Verificar que las lecturas también se eliminaron
        lecturas_restantes = self.session.query(LecturaDispositivo).all()
        self.assertEqual(len(lecturas_restantes), 0)
    
    def test_consulta_con_join(self):
        """Test: Consultas con JOIN funcionan correctamente"""
        # Crear dispositivos con lecturas
        for i in range(3):
            dispositivo = DispositivoIndustrial(
                nombre=f"DEVICE_{i}",
                tipo="sensor"
            )
            self.session.add(dispositivo)
            self.session.flush()
            
            # Agregar lecturas
            for j in range(2):
                lectura = LecturaDispositivo(
                    dispositivo_id=dispositivo.id,
                    valor=i * 10 + j
                )
                self.session.add(lectura)
        
        self.session.commit()
        
        # Consulta con JOIN
        resultado = self.session.query(DispositivoIndustrial, LecturaDispositivo)\
            .join(LecturaDispositivo)\
            .filter(LecturaDispositivo.valor > 10)\
            .all()
        
        # Verificar resultados
        self.assertTrue(len(resultado) > 0)
        for dispositivo, lectura in resultado:
            self.assertGreater(lectura.valor, 10)
            self.assertEqual(lectura.dispositivo_id, dispositivo.id)

"""
=================================================================
PERFORMANCE TESTS
=================================================================
"""

class TestPerformanceORM(unittest.TestCase):
    """Tests de performance para operaciones ORM"""
    
    def setUp(self):
        """Configuración para tests de performance"""
        self.engine = TestConfig.get_test_engine()
        Base.metadata.create_all(self.engine)
        self.session = TestConfig.get_test_session(self.engine)
        
        # Crear datos de prueba masivos
        self._crear_datos_masivos()
    
    def tearDown(self):
        """Limpieza después de cada test"""
        self.session.close()
        Base.metadata.drop_all(self.engine)
    
    def _crear_datos_masivos(self):
        """Crea datos masivos para tests de performance"""
        dispositivos = []
        
        # Crear 100 dispositivos
        for i in range(100):
            dispositivo = DispositivoIndustrial(
                nombre=f"DEVICE_PERF_{i:03d}",
                tipo=random.choice(['temperatura', 'presion', 'flujo']),
                numero_serie=f"SN{i:06d}"
            )
            dispositivos.append(dispositivo)
        
        self.session.add_all(dispositivos)
        self.session.commit()
        
        # Crear 10,000 lecturas
        lecturas = []
        for dispositivo in dispositivos:
            for j in range(100):  # 100 lecturas por dispositivo
                lectura = LecturaDispositivo(
                    dispositivo_id=dispositivo.id,
                    valor=random.uniform(0, 1000),
                    timestamp=datetime.utcnow() - timedelta(hours=j)
                )
                lecturas.append(lectura)
        
        # Inserción en lotes para mejor performance
        for i in range(0, len(lecturas), 1000):
            batch = lecturas[i:i+1000]
            self.session.add_all(batch)
            self.session.commit()
    
    def test_consulta_simple_performance(self):
        """Test: Performance de consulta simple"""
        import time
        
        start_time = time.time()
        
        # Consulta simple
        dispositivos = self.session.query(DispositivoIndustrial)\
            .filter(DispositivoIndustrial.tipo == 'temperatura')\
            .all()
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        # Verificar que la consulta fue rápida (< 1 segundo)
        self.assertLess(elapsed, 1.0)
        self.assertGreater(len(dispositivos), 0)
    
    def test_consulta_con_agregacion_performance(self):
        """Test: Performance de consultas con agregación"""
        import time
        from sqlalchemy import func
        
        start_time = time.time()
        
        # Consulta con agregación
        resultado = self.session.query(
            DispositivoIndustrial.tipo,
            func.count(LecturaDispositivo.id).label('total_lecturas'),
            func.avg(LecturaDispositivo.valor).label('promedio')
        ).join(LecturaDispositivo)\
        .group_by(DispositivoIndustrial.tipo)\
        .all()
        
        end_time = time.time()
        elapsed = end_time - start_time
        
        # Verificar performance y resultados
        self.assertLess(elapsed, 2.0)  # Máximo 2 segundos
        self.assertGreater(len(resultado), 0)
    
    def test_lazy_loading_vs_eager_loading(self):
        """Test: Comparar lazy vs eager loading"""
        import time
        
        # Test Lazy Loading (problemático - N+1 queries)
        start_time = time.time()
        
        dispositivos_lazy = self.session.query(DispositivoIndustrial).limit(10).all()
        for dispositivo in dispositivos_lazy:
            _ = len(dispositivo.lecturas)  # Trigger lazy loading
        
        lazy_time = time.time() - start_time
        
        # Test Eager Loading (optimizado)
        start_time = time.time()
        
        from sqlalchemy.orm import joinedload
        
        dispositivos_eager = self.session.query(DispositivoIndustrial)\
            .options(joinedload(DispositivoIndustrial.lecturas))\
            .limit(10)\
            .all()
        
        for dispositivo in dispositivos_eager:
            _ = len(dispositivo.lecturas)  # Sin queries adicionales
        
        eager_time = time.time() - start_time
        
        # Eager loading debe ser más rápido
        self.assertLess(eager_time, lazy_time)
        print(f"Lazy: {lazy_time:.3f}s, Eager: {eager_time:.3f}s")

"""
=================================================================
FACTORIES Y FIXTURES PARA TESTING
=================================================================
"""

class DispositivoFactory:
    """Factory para crear dispositivos de prueba"""
    
    @staticmethod
    def crear_sensor_temperatura(session, nombre=None):
        """Crea un sensor de temperatura para testing"""
        dispositivo = DispositivoIndustrial(
            nombre=nombre or f"TEMP_SENSOR_{random.randint(1000, 9999)}",
            tipo="temperatura",
            modelo="TH200",
            fabricante="TechSensors",
            numero_serie=f"TS{random.randint(100000, 999999)}"
        )
        session.add(dispositivo)
        session.flush()
        return dispositivo
    
    @staticmethod
    def crear_con_lecturas(session, num_lecturas=10):
        """Crea dispositivo con lecturas de prueba"""
        dispositivo = DispositivoFactory.crear_sensor_temperatura(session)
        
        for i in range(num_lecturas):
            lectura = LecturaDispositivo(
                dispositivo_id=dispositivo.id,
                valor=random.uniform(20, 80),
                timestamp=datetime.utcnow() - timedelta(hours=i)
            )
            session.add(lectura)
        
        session.commit()
        return dispositivo

class TestConFixtures(unittest.TestCase):
    """Ejemplo de tests usando factories y fixtures"""
    
    def setUp(self):
        self.engine = TestConfig.get_test_engine()
        Base.metadata.create_all(self.engine)
        self.session = TestConfig.get_test_session(self.engine)
    
    def tearDown(self):
        self.session.close()
        Base.metadata.drop_all(self.engine)
    
    def test_usando_factory(self):
        """Test usando factory para crear datos"""
        # Usar factory para crear datos de prueba
        dispositivo = DispositivoFactory.crear_con_lecturas(self.session, 5)
        
        # Verificaciones
        self.assertEqual(len(dispositivo.lecturas), 5)
        self.assertEqual(dispositivo.tipo, "temperatura")
        
        # Verificar que las lecturas están ordenadas por tiempo
        timestamps = [l.timestamp for l in dispositivo.lecturas]
        self.assertEqual(timestamps, sorted(timestamps, reverse=True))

"""
=================================================================
3. CONFIGURACIÓN ROBUSTA PARA PRODUCCIÓN
=================================================================

🏭 CONFIGURACIÓN EMPRESARIAL
===========================

La configuración para producción debe ser:
- Segura (secrets management)
- Escalable (connection pooling)
- Monitoreable (logging detallado)
- Configurable por ambiente
- Respaldable (backup automático)
"""

import os
import logging
from logging.handlers import RotatingFileHandler
import json
from pathlib import Path
from typing import Dict, Any
from urllib.parse import quote_plus

class ConfiguracionProductiva:
    """Configuración robusta para ambiente productivo"""
    
    def __init__(self, ambiente: str = None):
        self.ambiente = ambiente or os.getenv('ENVIRONMENT', 'development')
        self.config = self._cargar_configuracion()
        self._configurar_logging()
    
    def _cargar_configuracion(self) -> Dict[str, Any]:
        """Carga configuración desde múltiples fuentes"""
        
        # 1. Configuración base
        config_base = {
            'database': {
                'pool_size': 10,
                'max_overflow': 20,
                'pool_timeout': 30,
                'pool_recycle': 3600,
                'echo': False
            },
            'logging': {
                'level': 'INFO',
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                'max_bytes': 10 * 1024 * 1024,  # 10MB
                'backup_count': 5
            },
            'security': {
                'encrypt_connection': True,
                'ssl_required': False,
                'connection_timeout': 30
            }
        }
        
        # 2. Configuración por ambiente
        config_ambiente = self._obtener_config_ambiente()
        
        # 3. Variables de entorno (override)
        config_env = self._obtener_config_env()
        
        # Merge de configuraciones (env override ambiente override base)
        config_final = {**config_base}
        self._merge_config(config_final, config_ambiente)
        self._merge_config(config_final, config_env)
        
        return config_final
    
    def _obtener_config_ambiente(self) -> Dict[str, Any]:
        """Configuración específica por ambiente"""
        
        configs = {
            'development': {
                'database': {
                    'url': 'sqlite:///desarrollo.db',
                    'echo': True,
                    'pool_size': 5
                },
                'logging': {
                    'level': 'DEBUG'
                }
            },
            'testing': {
                'database': {
                    'url': 'sqlite:///:memory:',
                    'echo': False,
                    'pool_size': 1,
                    'max_overflow': 0
                },
                'logging': {
                    'level': 'WARNING'
                }
            },
            'staging': {
                'database': {
                    'pool_size': 15,
                    'max_overflow': 25
                },
                'logging': {
                    'level': 'INFO'
                },
                'security': {
                    'ssl_required': True
                }
            },
            'production': {
                'database': {
                    'pool_size': 25,
                    'max_overflow': 50,
                    'pool_timeout': 60
                },
                'logging': {
                    'level': 'WARNING'
                },
                'security': {
                    'ssl_required': True,
                    'encrypt_connection': True
                }
            }
        }
        
        return configs.get(self.ambiente, {})
    
    def _obtener_config_env(self) -> Dict[str, Any]:
        """Configuración desde variables de entorno"""
        config = {}
        
        # Database URL desde variable de entorno
        db_url = os.getenv('DATABASE_URL')
        if db_url:
            config['database'] = {'url': db_url}
        
        # Configuración de pool desde env
        pool_size = os.getenv('DB_POOL_SIZE')
        if pool_size:
            config.setdefault('database', {})['pool_size'] = int(pool_size)
        
        # Logging level desde env
        log_level = os.getenv('LOG_LEVEL')
        if log_level:
            config['logging'] = {'level': log_level.upper()}
        
        return config
    
    def _merge_config(self, base: dict, update: dict):
        """Merge recursivo de configuraciones"""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._merge_config(base[key], value)
            else:
                base[key] = value
    
    def _configurar_logging(self):
        """Configura logging según ambiente"""
        log_config = self.config['logging']
        
        # Crear directorio de logs
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        
        # Configurar logger principal
        logger = logging.getLogger('industrial_system')
        logger.setLevel(getattr(logging, log_config['level']))
        
        # Handler para archivo con rotación
        file_handler = RotatingFileHandler(
            log_dir / f'industrial_{self.ambiente}.log',
            maxBytes=log_config['max_bytes'],
            backupCount=log_config['backup_count']
        )
        
        # Handler para consola
        console_handler = logging.StreamHandler()
        
        # Formatter
        formatter = logging.Formatter(log_config['format'])
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Agregar handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
        self.logger = logger
    
    def obtener_database_url(self) -> str:
        """Obtiene URL de base de datos con secrets management"""
        
        # Si ya está configurada directamente, usarla
        if 'url' in self.config['database']:
            return self.config['database']['url']
        
        # Construir URL desde componentes
        db_config = {
            'driver': os.getenv('DB_DRIVER', 'postgresql'),
            'user': os.getenv('DB_USER', 'industrial_user'),
            'password': os.getenv('DB_PASSWORD', ''),
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': os.getenv('DB_PORT', '5432'),
            'database': os.getenv('DB_NAME', 'industrial_db')
        }
        
        # URL encoding para caracteres especiales en password
        password_encoded = quote_plus(db_config['password'])
        
        url = f"{db_config['driver']}://{db_config['user']}:{password_encoded}@{db_config['host']}:{db_config['port']}/{db_config['database']}"
        
        return url
    
    def obtener_engine_config(self) -> Dict[str, Any]:
        """Configuración completa para crear engine"""
        db_config = self.config['database']
        
        engine_config = {
            'url': self.obtener_database_url(),
            'echo': db_config.get('echo', False),
            'pool_size': db_config.get('pool_size', 10),
            'max_overflow': db_config.get('max_overflow', 20),
            'pool_timeout': db_config.get('pool_timeout', 30),
            'pool_recycle': db_config.get('pool_recycle', 3600),
            'pool_pre_ping': True,  # Verificar conexiones
        }
        
        # Configuraciones SSL para producción
        if self.config['security'].get('ssl_required', False):
            engine_config['connect_args'] = {
                'sslmode': 'require',
                'connect_timeout': self.config['security'].get('connection_timeout', 30)
            }
        
        return engine_config

# ========================== PUNTO DE PAUSA 2 ==========================
print("""
🛑 PUNTO DE PAUSA 2 - TESTING Y CONFIGURACIÓN PRODUCTIVA
========================================================

He agregado hasta aquí:
✅ Testing exhaustivo de modelos ORM (Unit + Integration + Performance)
✅ Factories y fixtures para testing profesional
✅ Configuración robusta para múltiples ambientes
✅ Secrets management y variables de entorno
✅ Logging avanzado con rotación de archivos
✅ Connection pooling optimizado para producción

📋 PRÓXIMO BLOQUE FINAL INCLUIRÁ:
- Ejemplos prácticos de migraciones con Alembic
- Monitoreo y métricas de performance
- Estrategias de deployment con Docker
- CI/CD pipelines para aplicaciones SQLAlchemy
- Backup y recovery automatizado
- Cuestionario de consolidación final

💬 ¿Continúo con la sección final de Deployment y el resumen completo?
""")

def continuar_con_deployment():
    """Función placeholder para continuar con deployment"""
    return "Listo para continuar con Deployment y finalización"

if __name__ == "__main__":
    print("🐍🔧 MÓDULO 3.3 PARTE 4: TESTING Y CONFIGURACIÓN COMPLETADOS")
    print("=" * 65)
    print("🧪 Testing exhaustivo implementado")
    print("🏭 Configuración productiva lista")
    print("🛑 Esperando confirmación para la sección final...")

# ========================== SECCIÓN FINAL - DEPLOYMENT Y CONSOLIDACIÓN ==========================

"""
=================================================================
4. EJEMPLOS PRÁCTICOS DE MIGRACIONES CON ALEMBIC
=================================================================

🔄 WORKFLOW COMPLETO DE MIGRACIONES
==================================

Aquí demostramos un flujo completo de migraciones desde el setup
inicial hasta la evolución del esquema en producción.
"""

class EjemplosMigracionesAlembic:
    """Ejemplos prácticos paso a paso de migraciones con Alembic"""
    
    def __init__(self, directorio_proyecto: str = "."):
        self.directorio_proyecto = directorio_proyecto
        self.archivo_alembic_ini = "alembic.ini"
        self.directorio_alembic = "alembic"
    
    def setup_inicial_alembic(self):
        """Setup inicial completo de Alembic"""
        
        print("🔧 SETUP INICIAL DE ALEMBIC")
        print("=" * 40)
        
        comandos = [
            "# 1. Instalar Alembic",
            "pip install alembic",
            "",
            "# 2. Inicializar Alembic en el proyecto",
            "alembic init alembic",
            "",
            "# 3. Configurar alembic.ini",
            "# Editar sqlalchemy.url en alembic.ini",
            "",
            "# 4. Configurar env.py",
            "# Importar modelos y configurar target_metadata"
        ]
        
        for comando in comandos:
            print(f"💻 {comando}")
        
        print("\n📁 ESTRUCTURA RESULTANTE:")
        estructura = """
        proyecto/
        ├── alembic/
        │   ├── env.py              # Configuración del entorno
        │   ├── script.py.mako      # Template para migraciones
        │   └── versions/           # Archivos de migración
        ├── alembic.ini             # Configuración principal
        ├── models.py               # Modelos SQLAlchemy
        └── main.py                 # Aplicación principal
        """
        print(estructura)
    
    def ejemplo_migracion_inicial(self):
        """Ejemplo de primera migración"""
        
        print("\n🚀 PRIMERA MIGRACIÓN: CREAR ESQUEMA INICIAL")
        print("=" * 50)
        
        print("📋 MODELOS INICIALES:")
        modelos_iniciales = '''
# models.py
class DispositivoIndustrial(Base):
    __tablename__ = 'dispositivos_industriales'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    fecha_instalacion = Column(DateTime, default=datetime.utcnow)
    activo = Column(Boolean, default=True)

class LecturaDispositivo(Base):
    __tablename__ = 'lecturas_dispositivos'
    
    id = Column(Integer, primary_key=True)
    dispositivo_id = Column(Integer, ForeignKey('dispositivos_industriales.id'))
    valor = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
        '''
        print(modelos_iniciales)
        
        print("\n💻 COMANDOS DE MIGRACIÓN:")
        comandos_migracion = [
            "# Generar migración inicial automáticamente",
            "alembic revision --autogenerate -m 'Initial migration: dispositivos y lecturas'",
            "",
            "# Aplicar migración",
            "alembic upgrade head",
            "",
            "# Verificar estado actual",
            "alembic current",
            "",
            "# Ver historial de migraciones",
            "alembic history"
        ]
        
        for comando in comandos_migracion:
            print(f"  {comando}")
    
    def ejemplo_migracion_evolutiva(self):
        """Ejemplo de migración evolutiva"""
        
        print("\n🔄 MIGRACIÓN EVOLUTIVA: AGREGAR NUEVAS FUNCIONALIDADES")
        print("=" * 60)
        
        print("📋 CAMBIOS EN MODELOS:")
        cambios = '''
# Agregar campos a DispositivoIndustrial
class DispositivoIndustrial(Base):
    # ...campos existentes...
    numero_serie = Column(String(100), unique=True)  # NUEVO
    fabricante = Column(String(100))                  # NUEVO
    modelo = Column(String(100))                      # NUEVO

# Nuevo modelo: Alarmas
class AlarmaDispositivo(Base):                        # NUEVO MODELO
    __tablename__ = 'alarmas_dispositivos'
    
    id = Column(Integer, primary_key=True)
    dispositivo_id = Column(Integer, ForeignKey('dispositivos_industriales.id'))
    tipo_alarma = Column(String(50), nullable=False)
    mensaje = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
    reconocida = Column(Boolean, default=False)
        '''
        print(cambios)
        
        print("\n💻 PROCESO DE MIGRACIÓN:")
        proceso = [
            "# 1. Generar migración automática",
            "alembic revision --autogenerate -m 'Add device metadata and alarms table'",
            "",
            "# 2. Revisar archivo de migración generado",
            "# Verificar que Alembic detectó todos los cambios",
            "",
            "# 3. Aplicar migración",
            "alembic upgrade head",
            "",
            "# 4. Verificar en base de datos",
            "# Confirmar que se agregaron columnas y tabla"
        ]
        
        for paso in proceso:
            print(f"  {paso}")
    
    def ejemplo_migracion_con_datos(self):
        """Ejemplo de migración que requiere manejo de datos"""
        
        print("\n📊 MIGRACIÓN CON TRANSFORMACIÓN DE DATOS")
        print("=" * 50)
        
        print("🎯 ESCENARIO: Separar ubicación en ubicacion_planta y ubicacion_area")
        
        migracion_compleja = '''
"""Separate ubicacion into planta and area

Revision ID: 001_separate_location
Revises: previous_revision
Create Date: 2025-07-05 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

def upgrade():
    # 1. Agregar nuevas columnas
    op.add_column('dispositivos_industriales', 
                  sa.Column('ubicacion_planta', sa.String(50)))
    op.add_column('dispositivos_industriales', 
                  sa.Column('ubicacion_area', sa.String(50)))
    
    # 2. Migrar datos existentes
    connection = op.get_bind()
    
    # Obtener datos existentes
    result = connection.execute(
        "SELECT id, ubicacion FROM dispositivos_industriales WHERE ubicacion IS NOT NULL"
    )
    
    # Procesar cada registro
    for row in result:
        if ' - ' in row.ubicacion:
            planta, area = row.ubicacion.split(' - ', 1)
        else:
            planta, area = row.ubicacion, 'General'
        
        # Actualizar con nuevos valores
        connection.execute(
            "UPDATE dispositivos_industriales SET ubicacion_planta = ?, ubicacion_area = ? WHERE id = ?",
            (planta, area, row.id)
        )
    
    # 3. Eliminar columna antigua (después de verificar)
    # op.drop_column('dispositivos_industriales', 'ubicacion')

def downgrade():
    # 1. Recrear columna original
    op.add_column('dispositivos_industriales', 
                  sa.Column('ubicacion', sa.String(200)))
    
    # 2. Restaurar datos
    connection = op.get_bind()
    connection.execute(
        "UPDATE dispositivos_industriales SET ubicacion = ubicacion_planta || ' - ' || ubicacion_area"
    )
    
    # 3. Eliminar nuevas columnas
    op.drop_column('dispositivos_industriales', 'ubicacion_area')
    op.drop_column('dispositivos_industriales', 'ubicacion_planta')
        '''
        print(migracion_compleja)
    
    def estrategias_deployment(self):
        """Estrategias de deployment con migraciones"""
        
        print("\n🚀 ESTRATEGIAS DE DEPLOYMENT CON MIGRACIONES")
        print("=" * 55)
        
        estrategias = {
            "Blue-Green Deployment": [
                "1. Preparar entorno green con nueva versión",
                "2. Aplicar migraciones en green: alembic upgrade head",
                "3. Verificar funcionamiento completo",
                "4. Cambiar tráfico de blue a green",
                "5. Mantener blue como fallback"
            ],
            "Rolling Deployment": [
                "1. Aplicar migraciones compatibles hacia atrás",
                "2. Desplegar aplicación nodo por nodo",
                "3. Verificar cada nodo antes del siguiente",
                "4. Aplicar migraciones no compatibles al final"
            ],
            "Canary Deployment": [
                "1. Aplicar migraciones en subset de datos",
                "2. Desplegar a pequeño porcentaje de usuarios",
                "3. Monitorear métricas de performance/errores",
                "4. Escalar gradualmente si todo está bien"
            ]
        }
        
        for estrategia, pasos in estrategias.items():
            print(f"\n📋 {estrategia}:")
            for paso in pasos:
                print(f"  {paso}")

"""
=================================================================
5. MONITOREO Y MÉTRICAS AVANZADAS
=================================================================

🔍 MONITOREO INTEGRAL DE APLICACIONES SQLALCHEMY
===============================================

El monitoreo en producción es crítico para detectar problemas
antes de que afecten a los usuarios.
"""

import time
import psutil
from functools import wraps
from collections import defaultdict
import json
from datetime import datetime

class MonitoreoSQLAlchemy:
    """Sistema de monitoreo completo para aplicaciones SQLAlchemy"""
    
    def __init__(self):
        self.metricas = defaultdict(list)
        self.alertas_configuradas = {}
        self.umbral_query_lenta = 1.0  # segundos
        self.logger = self._configurar_logger()
    
    def _configurar_logger(self):
        """Configurar logger específico para monitoreo"""
        import logging
        
        logger = logging.getLogger('sqlalchemy_monitor')
        logger.setLevel(logging.INFO)
        
        # Handler para métricas
        handler = logging.FileHandler('logs/sqlalchemy_metrics.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def monitor_query_performance(self, func):
        """Decorator para monitorear performance de queries"""
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            
            try:
                resultado = func(*args, **kwargs)
                exito = True
                error = None
            except Exception as e:
                resultado = None
                exito = False
                error = str(e)
            
            end_time = time.time()
            duracion = end_time - start_time
            
            # Registrar métrica
            metrica = {
                'funcion': func.__name__,
                'duracion': duracion,
                'timestamp': datetime.utcnow().isoformat(),
                'exito': exito,
                'error': error
            }
            
            self.metricas['queries'].append(metrica)
            
            # Log si es query lenta
            if duracion > self.umbral_query_lenta:
                self.logger.warning(f"Query lenta detectada: {func.__name__} tomó {duracion:.2f}s")
            
            # Alerta si hay error
            if not exito:
                self.logger.error(f"Error en query {func.__name__}: {error}")
                self._enviar_alerta('query_error', metrica)
            
            if exito:
                return resultado
            else:
                raise Exception(error)
        
        return wrapper
    
    def monitor_connection_pool(self, engine):
        """Monitorea el estado del connection pool"""
        
        pool = engine.pool
        
        metrica_pool = {
            'timestamp': datetime.utcnow().isoformat(),
            'pool_size': pool.size(),
            'checked_out_connections': pool.checkedout(),
            'overflow_connections': pool.overflow(),
            'invalid_connections': pool.invalidated()
        }
        
        self.metricas['connection_pool'].append(metrica_pool)
        
        # Alertas por uso excesivo del pool
        if pool.checkedout() > pool.size() * 0.8:
            self.logger.warning(f"Pool de conexiones al 80%: {pool.checkedout()}/{pool.size()}")
        
        return metrica_pool
    
    def monitor_system_resources(self):
        """Monitorea recursos del sistema"""
        
        metrica_sistema = {
            'timestamp': datetime.utcnow().isoformat(),
            'cpu_percent': psutil.cpu_percent(interval=1),
            'memory_percent': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'active_connections': len(psutil.net_connections())
        }
        
        self.metricas['system'].append(metrica_sistema)
        
        # Alertas por recursos críticos
        if metrica_sistema['memory_percent'] > 85:
            self._enviar_alerta('high_memory', metrica_sistema)
        
        if metrica_sistema['cpu_percent'] > 90:
            self._enviar_alerta('high_cpu', metrica_sistema)
        
        return metrica_sistema
    
    def _enviar_alerta(self, tipo_alerta: str, datos: dict):
        """Envía alertas críticas"""
        
        alerta = {
            'tipo': tipo_alerta,
            'timestamp': datetime.utcnow().isoformat(),
            'datos': datos,
            'severidad': 'CRITICAL' if tipo_alerta in ['query_error', 'high_memory'] else 'WARNING'
        }
        
        # Log de la alerta
        self.logger.critical(f"ALERTA {tipo_alerta}: {json.dumps(alerta, indent=2)}")
        
        # Aquí se integraría con sistemas de alertas (Slack, email, PagerDuty, etc.)
        print(f"🚨 ALERTA {alerta['severidad']}: {tipo_alerta}")
    
    def generar_reporte_metricas(self):
        """Genera reporte completo de métricas"""
        
        print("📊 REPORTE DE MÉTRICAS SQLALCHEMY")
        print("=" * 50)
        
        # Métricas de queries
        if self.metricas['queries']:
            queries = self.metricas['queries']
            duraciones = [q['duracion'] for q in queries if q['exito']]
            
            print(f"\n🔍 QUERIES ({len(queries)} ejecutadas):")
            print(f"  ✅ Exitosas: {sum(1 for q in queries if q['exito'])}")
            print(f"  ❌ Fallidas: {sum(1 for q in queries if not q['exito'])}")
            
            if duraciones:
                print(f"  ⏱️ Duración promedio: {sum(duraciones)/len(duraciones):.3f}s")
                print(f"  🐌 Query más lenta: {max(duraciones):.3f}s")
                print(f"  ⚡ Query más rápida: {min(duraciones):.3f}s")
        
        # Métricas de connection pool
        if self.metricas['connection_pool']:
            ultima_pool = self.metricas['connection_pool'][-1]
            print(f"\n🔗 CONNECTION POOL:")
            print(f"  📊 Tamaño del pool: {ultima_pool['pool_size']}")
            print(f"  🔓 Conexiones activas: {ultima_pool['checked_out_connections']}")
            print(f"  ➕ Conexiones overflow: {ultima_pool['overflow_connections']}")
        
        # Métricas del sistema
        if self.metricas['system']:
            ultima_sistema = self.metricas['system'][-1]
            print(f"\n💻 RECURSOS DEL SISTEMA:")
            print(f"  🧠 CPU: {ultima_sistema['cpu_percent']:.1f}%")
            print(f"  💾 Memoria: {ultima_sistema['memory_percent']:.1f}%")
            print(f"  💿 Disco: {ultima_sistema['disk_usage']:.1f}%")
        
        return self.metricas

# Ejemplo de uso del monitoreo
def ejemplo_uso_monitoreo():
    """Ejemplo práctico de monitoreo en acción"""
    
    print("\n🔍 EJEMPLO DE MONITOREO EN ACCIÓN")
    print("=" * 45)
    
    # Crear instancia de monitoreo
    monitor = MonitoreoSQLAlchemy()
    
    # Función de ejemplo que simula operaciones de BD
    @monitor.monitor_query_performance
    def consulta_compleja_simulada():
        """Simula una consulta compleja"""
        import time
        time.sleep(0.5)  # Simular procesamiento
        return "Resultados de consulta"
    
    @monitor.monitor_query_performance  
    def consulta_lenta_simulada():
        """Simula una consulta lenta"""
        import time
        time.sleep(1.5)  # Simular consulta lenta
        return "Resultados de consulta lenta"
    
    @monitor.monitor_query_performance
    def consulta_con_error():
        """Simula una consulta que falla"""
        raise Exception("Error simulado de conexión")
    
    # Ejecutar consultas monitoreadas
    print("💻 Ejecutando consultas monitoreadas...")
    
    try:
        consulta_compleja_simulada()
        print("  ✅ Consulta compleja ejecutada")
    except:
        print("  ❌ Error en consulta compleja")
    
    try:
        consulta_lenta_simulada()
        print("  🐌 Consulta lenta ejecutada")
    except:
        print("  ❌ Error en consulta lenta")
    
    try:
        consulta_con_error()
        print("  ✅ Consulta con error ejecutada")
    except:
        print("  ❌ Error capturado correctamente")
    
    # Monitorear recursos del sistema
    monitor.monitor_system_resources()
    
    # Generar reporte
    print("\n📊 GENERANDO REPORTE DE MÉTRICAS:")
    monitor.generar_reporte_metricas()

"""
=================================================================
6. DEPLOYMENT CON DOCKER Y CI/CD
=================================================================

🐳 CONTAINERIZACIÓN PARA PRODUCCIÓN
===================================

Docker permite deployments consistentes y escalables de aplicaciones
SQLAlchemy en cualquier ambiente.
"""

def generar_dockerfile_sqlalchemy():
    """Genera Dockerfile optimizado para aplicaciones SQLAlchemy"""
    
    dockerfile_content = '''
# Dockerfile para aplicación SQLAlchemy
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \\
    gcc \\
    libpq-dev \\
    && rm -rf /var/lib/apt/lists/*

# Crear usuario no-root para seguridad
RUN useradd --create-home --shell /bin/bash app

# Directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código de la aplicación
COPY . .

# Cambiar propietario de archivos al usuario app
RUN chown -R app:app /app

# Cambiar a usuario no-root
USER app

# Variables de entorno
ENV PYTHONPATH=/app
ENV ENVIRONMENT=production

# Exponer puerto
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \\
    CMD python -c "import requests; requests.get('http://localhost:8000/health')"

# Comando por defecto
CMD ["python", "main.py"]
    '''
    
    print("🐳 DOCKERFILE PARA SQLALCHEMY:")
    print(dockerfile_content)
    
    return dockerfile_content

def generar_docker_compose():
    """Genera docker-compose.yml para ambiente completo"""
    
    docker_compose_content = '''
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://industrial_user:secure_password@postgres:5432/industrial_db
      - ENVIRONMENT=production
      - LOG_LEVEL=INFO
    depends_on:
      postgres:
        condition: service_healthy
    volumes:
      - ./logs:/app/logs
    restart: unless-stopped

  postgres:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=industrial_db
      - POSTGRES_USER=industrial_user
      - POSTGRES_PASSWORD=secure_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init-scripts:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U industrial_user -d industrial_db"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - app
    restart: unless-stopped

volumes:
  postgres_data:
  redis_data:
    '''
    
    print("🐙 DOCKER-COMPOSE PARA STACK COMPLETO:")
    print(docker_compose_content)
    
    return docker_compose_content

def generar_pipeline_ci_cd():
    """Genera pipeline CI/CD para GitHub Actions"""
    
    github_actions_content = '''
name: CI/CD Pipeline SQLAlchemy App

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test_db

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: postgres
          POSTGRES_DB: test_db
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5
        ports:
          - 5432:5432

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
        
    - name: Cache pip dependencies
      uses: actions/cache@v3
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
        
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
        
    - name: Run migrations
      run: |
        alembic upgrade head
        
    - name: Run tests
      run: |
        pytest --cov=. --cov-report=xml --cov-report=html
        
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  security-scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Run Bandit Security Scan
      run: |
        pip install bandit
        bandit -r . -f json -o bandit-report.json

  build-and-deploy:
    needs: [test, security-scan]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build Docker image
      run: |
        docker build -t industrial-app:${{ github.sha }} .
        
    - name: Run container tests
      run: |
        docker run --rm industrial-app:${{ github.sha }} python -m pytest
        
    - name: Deploy to staging
      if: github.ref == 'refs/heads/main'
      run: |
        echo "Deploying to staging environment"
        # Aquí irían los comandos específicos de deployment
        
    - name: Run smoke tests
      run: |
        echo "Running smoke tests against staging"
        # Pruebas básicas de funcionamiento
    '''
    
    print("🔄 PIPELINE CI/CD GITHUB ACTIONS:")
    print(github_actions_content)
    
    return github_actions_content

"""
=================================================================
7. CUESTIONARIO FINAL Y CONSOLIDACIÓN COMPLETA
=================================================================
"""

def cuestionario_final_modulo_33():
    """Cuestionario completo del Módulo 3.3"""
    
    print("📝 CUESTIONARIO FINAL - MÓDULO 3.3: ORM CON SQLALCHEMY")
    print("=" * 70)
    
    preguntas = {
        1: {
            'pregunta': '¿Cuál es la principal ventaja de usar SQLAlchemy ORM sobre SQL puro?',
            'opciones': [
                'a) Siempre es más rápido que SQL puro',
                'b) Abstracción orientada a objetos y portabilidad entre BD',
                'c) Usa menos memoria',
                'd) No requiere conocimientos de SQL'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'SQLAlchemy ORM proporciona abstracción orientada a objetos, portabilidad entre diferentes motores de BD, y prevención automática de inyección SQL.'
        },
        2: {
            'pregunta': '¿Para qué sirven las migraciones en Alembic?',
            'opciones': [
                'a) Optimizar queries automáticamente',
                'b) Evolucionar el esquema de BD de forma controlada y versionada',
                'c) Hacer respaldos automáticos',
                'd) Monitorear performance'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'Las migraciones permiten evolucionar el esquema de la base de datos de manera controlada, versionada y reproducible entre diferentes ambientes.'
        },
        3: {
            'pregunta': '¿Cuál es el problema N+1 en ORMs y cómo se soluciona?',
            'opciones': [
                'a) Muchas conexiones simultáneas; usar connection pooling',
                'b) Una query inicial + N queries por relación; usar eager loading',
                'c) Errores de sintaxis; usar validadores',
                'd) Datos duplicados; usar constraints'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'El problema N+1 ocurre cuando se hace una query inicial y luego N queries adicionales para cargar relaciones. Se soluciona con eager loading (joinedload, selectinload).'
        },
        4: {
            'pregunta': '¿Qué estrategia de testing es más apropiada para modelos ORM complejos?',
            'opciones': [
                'a) Solo unit tests aislados',
                'b) Solo integration tests con BD real',
                'c) Combinación de unit, integration y performance tests',
                'd) Solo testing manual'
            ],
            'respuesta_correcta': 'c',
            'explicacion': 'Los modelos ORM complejos requieren una estrategia integral: unit tests para lógica individual, integration tests para relaciones, y performance tests para optimización.'
        },
        5: {
            'pregunta': '¿Cuál es la configuración más crítica para production en SQLAlchemy?',
            'opciones': [
                'a) echo=True para debugging',
                'b) Connection pooling y gestión de secretos',
                'c) Usar SQLite para simplicidad',
                'd) Deshabilitar todas las validaciones'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'En producción es crítico configurar connection pooling apropiado y gestión segura de secretos (credenciales de BD, variables de entorno).'
        },
        6: {
            'pregunta': '¿Qué herramienta es esencial para monitoreo de aplicaciones SQLAlchemy?',
            'opciones': [
                'a) Solo logs de la aplicación',
                'b) Métricas de queries, connection pool y recursos del sistema',
                'c) Solo monitoring de la base de datos',
                'd) Únicamente alertas de errores'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'Un monitoreo integral debe incluir métricas de queries (duración, errores), estado del connection pool, y recursos del sistema (CPU, memoria).'
        }
    }
    
    print("✅ RESPUESTAS CORRECTAS Y EXPLICACIONES:")
    for num, data in preguntas.items():
        print(f"\n{num}. {data['pregunta']}")
        for opcion in data['opciones']:
            marca = "✓" if opcion.startswith(data['respuesta_correcta']) else "○"
            print(f"   {marca} {opcion}")
        print(f"   💡 Explicación: {data['explicacion']}")

def checklist_consolidacion_completa():
    """Checklist completo de consolidación del Módulo 3.3"""
    
    print("\n🎯 CHECKLIST DE CONSOLIDACIÓN COMPLETA - MÓDULO 3.3")
    print("🗄️ ORM CON SQLALCHEMY - DOMINIO COMPLETO")
    print("=" * 75)
    
    secciones = {
        "PARTE 1 - FUNDAMENTOS": [
            "✅ Comprendo qué es un ORM y sus ventajas",
            "✅ Entiendo la arquitectura de SQLAlchemy",
            "✅ Conozco la diferencia entre Core y ORM",
            "✅ Domino la configuración de engines y conexiones"
        ],
        "PARTE 2 - CONFIGURACIÓN PRÁCTICA": [
            "✅ Puedo configurar SQLAlchemy desde cero",
            "✅ Domino la creación de modelos declarativos",
            "✅ Manejo sessions y transacciones correctamente",
            "✅ Implemento operaciones CRUD con ORM",
            "✅ Gestiono el ciclo de vida de objetos"
        ],
        "PARTE 3 - RELACIONES AVANZADAS": [
            "✅ Domino relaciones One-to-Many (1:N)",
            "✅ Implemento relaciones Many-to-Many (N:M)",
            "✅ Comprendo herencia de modelos",
            "✅ Optimizo consultas con eager/lazy loading",
            "✅ Realizo consultas complejas con joins",
            "✅ Uso funciones de agregación eficientemente"
        ],
        "PARTE 4 - PRODUCCIÓN Y TESTING": [
            "✅ Configuro migraciones con Alembic",
            "✅ Escribo tests unitarios para modelos ORM",
            "✅ Implemento tests de integración y performance",
            "✅ Configuro aplicaciones para múltiples ambientes",
            "✅ Gestiono secrets y variables de entorno",
            "✅ Implemento monitoreo y métricas",
            "✅ Configuro deployment con Docker",
            "✅ Establezco pipelines CI/CD"
        ],
        "COMPETENCIAS INDUSTRIALES": [
            "✅ Diseño sistemas industriales complejos con ORM",
            "✅ Gestiono plantas, sensores y equipos con relaciones",
            "✅ Implemento dashboards industriales avanzados",
            "✅ Optimizo performance para grandes volúmenes",
            "✅ Manejo migraciones en sistemas productivos",
            "✅ Monitoreo aplicaciones industriales críticas"
        ]
    }
    
    total_objetivos = 0
    for seccion, objetivos in secciones.items():
        print(f"\n📋 {seccion}:")
        for objetivo in objetivos:
            print(f"  {objetivo}")
        total_objetivos += len(objetivos)
    
    print(f"\n🏆 TOTAL OBJETIVOS COMPLETADOS: {total_objetivos}/{total_objetivos} (100%)")
    print("🎓 NIVEL ALCANZADO: EXPERTO EN SQLALCHEMY ORM")
    print("📈 PREPARACIÓN PARA PROYECTOS REALES: ÓPTIMA")

def resumen_final_modulo_33():
    """Resumen final completo del Módulo 3.3"""
    
    print("\n" + "="*80)
    print("🎉 MÓDULO 3.3: ORM CON SQLALCHEMY - COMPLETADO EXITOSAMENTE")
    print("="*80)
    
    print("\n🏆 LOGROS ALCANZADOS:")
    logros = [
        "🔧 Dominio completo de SQLAlchemy ORM desde fundamentos hasta producción",
        "🏗️ Implementación de sistemas industriales complejos con relaciones avanzadas",
        "🔄 Gestión profesional de migraciones con Alembic",
        "🧪 Testing exhaustivo de aplicaciones ORM (Unit + Integration + Performance)",
        "🏭 Configuración robusta para múltiples ambientes productivos",
        "📊 Monitoreo avanzado con métricas y alertas automáticas",
        "🐳 Deployment completo con Docker y CI/CD pipelines",
        "⚡ Optimización de performance para aplicaciones críticas"
    ]
    
    for logro in logros:
        print(f"  {logro}")
    
    print("\n🎯 COMPETENCIAS DESARROLLADAS:")
    competencias = [
        "🔧 TÉCNICAS: ORM avanzado, migraciones, testing, monitoreo",
        "🏭 INDUSTRIALES: Sistemas SCADA, gestión de dispositivos, dashboards",
        "💼 PROFESIONALES: Deployment, CI/CD, configuración multi-ambiente",
        "📊 ANALÍTICAS: Performance tuning, métricas, optimización"
    ]
    
    for competencia in competencias:
        print(f"  {competencia}")
    
    print("\n🚀 PREPARACIÓN PARA EL FUTURO:")
    preparacion = [
        "📈 Módulo 3.4: APIs REST con FastAPI + SQLAlchemy",
        "🔄 Módulo 3.5: Microservicios y arquitecturas distribuidas",
        "☁️ Módulo 3.6: Cloud computing y bases de datos en la nube",
        "🤖 Módulo 4.1: Machine Learning con datos industriales"
    ]
    
    for prep in preparacion:
        print(f"  {prep}")
    
    print("\n💪 ¡EXCELENTE TRABAJO!")
    print("Has dominado uno de los ORMs más potentes del ecosistema Python")
    print("y estás preparado para desarrollar aplicaciones industriales robustas.")
    
    print("\n🎓 TU NIVEL ACTUAL: EXPERTO EN SQLALCHEMY ORM")
    print("📊 PROGRESO GENERAL: AVANZADO EN GESTIÓN DE DATOS CON PYTHON")
    print("🎯 SIGUIENTE OBJETIVO: APIS Y MICROSERVICIOS INDUSTRIALES")

"""
=================================================================
FUNCIÓN PRINCIPAL DE DEMOSTRACIÓN COMPLETA
================================================================="""

def main_demo_completa_parte4():
    """Demostración completa de la Parte 4 final"""
    
    print("🐍🔧 MÓDULO 3.3 PARTE 4: DEMOSTRACIÓN FINAL COMPLETA")
    print("🚀 MIGRACIONES, TESTING, PRODUCCIÓN Y DEPLOYMENT")
    print("=" * 80)
    
    try:
        # 1. Ejemplos de migraciones
        print("\n1️⃣ EJEMPLOS PRÁCTICOS DE MIGRACIONES CON ALEMBIC")
        print("=" * 55)
        ejemplos_migraciones = EjemplosMigracionesAlembic()
        ejemplos_migraciones.setup_inicial_alembic()
        ejemplos_migraciones.ejemplo_migracion_inicial()
        ejemplos_migraciones.ejemplo_migracion_evolutiva()
        ejemplos_migraciones.ejemplo_migracion_con_datos()
        ejemplos_migraciones.estrategias_deployment()
        
        # 2. Monitoreo en acción
        print("\n2️⃣ MONITOREO Y MÉTRICAS AVANZADAS")
        print("=" * 45)
        ejemplo_uso_monitoreo()
        
        # 3. Configuración de deployment
        print("\n3️⃣ CONFIGURACIÓN DE DEPLOYMENT")
        print("=" * 40)
        generar_dockerfile_sqlalchemy()
        generar_docker_compose()
        generar_pipeline_ci_cd()
        
        # 4. Evaluación final
        print("\n4️⃣ EVALUACIÓN Y CONSOLIDACIÓN FINAL")
        print("=" * 45)
        cuestionario_final_modulo_33()
        checklist_consolidacion_completa()
        
        # 5. Resumen final
        resumen_final_modulo_33()
        
        print("\n" + "="*80)
        print("🎉 ¡MÓDULO 3.3 COMPLETAMENTE FINALIZADO!")
        print("🏆 SQLALCHEMY ORM DOMINADO AL NIVEL EXPERTO")
        print("🚀 LISTO PARA PROYECTOS INDUSTRIALES REALES")
        print("="*80)
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error en demostración: {e}")
        print("🔧 Verifica configuración y dependencias")
        return False

if __name__ == "__main__":
    print("🐍🔧 MÓDULO 3.3 PARTE 4: SECCIÓN FINAL")
    print("=" * 50)
    print("🚀 Deployment, Monitoreo y Consolidación")
    print("🎯 Preparación completa para producción")
    main_demo_completa_parte4()
