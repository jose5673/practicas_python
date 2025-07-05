"""
🔧 ARCHIVO DE CORRECCIONES Y REVISIONES
📚 PYTHON PARA AUTOMATIZACIÓN INDUSTRIAL
=====================================================

🎯 PROPÓSITO:
Este archivo será utilizado para realizar correcciones, revisiones y 
refinamientos del código desarrollado durante el programa de aprendizaje.

📋 ESTRUCTURA:
- Correcciones de errores comunes
- Optimizaciones de código  
- Refactoring de soluciones
- Mejores prácticas aplicadas
- Feedback detallado de ejercicios

═══════════════════════════════════════════════════════════════════════════════
🎨 CREADO POR: Tu Tutor Experto en Python y Coach Motivacional
📅 FECHA DE CREACIÓN: 1 de Julio, 2025
🔄 ÚLTIMA ACTUALIZACIÓN: [Se actualizará en cada revisión]
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 1: PLANTILLA DE REVISIÓN
# ═══════════════════════════════════════════════════════════════════════════════

class RevisionTemplate:
    """
    Plantilla estándar para realizar revisiones de código.
    
    Esta clase proporciona una estructura consistente para documentar
    correcciones, mejoras y feedback del código desarrollado.
    """
    
    def __init__(self, modulo, ejercicio, fecha):
        self.modulo = modulo
        self.ejercicio = ejercicio
        self.fecha = fecha
        self.errores_encontrados = []
        self.mejoras_sugeridas = []
        self.codigo_original = ""
        self.codigo_corregido = ""
        self.comentarios = []
        
    def agregar_error(self, descripcion, linea=None, severidad="MEDIO"):
        """Registra un error encontrado en el código."""
        error = {
            'descripcion': descripcion,
            'linea': linea,
            'severidad': severidad,
            'tipo': 'ERROR'
        }
        self.errores_encontrados.append(error)
        
    def agregar_mejora(self, descripcion, razon, impacto="MEDIO"):
        """Registra una mejora sugerida."""
        mejora = {
            'descripcion': descripcion,
            'razon': razon,
            'impacto': impacto,
            'tipo': 'MEJORA'
        }
        self.mejoras_sugeridas.append(mejora)
        
    def generar_reporte(self):
        """Genera un reporte completo de la revisión."""
        reporte = f"""
🔍 REPORTE DE REVISIÓN
=====================
📚 Módulo: {self.modulo}
🎯 Ejercicio: {self.ejercicio}  
📅 Fecha: {self.fecha}

❌ ERRORES ENCONTRADOS ({len(self.errores_encontrados)}):
{self._formatear_lista(self.errores_encontrados)}

✅ MEJORAS SUGERIDAS ({len(self.mejoras_sugeridas)}):
{self._formatear_lista(self.mejoras_sugeridas)}

📝 COMENTARIOS ADICIONALES:
{chr(10).join(self.comentarios)}
        """
        return reporte
        
    def _formatear_lista(self, items):
        """Formatea una lista de errores o mejoras."""
        if not items:
            return "   ✅ ¡Ninguno encontrado!"
            
        resultado = ""
        for i, item in enumerate(items, 1):
            resultado += f"   {i}. {item['descripcion']}"
            if item.get('linea'):
                resultado += f" (Línea {item['linea']})"
            resultado += f" - Severidad: {item['severidad']}\n"
        return resultado

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 2: ERRORES COMUNES Y SOLUCIONES
# ═══════════════════════════════════════════════════════════════════════════════

ERRORES_COMUNES = {
    "nomenclatura": {
        "descripcion": "Nomenclatura inconsistente o poco descriptiva",
        "ejemplos_malos": [
            "temp = 25.5",
            "x = True", 
            "data1 = 'sensor'"
        ],
        "ejemplos_buenos": [
            "temperatura_motor = 25.5",
            "bomba_encendida = True",
            "id_sensor_presion = 'PRES_001'"
        ],
        "solucion": "Usar snake_case y nombres descriptivos que reflejen el contexto industrial"
    },
    
    "tipos_datos": {
        "descripcion": "Uso incorrecto de tipos de datos",
        "ejemplos_malos": [
            "temperatura = '25.5'  # string en lugar de float",
            "contador = 25.0       # float en lugar de int"
        ],
        "ejemplos_buenos": [
            "temperatura = 25.5    # float para valores decimales",
            "contador = 25         # int para conteos"
        ],
        "solucion": "Elegir el tipo apropiado según el contexto de uso"
    },
    
    "conversiones": {
        "descripcion": "Conversiones de tipo sin validación",
        "ejemplos_malos": [
            "valor = int(input('Ingrese número: '))"
        ],
        "ejemplos_buenos": [
            """try:
    valor = int(input('Ingrese número: '))
