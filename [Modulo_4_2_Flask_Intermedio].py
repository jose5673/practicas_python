# ================================================================
# 🌟 MÓDULO 4.2: FLASK INTERMEDIO - DESARROLLO WEB AVANZADO
# ================================================================

"""
📚 FASE 4: DESARROLLO WEB CON FLASK - NIVEL INTERMEDIO

🎯 OBJETIVO DEL MÓDULO:
Dominar funcionalidades intermedias de Flask para crear aplicaciones web 
robustas con formularios, autenticación, sesiones, y bases de datos, 
aplicadas a sistemas de automatización industrial.

📋 PRERREQUISITOS:
✅ Módulo 4.1 - Flask Básico (COMPLETADO)
✅ Módulo 3.2 - Python + SQLite (COMPLETADO) 
✅ Módulo 3.3 - ORM SQLAlchemy (COMPLETADO)

🗓️ INFORMACIÓN DEL MÓDULO:
- Creado: 5 de julio de 2025
- Tutor: GitHub Copilot
- Metodología: Aprendizaje Deliberado
- Enfoque: Automatización Industrial
"""

import datetime
print(f"""
🌟 MÓDULO 4.2: FLASK INTERMEDIO - DESARROLLO WEB AVANZADO
========================================================

📅 Iniciado: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
🎯 Nivel: Intermedio
🏭 Enfoque: Automatización Industrial

📋 CONTENIDO PLANIFICADO:
========================

🔥 PARTE 1: FORMULARIOS AVANZADOS CON FLASK-WTF
   📝 Instalación y configuración de Flask-WTF
   📝 Creación de formularios complejos
   📝 Validaciones personalizadas
   📝 Manejo de archivos (uploads)
   📝 Formularios para sistemas industriales

🔥 PARTE 2: GESTIÓN DE SESIONES Y COOKIES  
   🔐 Sistema de sesiones en Flask
   🔐 Manejo seguro de cookies
   🔐 Almacenamiento de estado de usuario
   🔐 Sesiones para operadores industriales

🔥 PARTE 3: AUTENTICACIÓN Y AUTORIZACIÓN
   👤 Sistema de usuarios completo
   👤 Hash de contraseñas (bcrypt)
   👤 Login/logout funcional
   👤 Protección de rutas (decoradores)
   👤 Roles y permisos (operador, supervisor, admin)

🔥 PARTE 4: INTEGRACIÓN CON BASES DE DATOS
   🗄️ Flask + SQLAlchemy integrado
   🗄️ Modelos avanzados de datos
   🗄️ Migraciones de base de datos
   🗄️ Queries complejas y relaciones

🔥 PARTE 5: MANEJO DE ERRORES Y LOGGING
   ❌ Páginas de error personalizadas
   ❌ Sistema de logging robusto  
   ❌ Debugging avanzado
   ❌ Monitoreo de errores en producción

🔥 PARTE 6: APIS REST AVANZADAS
   🔌 Serialización con Marshmallow
   🔌 Documentación automática (Swagger)
   🔌 Validación de datos de entrada
   🔌 Códigos de estado HTTP apropiados
   🔌 APIs para sistemas industriales

🔥 PARTE 7: PROYECTO PRÁCTICO AVANZADO
   🏭 Sistema SCADA web completo
   🏭 Gestión de usuarios y roles
   🏭 Dashboard con autenticación
   🏭 Base de datos histórica de sensores
   🏭 APIs para PLCs y dispositivos IoT

📊 PROGRESO ACTUAL:
==================
📋 Teoría: Iniciando...
💻 Ejemplos: Pendiente
🏭 Proyecto: Pendiente  
📝 Prácticas: Pendiente

🚀 ¡Comenzamos el viaje hacia Flask Intermedio!
""")

# ================================================================
# 🎯 FUNDAMENTOS TEÓRICOS - ESCALADO DESDE FLASK BÁSICO
# ================================================================

