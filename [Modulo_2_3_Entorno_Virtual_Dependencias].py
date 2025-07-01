"""
🎯 MÓDULO 2.3: ENTORNO VIRTUAL Y GESTIÓN DE DEPENDENCIAS
📚 PYTHON PARA AUTOMATIZACIÓN INDUSTRIAL
==================================================

📋 OBJETIVOS DE APRENDIZAJE:
• Comprender la importancia de los entornos virtuales en Python
• Dominar venv para crear y gestionar entornos aislados
• Gestionar dependencias con pip y requirements.txt
• Estructurar proyectos Python de forma profesional
• Aplicar buenas prácticas de desarrollo industrial

🎯 PROYECTO DEL MÓDULO: Setup completo de proyecto de automatización

⚠️  ADVERTENCIA CRÍTICA:
Sin entornos virtuales, tus proyectos pueden sufrir conflictos de dependencias
que causen fallos inesperados en producción. Es FUNDAMENTAL dominar este tema.

═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 1: CONCEPTOS FUNDAMENTALES DE ENTORNOS VIRTUALES
# ═══════════════════════════════════════════════════════════════════════════════

"""
🔍 ¿QUÉ ES UN ENTORNO VIRTUAL?

🏭 ANALOGÍA INDUSTRIAL:
Imagina una fábrica donde cada línea de producción necesita herramientas específicas.
Si mezclamos todas las herramientas en un almacén común:
- Las herramientas se pierden
- Versiones incompatibles causan problemas
- Un cambio afecta todas las líneas

Un ENTORNO VIRTUAL es como tener un almacén dedicado para cada línea de producción:
- Herramientas específicas para cada proyecto
- Versiones controladas
- Aislamiento total entre proyectos

🎯 DEFINICIÓN TÉCNICA:
Un entorno virtual es un directorio que contiene una instalación independiente
de Python con sus propios paquetes, separado del sistema principal.

📊 BENEFICIOS CLAVE:
✅ Aislamiento de dependencias
✅ Control de versiones de paquetes
✅ Reproducibilidad del entorno
✅ Prevención de conflictos
✅ Facilita el deployment
✅ Permite múltiples versiones de Python
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 2: TRABAJANDO CON VENV
# ═══════════════════════════════════════════════════════════════════════════════

"""
🛠️ VENV: EL GESTOR DE ENTORNOS VIRTUALES NATIVO

🔧 COMANDOS FUNDAMENTALES (Windows PowerShell):

1️⃣ CREAR ENTORNO VIRTUAL:
   python -m venv nombre_entorno
   
2️⃣ ACTIVAR ENTORNO (Windows):
   nombre_entorno\Scripts\Activate.ps1
   
3️⃣ DESACTIVAR ENTORNO:
   deactivate
   
4️⃣ VERIFICAR ENTORNO ACTIVO:
   where python
   python --version

⚠️  IMPORTANTE EN WINDOWS:
Si tienes problemas con PowerShell, usa:
nombre_entorno\Scripts\activate.bat

🎯 ESTRUCTURA DE UN ENTORNO VIRTUAL:
mi_proyecto/
├── Scripts/              # Ejecutables (Windows)
│   ├── activate.bat      # Activador batch
│   ├── Activate.ps1      # Activador PowerShell
│   ├── python.exe        # Intérprete Python
│   └── pip.exe          # Gestor de paquetes
├── Lib/                 # Librerías instaladas
│   └── site-packages/   # Paquetes de terceros
├── Include/             # Headers C/C++
└── pyvenv.cfg          # Configuración del entorno
"""

import subprocess
import sys
import os
from pathlib import Path

def verificar_entorno_virtual():
    """
    🔍 Función para verificar si estamos en un entorno virtual
    
    Returns:
        bool: True si estamos en un entorno virtual
    """
    # Método 1: Variable de entorno VIRTUAL_ENV
    if os.environ.get('VIRTUAL_ENV'):
        print("✅ Entorno virtual detectado via VIRTUAL_ENV")
        print(f"📍 Ruta: {os.environ['VIRTUAL_ENV']}")
        return True
    
    # Método 2: Comparar sys.prefix con sys.base_prefix
    if sys.prefix != sys.base_prefix:
        print("✅ Entorno virtual detectado via sys.prefix")
        print(f"📍 Entorno: {sys.prefix}")
        print(f"📍 Sistema: {sys.base_prefix}")
        return True
    
    print("❌ No estás en un entorno virtual")
    return False

