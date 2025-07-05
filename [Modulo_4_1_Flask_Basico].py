#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌟 MÓDULO 4.1: FLASK BÁSICO - DESARROLLO WEB CON PYTHON
📚 FASE 4: DESARROLLO WEB CON FLASK

🎯 OBJETIVO DEL MÓDULO:
Dominar los fundamentos de Flask para crear aplicaciones web básicas,
preparándonos para el desarrollo de dashboards industriales y APIs REST.

🗓️ Creado: 5 de julio de 2025
👨‍💻 Tutor: GitHub Copilot
📖 Guía: Lineamiento de Aprendizaje Deliberado

===============================================================================
                            📑 ÍNDICE DEL MÓDULO
===============================================================================

🔥 PARTE 1: INTRODUCCIÓN A FLASK
   📌 1.1 ¿Qué es Flask y por qué usarlo?
   📌 1.2 Arquitectura de Flask
   📌 1.3 Comparación con otros frameworks
   📌 1.4 Casos de uso en automatización industrial

🔥 PARTE 2: CONFIGURACIÓN Y PRIMERA APLICACIÓN
   📌 2.1 Instalación de Flask
   📌 2.2 Aplicación Flask mínima
   📌 2.3 Servidor de desarrollo
   📌 2.4 Configuración básica

🔥 PARTE 3: RUTAS Y MÉTODOS HTTP
   📌 3.1 Conceptos de routing
   📌 3.2 Rutas básicas
   📌 3.3 Métodos HTTP (GET, POST, PUT, DELETE)
   📌 3.4 Parámetros de URL y query strings

🔥 PARTE 4: TEMPLATES CON JINJA2
   📌 4.1 Motor de templates Jinja2
   📌 4.2 Sintaxis básica de Jinja2
   📌 4.3 Herencia de templates
   📌 4.4 Filtros y funciones

🔥 PARTE 5: ARCHIVOS ESTÁTICOS
   📌 5.1 CSS, JavaScript e imágenes
   📌 5.2 Organización de archivos estáticos
   📌 5.3 URLs para archivos estáticos

🔥 PARTE 6: PROYECTO PRÁCTICO
   📌 6.1 Dashboard básico de monitoreo
   📌 6.2 Estructura del proyecto
   📌 6.3 Implementación paso a paso

===============================================================================
                        🔥 PARTE 1: INTRODUCCIÓN A FLASK
===============================================================================

📌 1.1 ¿QUÉ ES FLASK Y POR QUÉ USARLO?
=====================================

Flask es un microframework de Python para desarrollo web que se caracteriza por:

🎯 **CARACTERÍSTICAS PRINCIPALES:**
   • Simplicidad y minimalismo
   • Flexibilidad y extensibilidad
   • Excelente documentación
   • Gran comunidad de desarrolladores
   • Perfecto para prototipado rápido

💡 **VENTAJAS DE FLASK:**
   ✅ Curva de aprendizaje suave
   ✅ Configuración mínima para empezar
   ✅ Control total sobre la aplicación
   ✅ Extensiones para funcionalidades avanzadas
   ✅ Ideal para APIs REST
   ✅ Perfecto para dashboards industriales

⚡ **CASOS DE USO EN AUTOMATIZACIÓN INDUSTRIAL:**
   🏭 Dashboards de monitoreo en tiempo real
   🏭 APIs para comunicación con PLCs
   🏭 Interfaces web para SCADA
   🏭 Sistemas de reportes automáticos
   🏭 Paneles de control remotos

📌 1.2 ARQUITECTURA DE FLASK
============================

Flask sigue el patrón arquitectónico WSGI (Web Server Gateway Interface):

┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   NAVEGADOR     │───▶│   SERVIDOR WEB  │───▶│   APLICACIÓN    │
│   (Cliente)     │    │   (Flask Dev)   │    │   (Flask App)   │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         ▲                       │                       │
         │                       ▼                       ▼
         └─────────────── HTTP Response ◀────── Python Logic

🔧 **COMPONENTES CLAVE:**
   📦 Application Object (app)
   📦 Request Context
   📦 URL Routing
   📦 Template Engine (Jinja2)
   📦 Static Files Handler

📌 1.3 COMPARACIÓN CON OTROS FRAMEWORKS
=======================================

┌──────────────┬─────────────┬─────────────┬─────────────┐
│ FRAMEWORK    │ COMPLEJIDAD │ FLEXIBILIDAD│ CURVA APREND│
├──────────────┼─────────────┼─────────────┼─────────────┤
│ Flask        │ Baja        │ Muy Alta    │ Suave       │
│ Django       │ Alta        │ Media       │ Empinada    │
│ FastAPI      │ Media       │ Alta        │ Media       │
│ Bottle       │ Muy Baja    │ Media       │ Muy Suave   │
└──────────────┴─────────────┴─────────────┴─────────────┘

🎯 **¿CUÁNDO USAR FLASK?**
   ✅ Proyectos pequeños a medianos
   ✅ APIs REST simples
   ✅ Prototipado rápido
   ✅ Dashboards personalizados
   ✅ Microservicios

===============================================================================
                  🔥 PARTE 2: CONFIGURACIÓN Y PRIMERA APLICACIÓN
===============================================================================

📌 2.1 INSTALACIÓN DE FLASK
===========================

Flask se instala fácilmente con pip:

```bash
# Instalación básica
pip install Flask

# Instalación con dependencias adicionales
pip install Flask[async]

# Verificar instalación
python -c "import flask; print(flask.__version__)"
```

📌 2.2 APLICACIÓN FLASK MÍNIMA
==============================

La aplicación Flask más simple posible:
"""

# 🚀 EJEMPLO 1: APLICACIÓN FLASK MÍNIMA
from flask import Flask

# Crear instancia de la aplicación Flask
app = Flask(__name__)

# Definir ruta principal
@app.route('/')
def home():
    """Página principal de la aplicación"""
    return '<h1>¡Hola Mundo desde Flask!</h1>'

# Ejecutar la aplicación en modo desarrollo
if __name__ == '__main__':
    app.run(debug=True)

"""
💡 **EXPLICACIÓN DEL CÓDIGO:**
   1. `Flask(__name__)`: Crea la instancia de la aplicación
   2. `@app.route('/')`: Decorador que define la URL
   3. `def home()`: Función que maneja la ruta
   4. `app.run(debug=True)`: Ejecuta el servidor de desarrollo

📌 2.3 SERVIDOR DE DESARROLLO
=============================

El servidor de desarrollo de Flask incluye:
   🔄 Recarga automática cuando cambia el código
   🐛 Debugger interactivo en el navegador
   📊 Información detallada de errores
   ⚡ Hot reload para desarrollo ágil

🔧 **CONFIGURACIÓN DEL SERVIDOR:**
"""

# 🚀 EJEMPLO 2: CONFIGURACIÓN AVANZADA DEL SERVIDOR
def create_app():
    """Factory pattern para crear la aplicación"""
    app = Flask(__name__)
    
    # Configuración para desarrollo
    app.config['DEBUG'] = True
    app.config['ENV'] = 'development'
    app.config['TESTING'] = False
    
    @app.route('/')
    def index():
        return '''
        <html>
            <head><title>Sistema de Monitoreo Industrial</title></head>
            <body>
                <h1>🏭 Dashboard Industrial</h1>
                <p>Sistema de monitoreo en tiempo real</p>
                <ul>
                    <li>📊 Sensores conectados: 15</li>
                    <li>🟢 Estado: Operativo</li>
                    <li>⏰ Última actualización: 10:30 AM</li>
                </ul>
            </body>
        </html>
        '''
    
    return app

"""
📌 2.4 CONFIGURACIÓN BÁSICA
===========================