print("""
🎯 FUNDAMENTOS TEÓRICOS - TRANSICIÓN A FLASK INTERMEDIO
======================================================

📈 EVOLUCIÓN DEL CONOCIMIENTO:
------------------------------

🔰 FLASK BÁSICO (YA DOMINADO):
   ✅ Aplicaciones simples con rutas estáticas
   ✅ Templates básicos con Jinja2
   ✅ Archivos estáticos simples
   ✅ APIs REST básicas sin autenticación
   ✅ Datos en memoria (sin persistencia)

🚀 FLASK INTERMEDIO (OBJETIVO ACTUAL):
   🎯 Aplicaciones dinámicas con estado
   🎯 Formularios complejos con validación
   🎯 Sistema de usuarios y autenticación  
   🎯 Base de datos relacional integrada
   🎯 Manejo de errores y logging
   🎯 APIs seguras y documentadas

🏭 APLICACIONES EN AUTOMATIZACIÓN INDUSTRIAL:
--------------------------------------------

🔰 NIVEL BÁSICO (Completado):
   ✅ Dashboards de solo lectura
   ✅ Visualización de sensores
   ✅ Alertas básicas

🚀 NIVEL INTERMEDIO (Objetivo):
   🎯 Sistemas SCADA web completos
   🎯 Gestión de usuarios (operadores, supervisores, admins)
   🎯 Configuración remota de dispositivos
   🎯 Histórico persistente de datos
   🎯 Control de acceso granular
   🎯 Integración con bases de datos industriales

💡 VENTAJAS DEL NIVEL INTERMEDIO:
   • 🔐 Seguridad robusta
   • 📊 Persistencia de datos
   • 👥 Multi-usuario con roles
   • 🔧 Configuración dinámica
   • 📈 Escalabilidad mejorada
   • 🛡️ Manejo de errores profesional
""")

# ================================================================
# 🔥 PARTE 1: FORMULARIOS AVANZADOS CON FLASK-WTF
# ================================================================

print("""
🔥 PARTE 1: FORMULARIOS AVANZADOS CON FLASK-WTF
===============================================

📝 ¿QUÉ ES FLASK-WTF?
Flask-WTF es una extensión que integra Flask con WTForms, 
proporcionando formularios seguros y validación robusta.

🎯 VENTAJAS DE FLASK-WTF:
   ✅ Protección CSRF automática
   ✅ Validaciones del lado servidor
   ✅ Integración perfecta con Jinja2
   ✅ Manejo de archivos seguro
   ✅ Formularios reutilizables

🏭 CASOS DE USO INDUSTRIALES:
   • 📝 Configuración de parámetros de PLCs
   • 📊 Creación de reportes personalizados  
   • 👤 Registro de operadores
   • ⚙️ Configuración de alarmas
   • 📈 Definición de setpoints
""")

# Instalación de dependencias para formularios
install_commands = [
    "flask",
    "flask-wtf", 
    "wtforms",
    "flask-sqlalchemy",
    "flask-login",
    "flask-bcrypt",
    "email-validator"
]

print(f"""
📦 DEPENDENCIAS REQUERIDAS PARA EL MÓDULO:
=========================================

Las siguientes librerías serán necesarias:
{chr(10).join(f"   pip install {lib}" for lib in install_commands)}

💡 Estas dependencias nos permitirán crear:
   • 📝 Formularios avanzados y seguros
   • 🔐 Sistema de autenticación completo
   • 🗄️ Integración robusta con bases de datos
   • 👤 Gestión de usuarios y sesiones
   • 🛡️ Validaciones y seguridad
""")

# ================================================================
# 📝 EJEMPLO 1: FORMULARIO BÁSICO CON FLASK-WTF
# ================================================================

print("""
📝 EJEMPLO 1: FORMULARIO BÁSICO CON FLASK-WTF
============================================

Vamos a crear un formulario para configuración de sensores industriales.
""")

