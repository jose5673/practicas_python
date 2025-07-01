"""
📚 TEMARIO: DICCIONARIOS EN PYTHON
==================================

🎯 OBJETIVO DE APRENDIZAJE:
Dominar los diccionarios como estructura de datos clave-valor para crear sistemas
de configuración avanzados, bases de datos en memoria, y preparar datos para
APIs JSON. Fundamental para PyModbus, Flask y sistemas de gestión industrial.

📖 BASADO EN: "Curso Intensivo de Python" - Eric Matthes (Capítulo 6)

🗓️ FECHA: 30 de junio de 2025
👨‍🏫 TUTOR: GitHub Copilot (Experto en Python)
👨‍🎓 ESTUDIANTE: José

═══════════════════════════════════════════════════════════════════════════════
SECUENCIA DE ENSEÑANZA DETALLADA
═══════════════════════════════════════════════════════════════════════════════
"""

# ═══════════════════════════════════════════════════════════════════════════════
# PASO 1: INTRODUCCIÓN A LOS DICCIONARIOS - MAPEO CLAVE-VALOR
# ═══════════════════════════════════════════════════════════════════════════════

def paso_1_introduccion_diccionarios():
    """
    🎯 OBJETIVO: Entender qué son los diccionarios y por qué son revolucionarios
    
    💡 ANALOGÍA INDUSTRIAL: Un diccionario es como una "base de datos en memoria"
    donde cada dispositivo, sensor o configuración tiene un ID único (clave) y
    toda su información asociada (valor).
    
    🏭 APLICACIONES CRÍTICAS:
    - Configuraciones de dispositivos PyModbus por ID
    - Datos JSON para APIs Flask
    - Mapeo de señales en sistemas SCADA
    - Caché de lecturas de sensores
    - Configuraciones de usuarios y permisos
    """
    print("=" * 70)
    print("PASO 1: INTRODUCCIÓN A LOS DICCIONARIOS")
    print("=" * 70)
    
    # CREAR DICCIONARIOS - SINTAXIS BÁSICA
    print("\n📋 CREACIÓN DE DICCIONARIOS:")
    
    # Diccionario de sensor individual
    sensor_temperatura = {
        "id": "TEMP_001",
        "descripcion": "Temperatura Reactor Principal",
        "valor_actual": 75.3,
        "unidad": "°C",
        "estado": "OK",
        "ip": "192.168.1.101",
        "puerto": 502
    }
    
    print(f"Sensor: {sensor_temperatura}")
    print(f"Tipo: {type(sensor_temperatura)}")
    print(f"Número de propiedades: {len(sensor_temperatura)}")
    
    # Diccionario de configuración Modbus
    config_modbus = {
        "timeout": 3.0,
        "retries": 3,
        "unit": 1,
        "protocolo": "TCP"
    }
    print(f"\nConfig Modbus: {config_modbus}")
    
    # ACCESO A VALORES - POR CLAVE
    print(f"\n🔍 ACCESO A VALORES:")
    print(f"ID del sensor: {sensor_temperatura['id']}")
    print(f"Valor actual: {sensor_temperatura['valor_actual']}°C")
    print(f"Estado: {sensor_temperatura['estado']}")
    print(f"Dirección: {sensor_temperatura['ip']}:{sensor_temperatura['puerto']}")
    
    # ACCESO SEGURO CON get()
    print(f"\n🛡️ ACCESO SEGURO:")
    print(f"Precisión: {sensor_temperatura.get('precision', 'No definida')}")
    print(f"Timeout: {config_modbus.get('timeout', 1.0)} segundos")
    
    # CARACTERÍSTICAS FUNDAMENTALES
    print(f"\n✅ CARACTERÍSTICAS CLAVE DE LOS DICCIONARIOS:")
    print("• Mapeo CLAVE → VALOR")
    print("• Son MUTABLES (se pueden modificar)")
    print("• Claves ÚNICAS (no duplicadas)")
    print("• Acceso RÁPIDO por clave (O(1))")
    print("• Ideales para CONFIGURACIONES")
    print("• Perfectos para datos JSON")