Flask utiliza un objeto de configuración para manejar settings:
"""

# 🚀 EJEMPLO 3: CONFIGURACIÓN PROFESIONAL
import os
from flask import Flask

class Config:
    """Configuración base de la aplicación"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-super-secreta-para-desarrollo'
    DEBUG = True
    HOST = '0.0.0.0'
    PORT = 5000

class DevelopmentConfig(Config):
    """Configuración específica para desarrollo"""
    DEBUG = True
    ENV = 'development'

class ProductionConfig(Config):
    """Configuración específica para producción"""
    DEBUG = False
    ENV = 'production'

def create_configured_app():
    """Crear aplicación con configuración"""
    app = Flask(__name__)
    
    # Cargar configuración
    app.config.from_object(DevelopmentConfig)
    
    @app.route('/')
    def dashboard():
        return f'''
        <h1>🔧 Sistema de Automatización</h1>
        <p><strong>Modo:</strong> {app.config['ENV']}</p>
        <p><strong>Debug:</strong> {app.config['DEBUG']}</p>
        <p><strong>Host:</strong> {app.config['HOST']}</p>
        <p><strong>Puerto:</strong> {app.config['PORT']}</p>
        '''
    
    return app

"""
===============================================================================
                      🔥 PARTE 3: RUTAS Y MÉTODOS HTTP
===============================================================================

📌 3.1 CONCEPTOS DE ROUTING
===========================

El routing en Flask mapea URLs a funciones Python:

URL Pattern → Python Function → HTTP Response

🎯 **CARACTERÍSTICAS DEL ROUTING:**
   • Flexibilidad en el patrón de URLs
   • Soporte para parámetros dinámicos
   • Múltiples métodos HTTP por ruta
   • Validación automática de tipos

📌 3.2 RUTAS BÁSICAS
====================
"""

# 🚀 EJEMPLO 4: RUTAS BÁSICAS PARA SISTEMA INDUSTRIAL
def create_routing_app():
    """Aplicación con múltiples rutas"""
    app = Flask(__name__)
    
    @app.route('/')
    def home():
        """Página principal del sistema"""
        return '''
        <h1>🏭 Sistema de Control Industrial</h1>
        <nav>
            <a href="/dashboard">📊 Dashboard</a> |
            <a href="/sensores">🌡️ Sensores</a> |
            <a href="/reportes">📋 Reportes</a> |
            <a href="/configuracion">⚙️ Configuración</a>
        </nav>
        '''
    
    @app.route('/dashboard')
    def dashboard():
        """Dashboard principal de monitoreo"""
        return '''
        <h2>📊 Dashboard de Monitoreo</h2>
        <div>
            <h3>Estado Actual del Sistema</h3>
            <ul>
                <li>🟢 Línea de Producción 1: Operativa</li>
                <li>🟡 Línea de Producción 2: Mantenimiento</li>
                <li>🔴 Línea de Producción 3: Detenida</li>
            </ul>
        </div>
        <a href="/">← Volver al inicio</a>
        '''
    
    @app.route('/sensores')
    def sensores():
        """Lista de sensores conectados"""
        return '''
        <h2>🌡️ Sensores del Sistema</h2>
        <table border="1">
            <tr><th>ID</th><th>Tipo</th><th>Valor</th><th>Estado</th></tr>
            <tr><td>S001</td><td>Temperatura</td><td>75°C</td><td>🟢 OK</td></tr>
            <tr><td>S002</td><td>Presión</td><td>2.5 bar</td><td>🟢 OK</td></tr>
            <tr><td>S003</td><td>Flujo</td><td>150 L/min</td><td>🟡 Alerta</td></tr>
        </table>
        <a href="/">← Volver al inicio</a>
        '''
    
    return app

"""
📌 3.3 MÉTODOS HTTP (GET, POST, PUT, DELETE)
============================================

Flask soporta todos los métodos HTTP estándar:
"""

# 🚀 EJEMPLO 5: MÉTODOS HTTP PARA API DE SENSORES
from flask import request, jsonify

def create_api_app():
    """Aplicación con API REST para sensores"""
    app = Flask(__name__)
    
    # Base de datos simulada
    sensores = [
        {'id': 1, 'nombre': 'Temperatura Motor 1', 'valor': 75.5, 'unidad': '°C'},
        {'id': 2, 'nombre': 'Presión Hidráulica', 'valor': 2.3, 'unidad': 'bar'},
        {'id': 3, 'nombre': 'Velocidad Cinta', 'valor': 120, 'unidad': 'm/min'}
    ]
    
    @app.route('/api/sensores', methods=['GET'])
    def get_sensores():
        """Obtener lista de todos los sensores"""
        return jsonify({
            'success': True,
            'data': sensores,
            'total': len(sensores)
        })
    
    @app.route('/api/sensores/<int:sensor_id>', methods=['GET'])
    def get_sensor(sensor_id):
        """Obtener un sensor específico por ID"""
        sensor = next((s for s in sensores if s['id'] == sensor_id), None)
        if sensor:
            return jsonify({'success': True, 'data': sensor})
        return jsonify({'success': False, 'error': 'Sensor no encontrado'}), 404
    
    @app.route('/api/sensores', methods=['POST'])
    def create_sensor():
        """Crear un nuevo sensor"""
        data = request.get_json()
        nuevo_sensor = {
            'id': len(sensores) + 1,
            'nombre': data.get('nombre'),
            'valor': data.get('valor', 0),
            'unidad': data.get('unidad', '')
        }
        sensores.append(nuevo_sensor)
        return jsonify({'success': True, 'data': nuevo_sensor}), 201
    
    @app.route('/api/sensores/<int:sensor_id>', methods=['PUT'])
    def update_sensor(sensor_id):
        """Actualizar un sensor existente"""
        sensor = next((s for s in sensores if s['id'] == sensor_id), None)
        if not sensor:
            return jsonify({'success': False, 'error': 'Sensor no encontrado'}), 404
        
        data = request.get_json()
        sensor.update(data)
        return jsonify({'success': True, 'data': sensor})
    
    @app.route('/api/sensores/<int:sensor_id>', methods=['DELETE'])
    def delete_sensor(sensor_id):
        """Eliminar un sensor"""
        global sensores
        sensores = [s for s in sensores if s['id'] != sensor_id]
        return jsonify({'success': True, 'message': 'Sensor eliminado'})
    
    return app

"""
📌 3.4 PARÁMETROS DE URL Y QUERY STRINGS
========================================

Flask permite capturar parámetros de diferentes formas:
"""