formulario_sensor_code = '''
# 📝 FORMULARIO PARA CONFIGURACIÓN DE SENSORES INDUSTRIALES

from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave-secreta-para-formularios-industriales'

# 📋 DEFINICIÓN DEL FORMULARIO DE SENSOR
class SensorConfigForm(FlaskForm):
    """Formulario para configuración de sensores industriales"""
    
    # Campos básicos del sensor
    nombre = StringField(
        'Nombre del Sensor',
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(min=3, max=50, message="El nombre debe tener entre 3 y 50 caracteres")
        ],
        render_kw={"placeholder": "Ej: Sensor Temperatura Motor 1"}
    )
    
    tipo = SelectField(
        'Tipo de Sensor',
        choices=[
            ('temperatura', 'Temperatura'),
            ('presion', 'Presión'),
            ('humedad', 'Humedad'),
            ('vibracion', 'Vibración'),
            ('flujo', 'Flujo'),
            ('nivel', 'Nivel')
        ],
        validators=[DataRequired(message="Seleccione un tipo de sensor")]
    )
    
    # Configuración de rangos
    valor_minimo = FloatField(
        'Valor Mínimo',
        validators=[
            DataRequired(message="El valor mínimo es obligatorio"),
            NumberRange(min=-1000, max=1000, message="Valor fuera de rango permitido")
        ]
    )
    
    valor_maximo = FloatField(
        'Valor Máximo', 
        validators=[
            DataRequired(message="El valor máximo es obligatorio"),
            NumberRange(min=-1000, max=1000, message="Valor fuera de rango permitido")
        ]
    )
    
    unidad = StringField(
        'Unidad de Medida',
        validators=[
            DataRequired(message="La unidad es obligatoria"),
            Length(max=10, message="La unidad no puede exceder 10 caracteres")
        ],
        render_kw={"placeholder": "Ej: °C, Bar, %, mm/s"}
    )
    
    # Configuración de alarmas
    limite_alarma_baja = FloatField(
        'Límite Alarma Baja',
        validators=[NumberRange(min=-1000, max=1000, message="Valor fuera de rango")]
    )
    
    limite_alarma_alta = FloatField(
        'Límite Alarma Alta',
        validators=[NumberRange(min=-1000, max=1000, message="Valor fuera de rango")]
    )
    
    # Configuración adicional
    ubicacion = StringField(
        'Ubicación',
        validators=[Length(max=100, message="La ubicación no puede exceder 100 caracteres")],
        render_kw={"placeholder": "Ej: Línea de Producción A - Motor Principal"}
    )
    
    descripcion = TextAreaField(
        'Descripción',
        validators=[Length(max=500, message="La descripción no puede exceder 500 caracteres")],
        render_kw={"rows": 4, "placeholder": "Descripción detallada del sensor y su función..."}
    )
    
    # Botón de envío
    submit = SubmitField('Guardar Configuración')
    
    # 🔧 VALIDACIÓN PERSONALIZADA
    def validate_valor_maximo(self, field):
        """Validar que el valor máximo sea mayor que el mínimo"""
        if self.valor_minimo.data and field.data:
            if field.data <= self.valor_minimo.data:
                raise ValidationError('El valor máximo debe ser mayor que el valor mínimo')
    
    def validate_limite_alarma_alta(self, field):
        """Validar que la alarma alta esté dentro del rango del sensor"""
        if field.data and self.valor_maximo.data:
            if field.data > self.valor_maximo.data:
                raise ValidationError('La alarma alta no puede exceder el valor máximo del sensor')
    
    def validate_limite_alarma_baja(self, field):
        """Validar que la alarma baja esté dentro del rango del sensor"""
        if field.data and self.valor_minimo.data:
            if field.data < self.valor_minimo.data:
                raise ValidationError('La alarma baja no puede ser menor que el valor mínimo del sensor')

# 🏠 RUTA PRINCIPAL CON FORMULARIO
@app.route('/', methods=['GET', 'POST'])
def configurar_sensor():
    """Ruta para configurar un nuevo sensor"""
    form = SensorConfigForm()
    
    if form.validate_on_submit():
        # 📊 Procesar datos del formulario
        sensor_data = {
            'nombre': form.nombre.data,
            'tipo': form.tipo.data,
            'valor_minimo': form.valor_minimo.data,
            'valor_maximo': form.valor_maximo.data,
            'unidad': form.unidad.data,
            'limite_alarma_baja': form.limite_alarma_baja.data,
            'limite_alarma_alta': form.limite_alarma_alta.data,
            'ubicacion': form.ubicacion.data,
            'descripcion': form.descripcion.data
        }
        
        # En una aplicación real, aquí guardaríamos en la base de datos
        print(f"✅ Sensor configurado: {sensor_data}")
        
        flash(f'Sensor "{form.nombre.data}" configurado exitosamente!', 'success')
        return redirect(url_for('configurar_sensor'))
    
    return render_template('configurar_sensor.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
'''

print("📄 CÓDIGO DEL FORMULARIO DE SENSOR:")
print("="*50)
print(formulario_sensor_code)

# ================================================================
# 📄 TEMPLATE HTML PARA EL FORMULARIO
# ================================================================