def paso_2_operaciones_diccionarios():
    """
    🎯 OBJETIVO: Dominar todas las operaciones con diccionarios
    
    🔧 APLICACIONES PARA PyModbus/Flask:
    - Agregar nuevos dispositivos dinámicamente
    - Actualizar estados de sensores
    - Configurar parámetros de conexión
    - Estructurar respuestas JSON
    """
    print("\n" + "=" * 70)
    print("PASO 2: OPERACIONES FUNDAMENTALES CON DICCIONARIOS")
    print("=" * 70)
    
    # DICCIONARIO INICIAL - REGISTRO DE DISPOSITIVOS
    dispositivos_planta = {
        "TEMP_001": {
            "tipo": "Sensor Temperatura",
            "ubicacion": "Reactor A",
            "valor": 75.3,
            "estado": "OK"
        },
        "PRES_002": {
            "tipo": "Sensor Presión", 
            "ubicacion": "Sistema Principal",
            "valor": 2.1,
            "estado": "OK"
        }
    }
    
    print(f"📊 Dispositivos iniciales: {len(dispositivos_planta)}")
    for id_dispositivo, info in dispositivos_planta.items():
        print(f"   {id_dispositivo}: {info['tipo']} - {info['valor']}")
    
    # AGREGAR NUEVOS DISPOSITIVOS
    print(f"\n➕ AGREGAR DISPOSITIVOS:")
    
    # Método 1: Asignación directa
    dispositivos_planta["NIVEL_003"] = {
        "tipo": "Sensor Nivel",
        "ubicacion": "Tanque Principal", 
        "valor": 67.5,
        "estado": "OK"
    }
    
    # Método 2: update() con diccionario
    nuevos_dispositivos = {
        "FLUJO_004": {
            "tipo": "Medidor Flujo",
            "ubicacion": "Bomba A",
            "valor": 15.2,
            "estado": "WARNING"
        },
        "MOTOR_005": {
            "tipo": "Motor Principal",
            "ubicacion": "Sala Máquinas",
            "valor": 1450,  # RPM
            "estado": "OK"
        }
    }
    dispositivos_planta.update(nuevos_dispositivos)
    
    print(f"Dispositivos después de agregar: {len(dispositivos_planta)}")
    
    # MODIFICAR VALORES EXISTENTES
    print(f"\n🔧 ACTUALIZAR LECTURAS:")
    
    # Actualizar valor de sensor
    dispositivos_planta["TEMP_001"]["valor"] = 78.1
    dispositivos_planta["TEMP_001"]["timestamp"] = "2025-06-30 15:45:00"
    
    # Cambiar estado de dispositivo
    dispositivos_planta["FLUJO_004"]["estado"] = "CRÍTICO"
    dispositivos_planta["FLUJO_004"]["alarma"] = "Flujo muy bajo"
    
    print(f"TEMP_001 actualizado: {dispositivos_planta['TEMP_001']['valor']}°C")
    print(f"FLUJO_004 estado: {dispositivos_planta['FLUJO_004']['estado']}")
    
    # ELIMINAR DISPOSITIVOS
    print(f"\n❌ ELIMINAR DISPOSITIVOS:")
    
    # Método 1: del
    if "MOTOR_005" in dispositivos_planta:
        del dispositivos_planta["MOTOR_005"]
        print("Motor eliminado del sistema")
    
    # Método 2: pop() - eliminar y obtener valor
    dispositivo_removido = dispositivos_planta.pop("PRES_002", None)
    if dispositivo_removido:
        print(f"Dispositivo removido: {dispositivo_removido['tipo']}")
    
    # MÉTODOS DE CONSULTA
    print(f"\n🔍 MÉTODOS DE CONSULTA:")
    
    print(f"Claves (IDs): {list(dispositivos_planta.keys())}")
    print(f"Tipos de dispositivos: {[info['tipo'] for info in dispositivos_planta.values()]}")
    
    # Buscar dispositivos por criterio
    dispositivos_criticos = {
        id_dev: info for id_dev, info in dispositivos_planta.items() 
        if info['estado'] == 'CRÍTICO'
    }
    print(f"Dispositivos críticos: {len(dispositivos_criticos)}")
    
    # VERIFICACIÓN DE EXISTENCIA
    print(f"\n✓ VERIFICACIONES:")
    print(f"¿Existe TEMP_001? {'TEMP_001' in dispositivos_planta}")
    print(f"¿Existe MOTOR_005? {'MOTOR_005' in dispositivos_planta}")

