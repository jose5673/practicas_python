"""
🐍🗄️ MÓDULO 3.3: ORM CON SQLALCHEMY - PARTE 3
📊 MODELOS AVANZADOS Y RELACIONES COMPLEJAS
📈 Maestría en Python - Fase 3: Gestión Avanzada de Datos

=================================================================
OBJETIVO PRINCIPAL: Dominar relaciones complejas y consultas avanzadas con SQLAlchemy ORM
=================================================================

Esta parte del módulo 3.3 se enfoca en las capacidades avanzadas de SQLAlchemy:
- Relaciones One-to-Many y Many-to-Many
- Herencia de modelos
- Consultas complejas y optimización
- Lazy loading vs Eager loading
- Transacciones avanzadas
- Casos de uso industriales complejos

📋 CONTENIDO DE LA PARTE 3:
=========================

1. RELACIONES ENTRE MODELOS
   - One-to-Many (1:N)
   - Many-to-Many (N:M)
   - One-to-One (1:1)
   - Self-referencing relationships

2. HERENCIA DE MODELOS
   - Single Table Inheritance
   - Joined Table Inheritance
   - Concrete Table Inheritance

3. CONSULTAS AVANZADAS
   - Joins complejos
   - Subconsultas
   - Funciones de agregación
   - Window functions

4. OPTIMIZACIÓN DE PERFORMANCE
   - Lazy vs Eager loading
   - Query optimization
   - Índices personalizados
   - Bulk operations

5. TRANSACCIONES AVANZADAS
   - ACID properties
   - Savepoints
   - Rollback strategies
   - Connection pooling

=================================================================
TEORÍA FUNDAMENTAL: RELACIONES EN ORM
=================================================================

Las relaciones son la esencia de las bases de datos relacionales.
SQLAlchemy ORM proporciona una abstracción poderosa para manejar
estas relaciones de manera intuitiva y eficiente.

"""

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Table, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, joinedload, selectinload, Session
from sqlalchemy.sql import func
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import enum
from contextlib import contextmanager

# Configuración base
Base = declarative_base()
engine = create_engine('sqlite:///sistema_industrial_avanzado.db', echo=False)
Session = sessionmaker(bind=engine)

"""
=================================================================
1. RELACIONES ONE-TO-MANY (1:N)
=================================================================

La relación más común en sistemas industriales: un elemento padre
puede tener múltiples elementos hijos.

Ejemplo: Una Planta Industrial tiene múltiples Sensores
"""

class PlantaIndustrial(Base):
    """Modelo de Planta Industrial - Lado 'One' de la relación"""
    __tablename__ = 'plantas_industriales'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    ubicacion = Column(String(200))
    tipo_industria = Column(String(50))
    capacidad_produccion = Column(Float)
    fecha_inauguracion = Column(DateTime)
    activa = Column(Boolean, default=True)
    
    # Relación One-to-Many: Una planta tiene muchos sensores
    sensores = relationship("SensorAvanzado", back_populates="planta", cascade="all, delete-orphan")
    # cascade="all, delete-orphan" significa que si eliminas la planta, se eliminan todos sus sensores
    
    # Relación One-to-Many: Una planta tiene muchas líneas de producción
    lineas_produccion = relationship("LineaProduccion", back_populates="planta")
    
    def __repr__(self):
        return f"<PlantaIndustrial(nombre='{self.nombre}', sensores={len(self.sensores)})>"

