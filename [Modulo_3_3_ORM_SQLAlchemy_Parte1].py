"""
🗄️🔗 MÓDULO 3.3: ORM CON SQLALCHEMY - PARTE 1
📊 Maestría en Python - Fase 3: Object-Relational Mapping

=================================================================
OBJETIVO PRINCIPAL: Dominar SQLAlchemy como ORM profesional
=================================================================

Este módulo introduce SQLAlchemy, el ORM más poderoso de Python,
para crear aplicaciones industriales robustas con mapeo objeto-relacional
que elimine la necesidad de escribir SQL manualmente.

🎯 OBJETIVOS ESPECÍFICOS DEL MÓDULO 3.3:
========================================

1. CONFIGURACIÓN PROFESIONAL DE SQLALCHEMY
   - Instalación y setup del entorno
   - Configuración de engines y conexiones
   - Manejo de diferentes bases de datos

2. MODELOS DECLARATIVOS
   - Definición de clases modelo
   - Tipos de datos SQLAlchemy
   - Relaciones entre modelos
   - Constraints y validaciones

3. OPERACIONES CRUD CON ORM
   - Sessions y transacciones
   - Consultas con query API
   - Inserción, actualización y eliminación
   - Manejo avanzado de relaciones

4. MIGRACIONES Y VERSIONADO
   - Alembic para migraciones automáticas
   - Evolución del esquema de base de datos
   - Control de versiones del schema

5. OPTIMIZACIÓN Y PERFORMANCE
   - Lazy vs Eager loading
   - Consultas complejas optimizadas
   - Connection pooling
   - Debugging de consultas

=================================================================
PARTE 1: FUNDAMENTOS TEÓRICOS Y CONFIGURACIÓN
=================================================================

📚 ¿QUÉ ES UN ORM?
==================

ORM (Object-Relational Mapping) es una técnica que permite:

✅ VENTAJAS:
- Trabajar con objetos Python en lugar de SQL puro
- Portabilidad entre diferentes bases de datos
- Validación automática de datos
- Prevención de inyección SQL
- Mantenimiento más fácil del código
- Migraciones automáticas del esquema

⚠️ CONSIDERACIONES:
- Curva de aprendizaje inicial
- Overhead de performance en casos específicos
- Abstracción que puede ocultar detalles SQL

🔧 ¿POR QUÉ SQLALCHEMY?
=======================

SQLAlchemy es considerado el ORM más maduro y potente de Python:

🏆 FORTALEZAS:
- Arquitectura flexible y modular
- Core de bajo nivel + ORM de alto nivel
- Soporte excepcional para relaciones complejas
- Pool de conexiones avanzado
- Compatibilidad con múltiples motores de BD
- Comunidad muy activa y documentación excelente

🏭 CASOS DE USO INDUSTRIALES:
- Sistemas SCADA con múltiples fuentes de datos
- Aplicaciones web robustas con Flask/FastAPI
- Pipelines de datos ETL complejos
- Sistemas de monitoreo en tiempo real
- APIs empresariales de alta disponibilidad

=================================================================
ARQUITECTURA DE SQLALCHEMY
=================================================================

SQLAlchemy tiene una arquitectura en capas:

📊 ESQUEMA DE CAPAS:
┌─────────────────────────────────────┐
│        APLICACIÓN PYTHON            │
├─────────────────────────────────────┤
│          ORM LAYER                  │ ← Modelos, Sessions, Query API
├─────────────────────────────────────┤
│         CORE LAYER                  │ ← Expressions, Tables, MetaData
├─────────────────────────────────────┤
│      CONNECTION POOL               │ ← Gestión de conexiones
├─────────────────────────────────────┤
│         DBAPI                      │ ← Driver específico (psycopg2, etc.)
├─────────────────────────────────────┤
│      BASE DE DATOS                 │ ← PostgreSQL, MySQL, SQLite, etc.
└─────────────────────────────────────┘

🔧 COMPONENTES PRINCIPALES:
===========================

1. **ENGINE** 🚗
   - Punto central de acceso a la base de datos
   - Gestiona pool de conexiones
   - Dialecto específico para cada motor de BD

2. **METADATA** 📋
   - Catálogo de tablas y esquemas
   - Estructura de la base de datos
   - Generación automática de DDL

3. **SESSION** 🔄
   - Unidad de trabajo (Unit of Work)
   - Gestión de transacciones
   - Identity map para objetos

4. **DECLARATIVE BASE** 🏗️
   - Clase base para modelos ORM
   - Mapeo automático tabla ↔ clase
   - Definición de relaciones

=================================================================
CONFIGURACIÓN DEL ENTORNO
=================================================================

📦 INSTALACIÓN DE DEPENDENCIAS:
===============================

Para este módulo necesitamos instalar SQLAlchemy y dependencias:

```bash
# Entorno virtual recomendado
python -m venv venv_sqlalchemy
source venv_sqlalchemy/bin/activate  # Linux/Mac
# o
venv_sqlalchemy\\Scripts\\activate   # Windows

# Instalación base de SQLAlchemy
pip install sqlalchemy

# Para diferentes motores de base de datos:
pip install sqlalchemy[postgresql]  # PostgreSQL
pip install sqlalchemy[mysql]       # MySQL
pip install sqlalchemy[oracle]      # Oracle

# Para migraciones (Alembic)
pip install alembic

# Para desarrollo y testing
pip install sqlalchemy[dev]
```

🗃️ MOTORES DE BASE DE DATOS SOPORTADOS:
=======================================

SQLAlchemy soporta múltiples motores:

1. **SQLite** (incluido en Python)
   - Ideal para desarrollo y testing
   - No requiere servidor
   - URL: `sqlite:///archivo.db`

2. **PostgreSQL** (recomendado para producción)
   - Open source y muy robusto
   - Excelente para aplicaciones complejas
   - URL: `postgresql://usuario:password@host:puerto/database`

3. **MySQL/MariaDB**
   - Ampliamente utilizado
   - Buena performance
   - URL: `mysql://usuario:password@host:puerto/database`

4. **SQL Server**
   - Para entornos empresariales Microsoft
   - URL: `mssql+pyodbc://usuario:password@dsn`

5. **Oracle**
   - Para aplicaciones empresariales grandes
   - URL: `oracle://usuario:password@host:puerto/database`

=================================================================
PRIMEROS CONCEPTOS CLAVE
=================================================================

🔧 ENGINE - EL CORAZÓN DE SQLALCHEMY:
====================================

El Engine es el punto central que:
- Gestiona conexiones a la base de datos
- Mantiene un pool de conexiones reutilizables
- Traduce instrucciones SQL al dialecto específico
- Maneja transacciones automáticamente

Ejemplo básico de configuración:

```python
from sqlalchemy import create_engine

# SQLite para desarrollo
engine = create_engine('sqlite:///industrial.db', echo=True)

# PostgreSQL para producción
engine = create_engine(
    'postgresql://user:password@localhost:5432/industrial_db',
    pool_size=20,
    max_overflow=30,
    echo=False  # No mostrar SQL en producción
)
```

🗂️ DECLARATIVE BASE:
====================

Base clase que permite definir modelos como clases Python:

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Sensor(Base):
    __tablename__ = 'sensores'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    tipo = Column(String(30), nullable=False)
    ubicacion = Column(String(100))
```

🔄 SESSION - UNIDAD DE TRABAJO:
===============================

Session gestiona el ciclo de vida de los objetos:
- Tracking de cambios en objetos
- Lazy loading de relaciones
- Transacciones automáticas
- Identity map (un objeto = una instancia)

```python
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Uso básico
sensor = Sensor(nombre='TEMP_01', tipo='temperatura')
session.add(sensor)
session.commit()
```

=================================================================
COMPARACIÓN: SQL PURO VS SQLALCHEMY
=================================================================

📊 EJEMPLO COMPARATIVO:
=======================

**CON SQL PURO (Módulo 3.2):**
```python
import sqlite3

conn = sqlite3.connect('industrial.db')
cursor = conn.cursor()

# Crear tabla
cursor.execute('''
    CREATE TABLE sensores (
        id INTEGER PRIMARY KEY,
        nombre TEXT UNIQUE NOT NULL,
        tipo TEXT NOT NULL,
        valor REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Insertar datos
cursor.execute(
    "INSERT INTO sensores (nombre, tipo, valor) VALUES (?, ?, ?)",
    ('TEMP_01', 'temperatura', 25.5)
)

# Consultar
cursor.execute("SELECT * FROM sensores WHERE tipo = ?", ('temperatura',))
resultados = cursor.fetchall()

conn.commit()
conn.close()
```

**CON SQLALCHEMY ORM:**
```python
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Configuración
engine = create_engine('sqlite:///industrial.db')
Base = declarative_base()

# Modelo
class Sensor(Base):
    __tablename__ = 'sensores'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    tipo = Column(String(30), nullable=False)
    valor = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Crear tablas
Base.metadata.create_all(engine)

# Sesión
Session = sessionmaker(bind=engine)
session = Session()

# Insertar (más intuitivo)
sensor = Sensor(nombre='TEMP_01', tipo='temperatura', valor=25.5)
session.add(sensor)
session.commit()

# Consultar (orientado a objetos)
sensores_temp = session.query(Sensor).filter(
    Sensor.tipo == 'temperatura'
).all()

session.close()
```

📈 VENTAJAS EVIDENTES DEL ORM:
=============================

1. **Código más legible y mantenible**
2. **Validación automática de tipos**
3. **Prevención de inyección SQL**
4. **Portabilidad entre diferentes BD**
5. **Gestión automática de conexiones**
6. **Relaciones complejas simplificadas**

=================================================================
CASOS DE USO INDUSTRIALES ESPECÍFICOS
=================================================================

🏭 ESCENARIOS DONDE SQLALCHEMY BRILLA:
======================================

1. **SISTEMAS SCADA COMPLEJOS**
   - Múltiples tipos de sensores con relaciones
   - Históricos con millones de registros
   - Alarmas y eventos correlacionados

2. **APIS DE AUTOMATIZACIÓN**
   - Endpoints RESTful para múltiples dispositivos
   - Validación de datos de entrada
   - Respuestas JSON automáticas

3. **DASHBOARDS EN TIEMPO REAL**
   - Consultas optimizadas para visualización
   - Agregaciones complejas de datos
   - Filtros dinámicos avanzados

4. **INTEGRACIÓN DE SISTEMAS**
   - ETL entre diferentes fuentes de datos
   - Sincronización entre bases de datos
   - Migración de sistemas legacy

=================================================================
PRÓXIMOS PASOS EN ESTE MÓDULO
=================================================================

🗺️ ROADMAP DE APRENDIZAJE:
==========================

**PARTE 2: Configuración Práctica y Primer Modelo**
- Instalación del entorno completo
- Configuración de engine y sesiones
- Primer modelo de sensor industrial

**PARTE 3: Modelos Avanzados y Relaciones**
- Relaciones One-to-Many y Many-to-Many
- Modelos para sistema industrial completo
- Constraints y validaciones

**PARTE 4: Operaciones CRUD Avanzadas**
- Query API completo
- Joins y subconsultas con ORM
- Bulk operations para performance

**PARTE 5: Migraciones con Alembic**
- Setup de Alembic
- Creación y aplicación de migraciones
- Versionado del esquema

**PARTE 6: Optimización y Performance**
- Eager vs Lazy loading
- Query optimization
- Connection pooling avanzado

**PARTE 7: Proyecto Integrador**
- Sistema completo de gestión de dispositivos
- API REST con SQLAlchemy
- Dashboard con datos en tiempo real

=================================================================
PREPARACIÓN MENTAL PARA EL CAMBIO DE PARADIGMA
=================================================================

🧠 MINDSET IMPORTANTE:
=====================

**DESDE:** "Pienso en tablas y consultas SQL"
**HACIA:** "Pienso en objetos Python y sus relaciones"

**DESDE:** "Escribo queries manualmente"
**HACIA:** "Defino modelos y dejo que el ORM genere SQL"

**DESDE:** "Gestiono conexiones manualmente"
**HACIA:** "El ORM gestiona todo transparentemente"

Este cambio mental es fundamental para aprovechar al máximo SQLAlchemy.

=================================================================
¿ESTÁS LISTO PARA LA PARTE 2?
=================================================================

En la Parte 2 vamos a:
✅ Configurar el entorno completo
✅ Crear nuestro primer engine y sesión
✅ Definir el primer modelo industrial
✅ Ejecutar operaciones básicas

💬 **¿Confirmas que esta base teórica está clara y quieres continuar con la configuración práctica?**

"""

if __name__ == "__main__":
    print("🗄️🔗 MÓDULO 3.3: ORM CON SQLALCHEMY - PARTE 1")
    print("=" * 60)
    print("📚 Fundamentos teóricos y conceptos clave del ORM")
    print("🎯 Base sólida para configuración práctica")
    print("💡 ¿Listo para la Parte 2?")