def mostrar_info_python():
    """
    📊 Muestra información detallada del entorno Python actual
    """
    print("=" * 60)
    print("🐍 INFORMACIÓN DEL ENTORNO PYTHON")
    print("=" * 60)
    
    print(f"🔖 Versión Python: {sys.version}")
    print(f"📍 Ejecutable: {sys.executable}")
    print(f"📍 Ruta del sistema: {sys.prefix}")
    print(f"📍 Ruta base: {sys.base_prefix}")
    
    # Verificar si estamos en entorno virtual
    verificar_entorno_virtual()
    
    # Mostrar rutas de módulos
    print(f"📚 Rutas de módulos:")
    for i, path in enumerate(sys.path[:5]):  # Primeras 5 rutas
        print(f"   {i+1}. {path}")
    
    if len(sys.path) > 5:
        print(f"   ... y {len(sys.path)-5} rutas más")

# Ejemplo de uso
if __name__ == "__main__":
    mostrar_info_python()

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 3: GESTIÓN DE DEPENDENCIAS CON PIP
# ═══════════════════════════════════════════════════════════════════════════════

"""
📦 PIP: EL GESTOR DE PAQUETES DE PYTHON

🔧 COMANDOS ESENCIALES:

1️⃣ INSTALAR PAQUETE:
   pip install nombre_paquete
   pip install nombre_paquete==1.4.2  # Versión específica
   pip install nombre_paquete>=1.0    # Versión mínima
   
2️⃣ ACTUALIZAR PAQUETE:
   pip install --upgrade nombre_paquete
   pip install -U nombre_paquete      # Forma corta
   
3️⃣ DESINSTALAR PAQUETE:
   pip uninstall nombre_paquete
   
4️⃣ LISTAR PAQUETES INSTALADOS:
   pip list
   pip list --outdated               # Paquetes desactualizados
   
5️⃣ MOSTRAR INFORMACIÓN DE PAQUETE:
   pip show nombre_paquete
   
6️⃣ BUSCAR PAQUETES:
   pip search nombre_paquete

⚠️  MEJORES PRÁCTICAS:
• Siempre instala en entorno virtual activado
• Usa versiones específicas para proyectos críticos
• Mantén un registro de dependencias actualizado
• Actualiza pip regularmente: pip install --upgrade pip
"""

def mostrar_paquetes_instalados():
    """
    📋 Muestra los paquetes instalados en el entorno actual
    """
    try:
        import pkg_resources
        
        print("=" * 60)
        print("📦 PAQUETES INSTALADOS EN EL ENTORNO")
        print("=" * 60)
        
        installed_packages = [d for d in pkg_resources.working_set]
        installed_packages.sort(key=lambda x: x.project_name.lower())
        
        for i, package in enumerate(installed_packages, 1):
            print(f"{i:2d}. {package.project_name:20} {package.version}")
            
        print(f"\n📊 Total de paquetes: {len(installed_packages)}")
        
    except ImportError:
        print("❌ No se puede importar pkg_resources")

def verificar_dependencias_criticas():
    """
    🔍 Verifica la instalación de paquetes críticos para automatización
    """
    dependencias_criticas = [
        'requests',    # Para comunicación HTTP
        'pyserial',    # Para comunicación serial
        'pandas',      # Para análisis de datos
        'flask',       # Para desarrollo web
        'sqlalchemy',  # Para bases de datos
        'pymodbus'     # Para comunicación Modbus
    ]
    
    print("=" * 60)
    print("🔍 VERIFICACIÓN DE DEPENDENCIAS CRÍTICAS")
    print("=" * 60)
    
    for paquete in dependencias_criticas:
        try:
            __import__(paquete)
            print(f"✅ {paquete:15} - INSTALADO")
        except ImportError:
            print(f"❌ {paquete:15} - NO INSTALADO")

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 4: REQUIREMENTS.TXT - GESTIÓN DE DEPENDENCIAS
# ═══════════════════════════════════════════════════════════════════════════════