class SensorAvanzado(Base):
    """Modelo de Sensor - Lado 'Many' de la relación"""
    __tablename__ = 'sensores_avanzados'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50))
    ubicacion_especifica = Column(String(200))
    unidad_medida = Column(String(20))
    valor_min = Column(Float)
    valor_max = Column(Float)
    precision = Column(Float, default=0.01)
    frecuencia_lectura = Column(Integer, default=60)  # segundos
    
    # Foreign Key hacia la planta
    planta_id = Column(Integer, ForeignKey('plantas_industriales.id'), nullable=False)
    
    # Relación Many-to-One: Muchos sensores pertenecen a una planta
    planta = relationship("PlantaIndustrial", back_populates="sensores")
    
    # Relación One-to-Many: Un sensor tiene muchas lecturas
    lecturas = relationship("LecturaAvanzada", back_populates="sensor", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<SensorAvanzado(nombre='{self.nombre}', planta='{self.planta.nombre if self.planta else None}')>"

"""
=================================================================
2. RELACIONES MANY-TO-MANY (N:M)
=================================================================

Cuando ambos lados de la relación pueden tener múltiples elementos
del otro lado. Requiere una tabla de asociación.

Ejemplo: Técnicos pueden trabajar en múltiples Plantas,
y una Planta puede tener múltiples Técnicos
"""

# Tabla de asociación para la relación Many-to-Many
tecnico_planta_asociacion = Table(
    'tecnico_planta',
    Base.metadata,
    Column('tecnico_id', Integer, ForeignKey('tecnicos.id'), primary_key=True),
    Column('planta_id', Integer, ForeignKey('plantas_industriales.id'), primary_key=True),
    Column('fecha_asignacion', DateTime, default=datetime.utcnow),
    Column('rol_en_planta', String(50), default='Técnico General')
)

class Tecnico(Base):
    """Modelo de Técnico especializado"""
    __tablename__ = 'tecnicos'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    especialidad = Column(String(100))
    nivel_experiencia = Column(String(20))  # Junior, Senior, Expert
    telefono = Column(String(20))
    email = Column(String(100))
    activo = Column(Boolean, default=True)
    
    # Relación Many-to-Many: Un técnico puede trabajar en múltiples plantas
    plantas_asignadas = relationship(
        "PlantaIndustrial",
        secondary=tecnico_planta_asociacion,
        backref=backref("tecnicos_asignados", lazy="select")
    )
    
    def __repr__(self):
        return f"<Tecnico(nombre='{self.nombre} {self.apellido}', especialidad='{self.especialidad}')>"

"""
=================================================================
3. HERENCIA DE MODELOS
=================================================================

SQLAlchemy soporta tres tipos de herencia:
1. Single Table Inheritance: Todas las clases en una tabla
2. Joined Table Inheritance: Cada clase tiene su tabla
3. Concrete Table Inheritance: Tablas completamente separadas
"""

# Enum para tipos de equipos
class TipoEquipo(enum.Enum):
    SENSOR = "sensor"
    ACTUADOR = "actuador"
    CONTROLADOR = "controlador"
    MOTOR = "motor"
    BOMBA = "bomba"

# Single Table Inheritance - Todas las clases hijas en una tabla
class EquipoIndustrial(Base):
    """Clase base para todos los equipos industriales"""
    __tablename__ = 'equipos_industriales'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    modelo = Column(String(100))
    fabricante = Column(String(100))
    numero_serie = Column(String(100), unique=True)
    fecha_instalacion = Column(DateTime)
    estado_operativo = Column(String(20), default='Operativo')
    
    # Discriminator para Single Table Inheritance
    tipo_equipo = Column(Enum(TipoEquipo))
    
    # Foreign Key hacia la línea de producción
    linea_produccion_id = Column(Integer, ForeignKey('lineas_produccion.id'))
    linea_produccion = relationship("LineaProduccion", back_populates="equipos")
    
    __mapper_args__ = {
        'polymorphic_identity': TipoEquipo.SENSOR,
        'polymorphic_on': tipo_equipo
    }
    
    def __repr__(self):
        return f"<EquipoIndustrial(nombre='{self.nombre}', tipo='{self.tipo_equipo}')>"

class SensorEspecializado(EquipoIndustrial):
    """Sensor especializado que hereda de EquipoIndustrial"""
    
    # Campos específicos de sensores
    tipo_sensor = Column(String(50))  # Temperatura, Presión, Vibración, etc.
    rango_medicion = Column(String(50))
    precision_especificada = Column(Float)
    protocolo_comunicacion = Column(String(50))  # Modbus, OPC-UA, etc.
    
    __mapper_args__ = {
        'polymorphic_identity': TipoEquipo.SENSOR,
    }

class MotorIndustrial(EquipoIndustrial):
    """Motor industrial que hereda de EquipoIndustrial"""
    
    # Campos específicos de motores
    potencia_kw = Column(Float)
    voltaje_operacion = Column(Float)
    velocidad_rpm = Column(Integer)
    tipo_motor = Column(String(50))  # AC, DC, Servo, etc.
    eficiencia_energetica = Column(Float)
    
    __mapper_args__ = {
        'polymorphic_identity': TipoEquipo.MOTOR,
    }

"""
=================================================================
4. MODELOS CON RELACIONES COMPLEJAS
=================================================================
"""

class LineaProduccion(Base):
    """Línea de producción con múltiples relaciones"""
    __tablename__ = 'lineas_produccion'
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)
    capacidad_hora = Column(Float)  # unidades por hora
    eficiencia_objetivo = Column(Float, default=85.0)  # porcentaje
    estado = Column(String(20), default='Activa')
    
    # Foreign Key hacia la planta
    planta_id = Column(Integer, ForeignKey('plantas_industriales.id'), nullable=False)
    
    # Relaciones
    planta = relationship("PlantaIndustrial", back_populates="lineas_produccion")
    equipos = relationship("EquipoIndustrial", back_populates="linea_produccion")
    turnos_produccion = relationship("TurnoProduccion", back_populates="linea")
    
    def __repr__(self):
        return f"<LineaProduccion(nombre='{self.nombre}', equipos={len(self.equipos)})>"

class TurnoProduccion(Base):
    """Turnos de producción con datos de performance"""
    __tablename__ = 'turnos_produccion'
    
    id = Column(Integer, primary_key=True)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime)
    supervisor = Column(String(100))
    unidades_producidas = Column(Integer, default=0)
    unidades_defectuosas = Column(Integer, default=0)
    tiempo_paro = Column(Integer, default=0)  # minutos
    observaciones = Column(Text)
    
    # Foreign Key hacia línea de producción
    linea_id = Column(Integer, ForeignKey('lineas_produccion.id'), nullable=False)
    
    # Relaciones
    linea = relationship("LineaProduccion", back_populates="turnos_produccion")
    
    @property
    def eficiencia_calculada(self):
        """Calcula la eficiencia del turno"""
        if not self.fecha_fin or not self.fecha_inicio:
            return 0.0
        
        duracion_total = (self.fecha_fin - self.fecha_inicio).total_seconds() / 60  # minutos
        tiempo_productivo = duracion_total - self.tiempo_paro
        
        if tiempo_productivo <= 0:
            return 0.0
        
        return (self.unidades_producidas / (tiempo_productivo / 60) / self.linea.capacidad_hora) * 100