def paso_3_diccionarios_anidados():
    """
    🎯 OBJETIVO: Manejar estructuras complejas de datos industriales
    
    🏭 APLICACIONES INDUSTRIALES:
    - Configuraciones jerárquicas de plantas
    - Datos de múltiples sensores por reactor
    - Estructuras JSON complejas para APIs
    - Sistemas de gestión de usuarios y permisos
    """
    print("\n" + "=" * 70)
    print("PASO 3: DICCIONARIOS ANIDADOS - ESTRUCTURAS COMPLEJAS")
    print("=" * 70)
    
    # ESTRUCTURA COMPLEJA DE PLANTA INDUSTRIAL
    planta_industrial = {
        "info_general": {
            "nombre": "Planta Petroquímica Norte",
            "ubicacion": "Zona Industrial A",
            "capacidad": "50,000 BPD",
            "operario_jefe": "Ing. García"
        },
        "reactores": {
            "R001": {
                "nombre": "Reactor Principal",
                "tipo": "CSTR",
                "capacidad": 5000,  # litros
                "sensores": {
                    "temperatura": {
                        "id": "TEMP_R001",
                        "valor": 78.5,
                        "limite_max": 85.0,
                        "estado": "OK"
                    },
                    "presion": {
                        "id": "PRES_R001", 
                        "valor": 2.3,
                        "limite_max": 3.0,
                        "estado": "OK"
                    },
                    "nivel": {
                        "id": "NIVEL_R001",
                        "valor": 67.5,
                        "limite_min": 20.0,
                        "estado": "OK"
                    }
                },
                "actuadores": {
                    "valvula_entrada": {"estado": "ABIERTA", "apertura": 75},
                    "agitador": {"estado": "ON", "rpm": 150},
                    "bomba_descarga": {"estado": "ON", "flujo": 25.3}
                }
            },
            "R002": {
                "nombre": "Reactor Secundario",
                "tipo": "PFR",
                "capacidad": 3000,
                "sensores": {
                    "temperatura": {
                        "id": "TEMP_R002",
                        "valor": 92.1,
                        "limite_max": 85.0,
                        "estado": "WARNING"
                    },
                    "presion": {
                        "id": "PRES_R002",
                        "valor": 1.8,
                        "limite_max": 3.0,
                        "estado": "OK"
                    }
                },
                "actuadores": {
                    "valvula_entrada": {"estado": "CERRADA", "apertura": 0},
                    "sistema_enfriamiento": {"estado": "ON", "potencia": 80}
                }
            }
        },
        "sistemas_auxiliares": {
            "compresor_aire": {
                "presion_descarga": 7.2,
                "estado": "OPERATIVO",
                "horas_operacion": 1250
            },
            "sistema_agua_enfriamiento": {
                "temperatura_entrada": 25.3,
                "temperatura_salida": 35.7,
                "flujo": 150.0,
                "estado": "OPERATIVO"
            }
        }
    }
    
    print(f"🏭 ANÁLISIS DE PLANTA COMPLEJA:")
    print(f"Planta: {planta_industrial['info_general']['nombre']}")
    print(f"Ubicación: {planta_industrial['info_general']['ubicacion']}")
    print(f"Capacidad: {planta_industrial['info_general']['capacidad']}")
    
    # ACCESO A DATOS ANIDADOS
    print(f"\n📊 ESTADO DE REACTORES:")
    for reactor_id, reactor_info in planta_industrial["reactores"].items():
        print(f"\n🔸 {reactor_id} - {reactor_info['nombre']}")
        print(f"   Tipo: {reactor_info['tipo']}")
        print(f"   Capacidad: {reactor_info['capacidad']:,} L")
        
        # Analizar sensores
        for sensor_tipo, sensor_data in reactor_info["sensores"].items():
            valor = sensor_data["valor"]
            estado = sensor_data["estado"]
            emoji = "✅" if estado == "OK" else "⚠️" if estado == "WARNING" else "🚨"
            print(f"   {emoji} {sensor_tipo.title()}: {valor} - {estado}")
    
    # MODIFICAR DATOS ANIDADOS
    print(f"\n🔧 ACTUALIZACIONES DEL SISTEMA:")
    
    # Actualizar temperatura crítica
    planta_industrial["reactores"]["R002"]["sensores"]["temperatura"]["valor"] = 87.5
    planta_industrial["reactores"]["R002"]["sensores"]["temperatura"]["estado"] = "CRÍTICO"
    
    # Activar sistema de emergencia
    planta_industrial["reactores"]["R002"]["actuadores"]["sistema_emergencia"] = {
        "estado": "ACTIVADO",
        "tipo": "ENFRIAMIENTO_RAPIDO",
        "timestamp": "2025-06-30 15:50:00"
    }
    
    print("⚠️ Sistema de emergencia activado en R002")
    print(f"Nueva temperatura R002: {planta_industrial['reactores']['R002']['sensores']['temperatura']['valor']}°C")
    
    # GENERAR REPORTE EJECUTIVO
    print(f"\n📋 REPORTE EJECUTIVO:")
    
    total_reactores = len(planta_industrial["reactores"])
    reactores_ok = 0
    reactores_warning = 0
    reactores_criticos = 0
    
    for reactor_info in planta_industrial["reactores"].values():
        estados_sensores = [sensor["estado"] for sensor in reactor_info["sensores"].values()]
        if "CRÍTICO" in estados_sensores:
            reactores_criticos += 1
        elif "WARNING" in estados_sensores:
            reactores_warning += 1
        else:
            reactores_ok += 1
    
    print(f"Total reactores: {total_reactores}")
    print(f"✅ Operativos: {reactores_ok}")
    print(f"⚠️ En advertencia: {reactores_warning}")
    print(f"🚨 Críticos: {reactores_criticos}")
    
    eficiencia = (reactores_ok / total_reactores) * 100
    print(f"🎯 Eficiencia operacional: {eficiencia:.1f}%")

def paso_4_iteracion_diccionarios():
    """
    🎯 OBJETIVO: Recorrer diccionarios de forma eficiente
    
    🔄 MÉTODOS DE ITERACIÓN:
    - items(): clave y valor
    - keys(): solo claves
    - values(): solo valores
    - Comprensión de diccionarios
    """
    print("\n" + "=" * 70)
    print("PASO 4: ITERACIÓN Y RECORRIDO DE DICCIONARIOS")
    print("=" * 70)
    
    # DATOS DE EJEMPLO: RED DE SENSORES
    red_sensores = {
        "TEMP_001": {"valor": 75.3, "limite": 80.0, "ubicacion": "Reactor A"},
        "TEMP_002": {"valor": 82.1, "limite": 80.0, "ubicacion": "Reactor B"},
        "PRES_001": {"valor": 2.1, "limite": 3.0, "ubicacion": "Sistema Principal"},
        "PRES_002": {"valor": 3.2, "limite": 3.0, "ubicacion": "Línea Secundaria"},
        "NIVEL_001": {"valor": 67.5, "limite": 20.0, "ubicacion": "Tanque A"},
        "FLUJO_001": {"valor": 15.2, "limite": 10.0, "ubicacion": "Bomba Principal"}
    }
    
    print(f"📊 RED DE SENSORES ({len(red_sensores)} dispositivos)")
    
    # ITERACIÓN BÁSICA - items()
    print(f"\n🔄 ITERACIÓN CON items() - CLAVE Y VALOR:")
    for sensor_id, datos in red_sensores.items():
        valor = datos["valor"]
        limite = datos["limite"]
        ubicacion = datos["ubicacion"]
        estado = "ALARMA" if valor > limite else "OK"
        print(f"   {sensor_id}: {valor} ({estado}) - {ubicacion}")
    
    # ITERACIÓN SOLO CLAVES - keys()
    print(f"\n🔑 ITERACIÓN CON keys() - SOLO CLAVES:")
    sensores_temperatura = [sensor for sensor in red_sensores.keys() if sensor.startswith("TEMP")]
    print(f"Sensores de temperatura: {sensores_temperatura}")
    
    # ITERACIÓN SOLO VALORES - values()
    print(f"\n📈 ITERACIÓN CON values() - SOLO VALORES:")
    todos_valores = [datos["valor"] for datos in red_sensores.values()]
    valor_promedio = sum(todos_valores) / len(todos_valores)
    print(f"Valores actuales: {todos_valores}")
    print(f"Promedio general: {valor_promedio:.2f}")
    
    # COMPRENSIÓN DE DICCIONARIOS
    print(f"\n🧠 COMPRENSIÓN DE DICCIONARIOS:")
    
    # Filtrar sensores en alarma
    sensores_alarma = {
        sensor_id: datos for sensor_id, datos in red_sensores.items()
        if datos["valor"] > datos["limite"]
    }
    print(f"Sensores en alarma: {list(sensores_alarma.keys())}")
    
    # Crear diccionario de estados
    estados_sensores = {
        sensor_id: "ALARMA" if datos["valor"] > datos["limite"] else "OK"
        for sensor_id, datos in red_sensores.items()
    }
    print(f"Estados: {estados_sensores}")
    
    # Sensores por tipo
    sensores_por_tipo = {}
    for sensor_id in red_sensores.keys():
        tipo = sensor_id.split("_")[0]  # TEMP, PRES, NIVEL, FLUJO
        if tipo not in sensores_por_tipo:
            sensores_por_tipo[tipo] = []
        sensores_por_tipo[tipo].append(sensor_id)
    
    print(f"\n📋 SENSORES AGRUPADOS POR TIPO:")
    for tipo, lista_sensores in sensores_por_tipo.items():
        print(f"   {tipo}: {len(lista_sensores)} sensores - {lista_sensores}")
    
    # ANÁLISIS ESTADÍSTICO
    print(f"\n📊 ANÁLISIS ESTADÍSTICO:")
    
    for tipo, lista_sensores in sensores_por_tipo.items():
        valores_tipo = [red_sensores[sensor]["valor"] for sensor in lista_sensores]
        if valores_tipo:
            promedio = sum(valores_tipo) / len(valores_tipo)
            maximo = max(valores_tipo)
            minimo = min(valores_tipo)
            print(f"   {tipo}: Promedio={promedio:.1f}, Máx={maximo}, Mín={minimo}")