"""
📋 REQUIREMENTS.TXT: EL ARCHIVO DE DEPENDENCIAS

🎯 PROPÓSITO:
Archivo que lista todas las dependencias del proyecto con sus versiones exactas,
permitiendo recrear el mismo entorno en cualquier máquina.

🔧 COMANDOS PARA REQUIREMENTS.TXT:

1️⃣ GENERAR REQUIREMENTS:
   pip freeze > requirements.txt
   
2️⃣ INSTALAR DESDE REQUIREMENTS:
   pip install -r requirements.txt
   
3️⃣ ACTUALIZAR REQUIREMENTS:
   pip freeze > requirements.txt    # Sobreescribe
   pip list --format=freeze > requirements.txt  # Alternativa

📝 FORMATO DE REQUIREMENTS.TXT:
requests==2.28.1
flask==2.2.2
pandas>=1.5.0
pymodbus~=3.0.0
sqlalchemy>=1.4,<2.0

🔍 OPERADORES DE VERSIÓN:
==  Versión exacta
>=  Versión mínima
<=  Versión máxima
~=  Versión compatible (ej: ~=1.4.0 acepta 1.4.x pero no 1.5.0)
!=  Excluir versión específica

🏭 EJEMPLO INDUSTRIAL - REQUIREMENTS.TXT:
"""

def generar_requirements_ejemplo():
    """
    📝 Genera un archivo requirements.txt de ejemplo para automatización industrial
    """
    requirements_contenido = """# ======================================================================
# 🏭 DEPENDENCIAS PARA PROYECTO DE AUTOMATIZACIÓN INDUSTRIAL
# ======================================================================
# Generado el: 2025-01-07
# Python: 3.9+
# Proyecto: Sistema SCADA Industrial

# 🌐 Comunicación y APIs
requests==2.31.0           # HTTP requests para APIs
flask==2.3.3               # Framework web para dashboard
flask-sqlalchemy==3.0.5    # ORM para Flask

# 📊 Análisis y manipulación de datos
pandas==2.0.3              # Análisis de datos de sensores
numpy==1.24.3              # Cálculos numéricos
matplotlib==3.7.2          # Gráficos y visualización

# 🔌 Comunicación industrial
pymodbus==3.4.1            # Protocolo Modbus TCP/RTU
pyserial==3.5               # Comunicación serial RS485/RS232

# 🗃️ Base de datos
sqlalchemy==2.0.20         # ORM avanzado
sqlite3                    # Base de datos embebida (built-in)

# ⏰ Programación de tareas
schedule==1.2.0            # Programador de tareas
python-crontab==2.7.1      # Integración con crontab

# 📝 Logging y configuración
pyyaml==6.0.1              # Archivos de configuración YAML
python-dotenv==1.0.0       # Variables de entorno

# 🧪 Testing (desarrollo)
pytest==7.4.0              # Framework de testing
pytest-cov==4.1.0          # Coverage de tests

# 📈 Monitoreo y alertas
psutil==5.9.5              # Información del sistema
email-validator==2.0.0     # Validación de emails para alertas

# 🔒 Seguridad
cryptography==41.0.3       # Encriptación de datos sensibles
"""
    
    return requirements_contenido