class LecturaAvanzada(Base):
    """Lecturas de sensores con datos enriquecidos"""
    __tablename__ = 'lecturas_avanzadas'
    
    id = Column(Integer, primary_key=True)
    valor = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    calidad_senal = Column(Float, default=100.0)  # porcentaje
    estado_sensor = Column(String(20), default='Normal')
    procesado = Column(Boolean, default=False)
    
    # Foreign Key hacia sensor
    sensor_id = Column(Integer, ForeignKey('sensores_avanzados.id'), nullable=False)
    
    # Relación
    sensor = relationship("SensorAvanzado", back_populates="lecturas")
    
    def __repr__(self):
        return f"<LecturaAvanzada(sensor='{self.sensor.nombre}', valor={self.valor})>"

"""
=================================================================
5. GESTORES DE DATOS AVANZADOS
=================================================================
"""

class GestorPlantasIndustriales:
    """Gestor avanzado para plantas industriales con relaciones complejas"""
    
    def __init__(self, session: Session):
        self.session = session
    
    def crear_planta_completa(self, datos_planta: Dict[str, Any]) -> PlantaIndustrial:
        """Crea una planta con todos sus componentes"""
        
        # Crear la planta
        planta = PlantaIndustrial(
            nombre=datos_planta['nombre'],
            ubicacion=datos_planta['ubicacion'],
            tipo_industria=datos_planta['tipo_industria'],
            capacidad_produccion=datos_planta.get('capacidad_produccion', 1000),
            fecha_inauguracion=datos_planta.get('fecha_inauguracion', datetime.utcnow())
        )
        
        self.session.add(planta)
        self.session.flush()  # Para obtener el ID sin hacer commit
        
        # Crear líneas de producción
        for linea_data in datos_planta.get('lineas_produccion', []):
            linea = LineaProduccion(
                nombre=linea_data['nombre'],
                descripcion=linea_data.get('descripcion', ''),
                capacidad_hora=linea_data.get('capacidad_hora', 100),
                planta_id=planta.id
            )
            self.session.add(linea)
            self.session.flush()
            
            # Crear sensores para la línea
            for sensor_data in linea_data.get('sensores', []):
                sensor = SensorAvanzado(
                    nombre=sensor_data['nombre'],
                    tipo=sensor_data['tipo'],
                    ubicacion_especifica=sensor_data.get('ubicacion', ''),
                    unidad_medida=sensor_data.get('unidad', 'unidades'),
                    valor_min=sensor_data.get('valor_min', 0),
                    valor_max=sensor_data.get('valor_max', 100),
                    planta_id=planta.id
                )
                self.session.add(sensor)
        
        self.session.commit()
        return planta
    
    def obtener_resumen_planta(self, planta_id: int) -> Dict[str, Any]:
        """Obtiene un resumen completo de la planta con todas sus relaciones"""
        
        # Usar joinedload para cargar las relaciones de una vez (Eager loading)
        planta = self.session.query(PlantaIndustrial)\
            .options(
                joinedload(PlantaIndustrial.sensores),
                joinedload(PlantaIndustrial.lineas_produccion),
                joinedload(PlantaIndustrial.tecnicos_asignados)
            )\
            .filter(PlantaIndustrial.id == planta_id)\
            .first()
        
        if not planta:
            return {}
        
        return {
            'planta': {
                'id': planta.id,
                'nombre': planta.nombre,
                'ubicacion': planta.ubicacion,
                'tipo_industria': planta.tipo_industria,
                'activa': planta.activa
            },
            'estadisticas': {
                'total_sensores': len(planta.sensores),
                'total_lineas': len(planta.lineas_produccion),
                'total_tecnicos': len(planta.tecnicos_asignados),
                'sensores_por_tipo': self._contar_sensores_por_tipo(planta.sensores)
            },
            'lineas_produccion': [
                {
                    'nombre': linea.nombre,
                    'capacidad_hora': linea.capacidad_hora,
                    'total_equipos': len(linea.equipos)
                }
                for linea in planta.lineas_produccion
            ]
        }
    
    def _contar_sensores_por_tipo(self, sensores: List[SensorAvanzado]) -> Dict[str, int]:
        """Cuenta sensores por tipo"""
        conteo = {}
        for sensor in sensores:
            tipo = sensor.tipo or 'Sin especificar'
            conteo[tipo] = conteo.get(tipo, 0) + 1
        return conteo
    
    def asignar_tecnico_planta(self, tecnico_id: int, planta_id: int, rol: str = 'Técnico General'):
        """Asigna un técnico a una planta (relación Many-to-Many)"""
        
        tecnico = self.session.query(Tecnico).get(tecnico_id)
        planta = self.session.query(PlantaIndustrial).get(planta_id)
        
        if not tecnico or not planta:
            raise ValueError("Técnico o planta no encontrados")
        
        # Verificar si ya está asignado
        if planta in tecnico.plantas_asignadas:
            print(f"El técnico {tecnico.nombre} ya está asignado a {planta.nombre}")
            return False
        
        # Asignar la relación
        tecnico.plantas_asignadas.append(planta)
        self.session.commit()
        
        print(f"✅ Técnico {tecnico.nombre} asignado a planta {planta.nombre}")
        return True