def paso_5_json_y_diccionarios():
    """
    🎯 OBJETIVO: Preparar datos para APIs Flask y sistemas web
    
    🌐 APLICACIONES PARA FLASK:
    - Respuestas JSON estructuradas
    - Configuraciones de API
    - Datos de sensores para dashboards
    - Intercambio de información con sistemas externos
    """
    print("\n" + "=" * 70)
    print("PASO 5: JSON Y DICCIONARIOS - PREPARACIÓN PARA APIS")
    print("=" * 70)
    
    import json
    from datetime import datetime
    
    # ESTRUCTURA DE DATOS PARA API REST
    print(f"🌐 ESTRUCTURA DE RESPUESTA API:")
    
    # Respuesta típica de API de sensores
    respuesta_api = {
        "meta": {
            "timestamp": datetime.now().isoformat(),
            "version": "v1.2.3",
            "endpoint": "/api/sensores/estado",
            "status": "success"
        },
        "data": {
            "planta_id": "PLANT_001",
            "nombre": "Planta Norte",
            "sensores": [
                {
                    "id": "TEMP_001",
                    "tipo": "temperatura",
                    "valor": 75.3,
                    "unidad": "celsius",
                    "estado": "normal",
                    "ubicacion": {
                        "reactor": "R001",
                        "zona": "Producción",
                        "coordenadas": {"x": 10.5, "y": 25.3, "z": 5.0}
                    },
                    "configuracion": {
                        "limite_inferior": 20.0,
                        "limite_superior": 80.0,
                        "precision": 0.1,
                        "frecuencia_lectura": 5  # segundos
                    }
                },
                {
                    "id": "PRES_001", 
                    "tipo": "presion",
                    "valor": 2.1,
                    "unidad": "bar",
                    "estado": "normal",
                    "ubicacion": {
                        "reactor": "R001",
                        "zona": "Producción", 
                        "coordenadas": {"x": 10.5, "y": 25.3, "z": 6.0}
                    },
                    "configuracion": {
                        "limite_inferior": 0.5,
                        "limite_superior": 3.0,
                        "precision": 0.01,
                        "frecuencia_lectura": 2
                    }
                }
            ],
            "estadisticas": {
                "total_sensores": 2,
                "sensores_activos": 2,
                "sensores_alarma": 0,
                "ultima_actualizacion": datetime.now().isoformat()
            }
        }
    }
    
    # CONVERTIR A JSON
    json_response = json.dumps(respuesta_api, indent=2, ensure_ascii=False)
    print("Respuesta JSON generada:")
    print(json_response[:500] + "..." if len(json_response) > 500 else json_response)
    
    # CONFIGURACIÓN DE ENDPOINTS
    print(f"\n🔧 CONFIGURACIÓN DE ENDPOINTS FLASK:")
    
    endpoints_config = {
        "/api/sensores": {
            "methods": ["GET", "POST"],
            "descripcion": "Gestión de sensores",
            "parametros": {
                "tipo": {"required": False, "type": "string"},
                "ubicacion": {"required": False, "type": "string"},
                "estado": {"required": False, "type": "string"}
            },
            "respuesta_ejemplo": {
                "sensores": [],
                "total": 0,
                "timestamp": "ISO8601"
            }
        },
        "/api/configuracion": {
            "methods": ["GET", "PUT"],
            "descripcion": "Configuración del sistema",
            "auth_required": True,
            "parametros": {
                "seccion": {"required": True, "type": "string"},
                "valores": {"required": True, "type": "object"}
            }
        },
        "/api/reportes/diario": {
            "methods": ["GET"],
            "descripcion": "Reporte diario de operaciones",
            "cache_ttl": 3600,  # 1 hora
            "formato": ["json", "pdf", "excel"]
        }
    }
    
    print("Endpoints configurados:")
    for endpoint, config in endpoints_config.items():
        print(f"   {endpoint}: {config['methods']} - {config['descripcion']}")
    
    # PREPARAR DATOS PARA DASHBOARD
    print(f"\n📊 DATOS PARA DASHBOARD WEB:")
    
    dashboard_data = {
        "kpis": {
            "eficiencia_operacional": 87.5,
            "sensores_activos": 24,
            "alarmas_activas": 2,
            "tiempo_operacion": "14:32:15"
        },
        "graficos": {
            "temperatura_24h": {
                "labels": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00"],
                "datasets": [
                    {
                        "label": "Reactor A",
                        "data": [72.1, 73.5, 75.8, 78.2, 76.9, 74.3],
                        "color": "#FF6384"
                    },
                    {
                        "label": "Reactor B", 
                        "data": [70.5, 72.1, 74.2, 76.8, 75.1, 72.9],
                        "color": "#36A2EB"
                    }
                ]
            },
            "distribucion_alarmas": {
                "criticas": 1,
                "warning": 3,
                "info": 5
            }
        },
        "tablas": {
            "sensores_criticos": [
                {
                    "id": "TEMP_003",
                    "ubicacion": "Reactor C",
                    "valor": 89.2,
                    "limite": 85.0,
                    "tiempo_alarma": "00:15:32"
                }
            ],
            "mantenimiento_programado": [
                {
                    "equipo": "Bomba Principal",
                    "fecha": "2025-07-05",
                    "tipo": "Preventivo",
                    "responsable": "Equipo A"
                }
            ]
        }
    }
    
    print("Datos del dashboard preparados:")
    print(f"   KPIs: {len(dashboard_data['kpis'])} métricas")
    print(f"   Gráficos: {len(dashboard_data['graficos'])} visualizaciones")
    print(f"   Tablas: {len(dashboard_data['tablas'])} conjuntos de datos")