def crear_requirements_personalizado():
    """
    🛠️ Crea un requirements.txt personalizado para el proyecto actual
    """
    try:
        import subprocess
        
        print("🔄 Generando requirements.txt...")
        
        # Ejecutar pip freeze
        result = subprocess.run(['pip', 'freeze'], 
                              capture_output=True, 
                              text=True, 
                              check=True)
        
        # Crear contenido del archivo
        contenido = f"""# ======================================================================
# 📦 DEPENDENCIAS DEL PROYECTO
# ======================================================================
# Generado automáticamente el: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
# Python: {sys.version.split()[0]}

{result.stdout}"""
        
        # Escribir archivo
        with open('requirements.txt', 'w', encoding='utf-8') as f:
            f.write(contenido)
            
        print("✅ requirements.txt generado exitosamente")
        print("📍 Ubicación: requirements.txt")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error ejecutando pip freeze: {e}")
    except Exception as e:
        print(f"❌ Error creando requirements.txt: {e}")

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 5: ESTRUCTURA PROFESIONAL DE PROYECTOS
# ═══════════════════════════════════════════════════════════════════════════════

"""
🏗️ ESTRUCTURA PROFESIONAL DE PROYECTOS PYTHON

🎯 PRINCIPIOS DE ORGANIZACIÓN:
• Separación clara de responsabilidades
• Configuración centralizada
• Documentación integrada
• Testing estructurado
• Deployment simplificado

📁 ESTRUCTURA RECOMENDADA PARA AUTOMATIZACIÓN INDUSTRIAL:

proyecto_automatizacion/
├── 📄 README.md                    # Documentación principal
├── 📄 requirements.txt             # Dependencias
├── 📄 .env                        # Variables de entorno
├── 📄 .gitignore                  # Archivos a ignorar en Git
├── 📄 setup.py                    # Configuración del paquete
├── 📄 config.yaml                 # Configuración de la aplicación
│
├── 📁 src/                        # Código fuente principal
│   ├── 📁 automatizacion/         # Paquete principal
│   │   ├── 📄 __init__.py         # Inicializador del paquete
│   │   ├── 📄 main.py             # Punto de entrada
│   │   ├── 📁 modbus/             # Módulo Modbus
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 cliente.py      # Cliente Modbus
│   │   │   └── 📄 servidor.py     # Servidor Modbus
│   │   ├── 📁 database/           # Módulo base de datos
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 models.py       # Modelos de datos
│   │   │   └── 📄 conexion.py     # Gestión de conexiones
│   │   ├── 📁 web/                # Módulo web (Flask)
│   │   │   ├── 📄 __init__.py
│   │   │   ├── 📄 app.py          # Aplicación Flask
│   │   │   ├── 📄 routes.py       # Rutas web
│   │   │   └── 📁 templates/      # Templates HTML
│   │   └── 📁 utils/              # Utilidades
│   │       ├── 📄 __init__.py
│   │       ├── 📄 logger.py       # Configuración de logs
│   │       └── 📄 config.py       # Carga de configuración
│
├── 📁 tests/                      # Tests unitarios
│   ├── 📄 __init__.py
│   ├── 📄 test_modbus.py
│   ├── 📄 test_database.py
│   └── 📄 test_web.py
│
├── 📁 docs/                       # Documentación
│   ├── 📄 instalacion.md
│   ├── 📄 configuracion.md
│   └── 📄 api.md
│
├── 📁 scripts/                    # Scripts de utilidad
│   ├── 📄 setup_env.py           # Configuración inicial
│   ├── 📄 backup_db.py           # Backup de base de datos
│   └── 📄 deploy.py              # Script de deployment
│
├── 📁 data/                       # Datos del proyecto
│   ├── 📁 input/                  # Datos de entrada
│   ├── 📁 output/                 # Datos de salida
│   └── 📁 backup/                 # Respaldos
│
└── 📁 logs/                       # Archivos de log
    ├── 📄 app.log
    ├── 📄 modbus.log
    └── 📄 error.log
"""

from pathlib import Path
import os