"""
=================================================================
6. CONSULTAS AVANZADAS CON ORM
=================================================================
"""

class ConsultasAvanzadas:
    """Clase con ejemplos de consultas complejas usando SQLAlchemy ORM"""
    
    def __init__(self, session: Session):
        self.session = session
    
    def plantas_con_mas_sensores(self, limite: int = 5) -> List[Dict[str, Any]]:
        """Obtiene las plantas con más sensores usando subconsultas"""
        
        resultado = self.session.query(
            PlantaIndustrial.nombre,
            PlantaIndustrial.ubicacion,
            func.count(SensorAvanzado.id).label('total_sensores')
        ).join(SensorAvanzado)\
        .group_by(PlantaIndustrial.id)\
        .order_by(func.count(SensorAvanzado.id).desc())\
        .limit(limite)\
        .all()
        
        return [
            {
                'nombre': r.nombre,
                'ubicacion': r.ubicacion,
                'total_sensores': r.total_sensores
            }
            for r in resultado
        ]
    
    def eficiencia_promedio_por_linea(self) -> List[Dict[str, Any]]:
        """Calcula eficiencia promedio por línea de producción"""
        
        # Subconsulta para calcular eficiencia por turno
        subquery = self.session.query(
            TurnoProduccion.linea_id,
            TurnoProduccion.id,
            TurnoProduccion.unidades_producidas,
            TurnoProduccion.tiempo_paro,
            func.julianday(TurnoProduccion.fecha_fin) - func.julianday(TurnoProduccion.fecha_inicio).label('duracion_dias'),
            LineaProduccion.capacidad_hora
        ).join(LineaProduccion)\
        .filter(TurnoProduccion.fecha_fin.isnot(None))\
        .subquery()
        
        # Consulta principal con cálculo de eficiencia
        resultado = self.session.query(
            LineaProduccion.nombre,
            func.avg(
                (subquery.c.unidades_producidas / 
                 ((subquery.c.duracion_dias * 24 * 60 - subquery.c.tiempo_paro) / 60) /
                 subquery.c.capacidad_hora) * 100
            ).label('eficiencia_promedio')
        ).join(subquery, LineaProduccion.id == subquery.c.linea_id)\
        .group_by(LineaProduccion.id)\
        .all()
        
        return [
            {
                'linea': r.nombre,
                'eficiencia_promedio': round(r.eficiencia_promedio, 2)
            }
            for r in resultado
        ]
    
    def sensores_con_lecturas_anomalas(self, dias_atras: int = 7) -> List[Dict[str, Any]]:
        """Identifica sensores con lecturas fuera de rango"""
        
        fecha_limite = datetime.utcnow() - timedelta(days=dias_atras)
        
        resultado = self.session.query(
            SensorAvanzado.nombre,
            SensorAvanzado.tipo,
            PlantaIndustrial.nombre.label('planta'),
            func.count(LecturaAvanzada.id).label('lecturas_anomalas'),
            func.avg(LecturaAvanzada.valor).label('valor_promedio')
        ).join(LecturaAvanzada)\
        .join(PlantaIndustrial)\
        .filter(
            LecturaAvanzada.timestamp >= fecha_limite,
            # Lecturas fuera del rango permitido
            (LecturaAvanzada.valor < SensorAvanzado.valor_min) |
            (LecturaAvanzada.valor > SensorAvanzado.valor_max)
        ).group_by(SensorAvanzado.id)\
        .having(func.count(LecturaAvanzada.id) > 5)\
        .order_by(func.count(LecturaAvanzada.id).desc())\
        .all()
        
        return [
            {
                'sensor': r.nombre,
                'tipo': r.tipo,
                'planta': r.planta,
                'lecturas_anomalas': r.lecturas_anomalas,
                'valor_promedio': round(r.valor_promedio, 2)
            }
            for r in resultado
        ]
    
    def ranking_tecnicos_por_plantas(self) -> List[Dict[str, Any]]:
        """Ranking de técnicos por número de plantas asignadas"""
        
        resultado = self.session.query(
            Tecnico.nombre,
            Tecnico.apellido,
            Tecnico.especialidad,
            func.count(tecnico_planta_asociacion.c.planta_id).label('plantas_asignadas')
        ).join(tecnico_planta_asociacion)\
        .group_by(Tecnico.id)\
        .order_by(func.count(tecnico_planta_asociacion.c.planta_id).desc())\
        .all()
        
        return [
            {
                'tecnico': f"{r.nombre} {r.apellido}",
                'especialidad': r.especialidad,
                'plantas_asignadas': r.plantas_asignadas
            }
            for r in resultado
        ]

"""
=================================================================
7. OPTIMIZACIÓN Y PERFORMANCE
=================================================================
"""