# 🚀 EJEMPLO 6: PARÁMETROS Y QUERY STRINGS
def create_params_app():
    """Aplicación demostrando parámetros de URL"""
    app = Flask(__name__)
    
    @app.route('/plc/<string:plc_id>')
    def get_plc_info(plc_id):
        """Información de un PLC específico"""
        return f'''
        <h2>📡 Información del PLC</h2>
        <p><strong>ID del PLC:</strong> {plc_id}</p>
        <p><strong>Estado:</strong> Conectado</p>
        <p><strong>Última comunicación:</strong> 2 segundos</p>
        '''
    
    @app.route('/sensor/<int:sensor_id>/historico')
    def sensor_historico(sensor_id):
        """Histórico de un sensor con parámetros de consulta"""
        # Obtener parámetros de query string
        dias = request.args.get('dias', default=7, type=int)
        formato = request.args.get('formato', default='json')
        
        return f'''
        <h2>📈 Histórico del Sensor {sensor_id}</h2>
        <p><strong>Período:</strong> {dias} días</p>
        <p><strong>Formato:</strong> {formato}</p>
        <p><strong>URL completa:</strong> {request.url}</p>
        <p><strong>Parámetros:</strong> {dict(request.args)}</p>
        '''
    
    @app.route('/reporte/<int:year>/<int:month>')
    def reporte_mensual(year, month):
        """Reporte mensual con validación de parámetros"""
        if month < 1 or month > 12:
            return "Error: Mes inválido", 400
        
        return f'''
        <h2>📊 Reporte Mensual</h2>
        <p><strong>Año:</strong> {year}</p>
        <p><strong>Mes:</strong> {month}</p>
        <p><strong>Período:</strong> {month:02d}/{year}</p>
        '''
    
    return app

"""
===============================================================================
                            📝 NOTAS IMPORTANTES
===============================================================================

🔥 **MEJORES PRÁCTICAS HASTA AHORA:**
   ✅ Usar factory pattern para crear aplicaciones
   ✅ Separar configuración por entornos
   ✅ Implementar APIs REST bien estructuradas
   ✅ Validar parámetros de entrada
   ✅ Usar códigos de estado HTTP apropiados
   ✅ Documentar todas las rutas y funciones

⚠️ **PENDIENTE EN LA SIGUIENTE PARTE:**
   🔄 Templates con Jinja2
   🔄 Archivos estáticos (CSS, JS)
   🔄 Proyecto práctico completo
   🔄 Manejo de errores avanzado

===============================================================================
                            🎯 CHECKLIST DE PROGRESO
===============================================================================

✅ Conceptos fundamentales de Flask
✅ Instalación y configuración
✅ Aplicación mínima funcional
✅ Routing básico y avanzado
✅ Métodos HTTP (GET, POST, PUT, DELETE)
✅ Parámetros de URL y query strings
⬜ Templates con Jinja2 (Próxima parte)
⬜ Archivos estáticos (Próxima parte)
⬜ Proyecto dashboard (Próxima parte)

===============================================================================
"""

if __name__ == '__main__':
    print("🎓 MÓDULO 4.1: FLASK BÁSICO - PARTE 1 COMPLETADA")
    print("📚 Conceptos cubiertos: Introducción, configuración, rutas y métodos HTTP")
    print("🔄 Próximo: Templates con Jinja2 y archivos estáticos")
    
    # Demostrar una aplicación básica
    print("\n🚀 Iniciando aplicación de demostración...")
    demo_app = create_routing_app()
    print("💡 Visita http://localhost:5000 para ver la demo")
    demo_app.run(debug=True, port=5000)

"""
===============================================================================
                        🔥 PARTE 4: TEMPLATES CON JINJA2
===============================================================================

📌 4.1 MOTOR DE TEMPLATES JINJA2
================================

Jinja2 es el motor de templates integrado en Flask que permite:
   🎨 Separar lógica de presentación
   🔄 Reutilizar código HTML
   📊 Renderizar datos dinámicos
   🛡️ Escapado automático para seguridad

🎯 **CARACTERÍSTICAS PRINCIPALES:**
   • Sintaxis simple y clara {{ variable }}
   • Estructuras de control {% if %}, {% for %}
   • Herencia de templates {% extends %}
   • Inclusión de templates {% include %}
   • Filtros para formatear datos {{ dato|filtro }}

📌 4.2 SINTAXIS BÁSICA DE JINJA2
================================
"""

# 🚀 EJEMPLO 7: APLICACIÓN CON TEMPLATES
from flask import Flask, render_template_string, render_template
from datetime import datetime
import os