def crear_estructura_proyecto(nombre_proyecto):
    """
    🏗️ Crea la estructura completa de un proyecto de automatización industrial
    
    Args:
        nombre_proyecto (str): Nombre del proyecto a crear
    """
    # Definir la estructura de directorios
    estructura = [
        '',  # Directorio raíz
        'src',
        f'src/{nombre_proyecto}',
        f'src/{nombre_proyecto}/modbus',
        f'src/{nombre_proyecto}/database',
        f'src/{nombre_proyecto}/web',
        f'src/{nombre_proyecto}/web/templates',
        f'src/{nombre_proyecto}/web/static',
        f'src/{nombre_proyecto}/web/static/css',
        f'src/{nombre_proyecto}/web/static/js',
        f'src/{nombre_proyecto}/utils',
        'tests',
        'docs',
        'scripts',
        'data',
        'data/input',
        'data/output',
        'data/backup',
        'logs',
        'config'
    ]
    
    # Crear directorios
    base_path = Path(nombre_proyecto)
    
    try:
        print(f"🏗️ Creando estructura del proyecto: {nombre_proyecto}")
        
        for directorio in estructura:
            dir_path = base_path / directorio if directorio else base_path
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"📁 Creado: {dir_path}")
        
        # Crear archivos __init__.py
        init_files = [
            f'src/{nombre_proyecto}/__init__.py',
            f'src/{nombre_proyecto}/modbus/__init__.py',
            f'src/{nombre_proyecto}/database/__init__.py',
            f'src/{nombre_proyecto}/web/__init__.py',
            f'src/{nombre_proyecto}/utils/__init__.py',
            'tests/__init__.py'
        ]
        
        for init_file in init_files:
            init_path = base_path / init_file
            init_path.touch()
            print(f"📄 Creado: {init_path}")
        
        print(f"✅ Estructura del proyecto '{nombre_proyecto}' creada exitosamente")
        return True
        
    except Exception as e:
        print(f"❌ Error creando estructura: {e}")
        return False

def generar_archivos_configuracion(nombre_proyecto):
    """
    📝 Genera archivos de configuración esenciales para el proyecto
    """
    base_path = Path(nombre_proyecto)
    
    # 1. README.md
    readme_content = f"""# {nombre_proyecto.upper()}

🏭 **Sistema de Automatización Industrial con Python**

## 📋 Descripción

Sistema completo de automatización industrial que integra:
- 🔌 Comunicación Modbus TCP/RTU
- 🗃️ Base de datos SQL para almacenamiento
- 🌐 Dashboard web con Flask
- 📊 Análisis de datos en tiempo real

## 🚀 Instalación Rápida

```bash
# 1. Clonar repositorio
git clone [URL_DEL_REPO]
cd {nombre_proyecto}

# 2. Crear entorno virtual
python -m venv venv

# 3. Activar entorno virtual
# Windows PowerShell:
venv\\Scripts\\Activate.ps1
# Windows CMD:
venv\\Scripts\\activate.bat

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Ejecutar aplicación
python src/{nombre_proyecto}/main.py
```

## 📚 Documentación

Ver carpeta `docs/` para documentación detallada.

## 🧪 Testing

```bash
pytest tests/
```

## 📄 Licencia

MIT License
"""
    
    # 2. .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