class OptimizadorPerformance:
    """Técnicas de optimización para consultas complejas"""
    
    def __init__(self, session: Session):
        self.session = session
    
    def ejemplo_lazy_vs_eager_loading(self):
        """Demuestra la diferencia entre lazy y eager loading"""
        
        print("🔍 COMPARACIÓN: LAZY vs EAGER LOADING")
        print("=" * 50)
        
        # LAZY LOADING (por defecto) - N+1 queries problem
        print("\n1️⃣ LAZY LOADING (problemático):")
        plantas_lazy = self.session.query(PlantaIndustrial).all()
        
        for planta in plantas_lazy[:3]:  # Solo primeras 3 para demo
            print(f"Planta: {planta.nombre}")
            # Cada acceso a sensores genera una nueva query (N+1 problem)
            print(f"  Sensores: {len(planta.sensores)}")  # Query adicional aquí
        
        # EAGER LOADING - Una sola query optimizada
        print("\n2️⃣ EAGER LOADING (optimizado):")
        plantas_eager = self.session.query(PlantaIndustrial)\
            .options(joinedload(PlantaIndustrial.sensores))\
            .all()
        
        for planta in plantas_eager[:3]:
            print(f"Planta: {planta.nombre}")
            print(f"  Sensores: {len(planta.sensores)}")  # Sin queries adicionales
    
    def consulta_optimizada_dashboard(self) -> Dict[str, Any]:
        """Consulta optimizada para dashboard industrial"""
        
        # Una sola query que obtiene todo lo necesario
        resultado = self.session.query(PlantaIndustrial)\
            .options(
                joinedload(PlantaIndustrial.sensores).joinedload(SensorAvanzado.lecturas),
                joinedload(PlantaIndustrial.lineas_produccion).joinedload(LineaProduccion.equipos),
                selectinload(PlantaIndustrial.tecnicos_asignados)
            )\
            .filter(PlantaIndustrial.activa == True)\
            .all()
        
        dashboard_data = {
            'total_plantas': len(resultado),
            'total_sensores': sum(len(p.sensores) for p in resultado),
            'total_lineas': sum(len(p.lineas_produccion) for p in resultado),
            'plantas_detalle': []
        }
        
        for planta in resultado:
            dashboard_data['plantas_detalle'].append({
                'nombre': planta.nombre,
                'sensores_activos': len([s for s in planta.sensores if s.lecturas]),
                'lineas_operativas': len([l for l in planta.lineas_produccion if l.estado == 'Activa']),
                'tecnicos_asignados': len(planta.tecnicos_asignados)
            })
        
        return dashboard_data
    
    def bulk_operations_ejemplo(self):
        """Demuestra operaciones en lote para mejor performance"""
        
        print("\n🚀 BULK OPERATIONS PARA PERFORMANCE")
        print("=" * 40)
        
        # Bulk insert - insertar múltiples registros de una vez
        lecturas_bulk = []
        fecha_base = datetime.utcnow()
        
        # Crear 1000 lecturas de ejemplo
        sensores = self.session.query(SensorAvanzado).limit(10).all()
        
        for i in range(1000):
            for sensor in sensores:
                lecturas_bulk.append({
                    'sensor_id': sensor.id,
                    'valor': 20 + (i % 60),  # Valores simulados
                    'timestamp': fecha_base + timedelta(minutes=i),
                    'calidad_senal': 95.0 + (i % 10)
                })
        
        # Inserción en lote (mucho más rápido que inserts individuales)
        self.session.bulk_insert_mappings(LecturaAvanzada, lecturas_bulk)
        self.session.commit()
        
        print(f"✅ Insertadas {len(lecturas_bulk)} lecturas en lote")
        
        # Bulk update - actualizar múltiples registros
        filas_actualizadas = self.session.query(LecturaAvanzada)\
            .filter(LecturaAvanzada.procesado == False)\
            .update({LecturaAvanzada.procesado: True})
        
        self.session.commit()
        print(f"✅ Actualizadas {filas_actualizadas} lecturas como procesadas")

"""
=================================================================
8. EJERCICIOS PRÁCTICOS PARTE 3
=================================================================
"""

def ejercicio_basico_relaciones():
    """Ejercicio básico: Crear y consultar relaciones One-to-Many"""
    
    print("\n🎯 EJERCICIO BÁSICO: Relaciones One-to-Many")
    print("=" * 50)
    
    with get_session() as session:
        gestor = GestorPlantasIndustriales(session)
        
        # Crear una planta con líneas y sensores
        datos_planta = {
            'nombre': 'Planta Ejercicio Básico',
            'ubicacion': 'Industrial Park Norte',
            'tipo_industria': 'Automotriz',
            'lineas_produccion': [
                {
                    'nombre': 'Línea de Ensamble',
                    'capacidad_hora': 50,
                    'sensores': [
                        {'nombre': 'Temp-Motor-01', 'tipo': 'Temperatura', 'valor_min': 20, 'valor_max': 80},
                        {'nombre': 'Presion-Hidraulica-01', 'tipo': 'Presión', 'valor_min': 5, 'valor_max': 25}
                    ]
                }
            ]
        }
        
        planta = gestor.crear_planta_completa(datos_planta)
        print(f"✅ Planta creada: {planta.nombre}")
        
        # Consultar las relaciones
        resumen = gestor.obtener_resumen_planta(planta.id)
        print(f"📊 Resumen de planta:")
        print(f"  - Sensores: {resumen['estadisticas']['total_sensores']}")
        print(f"  - Líneas: {resumen['estadisticas']['total_lineas']}")