def create_template_app():
    """Aplicación demostrando templates Jinja2"""
    app = Flask(__name__)
    
    # Template básico como string
    TEMPLATE_DASHBOARD = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ titulo }} - Sistema Industrial</title>
        <style>
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                margin: 0; padding: 20px; background: #f5f6fa; 
            }
            .header { 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white; padding: 20px; border-radius: 10px; 
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }
            .card { 
                background: white; padding: 20px; margin: 15px 0; 
                border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .sensor-grid { 
                display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); 
                gap: 15px; margin: 20px 0; 
            }
            .sensor-card { 
                background: white; padding: 15px; border-radius: 8px; 
                border-left: 4px solid #3498db; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .sensor-normal { border-left-color: #27ae60; }
            .sensor-alerta { border-left-color: #f39c12; }
            .sensor-error { border-left-color: #e74c3c; }
            .timestamp { font-size: 0.9em; color: #7f8c8d; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🏭 {{ titulo }}</h1>
            <p>{{ descripcion }}</p>
            <p class="timestamp">📅 {{ timestamp }}</p>
        </div>
        
        <div class="card">
            <h2>📊 Resumen del Sistema</h2>
            <ul>
                <li><strong>Planta:</strong> {{ planta_nombre }}</li>
                <li><strong>Sensores activos:</strong> {{ sensores_total }}</li>
                <li><strong>Estado general:</strong> 
                    {% if estado == 'operativo' %}
                        🟢 Operativo
                    {% elif estado == 'mantenimiento' %}
                        🟡 En Mantenimiento
                    {% else %}
                        🔴 Con Problemas
                    {% endif %}
                </li>
            </ul>
        </div>
        
        <div class="card">
            <h2>🌡️ Estado de Sensores</h2>
            <div class="sensor-grid">
                {% for sensor in sensores %}
                <div class="sensor-card sensor-{{ sensor.estado }}">
                    <h3>{{ sensor.icono }} {{ sensor.nombre }}</h3>
                    <p><strong>Valor:</strong> {{ sensor.valor }} {{ sensor.unidad }}</p>
                    <p><strong>Estado:</strong> {{ sensor.estado|title }}</p>
                    <p class="timestamp">Última lectura: {{ sensor.timestamp }}</p>
                </div>
                {% endfor %}
            </div>
        </div>
        
        <div class="card">
            <h2>🔗 Navegación</h2>
            <nav>
                <a href="/" style="margin-right: 15px;">🏠 Inicio</a>
                <a href="/api/sensores" style="margin-right: 15px;">📡 API Sensores</a>
                <a href="/reportes" style="margin-right: 15px;">📋 Reportes</a>
            </nav>
        </div>
    </body>
    </html>
    '''
    
    @app.route('/')
    def dashboard_template():
        """Dashboard usando template Jinja2"""
        # Datos del sistema
        sistema_data = {
            'titulo': 'Dashboard de Monitoreo Industrial',
            'descripcion': 'Sistema de control y monitoreo en tiempo real',
            'timestamp': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
            'planta_nombre': 'Planta Productiva Alpha',
            'sensores_total': 8,
            'estado': 'operativo',
            'sensores': [
                {
                    'icono': '🌡️',
                    'nombre': 'Temperatura Motor Principal',
                    'valor': 75.5,
                    'unidad': '°C',
                    'estado': 'normal',
                    'timestamp': '10:30:45'
                },
                {
                    'icono': '⚡',
                    'nombre': 'Presión Sistema Hidráulico',
                    'valor': 2.3,
                    'unidad': 'bar',
                    'estado': 'normal',
                    'timestamp': '10:30:42'
                },
                {
                    'icono': '🔄',
                    'nombre': 'Velocidad Cinta Transportadora',
                    'valor': 120,
                    'unidad': 'm/min',
                    'estado': 'alerta',
                    'timestamp': '10:30:38'
                },
                {
                    'icono': '💨',
                    'nombre': 'Flujo de Aire Comprimido',
                    'valor': 6.8,
                    'unidad': 'm³/min',
                    'estado': 'normal',
                    'timestamp': '10:30:40'
                }
            ]
        }
        
        return render_template_string(TEMPLATE_DASHBOARD, **sistema_data)
    
    return app

"""
📌 4.3 HERENCIA DE TEMPLATES
=============================

La herencia permite crear un template base y extenderlo:
"""

# 🚀 EJEMPLO 8: SISTEMA DE TEMPLATES CON HERENCIA
def create_advanced_template_app():
    """Aplicación con sistema avanzado de templates"""
    app = Flask(__name__)
    
    # Template base
    BASE_TEMPLATE = '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{% block title %}Sistema Industrial{% endblock %}</title>
        <style>
            {% block styles %}
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: #f8f9fa; min-height: 100vh;
            }
            .navbar {
                background: #2c3e50; color: white; padding: 15px 20px;
                display: flex; justify-content: space-between; align-items: center;
            }
            .navbar a { color: white; text-decoration: none; margin: 0 10px; }
            .navbar a:hover { color: #3498db; }
            .container { max-width: 1200px; margin: 20px auto; padding: 0 20px; }
            .footer { 
                background: #34495e; color: white; text-align: center; 
                padding: 20px; margin-top: 40px; 
            }
            {% endblock %}
        </style>
    </head>
    <body>
        <nav class="navbar">
            <div>
                <strong>🏭 {{ config.get('PLANT_NAME', 'Sistema Industrial') }}</strong>
            </div>
            <div>
                {% block navigation %}
                <a href="/">🏠 Inicio</a>
                <a href="/sensores">🌡️ Sensores</a>
                <a href="/reportes">📊 Reportes</a>
                <a href="/configuracion">⚙️ Config</a>
                {% endblock %}
            </div>
        </nav>
        
        <div class="container">
            {% block content %}
            <h1>Contenido por defecto</h1>
            {% endblock %}
        </div>
        
        <footer class="footer">
            {% block footer %}
            <p>&copy; 2025 Sistema de Automatización Industrial | 
               Última actualización: {{ moment().format('DD/MM/YYYY HH:mm') }}</p>
            {% endblock %}
        </footer>
    </body>
    </html>
    '''
    
    # Template para sensores que extiende la base
    SENSORES_TEMPLATE = '''
    {% extends "base.html" %}
    
    {% block title %}Sensores - {{ super() }}{% endblock %}
    
    {% block styles %}
    {{ super() }}
    .sensor-grid { 
        display: grid; 
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); 
        gap: 20px; 
        margin: 20px 0; 
    }
    .sensor-card { 
        background: white; 
        padding: 20px; 
        border-radius: 10px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #3498db;
    }
    .sensor-normal { border-left-color: #27ae60; }
    .sensor-alerta { border-left-color: #f39c12; }
    .sensor-error { border-left-color: #e74c3c; }
    .sensor-header { display: flex; justify-content: space-between; align-items: center; }
    .sensor-value { font-size: 2em; font-weight: bold; color: #2c3e50; }
    {% endblock %}
    
    {% block content %}
    <h1>🌡️ Monitoreo de Sensores</h1>
    
    <div class="sensor-grid">
        {% for sensor in sensores %}
        <div class="sensor-card sensor-{{ sensor.estado }}">
            <div class="sensor-header">
                <h3>{{ sensor.icono }} {{ sensor.nombre }}</h3>
                <span style="background: 
                    {%- if sensor.estado == 'normal' -%}#27ae60
                    {%- elif sensor.estado == 'alerta' -%}#f39c12
                    {%- else -%}#e74c3c{%- endif -%}; 
                    color: white; padding: 5px 10px; border-radius: 20px; font-size: 0.8em;">
                    {{ sensor.estado|upper }}
                </span>
            </div>
            
            <div style="margin: 15px 0;">
                <div class="sensor-value">{{ sensor.valor }} {{ sensor.unidad }}</div>
                <p style="color: #7f8c8d; font-size: 0.9em;">
                    Rango: {{ sensor.min_val }} - {{ sensor.max_val }} {{ sensor.unidad }}
                </p>
            </div>
            
            <div style="border-top: 1px solid #ecf0f1; padding-top: 10px; margin-top: 15px;">
                <small>
                    <strong>Última lectura:</strong> {{ sensor.timestamp }}<br>
                    <strong>Ubicación:</strong> {{ sensor.ubicacion }}
                </small>
            </div>
        </div>
        {% endfor %}
    </div>
    
    {% if sensores|length == 0 %}
    <div style="text-align: center; padding: 40px; background: white; border-radius: 10px;">
        <h3>📡 No hay sensores disponibles</h3>
        <p>Verifique la conexión con los dispositivos</p>
    </div>
    {% endif %}
    {% endblock %}
    '''
    
    @app.route('/')
    def home():
        """Página principal"""
        return render_template_string(BASE_TEMPLATE)
    
    @app.route('/sensores')
    def sensores():
        """Página de sensores con template avanzado"""
        sensores_data = [
            {
                'icono': '🌡️', 'nombre': 'Temperatura Motor A',
                'valor': 78.5, 'unidad': '°C', 'estado': 'normal',
                'min_val': 60, 'max_val': 90, 'timestamp': '10:45:22',
                'ubicacion': 'Sector A - Motor Principal'
            },
            {
                'icono': '⚡', 'nombre': 'Presión Hidráulica',
                'valor': 2.8, 'unidad': 'bar', 'estado': 'alerta',
                'min_val': 1.5, 'max_val': 3.0, 'timestamp': '10:45:18',
                'ubicacion': 'Sistema Hidráulico Central'
            },
            {
                'icono': '🔄', 'nombre': 'RPM Motor B',
                'valor': 1850, 'unidad': 'rpm', 'estado': 'normal',
                'min_val': 1200, 'max_val': 2000, 'timestamp': '10:45:20',
                'ubicacion': 'Sector B - Motor Secundario'
            },
            {
                'icono': '💨', 'nombre': 'Flujo de Aire',
                'valor': 0.2, 'unidad': 'm³/s', 'estado': 'error',
                'min_val': 0.5, 'max_val': 1.2, 'timestamp': '10:43:15',
                'ubicacion': 'Sistema de Ventilación'
            }
        ]
        
        # Función personalizada para templates
        def moment():
            return datetime.now()
        
        # Agregar función al contexto del template
        context = {
            'sensores': sensores_data,
            'moment': moment
        }
        
        return render_template_string(SENSORES_TEMPLATE, **context)
    
    return app

"""
📌 4.4 FILTROS Y FUNCIONES PERSONALIZADAS
==========================================

Jinja2 permite crear filtros personalizados para formatear datos:
"""

# 🚀 EJEMPLO 9: FILTROS PERSONALIZADOS PARA INDUSTRIA
def create_filtered_app():
    """Aplicación con filtros personalizados"""
    app = Flask(__name__)
    
    # Filtros personalizados
    @app.template_filter('formato_numero')
    def formato_numero(valor):
        """Formatear números con separadores de miles"""
        return f"{valor:,.2f}".replace(',', '.')
    
    @app.template_filter('estado_color')
    def estado_color(estado):
        """Convertir estado a color CSS"""
        colores = {
            'normal': '#27ae60',
            'alerta': '#f39c12', 
            'error': '#e74c3c',
            'mantenimiento': '#8e44ad'
        }
        return colores.get(estado.lower(), '#95a5a6')
    
    @app.template_filter('tiempo_relativo')
    def tiempo_relativo(timestamp):
        """Convertir timestamp a tiempo relativo"""
        # Simulación - en aplicación real usarías datetime
        return "hace 2 minutos"
    
    # Funciones globales para templates
    @app.template_global('calcular_eficiencia')
    def calcular_eficiencia(valor_actual, valor_maximo):
        """Calcular eficiencia como porcentaje"""
        return round((valor_actual / valor_maximo) * 100, 1)
    
    TEMPLATE_CON_FILTROS = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sistema con Filtros Personalizados</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .metric { 
                background: white; padding: 15px; margin: 10px 0; 
                border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                border-left: 4px solid {{ sensor.estado|estado_color }};
            }
            .valor-grande { font-size: 2em; font-weight: bold; }
            .eficiencia { 
                background: linear-gradient(90deg, #3498db 0%, #3498db {{ eficiencia }}%, #ecf0f1 {{ eficiencia }}%);
                height: 20px; border-radius: 10px; margin: 10px 0;
            }
        </style>
    </head>
    <body>
        <h1>📊 Dashboard con Filtros Personalizados</h1>
        
        {% for sensor in sensores %}
        {% set eficiencia = calcular_eficiencia(sensor.valor, sensor.valor_max) %}
        <div class="metric">
            <h3>{{ sensor.nombre }}</h3>
            <div class="valor-grande" style="color: {{ sensor.estado|estado_color }};">
                {{ sensor.valor|formato_numero }} {{ sensor.unidad }}
            </div>
            
            <div>
                <strong>Eficiencia:</strong> {{ eficiencia }}%
                <div class="eficiencia"></div>
            </div>
            
            <p>
                <strong>Estado:</strong> 
                <span style="color: {{ sensor.estado|estado_color }};">
                    {{ sensor.estado|title }}
                </span> | 
                <strong>Actualizado:</strong> {{ sensor.timestamp|tiempo_relativo }}
            </p>
        </div>
        {% endfor %}
        
        <div style="margin-top: 30px; padding: 20px; background: #f8f9fa; border-radius: 8px;">
            <h3>📈 Resumen General</h3>
            <ul>
                <li>Total de sensores: {{ sensores|length }}</li>
                <li>Sensores normales: {{ sensores|selectattr('estado', 'equalto', 'normal')|list|length }}</li>
                <li>Sensores en alerta: {{ sensores|selectattr('estado', 'equalto', 'alerta')|list|length }}</li>
                <li>Valor promedio: {{ (sensores|sum(attribute='valor') / sensores|length)|formato_numero }}</li>
            </ul>
        </div>
    </body>
    </html>
    '''
    
    @app.route('/')
    def dashboard_filtros():
        """Dashboard usando filtros personalizados"""
        sensores_data = [
            {
                'nombre': 'Temperatura Horno Principal',
                'valor': 850.75, 'unidad': '°C', 'valor_max': 1000,
                'estado': 'normal', 'timestamp': '2025-07-05 10:45:00'
            },
            {
                'nombre': 'Presión Sistema Vapor',
                'valor': 12.5, 'unidad': 'bar', 'valor_max': 15,
                'estado': 'alerta', 'timestamp': '2025-07-05 10:44:30'
            },
            {
                'nombre': 'Velocidad Turbina',
                'valor': 3600, 'unidad': 'rpm', 'valor_max': 4000,
                'estado': 'normal', 'timestamp': '2025-07-05 10:45:15'
            }
        ]
        
        return render_template_string(TEMPLATE_CON_FILTROS, sensores=sensores_data)
    
    return app

"""
===============================================================================
                        🔥 PARTE 5: ARCHIVOS ESTÁTICOS
===============================================================================

📌 5.1 ORGANIZACIÓN DE ARCHIVOS ESTÁTICOS
==========================================

Flask busca archivos estáticos en la carpeta 'static' por defecto:

proyecto/
├── app.py
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── app.js
│   └── img/
│       └── logo.png
└── templates/
    └── base.html

📌 5.2 URLS PARA ARCHIVOS ESTÁTICOS
===================================

Flask provee la función url_for() para generar URLs:
   {{ url_for('static', filename='css/styles.css') }}
   {{ url_for('static', filename='js/app.js') }}
"""

# 🚀 EJEMPLO 10: APLICACIÓN CON ARCHIVOS ESTÁTICOS COMPLETOS
def create_static_app():
    """Aplicación con archivos estáticos profesionales"""
    app = Flask(__name__)
    
    # CSS inline para demostración (en producción estaría en archivo separado)
    INDUSTRIAL_CSS = '''
    :root {
        --primary-color: #2c3e50;
        --secondary-color: #3498db;
        --success-color: #27ae60;
        --warning-color: #f39c12;
        --danger-color: #e74c3c;
        --light-bg: #f8f9fa;
        --dark-bg: #2c3e50;
        --border-radius: 8px;
        --box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }

    body {
        font-family: 'Roboto', 'Segoe UI', sans-serif;
        background-color: var(--light-bg);
        color: #2c3e50;
        line-height: 1.6;
    }

    .header {
        background: linear-gradient(135deg, var(--primary-color) 0%, var(--secondary-color) 100%);
        color: white;
        padding: 20px 0;
        box-shadow: var(--box-shadow);
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 20px;
    }

    .nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .nav-links {
        display: flex;
        gap: 20px;
    }

    .nav-links a {
        color: white;
        text-decoration: none;
        padding: 8px 16px;
        border-radius: var(--border-radius);
        transition: background-color 0.3s ease;
    }

    .nav-links a:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }

    .dashboard-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }

    .card {
        background: white;
        border-radius: var(--border-radius);
        box-shadow: var(--box-shadow);
        padding: 20px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }

    .sensor-status {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 15px;
    }

    .status-indicator {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }

    .status-normal { background-color: var(--success-color); }
    .status-warning { background-color: var(--warning-color); }
    .status-error { background-color: var(--danger-color); }

    .metric-value {
        font-size: 2.5em;
        font-weight: bold;
        color: var(--primary-color);
        margin: 10px 0;
    }

    .progress-bar {
        background-color: #e9ecef;
        border-radius: 10px;
        height: 8px;
        overflow: hidden;
        margin: 10px 0;
    }

    .progress-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 0.3s ease;
    }

    .btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: var(--secondary-color);
        color: white;
        text-decoration: none;
        border-radius: var(--border-radius);
        transition: background-color 0.3s ease;
        border: none;
        cursor: pointer;
    }

    .btn:hover {
        background-color: #2980b9;
    }

    .alert {
        padding: 15px;
        margin: 20px 0;
        border-radius: var(--border-radius);
        border-left: 4px solid;
    }

    .alert-warning {
        background-color: #fff3cd;
        border-left-color: var(--warning-color);
        color: #856404;
    }

    .alert-danger {
        background-color: #f8d7da;
        border-left-color: var(--danger-color);
        color: #721c24;
    }

    @media (max-width: 768px) {
        .dashboard-grid {
            grid-template-columns: 1fr;
        }
        
        .nav {
            flex-direction: column;
            gap: 15px;
        }
    }
    '''
    
    # JavaScript inline para demostración
    INDUSTRIAL_JS = '''
    // Sistema de Monitoreo Industrial - JavaScript
    class IndustrialDashboard {
        constructor() {
            this.sensores = [];
            this.intervalos = [];
            this.init();
        }
        
        init() {
            console.log('🏭 Iniciando Dashboard Industrial');
            this.cargarSensores();
            this.iniciarActualizacionAutomatica();
            this.configurarEventos();
        }
        
        cargarSensores() {
            // Simulación de datos de sensores
            this.sensores = [
                {id: 1, nombre: 'Temperatura', valor: 75.5, max: 100, estado: 'normal'},
                {id: 2, nombre: 'Presión', valor: 2.3, max: 5, estado: 'normal'},
                {id: 3, nombre: 'Velocidad', valor: 1850, max: 2000, estado: 'warning'},
                {id: 4, nombre: 'Flujo', valor: 0.5, max: 2, estado: 'error'}
            ];
        }
        
        actualizarDatos() {
            this.sensores.forEach(sensor => {
                // Simular variación en los datos
                const variacion = (Math.random() - 0.5) * 0.1;
                sensor.valor = Math.max(0, sensor.valor + (sensor.valor * variacion));
                
                // Actualizar estado basado en valor
                const porcentaje = (sensor.valor / sensor.max) * 100;
                if (porcentaje > 90) sensor.estado = 'error';
                else if (porcentaje > 75) sensor.estado = 'warning';
                else sensor.estado = 'normal';
            });
            
            this.renderizarSensores();
        }
        
        renderizarSensores() {
            const container = document.getElementById('sensores-container');
            if (!container) return;
            
            container.innerHTML = this.sensores.map(sensor => {
                const porcentaje = Math.min((sensor.valor / sensor.max) * 100, 100);
                const colorClase = `status-${sensor.estado}`;
                
                return `
                    <div class="card">
                        <div class="sensor-status">
                            <h3>🌡️ ${sensor.nombre}</h3>
                            <div class="status-indicator ${colorClase}"></div>
                        </div>
                        <div class="metric-value">${sensor.valor.toFixed(2)}</div>
                        <div class="progress-bar">
                            <div class="progress-fill ${colorClase}" 
                                 style="width: ${porcentaje}%; background-color: var(--${sensor.estado === 'normal' ? 'success' : sensor.estado === 'warning' ? 'warning' : 'danger'}-color);"></div>
                        </div>
                        <p>Estado: <strong>${sensor.estado.toUpperCase()}</strong></p>
                        <button class="btn" onclick="dashboard.calibrarSensor(${sensor.id})">
                            Calibrar
                        </button>
                    </div>
                `;
            }).join('');
        }
        
        calibrarSensor(sensorId) {
            const sensor = this.sensores.find(s => s.id === sensorId);
            if (sensor) {
                sensor.valor = sensor.max * 0.5; // Calibrar a 50%
                sensor.estado = 'normal';
                this.renderizarSensores();
                this.mostrarNotificacion(`Sensor ${sensor.nombre} calibrado`, 'success');
            }
        }
        
        mostrarNotificacion(mensaje, tipo = 'info') {
            const notificacion = document.createElement('div');
            notificacion.className = `alert alert-${tipo}`;
            notificacion.textContent = mensaje;
            
            document.body.appendChild(notificacion);
            
            setTimeout(() => {
                notificacion.remove();
            }, 3000);
        }
        
        iniciarActualizacionAutomatica() {
            // Actualizar cada 5 segundos
            const intervalo = setInterval(() => {
                this.actualizarDatos();
            }, 5000);
            
            this.intervalos.push(intervalo);
        }
        
        configurarEventos() {
            // Configurar eventos del DOM
            document.addEventListener('DOMContentLoaded', () => {
                this.renderizarSensores();
            });
            
            // Manejar visibilidad de la página
            document.addEventListener('visibilitychange', () => {
                if (document.hidden) {
                    console.log('Dashboard pausado');
                } else {
                    console.log('Dashboard reanudado');
                    this.actualizarDatos();
                }
            });
        }
        
        destruir() {
            this.intervalos.forEach(clearInterval);
            console.log('Dashboard destruido');
        }
    }
    
    // Inicializar dashboard
    const dashboard = new IndustrialDashboard();
    
    // Funciones utilitarias
    function exportarDatos() {
        const datos = JSON.stringify(dashboard.sensores, null, 2);
        const blob = new Blob([datos], {type: 'application/json'});
        const url = URL.createObjectURL(blob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = 'sensores_data.json';
        a.click();
        
        URL.revokeObjectURL(url);
    }
    
    function alternarTema() {
        document.body.classList.toggle('tema-oscuro');
    }
    '''
    
    # Template principal con archivos estáticos
    TEMPLATE_CON_ESTATICOS = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dashboard Industrial Profesional</title>
        
        <!-- CSS Inline (en producción estaría en archivo separado) -->
        <style>{INDUSTRIAL_CSS}</style>
        
        <!-- Google Fonts -->
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
    </head>
    <body>
        <header class="header">
            <div class="container">
                <nav class="nav">
                    <div>
                        <h1>🏭 Sistema Industrial Avanzado</h1>
                        <p>Dashboard de Monitoreo en Tiempo Real</p>
                    </div>
                    <div class="nav-links">
                        <a href="/">🏠 Inicio</a>
                        <a href="/sensores">📊 Sensores</a>
                        <a href="/reportes">📋 Reportes</a>
                        <a href="#" onclick="exportarDatos()">💾 Exportar</a>
                        <a href="#" onclick="alternarTema()">🌙 Tema</a>
                    </div>
                </nav>
            </div>
        </header>
        
        <main class="container">
            <div class="alert alert-warning">
                ⚠️ <strong>Atención:</strong> El sensor de flujo presenta valores anómalos. 
                Se recomienda inspección técnica.
            </div>
            
            <div id="sensores-container" class="dashboard-grid">
                <!-- Los sensores se cargarán dinámicamente con JavaScript -->
            </div>
            
            <div class="card">
                <h2>📈 Estadísticas del Sistema</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-top: 20px;">
                    <div>
                        <h4>Tiempo de Operación</h4>
                        <div class="metric-value" style="font-size: 1.5em;">247:32:15</div>
                    </div>
                    <div>
                        <h4>Eficiencia General</h4>
                        <div class="metric-value" style="font-size: 1.5em; color: var(--success-color);">87.3%</div>
                    </div>
                    <div>
                        <h4>Alarmas Activas</h4>
                        <div class="metric-value" style="font-size: 1.5em; color: var(--warning-color);">3</div>
                    </div>
                    <div>
                        <h4>Próximo Mantenimiento</h4>
                        <div class="metric-value" style="font-size: 1.2em;">En 5 días</div>
                    </div>
                </div>
            </div>
        </main>
        
        <!-- JavaScript Inline (en producción estaría en archivo separado) -->
        <script>{INDUSTRIAL_JS}</script>
    </body>
    </html>
    '''
    
    @app.route('/')
    def dashboard_profesional():
        """Dashboard profesional con archivos estáticos"""
        return render_template_string(TEMPLATE_CON_ESTATICOS)
    
    return app

"""
===============================================================================
                            📝 RESUMEN PARTE 2
===============================================================================

🔥 **CONCEPTOS AGREGADOS:**
   ✅ Motor de templates Jinja2
   ✅ Sintaxis básica de templates
   ✅ Herencia de templates
   ✅ Filtros y funciones personalizadas
   ✅ Archivos estáticos (CSS, JavaScript)
   ✅ Dashboard profesional completo

⚠️ **PENDIENTE EN LA SIGUIENTE FRACCIÓN:**
   🔄 Notebook de prácticas
   🔄 Proyecto dashboard industrial completo
   🔄 Ejercicios de consolidación
   🔄 Commit y documentación final

===============================================================================
"""

# 🚀 PROYECTO PRÁCTICO: DASHBOARD INDUSTRIAL COMPLETO
# ================================================================

print("""
🚀 PROYECTO PRÁCTICO: DASHBOARD INDUSTRIAL COMPLETO
==================================================

🎯 OBJETIVO: Crear un dashboard web completo para monitorear 
   datos industriales en tiempo real, aplicando todos los 
   conceptos aprendidos en Flask básico.

📊 CARACTERÍSTICAS:
   ✅ Múltiples páginas (Inicio, Sensores, Alertas, Configuración)
   ✅ Datos simulados de sensores industriales
   ✅ Interfaz moderna con Bootstrap
   ✅ Navegación intuitiva
   ✅ Responsive design
   ✅ API REST para datos en tiempo real

🏗️ ESTRUCTURA DEL PROYECTO:
dashboard_industrial/
│
├── app.py                    # Aplicación principal
├── requirements.txt          # Dependencias
│
├── templates/
│   ├── base.html            # Template base
│   ├── index.html           # Página principal
│   ├── sensores.html        # Dashboard de sensores
│   ├── alertas.html         # Gestión de alertas
│   └── configuracion.html   # Configuración del sistema
│
├── static/
│   ├── css/
│   │   └── style.css        # Estilos personalizados
│   ├── js/
│   │   └── dashboard.js     # JavaScript para interactividad
│   └── img/
│       └── logo.png         # Logo de la empresa
│
└── data/
    └── sensores.json        # Datos simulados de sensores
""")

# APLICACIÓN PRINCIPAL (app.py)
# ==============================

dashboard_app_code = '''
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import random
import json

app = Flask(__name__)

# 📊 DATOS SIMULADOS DE SENSORES INDUSTRIALES
def generar_datos_sensores():
    """Genera datos simulados de sensores industriales"""
    sensores = {
        'temperatura': {
            'valor': round(random.uniform(18.0, 85.0), 1),
            'unidad': '°C',
            'limite_min': 20.0,
            'limite_max': 80.0,
            'estado': 'normal'
        },
        'presion': {
            'valor': round(random.uniform(0.5, 15.0), 2),
            'unidad': 'Bar',
            'limite_min': 1.0,
            'limite_max': 12.0,
            'estado': 'normal'
        },
        'humedad': {
            'valor': round(random.uniform(30.0, 95.0), 1),
            'unidad': '%',
            'limite_min': 40.0,
            'limite_max': 80.0,
            'estado': 'normal'
        },
        'vibracion': {
            'valor': round(random.uniform(0.1, 5.0), 2),
            'unidad': 'mm/s',
            'limite_min': 0.2,
            'limite_max': 4.0,
            'estado': 'normal'
        }
    }
    
    # Evaluar estados
    for sensor, datos in sensores.items():
        if datos['valor'] < datos['limite_min'] or datos['valor'] > datos['limite_max']:
            datos['estado'] = 'alerta'
    
    return sensores

# 🏠 RUTA PRINCIPAL
@app.route('/')
def inicio():
    """Página principal del dashboard"""
    datos_sensores = generar_datos_sensores()
    return render_template('index.html', 
                         sensores=datos_sensores,
                         timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# 📊 RUTA DE SENSORES
@app.route('/sensores')
def sensores():
    """Dashboard de sensores"""
    datos_sensores = generar_datos_sensores()
    return render_template('sensores.html', sensores=datos_sensores)

# 🚨 RUTA DE ALERTAS
@app.route('/alertas')
def alertas():
    """Gestión de alertas"""
    datos_sensores = generar_datos_sensores()
    alertas_activas = []
    
    for nombre, datos in datos_sensores.items():
        if datos['estado'] == 'alerta':
            alertas_activas.append({
                'sensor': nombre.title(),
                'valor': datos['valor'],
                'unidad': datos['unidad'],
                'tipo': 'Fuera de rango',
                'timestamp': datetime.now().strftime('%H:%M:%S')
            })
    
    return render_template('alertas.html', alertas=alertas_activas)

# ⚙️ RUTA DE CONFIGURACIÓN
@app.route('/configuracion', methods=['GET', 'POST'])
def configuracion():
    """Configuración del sistema"""
    if request.method == 'POST':
        # Aquí se procesarían los cambios de configuración
        return jsonify({'status': 'success', 'mensaje': 'Configuración guardada'})
    
    return render_template('configuracion.html')

# 🔄 API PARA DATOS EN TIEMPO REAL
@app.route('/api/sensores')
def api_sensores():
    """API REST para obtener datos de sensores"""
    return jsonify(generar_datos_sensores())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''

print("📄 CÓDIGO DE LA APLICACIÓN PRINCIPAL:")
print("="*50)
print(dashboard_app_code)

# TEMPLATE BASE (base.html)
# =========================

base_template = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Dashboard Industrial{% endblock %}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
    <!-- CSS Personalizado -->
    <link href="{{ url_for('static', filename='css/style.css') }}" rel="stylesheet">
</head>
<body>
    <!-- 🧭 NAVEGACIÓN -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{{ url_for('inicio') }}">
                <i class="fas fa-industry"></i> Dashboard Industrial
            </a>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('inicio') }}">
                            <i class="fas fa-home"></i> Inicio
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('sensores') }}">
                            <i class="fas fa-thermometer-half"></i> Sensores
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('alertas') }}">
                            <i class="fas fa-exclamation-triangle"></i> Alertas
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{{ url_for('configuracion') }}">
                            <i class="fas fa-cog"></i> Configuración
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- 📄 CONTENIDO PRINCIPAL -->
    <main class="container mt-4">
        {% block content %}{% endblock %}
    </main>

    <!-- 📜 FOOTER -->
    <footer class="bg-light text-center py-3 mt-5">
        <div class="container">
            <p class="mb-0">&copy; 2025 Dashboard Industrial - Desarrollado con Flask</p>
        </div>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <!-- Chart.js para gráficos -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- JavaScript personalizado -->
    <script src="{{ url_for('static', filename='js/dashboard.js') }}"></script>
    
    {% block scripts %}{% endblock %}
</body>
</html>
'''

print("\n📄 TEMPLATE BASE (templates/base.html):")
print("="*50)
print(base_template)

# ESTILOS CSS PERSONALIZADOS
# ===========================

css_styles = '''
/* 🎨 ESTILOS PERSONALIZADOS PARA DASHBOARD INDUSTRIAL */

:root {
    --primary-color: #0d6efd;
    --success-color: #198754;
    --warning-color: #ffc107;
    --danger-color: #dc3545;
    --dark-color: #212529;
    --light-color: #f8f9fa;
}

/* 📱 RESPONSIVE DESIGN */
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background-color: var(--light-color);
}

/* 🧭 NAVEGACIÓN */
.navbar-brand {
    font-weight: bold;
    font-size: 1.3rem;
}

/* 📊 TARJETAS */
.card {
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
    border: 1px solid rgba(0, 0, 0, 0.125);
    transition: all 0.3s ease;
}

.card:hover {
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
    transform: translateY(-2px);
}

/* 🎯 BADGES PERSONALIZADOS */
.badge {
    font-size: 0.8em;
    padding: 0.375rem 0.75rem;
}

/* 📊 PROGRESS BARS */
.progress {
    background-color: #e9ecef;
    border-radius: 0.375rem;
    height: 8px;
    overflow: hidden;
    margin: 10px 0;
}

/* 🚨 ALERTAS */
.alert {
    border: none;
    border-radius: 0.5rem;
}

/* 📱 RESPONSIVE TABLES */
@media (max-width: 768px) {
    .table-responsive {
        font-size: 0.875rem;
    }
}

/* 🎨 ANIMACIONES */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.fade-in {
    animation: fadeIn 0.5s ease-in;
}

/* 🔄 LOADING SPINNER */
.spinner {
    display: inline-block;
    width: 20px;
    height: 20px;
    border: 3px solid #f3f3f3;
    border-top: 3px solid var(--primary-color);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
'''

print("\n🎨 CSS PERSONALIZADO (static/css/style.css):")
print("="*50)
print(css_styles)

# JAVASCRIPT PERSONALIZADO
# =========================

js_code = '''
// 📜 JAVASCRIPT PARA DASHBOARD INDUSTRIAL

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Dashboard Industrial cargado');
    
    // 🔄 Auto-refresh de datos
    initAutoRefresh();
    
    // 📊 Inicializar gráficos
    initCharts();
    
    // 🎨 Animaciones
    addFadeInAnimation();
});

// 🔄 AUTO-REFRESH DE DATOS
function initAutoRefresh() {
    const refreshInterval = 30000; // 30 segundos
    
    setInterval(() => {
        if (window.location.pathname === '/') {
            console.log('🔄 Actualizando datos...');
            fetchSensorData();
        }
    }, refreshInterval);
}

// 📊 OBTENER DATOS DE SENSORES VIA API
async function fetchSensorData() {
    try {
        const response = await fetch('/api/sensores');
        const data = await response.json();
        
        // Actualizar tarjetas de sensores
        updateSensorCards(data);
        
        console.log('✅ Datos actualizados');
    } catch (error) {
        console.error('❌ Error al obtener datos:', error);
        showNotification('Error al actualizar datos', 'error');
    }
}

// 📊 ACTUALIZAR TARJETAS DE SENSORES
function updateSensorCards(sensores) {
    Object.entries(sensores).forEach(([nombre, datos]) => {
        const card = document.querySelector(`[data-sensor="${nombre}"]`);
        if (card) {
            // Actualizar valor
            const valueElement = card.querySelector('.sensor-value');
            if (valueElement) {
                valueElement.textContent = `${datos.valor} ${datos.unidad}`;
                valueElement.className = datos.estado === 'alerta' ? 'text-danger' : 'text-success';
            }
            
            // Actualizar badge de estado
            const badgeElement = card.querySelector('.badge');
            if (badgeElement) {
                badgeElement.textContent = datos.estado.charAt(0).toUpperCase() + datos.estado.slice(1);
                badgeElement.className = datos.estado === 'alerta' ? 'badge bg-danger' : 'badge bg-success';
            }
        }
    });
}

// 📊 INICIALIZAR GRÁFICOS
function initCharts() {
    // Aquí se inicializarían los gráficos con Chart.js
    console.log('📊 Gráficos inicializados');
}

// 🎨 ANIMACIONES FADE-IN
function addFadeInAnimation() {
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('fade-in');
        }, index * 100);
    });
}

// 🔔 NOTIFICACIONES
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
    notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
    
    notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    document.body.appendChild(notification);
    
    // Auto-remove después de 5 segundos
    setTimeout(() => {
        if (notification.parentNode) {
            notification.remove();
        }
    }, 5000);
}

// 📊 UTILIDADES PARA GRÁFICOS
function createSensorChart(canvasId, data) {
    const ctx = document.getElementById(canvasId);
    if (!ctx) return;
    
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['10:00', '10:30', '11:00', '11:30', '12:00'],
            datasets: [{
                label: 'Valor',
                data: data,
                borderColor: '#0d6efd',
                backgroundColor: 'rgba(13, 110, 253, 0.1)',
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}
'''

print("\n📜 JAVASCRIPT PERSONALIZADO (static/js/dashboard.js):")
print("="*50)
print(js_code)

print("""
🚀 INSTRUCCIONES PARA EJECUTAR EL PROYECTO:
==========================================

1. 📋 Crear la estructura de directorios:
   mkdir dashboard_industrial
   cd dashboard_industrial
   mkdir templates static static/css static/js static/img data

2. 📄 Crear el archivo principal app.py con el código Python

3. 📄 Crear los templates HTML en la carpeta templates/

4. 📄 Crear los archivos CSS y JS en las carpetas static/

5. 📦 Instalar dependencias:
   pip install flask

6. 🚀 Ejecutar la aplicación:
   python app.py

7. 🌐 Abrir el navegador en: http://localhost:5000

🎯 CARACTERÍSTICAS IMPLEMENTADAS:
================================
✅ Página principal con resumen de sensores
✅ Dashboard de sensores con visualización detallada
✅ Sistema de alertas automático
✅ Página de configuración
✅ API REST para datos en tiempo real
✅ Diseño responsive con Bootstrap
✅ Interfaz moderna y profesional
✅ Auto-refresh cada 30 segundos

📚 CONCEPTOS APLICADOS:
======================
✅ Rutas y URLs (múltiples endpoints)
✅ Métodos HTTP (GET, POST)
✅ Templates Jinja2 (herencia, variables, filtros, loops)
✅ Archivos estáticos (CSS, JavaScript, imágenes)
✅ API REST (endpoint JSON)
✅ Bootstrap (grid system, componentes, responsividad)
✅ JavaScript (interactividad, AJAX, actualización automática)
✅ Enfoque industrial (monitoreo de sensores, alertas, dashboards)

🎉 ¡MÓDULO 4.1 FLASK BÁSICO COMPLETADO!
======================================

¿Estás listo para practicar con los ejercicios del notebook de prácticas
y luego avanzar al Módulo 4.2 - Flask Intermedio?
""")

# ================================================================
# 🎯 CHECKLIST DE CONSOLIDACIÓN MÓDULO 4.1
# ================================================================

print("""
✅ CHECKLIST DE CONSOLIDACIÓN MÓDULO 4.1:
=========================================

📋 Conocimientos Adquiridos:
□ Entiendo qué es Flask y sus ventajas
□ Puedo crear rutas básicas y avanzadas
□ Domino los métodos HTTP (GET, POST, PUT, DELETE)
□ Manejo templates con Jinja2 (variables, loops, herencia)
□ Integro archivos estáticos (CSS, JS, imágenes)
□ Creo APIs REST básicas
□ Implemento dashboards completos

🛠️ Habilidades Prácticas:
□ Configurar un proyecto Flask desde cero
□ Crear estructura de directorios profesional
□ Diseñar templates HTML reutilizables
□ Implementar sistemas de navegación
□ Crear interfaces responsive
□ Integrar bibliotecas externas (Bootstrap, Chart.js)

🏭 Aplicaciones Industriales:
□ Monitorear sensores industriales
□ Crear dashboards de supervisión
□ Implementar sistemas de alertas
□ Diseñar interfaces para operadores
□ Gestionar datos en tiempo real

🚀 PROYECTO COMPLETADO: Dashboard Industrial Básico
""")