logs/*.log
*.log

# Database
*.db
*.sqlite3

# Configuration
.env
config/local_config.yaml

# Data
data/input/*
data/output/*
!data/input/.gitkeep
!data/output/.gitkeep

# Backup
data/backup/*
!data/backup/.gitkeep
"""
    
    # 3. .env template
    env_content = """# ======================================================================
# 🔧 VARIABLES DE ENTORNO - CONFIGURACIÓN DEL SISTEMA
# ======================================================================
# IMPORTANTE: Renombra este archivo a .env y configura tus valores

# 🗃️ Base de Datos
DATABASE_URL=sqlite:///data/automatizacion.db
DATABASE_ECHO=False

# 🔌 Configuración Modbus
MODBUS_HOST=192.168.1.100
MODBUS_PORT=502
MODBUS_UNIT_ID=1
MODBUS_TIMEOUT=5

# 🌐 Configuración Web
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5000
SECRET_KEY=tu_clave_secreta_muy_segura

# 📝 Logging
LOG_LEVEL=INFO
LOG_FILE=logs/app.log

# 📧 Notificaciones (opcional)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=tu_email@gmail.com
EMAIL_PASSWORD=tu_contraseña
"""
    
    # 4. config.yaml
    config_content = """# ======================================================================
# ⚙️ CONFIGURACIÓN PRINCIPAL DEL SISTEMA
# ======================================================================

# 🏭 Información del proyecto
proyecto:
  nombre: "{nombre_proyecto}"
  version: "1.0.0"
  descripcion: "Sistema de automatización industrial"
  autor: "Tu Nombre"

# 🔌 Configuración Modbus
modbus:
  tcp:
    host: "192.168.1.100"
    port: 502
    timeout: 5
    unit_id: 1
  
  rtu:
    port: "COM1"
    baudrate: 9600
    bytesize: 8
    parity: "N"
    stopbits: 1
    timeout: 1

# 🗃️ Base de datos
database:
  url: "sqlite:///data/automatizacion.db"
  echo: false
  pool_size: 5
  max_overflow: 10

# 🌐 Servidor web
web:
  host: "0.0.0.0"
  port: 5000
  debug: true
  threaded: true

# 📝 Logging
logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  handlers:
    - type: "file"
      filename: "logs/app.log"
      max_bytes: 10485760  # 10MB
      backup_count: 5
    - type: "console"

# ⏰ Tareas programadas
scheduler:
  interval_lectura: 5  # segundos
  interval_backup: 3600  # 1 hora
  
# 🚨 Alertas
alertas:
  email_enabled: false
  sms_enabled: false
  telegram_enabled: false
""".format(nombre_proyecto=nombre_proyecto)
    
    # 5. setup.py
    setup_content = f"""from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="{nombre_proyecto}",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu_email@ejemplo.com",
    description="Sistema de automatización industrial con Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu_usuario/{nombre_proyecto}",
    package_dir={{"": "src"}},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Manufacturing",
        "Topic :: System :: Hardware",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={{
        "dev": ["pytest>=7.0", "pytest-cov>=4.0", "black", "flake8"],
        "docs": ["sphinx", "sphinx-rtd-theme"],
    }},
    entry_points={{
        "console_scripts": [
            "{nombre_proyecto}=src.{nombre_proyecto}.main:main",
        ],
    }},
)
"""
    
    # Escribir archivos
    archivos = [
        ("README.md", readme_content),
        (".gitignore", gitignore_content),
        (".env.template", env_content),
        ("config/config.yaml", config_content),
        ("setup.py", setup_content)
    ]
    
    try:
        for archivo, contenido in archivos:
            archivo_path = base_path / archivo
            archivo_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(archivo_path, 'w', encoding='utf-8') as f:
                f.write(contenido)
            
            print(f"📄 Creado: {archivo_path}")
        
        # Crear archivos .gitkeep para directorios vacíos
        gitkeep_dirs = ['data/input', 'data/output', 'data/backup', 'logs']
        for dir_name in gitkeep_dirs:
            gitkeep_path = base_path / dir_name / '.gitkeep'
            gitkeep_path.touch()
        
        print("✅ Archivos de configuración generados exitosamente")
        return True
        
    except Exception as e:
        print(f"❌ Error generando archivos: {e}")
        return False

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 6: BUENAS PRÁCTICAS Y CASOS DE USO INDUSTRIALES
# ═══════════════════════════════════════════════════════════════════════════════

"""
🏭 CASOS DE USO INDUSTRIALES REALES

🎯 CASO 1: MÚLTIPLES VERSIONES DE PYMODBUS
Problema: Proyecto A necesita PyModbus 2.5, Proyecto B necesita PyModbus 3.0
Solución: Entorno virtual separado para cada proyecto

🎯 CASO 2: DESARROLLO Y PRODUCCIÓN
Problema: Diferentes versiones de librerías entre desarrollo y producción
Solución: requirements-dev.txt y requirements-prod.txt separados

🎯 CASO 3: INTEGRACIÓN CONTINUA
Problema: Tests fallan por dependencias inconsistentes
Solución: Entornos virtuales en pipeline CI/CD

⚠️  ADVERTENCIAS CRÍTICAS:

❌ NUNCA hagas: pip install en el sistema global para proyectos
✅ SIEMPRE usa: entorno virtual activado

❌ NUNCA hagas: requirements.txt sin versiones específicas
✅ SIEMPRE usa: versiones exactas para producción

❌ NUNCA hagas: compartir entornos virtuales entre proyectos
✅ SIEMPRE usa: un entorno virtual por proyecto

🔒 MEJORES PRÁCTICAS INDUSTRIALES:

1️⃣ NOMENCLATURA CONSISTENTE:
   proyecto_venv, automatizacion_env, scada_python39

2️⃣ DOCUMENTACIÓN:
   Siempre documenta las versiones de Python y librerías utilizadas

3️⃣ BACKUP DE ENTORNOS:
   Mantén requirements.txt actualizado como backup

4️⃣ TESTING:
   Prueba la instalación desde requirements.txt regularmente

5️⃣ VERSIONADO:
   Usa Git para versionar requirements.txt y configuración
"""

def validar_configuracion_proyecto(ruta_proyecto):
    """
    🔍 Valida que la configuración del proyecto sea correcta
    
    Args:
        ruta_proyecto (str): Ruta al directorio del proyecto
    """
    proyecto_path = Path(ruta_proyecto)
    
    print("=" * 60)
    print("🔍 VALIDACIÓN DE CONFIGURACIÓN DEL PROYECTO")
    print("=" * 60)
    
    # Verificar archivos críticos
    archivos_criticos = [
        'requirements.txt',
        'README.md',
        '.gitignore',
        'src',
        'tests'
    ]
    
    print("📋 Verificando archivos críticos:")
    for archivo in archivos_criticos:
        archivo_path = proyecto_path / archivo
        if archivo_path.exists():
            print(f"✅ {archivo}")
        else:
            print(f"❌ {archivo} - FALTANTE")
    
    # Verificar entorno virtual
    print("\n🐍 Verificando entorno virtual:")
    if verificar_entorno_virtual():
        print("✅ Entorno virtual activo")
    else:
        print("⚠️  No se detectó entorno virtual activo")
    
    # Verificar requirements.txt
    requirements_path = proyecto_path / 'requirements.txt'
    if requirements_path.exists():
        print("\n📦 Analizando requirements.txt:")
        try:
            with open(requirements_path, 'r') as f:
                lineas = f.readlines()
            
            paquetes = [line.strip() for line in lineas 
                       if line.strip() and not line.startswith('#')]
            
            print(f"📊 Total de dependencias: {len(paquetes)}")
            
            # Verificar si hay versiones especificadas
            con_version = sum(1 for p in paquetes if any(op in p for op in ['==', '>=', '<=', '~=']))
            print(f"📌 Con versión especificada: {con_version}/{len(paquetes)}")
            
            if con_version < len(paquetes):
                print("⚠️  Recomendación: Especifica versiones para todas las dependencias")
            
        except Exception as e:
            print(f"❌ Error leyendo requirements.txt: {e}")
    
    print("\n" + "=" * 60)

# ═══════════════════════════════════════════════════════════════════════════════
# 🎯 PROYECTO INTEGRADOR: SETUP COMPLETO DE PROYECTO DE AUTOMATIZACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

def proyecto_setup_automatizacion():
    """
    🏭 PROYECTO PRINCIPAL: Setup completo de proyecto de automatización industrial
    
    Este proyecto integra todos los conceptos del módulo:
    • Creación de entorno virtual
    • Gestión de dependencias
    • Estructura profesional de proyecto
    • Configuración y documentación
    """
    import datetime
    
    print("=" * 80)
    print("🏭 PROYECTO: SETUP COMPLETO DE AUTOMATIZACIÓN INDUSTRIAL")
    print("=" * 80)
    
    # Configuración del proyecto
    nombre_proyecto = "sistema_scada_industrial"
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    
    print(f"📋 Configuración del proyecto:")
    print(f"   📦 Nombre: {nombre_proyecto}")
    print(f"   🐍 Python: {python_version}")
    print(f"   📅 Fecha: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Paso 1: Verificar entorno actual
    print(f"\n1️⃣ Verificando entorno actual...")
    mostrar_info_python()
    
    # Paso 2: Crear estructura del proyecto
    print(f"\n2️⃣ Creando estructura del proyecto...")
    if crear_estructura_proyecto(nombre_proyecto):
        print("✅ Estructura creada exitosamente")
    else:
        print("❌ Error creando estructura")
        return
    
    # Paso 3: Generar archivos de configuración
    print(f"\n3️⃣ Generando archivos de configuración...")
    if generar_archivos_configuracion(nombre_proyecto):
        print("✅ Configuración generada exitosamente")
    else:
        print("❌ Error generando configuración")
        return
    
    # Paso 4: Crear requirements.txt personalizado
    print(f"\n4️⃣ Generando requirements.txt...")
    requirements_industriales = generar_requirements_ejemplo()
    
    try:
        requirements_path = Path(nombre_proyecto) / "requirements.txt"
        with open(requirements_path, 'w', encoding='utf-8') as f:
            f.write(requirements_industriales)
        print("✅ requirements.txt generado")
    except Exception as e:
        print(f"❌ Error generando requirements.txt: {e}")
    
    # Paso 5: Validar configuración
    print(f"\n5️⃣ Validando configuración final...")
    validar_configuracion_proyecto(nombre_proyecto)
    
    # Paso 6: Instrucciones finales
    print(f"\n🎯 INSTRUCCIONES PARA CONTINUAR:")
    print(f"   1. cd {nombre_proyecto}")
    print(f"   2. python -m venv venv")
    print(f"   3. venv\\Scripts\\Activate.ps1  # (Windows PowerShell)")
    print(f"   4. pip install -r requirements.txt")
    print(f"   5. python src/{nombre_proyecto}/main.py")
    
    print(f"\n✅ ¡Proyecto {nombre_proyecto} configurado exitosamente!")
    print("🚀 ¡Listo para comenzar el desarrollo industrial!")

# ═══════════════════════════════════════════════════════════════════════════════
# 🎓 PREGUNTAS DE REFLEXIÓN Y AUTOEVALUACIÓN
# ═══════════════════════════════════════════════════════════════════════════════

"""
🤔 PREGUNTAS DE REFLEXIÓN:

1️⃣ ¿Por qué es crítico usar entornos virtuales en proyectos industriales?
2️⃣ ¿Qué problemas puede causar no especificar versiones en requirements.txt?
3️⃣ ¿Cómo estructurarías un proyecto que debe funcionar en múltiples plantas?
4️⃣ ¿Qué consideraciones especiales tiene el deployment en entornos industriales?
5️⃣ ¿Cómo garantizas la reproducibilidad del entorno en diferentes máquinas?

💡 EJERCICIOS PRÁCTICOS:

🔧 BÁSICO:
   Crear entorno virtual y instalar 3 paquetes específicos

🔧 INTERMEDIO:
   Migrar proyecto existente a estructura profesional

🔧 AVANZADO:
   Configurar múltiples entornos (dev, test, prod) para mismo proyecto

🔧 PROYECTO:
   Setup completo de sistema SCADA con todas las dependencias
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 🚀 EJECUCIÓN PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("🎯 MÓDULO 2.3: ENTORNO VIRTUAL Y GESTIÓN DE DEPENDENCIAS")
    print("=" * 60)
    
    # Ejecutar proyecto principal
    try:
        proyecto_setup_automatizacion()
    except KeyboardInterrupt:
        print("\n⚠️ Proceso interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error en la ejecución: {e}")
    
    print("\n🎓 ¡Módulo completado! Continúa con las prácticas.")

"""
📚 RESUMEN DEL MÓDULO:

✅ Conceptos fundamentales de entornos virtuales
✅ Uso avanzado de venv y pip
✅ Gestión profesional de dependencias con requirements.txt
✅ Estructura profesional de proyectos Python
✅ Mejores prácticas industriales
✅ Proyecto integrador completo

🎯 PRÓXIMO MÓDULO: FASE 3 - BASES DE DATOS CON SQL

💪 ¡Sigue adelante hacia la maestría en Python industrial!
"""