def ejercicio_intermedio_many_to_many():
    """Ejercicio intermedio: Relaciones Many-to-Many"""
    
    print("\n🎯 EJERCICIO INTERMEDIO: Relaciones Many-to-Many")
    print("=" * 55)
    
    with get_session() as session:
        gestor = GestorPlantasIndustriales(session)
        
        # Crear técnicos
        tecnicos_data = [
            {'nombre': 'Carlos', 'apellido': 'Rodriguez', 'especialidad': 'Mecánica Industrial'},
            {'nombre': 'Ana', 'apellido': 'Martinez', 'especialidad': 'Electricidad'},
            {'nombre': 'Luis', 'apellido': 'Garcia', 'especialidad': 'Automatización'}
        ]
        
        tecnicos = []
        for data in tecnicos_data:
            tecnico = Tecnico(**data)
            session.add(tecnico)
            tecnicos.append(tecnico)
        
        session.commit()
        
        # Obtener plantas existentes
        plantas = session.query(PlantaIndustrial).limit(2).all()
        
        # Asignar técnicos a plantas (relación Many-to-Many)
        for i, tecnico in enumerate(tecnicos):
            for j, planta in enumerate(plantas):
                if (i + j) % 2 == 0:  # Asignación parcial para demostrar
                    gestor.asignar_tecnico_planta(tecnico.id, planta.id)
        
        # Consultar las asignaciones
        consultas = ConsultasAvanzadas(session)
        ranking = consultas.ranking_tecnicos_por_plantas()
        
        print("👥 Ranking de técnicos por plantas asignadas:")
        for tecnico_info in ranking:
            print(f"  {tecnico_info['tecnico']}: {tecnico_info['plantas_asignadas']} plantas")

def ejercicio_avanzado_consultas_complejas():
    """Ejercicio avanzado: Consultas complejas y optimización"""
    
    print("\n🎯 EJERCICIO AVANZADO: Consultas Complejas")
    print("=" * 50)
    
    with get_session() as session:
        consultas = ConsultasAvanzadas(session)
        optimizador = OptimizadorPerformance(session)
        
        # 1. Análisis de plantas con más sensores
        print("\n1️⃣ Plantas con más sensores:")
        top_plantas = consultas.plantas_con_mas_sensores(3)
        for planta in top_plantas:
            print(f"  {planta['nombre']}: {planta['total_sensores']} sensores")
        
        # 2. Identificar sensores con lecturas anómalas
        print("\n2️⃣ Sensores con lecturas anómalas:")
        sensores_anomalos = consultas.sensores_con_lecturas_anomalas(30)
        for sensor in sensores_anomalos[:3]:
            print(f"  {sensor['sensor']}: {sensor['lecturas_anomalas']} lecturas anómalas")
        
        # 3. Dashboard optimizado
        print("\n3️⃣ Dashboard optimizado:")
        dashboard = optimizador.consulta_optimizada_dashboard()
        print(f"  Total plantas: {dashboard['total_plantas']}")
        print(f"  Total sensores: {dashboard['total_sensores']}")
        print(f"  Total líneas: {dashboard['total_lineas']}")
        
        # 4. Demostrar performance optimization
        optimizador.ejemplo_lazy_vs_eager_loading()

"""
=================================================================
9. UTILIDADES Y HELPERS
=================================================================
"""

@contextmanager
def get_session():
    """Context manager para sesiones de SQLAlchemy"""
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise
    finally:
        session.close()

def crear_schema_completo():
    """Crea todas las tablas del esquema avanzado"""
    print("🏗️ CREANDO ESQUEMA COMPLETO...")
    
    # Crear todas las tablas
    Base.metadata.create_all(engine)
    
    print("✅ Schema creado exitosamente")
    print("📋 Tablas creadas:")
    for table_name in Base.metadata.tables.keys():
        print(f"  - {table_name}")