except ValueError:
    print('Error: Debe ingresar un número válido')
    valor = 0"""
        ],
        "solucion": "Siempre validar conversiones con try/except"
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 3: MEJORES PRÁCTICAS INDUSTRIALES
# ═══════════════════════════════════════════════════════════════════════════════

MEJORES_PRACTICAS = {
    "documentacion": {
        "titulo": "Documentación de Código Industrial",
        "descripcion": "El código en automatización debe estar perfectamente documentado",
        "ejemplo": '''
def calcular_eficiencia_motor(potencia_entrada, potencia_salida):
    """
    Calcula la eficiencia de un motor industrial.
    
    Args:
        potencia_entrada (float): Potencia de entrada en Watts
        potencia_salida (float): Potencia de salida en Watts
        
    Returns:
        float: Eficiencia como porcentaje (0-100)
        
    Raises:
        ValueError: Si alguna potencia es negativa o cero
        
    Example:
        >>> calcular_eficiencia_motor(1500, 1275)
        85.0
    """
    if potencia_entrada <= 0 or potencia_salida <= 0:
        raise ValueError("Las potencias deben ser positivas")
        
    return (potencia_salida / potencia_entrada) * 100
        '''
    },
    
    "validaciones": {
        "titulo": "Validaciones de Seguridad",
        "descripcion": "Siempre validar datos en contextos industriales",
        "ejemplo": '''
def validar_temperatura(temperatura):
    """Valida que la temperatura esté en rango operacional."""
    TEMP_MIN = -20  # °C
    TEMP_MAX = 100  # °C
    
    if not isinstance(temperatura, (int, float)):
        raise TypeError("Temperatura debe ser numérica")
        
    if temperatura < TEMP_MIN or temperatura > TEMP_MAX:
        raise ValueError(f"Temperatura fuera de rango: {TEMP_MIN} a {TEMP_MAX}°C")
        
    return True
        '''
    },
    
    "constantes": {
        "titulo": "Uso de Constantes",
        "descripcion": "Definir valores críticos como constantes",
        "ejemplo": '''
# ✅ CONSTANTES INDUSTRIALES
TEMPERATURA_CRITICA_MOTOR = 85     # °C
PRESION_MAXIMA_TANQUE = 5.0       # bar
VELOCIDAD_NOMINAL_BOMBA = 1750    # RPM
FACTOR_CONVERSION_PRESION = 0.145 # bar a PSI

# ✅ USO EN CÓDIGO
if temperatura_motor > TEMPERATURA_CRITICA_MOTOR:
    activar_alarma("Temperatura crítica en motor")
        '''
    }
}

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 4: FUNCIÓN DE CORRECCIÓN AUTOMÁTICA
# ═══════════════════════════════════════════════════════════════════════════════

def revisar_codigo_estudiante(codigo, modulo="General"):
    """
    Realiza una revisión automática básica del código del estudiante.
    
    Args:
        codigo (str): Código Python a revisar
        modulo (str): Módulo al que pertenece el código
        
    Returns:
        RevisionTemplate: Objeto con los resultados de la revisión
    """
    from datetime import datetime
    
    revision = RevisionTemplate(
        modulo=modulo,
        ejercicio="Revisión Automática",
        fecha=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    
    revision.codigo_original = codigo
    
    # Verificaciones básicas
    lineas = codigo.split('\n')
    
    for i, linea in enumerate(lineas, 1):
        linea_limpia = linea.strip()
        
        # Verificar nomenclatura
        if '=' in linea_limpia and not linea_limpia.startswith('#'):
            if any(char.isupper() for char in linea_limpia.split('=')[0].strip()):
                revision.agregar_error(
                    f"Posible error de nomenclatura en variable: {linea_limpia}",
                    linea=i,
                    severidad="BAJO"
                )
        
        # Verificar comentarios
        if linea_limpia and not linea_limpia.startswith('#') and '#' not in linea_limpia:
            if any(palabra in linea_limpia.lower() for palabra in ['sensor', 'motor', 'temperatura']):
                revision.agregar_mejora(
                    f"Considerar agregar comentario explicativo: {linea_limpia}",
                    razon="Mejora la legibilidad en contexto industrial",
                    impacto="BAJO"
                )
    
    # Verificar estructura general
    if 'def ' not in codigo:
        revision.agregar_mejora(
            "Considerar crear funciones para código reutilizable",
            razon="Las funciones mejoran la modularidad y testing",
            impacto="MEDIO"
        )
    
    if 'print(' in codigo and 'f"' not in codigo:
        revision.agregar_mejora(
            "Usar f-strings para formateo de strings",
            razon="Más legible y eficiente que concatenación",
            impacto="BAJO"
        )
    
    return revision

# ═══════════════════════════════════════════════════════════════════════════════
# 📖 SECCIÓN 5: PLANTILLAS DE EJERCICIOS CORREGIDOS
# ═══════════════════════════════════════════════════════════════════════════════

PLANTILLAS_CORREGIDAS = {
    "variables_sensores": '''
# ✅ VERSIÓN CORREGIDA: Variables para Sensores Industriales
"""
Ejemplo de nomenclatura correcta para variables en automatización industrial.
Sigue convenciones PEP 8 y usa nombres descriptivos del dominio.
"""

# Constantes del sistema
TEMPERATURA_CRITICA = 85.0      # °C - Umbral de temperatura crítica
PRESION_MAXIMA = 5.0           # bar - Presión máxima del tanque
VELOCIDAD_NOMINAL = 1750       # RPM - Velocidad nominal de la bomba

# Variables de sensores con nomenclatura descriptiva
temperatura_motor_principal = 75.5    # °C - Sensor de temperatura del motor
presion_tanque_almacenamiento = 2.8   # bar - Sensor de presión del tanque
bomba_principal_activa = True         # bool - Estado de la bomba principal
id_sensor_temperatura = "TEMP_001"    # str - Identificador único del sensor
contador_lecturas_total = 1250        # int - Total de lecturas realizadas

# Validación de datos críticos
def validar_datos_sensor():
    """Valida que todos los valores estén en rangos seguros."""
    alertas = []
    
    if temperatura_motor_principal > TEMPERATURA_CRITICA:
        alertas.append(f"🚨 Temperatura crítica: {temperatura_motor_principal}°C")
    
    if presion_tanque_almacenamiento > PRESION_MAXIMA:
        alertas.append(f"🚨 Presión excesiva: {presion_tanque_almacenamiento} bar")
    
    return alertas

# Ejecución de validaciones
alertas_activas = validar_datos_sensor()
if alertas_activas:
    for alerta in alertas_activas:
        print(alerta)
else:
    print("✅ Todos los parámetros en rango normal")
    '''
}

if __name__ == "__main__":
    print("🔧 SISTEMA DE CORRECCIONES Y REVISIONES")
    print("=" * 50)
    print()
    print("📋 Este archivo contiene:")
    print("  ✅ Plantillas de revisión")
    print("  ✅ Errores comunes y soluciones")
    print("  ✅ Mejores prácticas industriales")
    print("  ✅ Función de corrección automática")
    print("  ✅ Plantillas de código corregido")
    print()
    print("🎯 Úsalo cuando necesites revisar y mejorar tu código.")
    print("💡 Recuerda: La calidad del código es FUNDAMENTAL en automatización industrial.")