def paso_6_configuraciones_avanzadas():
    """
    🎯 OBJETIVO: Crear sistemas de configuración profesionales
    
    ⚙️ APLICACIONES AVANZADAS:
    - Configuraciones por ambiente (dev, test, prod)
    - Gestión de usuarios y permisos
    - Parámetros de dispositivos PyModbus
    - Configuración de servicios Flask
    """
    print("\n" + "=" * 70)
    print("PASO 6: CONFIGURACIONES AVANZADAS DE SISTEMAS")
    print("=" * 70)
    
    # CONFIGURACIÓN POR AMBIENTES
    print(f"🌍 CONFIGURACIÓN POR AMBIENTES:")
    
    configuraciones = {
        "desarrollo": {
            "base_datos": {
                "host": "localhost",
                "puerto": 5432,
                "nombre": "planta_dev",
                "usuario": "dev_user",
                "debug": True
            },
            "modbus": {
                "timeout": 10.0,  # Más tiempo para debug
                "retries": 5,
                "log_level": "DEBUG"
            },
            "flask": {
                "host": "127.0.0.1",
                "puerto": 5000,
                "debug": True,
                "reload": True
            }
        },
        "produccion": {
            "base_datos": {
                "host": "db-prod.empresa.com",
                "puerto": 5432,
                "nombre": "planta_prod",
                "usuario": "prod_user",
                "debug": False
            },
            "modbus": {
                "timeout": 3.0,
                "retries": 3,
                "log_level": "ERROR"
            },
            "flask": {
                "host": "0.0.0.0",
                "puerto": 80,
                "debug": False,
                "reload": False
            }
        }
    }
    
    # Simular ambiente actual
    ambiente_actual = "desarrollo"
    config_activa = configuraciones[ambiente_actual]
    
    print(f"Ambiente activo: {ambiente_actual.upper()}")
    print(f"Base de datos: {config_activa['base_datos']['host']}:{config_activa['base_datos']['puerto']}")
    print(f"Modbus timeout: {config_activa['modbus']['timeout']}s")
    print(f"Flask debug: {config_activa['flask']['debug']}")
    
    # GESTIÓN DE USUARIOS Y PERMISOS
    print(f"\n👥 SISTEMA DE USUARIOS Y PERMISOS:")
    
    sistema_usuarios = {
        "usuarios": {
            "admin_001": {
                "nombre": "Carlos García",
                "email": "cgarcia@empresa.com",
                "rol": "administrador",
                "ultimo_acceso": "2025-06-30 08:15:00",
                "activo": True
            },
            "op_002": {
                "nombre": "Ana Martínez", 
                "email": "amartinez@empresa.com",
                "rol": "operador",
                "ultimo_acceso": "2025-06-30 14:30:00",
                "activo": True
            },
            "mant_003": {
                "nombre": "Luis Rodríguez",
                "email": "lrodriguez@empresa.com", 
                "rol": "mantenimiento",
                "ultimo_acceso": "2025-06-29 16:45:00",
                "activo": True
            }
        },
        "roles": {
            "administrador": {
                "permisos": ["leer", "escribir", "configurar", "eliminar", "reportes"],
                "areas": ["todas"],
                "nivel_acceso": 5
            },
            "operador": {
                "permisos": ["leer", "escribir", "reportes"],
                "areas": ["produccion", "monitoreo"],
                "nivel_acceso": 3
            },
            "mantenimiento": {
                "permisos": ["leer", "escribir", "configurar"],
                "areas": ["equipos", "sensores", "actuadores"],
                "nivel_acceso": 4
            }
        }
    }
    
    # Función para verificar permisos
    def verificar_permiso(usuario_id, accion, area=None):
        if usuario_id not in sistema_usuarios["usuarios"]:
            return False
        
        usuario = sistema_usuarios["usuarios"][usuario_id]
        rol = usuario["rol"]
        config_rol = sistema_usuarios["roles"][rol]
        
        # Verificar si tiene el permiso
        if accion not in config_rol["permisos"]:
            return False
        
        # Verificar acceso al área
        if area and "todas" not in config_rol["areas"] and area not in config_rol["areas"]:
            return False
        
        return True
    
    # Pruebas de permisos
    print("Verificación de permisos:")
    usuarios_prueba = ["admin_001", "op_002", "mant_003"]
    acciones_prueba = [("leer", "produccion"), ("eliminar", "sensores"), ("configurar", "equipos")]
    
    for usuario in usuarios_prueba:
        nombre = sistema_usuarios["usuarios"][usuario]["nombre"]
        print(f"\n   {nombre} ({usuario}):")
        for accion, area in acciones_prueba:
            permitido = verificar_permiso(usuario, accion, area)
            estado = "✅ Permitido" if permitido else "❌ Denegado"
            print(f"     {accion} en {area}: {estado}")
    
    # CONFIGURACIÓN DE DISPOSITIVOS MODBUS
    print(f"\n🔧 CONFIGURACIÓN AVANZADA MODBUS:")
    
    dispositivos_modbus = {
        "templates": {
            "sensor_temperatura": {
                "función_lectura": 3,  # Read Holding Registers
                "direccion_base": 0,
                "cantidad_registros": 2,
                "tipo_dato": "float32",
                "factor_escala": 0.1,
                "offset": 0,
                "unidad": "°C"
            },
            "sensor_presion": {
                "función_lectura": 4,  # Read Input Registers
                "direccion_base": 10,
                "cantidad_registros": 1,
                "tipo_dato": "uint16",
                "factor_escala": 0.01,
                "offset": 0,
                "unidad": "bar"
            }
        },
        "dispositivos": {
            "TEMP_R001": {
                "ip": "192.168.1.101",
                "puerto": 502,
                "slave_id": 1,
                "template": "sensor_temperatura",
                "timeout": 3.0,
                "scan_rate": 5.0,  # segundos
                "habilitado": True
            },
            "PRES_R001": {
                "ip": "192.168.1.101",
                "puerto": 502,
                "slave_id": 1,
                "template": "sensor_presion", 
                "timeout": 3.0,
                "scan_rate": 2.0,
                "habilitado": True
            }
        }
    }
    
    print("Configuración Modbus cargada:")
    print(f"   Templates: {len(dispositivos_modbus['templates'])}")
    print(f"   Dispositivos: {len(dispositivos_modbus['dispositivos'])}")
    
    for dev_id, config in dispositivos_modbus["dispositivos"].items():
        template = dispositivos_modbus["templates"][config["template"]]
        print(f"   {dev_id}: {config['ip']}:{config['puerto']} ({template['unidad']})")