def poblar_datos_demo():
    """Pobla la base de datos con datos de demostración"""
    print("\n📊 POBLANDO DATOS DE DEMOSTRACIÓN...")
    
    with get_session() as session:
        gestor = GestorPlantasIndustriales(session)
        
        # Datos de plantas de ejemplo
        plantas_demo = [
            {
                'nombre': 'Planta Norte - Automotriz',
                'ubicacion': 'Zona Industrial Norte',
                'tipo_industria': 'Automotriz',
                'capacidad_produccion': 1000,
                'lineas_produccion': [
                    {
                        'nombre': 'Línea de Motores',
                        'capacidad_hora': 25,
                        'sensores': [
                            {'nombre': 'TEMP-MOT-001', 'tipo': 'Temperatura', 'valor_min': 60, 'valor_max': 95},
                            {'nombre': 'VIB-MOT-001', 'tipo': 'Vibración', 'valor_min': 0, 'valor_max': 50},
                            {'nombre': 'PRES-OIL-001', 'tipo': 'Presión', 'valor_min': 2, 'valor_max': 8}
                        ]
                    },
                    {
                        'nombre': 'Línea de Transmisiones',
                        'capacidad_hora': 15,
                        'sensores': [
                            {'nombre': 'TEMP-TRANS-001', 'tipo': 'Temperatura', 'valor_min': 40, 'valor_max': 80},
                            {'nombre': 'TORQUE-TRANS-001', 'tipo': 'Torque', 'valor_min': 100, 'valor_max': 500}
                        ]
                    }
                ]
            },
            {
                'nombre': 'Planta Sur - Química',
                'ubicacion': 'Complejo Petroquímico Sur',
                'tipo_industria': 'Química',
                'capacidad_produccion': 2000,
                'lineas_produccion': [
                    {
                        'nombre': 'Reactor Principal',
                        'capacidad_hora': 100,
                        'sensores': [
                            {'nombre': 'TEMP-REACT-001', 'tipo': 'Temperatura', 'valor_min': 200, 'valor_max': 350},
                            {'nombre': 'PRES-REACT-001', 'tipo': 'Presión', 'valor_min': 5, 'valor_max': 15},
                            {'nombre': 'pH-REACT-001', 'tipo': 'pH', 'valor_min': 6.5, 'valor_max': 8.5}
                        ]
                    }
                ]
            }
        ]
        
        # Crear plantas
        for planta_data in plantas_demo:
            planta = gestor.crear_planta_completa(planta_data)
            print(f"✅ Planta creada: {planta.nombre}")
        
        # Crear técnicos de ejemplo
        tecnicos_demo = [
            {'nombre': 'Juan', 'apellido': 'Pérez', 'especialidad': 'Mecánica Industrial', 'nivel_experiencia': 'Senior'},
            {'nombre': 'María', 'apellido': 'González', 'especialidad': 'Instrumentación', 'nivel_experiencia': 'Expert'},
            {'nombre': 'Carlos', 'apellido': 'López', 'especialidad': 'Electricidad', 'nivel_experiencia': 'Junior'},
            {'nombre': 'Ana', 'apellido': 'Martín', 'especialidad': 'Automatización', 'nivel_experiencia': 'Senior'}
        ]
        
        for tecnico_data in tecnicos_demo:
            tecnico = Tecnico(**tecnico_data)
            session.add(tecnico)
        
        session.commit()
        print("👥 Técnicos creados exitosamente")

def demo_completa_parte3():
    """Demostración completa de la Parte 3"""
    
    print("🐍🗄️ MÓDULO 3.3 - PARTE 3: DEMOSTRACIÓN COMPLETA")
    print("🔗 MODELOS AVANZADOS Y RELACIONES COMPLEJAS")
    print("=" * 70)
    
    try:
        # 1. Crear schema
        crear_schema_completo()
        
        # 2. Poblar datos
        poblar_datos_demo()
        
        # 3. Ejercicios prácticos
        ejercicio_basico_relaciones()
        ejercicio_intermedio_many_to_many()
        ejercicio_avanzado_consultas_complejas()
        
        # 4. Generar lecturas de ejemplo
        print("\n📈 GENERANDO LECTURAS DE EJEMPLO...")
        with get_session() as session:
            optimizador = OptimizadorPerformance(session)
            optimizador.bulk_operations_ejemplo()
        
        print("\n" + "="*70)
        print("🎉 ¡PARTE 3 COMPLETAMENTE DEMOSTRADA!")
        print("✅ Relaciones One-to-Many, Many-to-Many implementadas")
        print("✅ Herencia de modelos funcionando")
        print("✅ Consultas avanzadas ejecutadas")
        print("✅ Optimizaciones de performance aplicadas")
        print("🚀 ¡Listo para la Parte 4: Migrations y Production!")
        
    except Exception as e:
        print(f"❌ Error en demostración: {e}")
        import traceback
        traceback.print_exc()

"""
=================================================================
10. CUESTIONARIO Y CONSOLIDACIÓN PARTE 3
=================================================================
"""