template_formulario = '''
<!-- 📄 TEMPLATE: configurar_sensor.html -->
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Configuración de Sensores - Sistema Industrial</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <!-- 📊 HEADER -->
                <div class="card shadow">
                    <div class="card-header bg-primary text-white">
                        <h2 class="mb-0">
                            <i class="fas fa-cog"></i> Configuración de Sensores Industriales
                        </h2>
                        <p class="mb-0 mt-2">Configure los parámetros del sensor para el sistema de monitoreo</p>
                    </div>
                    
                    <div class="card-body">
                        <!-- 🔔 MENSAJES FLASH -->
                        {% with messages = get_flashed_messages(with_categories=true) %}
                            {% if messages %}
                                {% for category, message in messages %}
                                    <div class="alert alert-{{ 'success' if category == 'success' else 'danger' }} alert-dismissible fade show">
                                        <i class="fas fa-{{ 'check-circle' if category == 'success' else 'exclamation-triangle' }}"></i>
                                        {{ message }}
                                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                                    </div>
                                {% endfor %}
                            {% endif %}
                        {% endwith %}
                        
                        <!-- 📝 FORMULARIO -->
                        <form method="POST" novalidate>
                            {{ form.hidden_tag() }}
                            
                            <div class="row">
                                <!-- Información básica -->
                                <div class="col-md-6">
                                    <h5 class="text-primary mb-3">
                                        <i class="fas fa-info-circle"></i> Información Básica
                                    </h5>
                                    
                                    <!-- Nombre del sensor -->
                                    <div class="mb-3">
                                        {{ form.nombre.label(class="form-label") }}
                                        {{ form.nombre(class="form-control" + (" is-invalid" if form.nombre.errors else "")) }}
                                        {% if form.nombre.errors %}
                                            <div class="invalid-feedback">
                                                {% for error in form.nombre.errors %}
                                                    {{ error }}
                                                {% endfor %}
                                            </div>
                                        {% endif %}
                                    </div>
                                    
                                    <!-- Tipo de sensor -->
                                    <div class="mb-3">
                                        {{ form.tipo.label(class="form-label") }}
                                        {{ form.tipo(class="form-select" + (" is-invalid" if form.tipo.errors else "")) }}
                                        {% if form.tipo.errors %}
                                            <div class="invalid-feedback">
                                                {% for error in form.tipo.errors %}
                                                    {{ error }}
                                                {% endfor %}
                                            </div>
                                        {% endif %}
                                    </div>
                                    
                                    <!-- Unidad -->
                                    <div class="mb-3">
                                        {{ form.unidad.label(class="form-label") }}
                                        {{ form.unidad(class="form-control" + (" is-invalid" if form.unidad.errors else "")) }}
                                        {% if form.unidad.errors %}
                                            <div class="invalid-feedback">
                                                {% for error in form.unidad.errors %}
                                                    {{ error }}
                                                {% endfor %}
                                            </div>
                                        {% endif %}
                                    </div>
                                    
                                    <!-- Ubicación -->
                                    <div class="mb-3">
                                        {{ form.ubicacion.label(class="form-label") }}
                                        {{ form.ubicacion(class="form-control" + (" is-invalid" if form.ubicacion.errors else "")) }}
                                        {% if form.ubicacion.errors %}
                                            <div class="invalid-feedback">
                                                {% for error in form.ubicacion.errors %}
                                                    {{ error }}
                                                {% endfor %}
                                            </div>
                                        {% endif %}
                                    </div>
                                </div>
                                
                                <!-- Configuración de rangos y alarmas -->
                                <div class="col-md-6">
                                    <h5 class="text-warning mb-3">
                                        <i class="fas fa-sliders-h"></i> Rangos y Alarmas
                                    </h5>
                                    
                                    <!-- Valores mínimo y máximo -->
                                    <div class="row">
                                        <div class="col-6">
                                            <div class="mb-3">
                                                {{ form.valor_minimo.label(class="form-label") }}
                                                {{ form.valor_minimo(class="form-control" + (" is-invalid" if form.valor_minimo.errors else "")) }}
                                                {% if form.valor_minimo.errors %}
                                                    <div class="invalid-feedback">
                                                        {% for error in form.valor_minimo.errors %}
                                                            {{ error }}
                                                        {% endfor %}
                                                    </div>
                                                {% endif %}
                                            </div>
                                        </div>
                                        <div class="col-6">
                                            <div class="mb-3">
                                                {{ form.valor_maximo.label(class="form-label") }}
                                                {{ form.valor_maximo(class="form-control" + (" is-invalid" if form.valor_maximo.errors else "")) }}
                                                {% if form.valor_maximo.errors %}
                                                    <div class="invalid-feedback">
                                                        {% for error in form.valor_maximo.errors %}
                                                            {{ error }}
                                                        {% endfor %}
                                                    </div>
                                                {% endif %}
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <!-- Límites de alarma -->
                                    <div class="row">
                                        <div class="col-6">
                                            <div class="mb-3">
                                                {{ form.limite_alarma_baja.label(class="form-label") }}
                                                {{ form.limite_alarma_baja(class="form-control" + (" is-invalid" if form.limite_alarma_baja.errors else "")) }}
                                                {% if form.limite_alarma_baja.errors %}
                                                    <div class="invalid-feedback">
                                                        {% for error in form.limite_alarma_baja.errors %}
                                                            {{ error }}
                                                        {% endfor %}
                                                    </div>
                                                {% endif %}
                                            </div>
                                        </div>
                                        <div class="col-6">
                                            <div class="mb-3">
                                                {{ form.limite_alarma_alta.label(class="form-label") }}
                                                {{ form.limite_alarma_alta(class="form-control" + (" is-invalid" if form.limite_alarma_alta.errors else "")) }}
                                                {% if form.limite_alarma_alta.errors %}
                                                    <div class="invalid-feedback">
                                                        {% for error in form.limite_alarma_alta.errors %}
                                                            {{ error }}
                                                        {% endfor %}
                                                    </div>
                                                {% endif %}
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <!-- Descripción -->
                                    <div class="mb-3">
                                        {{ form.descripcion.label(class="form-label") }}
                                        {{ form.descripcion(class="form-control" + (" is-invalid" if form.descripcion.errors else "")) }}
                                        {% if form.descripcion.errors %}
                                            <div class="invalid-feedback">
                                                {% for error in form.descripcion.errors %}
                                                    {{ error }}
                                                {% endfor %}
                                            </div>
                                        {% endif %}
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Botón de envío -->
                            <div class="text-center mt-4">
                                {{ form.submit(class="btn btn-primary btn-lg") }}
                                <a href="#" class="btn btn-secondary btn-lg ms-2">Cancelar</a>
                            </div>
                        </form>
                    </div>
                </div>
                
                <!-- 💡 AYUDA -->
                <div class="card mt-4 shadow-sm">
                    <div class="card-body">
                        <h6 class="text-info">
                            <i class="fas fa-lightbulb"></i> Consejos para la configuración:
                        </h6>
                        <ul class="mb-0 small">
                            <li>Use nombres descriptivos que identifiquen claramente el sensor</li>
                            <li>Configure los rangos según las especificaciones del fabricante</li>
                            <li>Los límites de alarma deben estar dentro del rango del sensor</li>
                            <li>La ubicación ayuda a los operadores a localizar físicamente el sensor</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

print("\n📄 TEMPLATE HTML DEL FORMULARIO:")
print("="*50)
print(template_formulario)

print("""

✅ CARACTERÍSTICAS DEL FORMULARIO AVANZADO:
==========================================

🔐 SEGURIDAD:
   • Protección CSRF automática con Flask-WTF
   • Validaciones del lado servidor robustas  
   • Sanitización automática de datos de entrada

📋 VALIDACIONES IMPLEMENTADAS:
   • Campos obligatorios con mensajes personalizados
   • Rangos numéricos apropiados para sensores
   • Longitud de texto controlada
   • Validaciones cruzadas (máximo > mínimo)
   • Validaciones personalizadas para lógica de negocio

🎨 INTERFAZ PROFESIONAL:
   • Bootstrap 5 para diseño responsive
   • Iconos Font Awesome para mejor UX
   • Mensajes de error contextuales
   • Feedback visual inmediato
   • Diseño optimizado para operadores industriales

🏭 ENFOQUE INDUSTRIAL:
   • Campos específicos para sensores industriales
   • Configuración de alarmas integrada
   • Unidades de medida apropiadas
   • Información de ubicación física
   • Descripción detallada para documentación

💡 PRÓXIMO PASO:
Una vez dominemos los formularios, avanzaremos a sesiones y autenticación 
para crear un sistema completo de usuarios industriales.

¿Estás listo para continuar con la siguiente parte del módulo?
""")

# ================================================================