def paso_7_ejemplo_integrador():
    """
    🎯 OBJETIVO: Sistema completo de gestión industrial con diccionarios
    
    🏭 PROYECTO: Centro de Control Unificado
    Integra todos los conceptos de diccionarios en un sistema real que podría
    valer $500,000+ en la industria.
    """
    print("\n" + "=" * 70)
    print("PASO 7: PROYECTO INTEGRADOR - CENTRO DE CONTROL")
    print("=" * 70)
    
    import random
    from datetime import datetime, timedelta
    
    # SISTEMA COMPLETO DE GESTIÓN
    centro_control = {
        "metadata": {
            "sistema": "SCADA Industrial v3.2.1",
            "planta": "Complejo Petroquímico Sur",
            "inicializado": datetime.now().isoformat(),
            "operador_turno": "Ing. María Fernández",
            "version_protocolo": "Modbus TCP v1.1b"
        },
        "configuracion": {
            "general": {
                "scan_rate_global": 1.0,  # segundos
                "timeout_comunicacion": 5.0,
                "max_reintentos": 3,
                "log_level": "INFO",
                "backup_automatico": True
            },
            "alarmas": {
                "escalamiento_critico": 300,  # segundos
                "notificacion_email": True,
                "notificacion_sms": True,
                "archivo_sonido": "alarm_critical.wav"
            },
            "base_datos": {
                "host": "db-cluster.empresa.com",
                "puerto": 5432,
                "esquema": "industrial_data",
                "retention_dias": 365
            }
        },
        "areas": {
            "destilacion": {
                "descripcion": "Unidad de Destilación Atmosférica",
                "supervisor": "Ing. Carlos Ruiz",
                "equipos": {
                    "T-101": {
                        "nombre": "Torre Destilación Principal",
                        "tipo": "Columna Destilación",
                        "sensores": {
                            "TI-101": {"tipo": "temperatura", "posicion": "Tope", "valor": 78.5, "unidad": "°C"},
                            "TI-102": {"tipo": "temperatura", "posicion": "Fondo", "valor": 145.2, "unidad": "°C"},
                            "PI-101": {"tipo": "presion", "posicion": "Tope", "valor": 1.2, "unidad": "bar"},
                            "LI-101": {"tipo": "nivel", "posicion": "Fondo", "valor": 67.3, "unidad": "%"}
                        },
                        "actuadores": {
                            "FV-101": {"tipo": "valvula", "descripcion": "Reflujo", "apertura": 45.2},
                            "FV-102": {"tipo": "valvula", "descripcion": "Vapor", "apertura": 78.5}
                        }
                    },
                    "P-101": {
                        "nombre": "Bomba Reflujo Principal", 
                        "tipo": "Bomba Centrífuga",
                        "sensores": {
                            "FI-201": {"tipo": "flujo", "posicion": "Descarga", "valor": 125.3, "unidad": "m3/h"},
                            "PI-201": {"tipo": "presion", "posicion": "Descarga", "valor": 5.2, "unidad": "bar"},
                            "VI-201": {"tipo": "vibracion", "posicion": "Carcasa", "valor": 3.1, "unidad": "mm/s"}
                        },
                        "actuadores": {
                            "M-201": {"tipo": "motor", "descripcion": "Motor Principal", "rpm": 1485, "corriente": 12.3}
                        }
                    }
                }
            },
            "cracking": {
                "descripcion": "Unidad de Cracking Catalítico",
                "supervisor": "Ing. Ana López",
                "equipos": {
                    "R-201": {
                        "nombre": "Reactor Cracking Principal",
                        "tipo": "Reactor Lecho Fluidizado", 
                        "sensores": {
                            "TI-301": {"tipo": "temperatura", "posicion": "Entrada", "valor": 485.7, "unidad": "°C"},
                            "TI-302": {"tipo": "temperatura", "posicion": "Salida", "valor": 512.3, "unidad": "°C"},
                            "PI-301": {"tipo": "presion", "posicion": "Reactor", "valor": 2.8, "unidad": "bar"}
                        }
                    }
                }
            }
        },
        "alarmas": {
            "activas": [],
            "historico": [],
            "configuracion": {
                "TI-101": {"limite_alto": 85.0, "limite_muy_alto": 95.0, "prioridad": "ALTA"},
                "TI-102": {"limite_alto": 155.0, "limite_muy_alto": 165.0, "prioridad": "CRITICA"},
                "PI-101": {"limite_alto": 1.5, "limite_muy_alto": 1.8, "prioridad": "MEDIA"},
                "VI-201": {"limite_alto": 4.5, "limite_muy_alto": 6.0, "prioridad": "ALTA"}
            }
        },
        "estadisticas": {
            "tiempo_operacion": {"horas": 0, "minutos": 0, "segundos": 0},
            "eventos_dia": 0,
            "alarmas_dia": 0,
            "eficiencia_comunicacion": 0.0,
            "dispositivos_online": 0,
            "dispositivos_total": 0
        }
    }
    
    # FUNCIÓN DE SIMULACIÓN DE OPERACIÓN
    def simular_ciclo_operacion():
        """Simula un ciclo de operación del sistema"""
        
        print(f"\n⏰ CICLO DE OPERACIÓN - {datetime.now().strftime('%H:%M:%S')}")
        
        # Actualizar lecturas de sensores
        dispositivos_online = 0
        dispositivos_total = 0
        alarmas_nuevas = 0
        
        for area_id, area_data in centro_control["areas"].items():
            print(f"\n🏭 Área: {area_data['descripcion']}")
            
            for equipo_id, equipo_data in area_data["equipos"].items():
                print(f"   📟 {equipo_data['nombre']}:")
                
                # Simular lecturas de sensores
                for sensor_id, sensor_data in equipo_data["sensores"].items():
                    dispositivos_total += 1
                    
                    # Simular variación de ±5%
                    valor_base = sensor_data["valor"]
                    variacion = random.uniform(-0.05, 0.05)
                    nuevo_valor = valor_base * (1 + variacion)
                    sensor_data["valor"] = round(nuevo_valor, 1)
                    sensor_data["timestamp"] = datetime.now().isoformat()
                    
                    # Simular comunicación (95% éxito)
                    comunicacion_ok = random.random() > 0.05
                    if comunicacion_ok:
                        dispositivos_online += 1
                        estado = "📡 ONLINE"
                    else:
                        estado = "❌ OFFLINE"
                    
                    print(f"      {sensor_id}: {sensor_data['valor']} {sensor_data['unidad']} {estado}")
                    
                    # Verificar alarmas
                    if sensor_id in centro_control["alarmas"]["configuracion"]:
                        config_alarma = centro_control["alarmas"]["configuracion"][sensor_id]
                        valor = sensor_data["valor"]
                        
                        if valor > config_alarma["limite_muy_alto"]:
                            nivel = "CRÍTICA"
                            alarmas_nuevas += 1
                        elif valor > config_alarma["limite_alto"]:
                            nivel = "ALTA"
                            alarmas_nuevas += 1
                        else:
                            nivel = None
                        
                        if nivel:
                            alarma = {
                                "timestamp": datetime.now().isoformat(),
                                "sensor": sensor_id,
                                "valor": valor,
                                "limite": config_alarma["limite_alto"],
                                "nivel": nivel,
                                "area": area_id,
                                "equipo": equipo_id,
                                "estado": "ACTIVA"
                            }
                            centro_control["alarmas"]["activas"].append(alarma)
                            print(f"        🚨 ALARMA {nivel}: {valor} > {config_alarma['limite_alto']}")
        
        # Actualizar estadísticas
        stats = centro_control["estadisticas"]
        stats["dispositivos_online"] = dispositivos_online
        stats["dispositivos_total"] = dispositivos_total
        stats["eficiencia_comunicacion"] = (dispositivos_online / dispositivos_total * 100) if dispositivos_total > 0 else 0
        stats["alarmas_dia"] += alarmas_nuevas
        stats["eventos_dia"] += 1
        
        return dispositivos_online, dispositivos_total, alarmas_nuevas
    
    # EJECUTAR SIMULACIÓN
    print(f"🚀 INICIANDO CENTRO DE CONTROL")
    print(f"Sistema: {centro_control['metadata']['sistema']}")
    print(f"Planta: {centro_control['metadata']['planta']}")
    print(f"Operador: {centro_control['metadata']['operador_turno']}")
    
    # Simular 3 ciclos de operación
    for ciclo in range(3):
        online, total, alarmas = simular_ciclo_operacion()
        
        print(f"\n📊 RESUMEN CICLO {ciclo + 1}:")
        print(f"   Dispositivos online: {online}/{total} ({online/total*100:.1f}%)")
        print(f"   Alarmas nuevas: {alarmas}")
        print(f"   Alarmas activas: {len(centro_control['alarmas']['activas'])}")
        
        # Simular pausa entre ciclos
        import time
        time.sleep(1)
    
    # REPORTE FINAL EJECUTIVO
    print(f"\n" + "="*70)
    print("📋 REPORTE EJECUTIVO DEL SISTEMA")
    print("="*70)
    
    stats = centro_control["estadisticas"]
    total_areas = len(centro_control["areas"])
    total_equipos = sum(len(area["equipos"]) for area in centro_control["areas"].values())
    total_sensores = sum(
        len(equipo["sensores"]) 
        for area in centro_control["areas"].values()
        for equipo in area["equipos"].values()
    )
    
    print(f"🏭 Estructura del Sistema:")
    print(f"   • Áreas monitoreadas: {total_areas}")
    print(f"   • Equipos controlados: {total_equipos}")
    print(f"   • Sensores instalados: {total_sensores}")
    
    print(f"\n📡 Estado de Comunicaciones:")
    print(f"   • Dispositivos online: {stats['dispositivos_online']}/{stats['dispositivos_total']}")
    print(f"   • Eficiencia comunicación: {stats['eficiencia_comunicacion']:.1f}%")
    
    print(f"\n🚨 Estado de Alarmas:")
    print(f"   • Alarmas activas: {len(centro_control['alarmas']['activas'])}")
    print(f"   • Alarmas del día: {stats['alarmas_dia']}")
    
    # Alarmas por nivel
    if centro_control['alarmas']['activas']:
        alarmas_por_nivel = {}
        for alarma in centro_control['alarmas']['activas']:
            nivel = alarma['nivel']
            alarmas_por_nivel[nivel] = alarmas_por_nivel.get(nivel, 0) + 1
        
        for nivel, cantidad in alarmas_por_nivel.items():
            print(f"     - {nivel}: {cantidad}")
    
    eficiencia_general = (
        stats['eficiencia_comunicacion'] * 0.4 +
        max(0, 100 - len(centro_control['alarmas']['activas']) * 10) * 0.6
    )
    
    print(f"\n🎯 Eficiencia General del Sistema: {eficiencia_general:.1f}%")
    
    estado_sistema = (
        "🟢 ÓPTIMO" if eficiencia_general >= 90 else
        "🟡 BUENO" if eficiencia_general >= 75 else
        "🟠 REGULAR" if eficiencia_general >= 60 else
        "🔴 CRÍTICO"
    )
    
    print(f"🎪 Estado General: {estado_sistema}")