def cuestionario_parte3():
    """Cuestionario de evaluación para la Parte 3"""
    
    print("\n📝 CUESTIONARIO - MÓDULO 3.3 PARTE 3")
    print("🔗 MODELOS AVANZADOS Y RELACIONES")
    print("=" * 50)
    
    preguntas = {
        1: {
            'pregunta': '¿Qué tipo de relación necesitas para "Un técnico puede trabajar en múltiples plantas"?',
            'opciones': [
                'a) One-to-Many',
                'b) Many-to-One',
                'c) Many-to-Many',
                'd) One-to-One'
            ],
            'respuesta_correcta': 'c',
            'explicacion': 'Many-to-Many porque un técnico puede estar en múltiples plantas Y una planta puede tener múltiples técnicos.'
        },
        2: {
            'pregunta': '¿Cuál es el principal problema del Lazy Loading?',
            'opciones': [
                'a) Usa mucha memoria',
                'b) Problema N+1 queries',
                'c) Es más lento que SQL puro',
                'd) No funciona con relaciones'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'El problema N+1 ocurre cuando se hace una query inicial y luego N queries adicionales para cada relación accedida.'
        },
        3: {
            'pregunta': '¿Qué técnica usarías para optimizar la carga de múltiples relaciones?',
            'opciones': [
                'a) lazy="select"',
                'b) joinedload()',
                'c) query.all()',
                'd) session.commit()'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'joinedload() usa JOIN para cargar las relaciones en una sola query, evitando el problema N+1.'
        },
        4: {
            'pregunta': '¿Qué hace cascade="all, delete-orphan" en una relación?',
            'opciones': [
                'a) Mejora el performance',
                'b) Elimina hijos cuando se elimina el padre',
                'c) Crea índices automáticos',
                'd) Valida los datos'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'cascade="all, delete-orphan" elimina automáticamente los registros hijos cuando se elimina el padre.'
        },
        5: {
            'pregunta': '¿Cuál es la ventaja de bulk_insert_mappings()?',
            'opciones': [
                'a) Mejor validación de datos',
                'b) Inserción masiva eficiente',
                'c) Relaciones automáticas',
                'd) Mejor debugging'
            ],
            'respuesta_correcta': 'b',
            'explicacion': 'bulk_insert_mappings() permite insertar múltiples registros de una vez, siendo mucho más eficiente que inserts individuales.'
        }
    }
    
    print("✅ RESPUESTAS CORRECTAS:")
    for num, data in preguntas.items():
        print(f"\nPregunta {num}: {data['pregunta']}")
        for opcion in data['opciones']:
            marca = "✓" if opcion.startswith(data['respuesta_correcta']) else " "
            print(f"  [{marca}] {opcion}")
        print(f"💡 Explicación: {data['explicacion']}")

def checklist_consolidacion_parte3():
    """Checklist de consolidación para la Parte 3"""
    
    print("\n🎯 CHECKLIST DE CONSOLIDACIÓN - PARTE 3")
    print("🔗 MODELOS AVANZADOS Y RELACIONES")
    print("=" * 60)
    
    checklist_items = [
        "✅ Comprendo las relaciones One-to-Many (1:N)",
        "✅ Domino las relaciones Many-to-Many (N:M) con tablas de asociación",
        "✅ Entiendo la herencia de modelos en SQLAlchemy",
        "✅ Sé cuándo usar Single Table vs Joined Table inheritance",
        "✅ Puedo crear modelos con relaciones complejas",
        "✅ Comprendo el concepto de Foreign Keys en ORM",
        "✅ Manejo relationship() y back_populates correctamente",
        "✅ Entiendo el problema N+1 queries y sus soluciones",
        "✅ Puedo usar joinedload() para optimizar consultas",
        "✅ Sé la diferencia entre lazy y eager loading",
        "✅ Domino consultas avanzadas con joins y subconsultas",
        "✅ Puedo usar funciones de agregación (COUNT, AVG, SUM)",
        "✅ Entiendo cascade options (delete-orphan, all, etc.)",
        "✅ Puedo hacer bulk operations para mejor performance",
        "✅ Sé optimizar consultas complejas",
        "✅ Comprendo context managers para sesiones",
        "✅ Puedo crear gestores de datos avanzados",
        "✅ Domino consultas con filtros complejos",
        "✅ Entiendo índices y optimización de queries",
        "✅ Puedo implementar sistemas industriales complejos con ORM"
    ]
    
    print("📋 CONOCIMIENTOS CONSOLIDADOS:")
    for item in checklist_items:
        print(f"  {item}")
    
    print(f"\n🏆 TOTAL OBJETIVOS COMPLETADOS: {len(checklist_items)}/20")
    print("\n🎓 NIVEL DE COMPETENCIA: EXPERTO EN RELACIONES ORM")
    print("📈 PREPARACIÓN PARA PARTE 4: 100% LISTO")
    print("🚀 SIGUIENTE: Migraciones, Testing y Producción")

"""
=================================================================
FUNCIÓN PRINCIPAL
=================================================================
"""

def main():
    """Función principal de demostración de la Parte 3"""
    
    print("🐍🗄️ MÓDULO 3.3 PARTE 3: MODELOS AVANZADOS Y RELACIONES")
    print("=" * 70)
    
    try:
        demo_completa_parte3()
        cuestionario_parte3()
        checklist_consolidacion_parte3()
        
    except Exception as e:
        print(f"❌ Error en ejecución: {e}")
        print("🔧 Verifica que SQLAlchemy esté instalado: pip install sqlalchemy")

if __name__ == "__main__":
    main()

"""
=================================================================
🎯 RESUMEN DE LA PARTE 3
=================================================================

📚 CONCEPTOS CLAVE APRENDIDOS:
- Relaciones One-to-Many, Many-to-Many, One-to-One
- Herencia de modelos (Single Table, Joined Table)
- Consultas avanzadas con joins y subconsultas
- Optimización de performance (lazy vs eager loading)
- Bulk operations para mejor rendimiento
- Context managers para gestión de sesiones
- Gestores de datos avanzados

🏭 APLICACIÓN INDUSTRIAL:
- Sistema completo de plantas industriales
- Gestión de sensores con relaciones complejas
- Asignación de técnicos a múltiples plantas
- Análisis de performance y eficiencia
- Dashboard industrial optimizado

🚀 PREPARACIÓN PARA PARTE 4:
- Migraciones con Alembic
- Testing de modelos ORM
- Configuración para producción
- Monitoreo y logging avanzado
- Deployment de aplicaciones industriales

¡Excelente progreso en el dominio de SQLAlchemy ORM avanzado!
"""