# ═══════════════════════════════════════════════════════════════════════════════
# FUNCIÓN PRINCIPAL - EJECUTA TODA LA SECUENCIA DE ENSEÑANZA
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    """
    🚀 FUNCIÓN PRINCIPAL
    Ejecuta toda la secuencia de enseñanza paso a paso
    """
    print("🐍 BIENVENIDO AL TEMARIO: DICCIONARIOS")
    print("📚 Curso Intensivo de Python - Aplicado a Automatización Industrial") 
    print("👨‍🏫 Tutor: GitHub Copilot | 👨‍🎓 Estudiante: José")
    print("\n🎯 Los diccionarios son el CORAZÓN de las aplicaciones industriales")
    print("   Configuraciones PyModbus, APIs Flask, JSON, sistemas de gestión\n")
    
    # Ejecutar cada paso secuencialmente
    paso_1_introduccion_diccionarios()
    paso_2_operaciones_diccionarios()
    paso_3_diccionarios_anidados()
    paso_4_iteracion_diccionarios()
    paso_5_json_y_diccionarios()
    paso_6_configuraciones_avanzadas()
    paso_7_ejemplo_integrador()
    
    print("\n" + "=" * 70)
    print("🎉 ¡TEMARIO DICCIONARIOS COMPLETADO!")
    print("=" * 70)
    print("✅ Dominas la estructura clave-valor fundamental")
    print("✅ Puedes crear configuraciones complejas")
    print("✅ Preparas datos perfectos para JSON/APIs")
    print("✅ Manejas sistemas de gestión profesionales")
    print("\n🚀 PRÓXIMO PASO: Practicar con casos industriales reales")
    print("📋 RECORDATORIO: Solo avanza cuando confirmes consolidación")
    print("\n💡 CONEXIÓN DIRECTA CON TUS METAS:")
    print("   • PyModbus: Configuraciones de dispositivos y mapeo de datos")
    print("   • Flask: Respuestas JSON estructuradas y configuración de endpoints")
    print("   • SQL: Preparación de datos y resultados de consultas")
    print("   • Tkinter: Configuración de interfaces y gestión de estado")
    print("   • ¡YA TIENES LAS BASES PARA CREAR SISTEMAS INDUSTRIALES REALES!")

if __name__ == "__main__":
    main()
