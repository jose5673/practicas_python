"""
=============================================================================
                     MÓDULO 3.1: BASES DE DATOS CON SQL
                         MAESTRÍA EN PYTHON - FASE 3
=============================================================================

ESTADO DEL ÁRBOL DE CONOCIMIENTO (ACTUALIZADO):

🌳 ÁRBOL DE CONOCIMIENTO - MAESTRÍA EN PYTHON
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 FASE 1: FUNDAMENTOS DE PYTHON ✅ [CONSOLIDADA]
├── 📝 Tipos de Datos y Variables ✅ [CONSOLIDADO]
├── 📋 Listas y Tuplas ✅ [CONSOLIDADO]
├── 📚 Diccionarios ✅ [CONSOLIDADO]
└── 🎯 Programación Orientada a Objetos ✅ [CONSOLIDADO]

🚀 FASE 2: PYTHON INTERMEDIO ✅ [CONSOLIDADA]
├── 📁 Archivos y Excepciones ✅ [CONSOLIDADO]
├── 📦 Librerías Fundamentales ✅ [CONSOLIDADO]
├── 🏗️ Entornos Virtuales y Dependencias ✅ [CONSOLIDADO]
└── ⭐ Buenas Prácticas en Python ✅ [CONSOLIDADO]

🗄️ FASE 3: BASES DE DATOS CON SQL 🆕 [EN CURSO]
├── 🔧 Fundamentos de SQL ⏳ [INICIADO]
├── 🐍 Python + SQLite ⏳ [PENDIENTE]
├── 📊 Consultas Avanzadas ⏳ [PENDIENTE]
├── 🔄 ORM con SQLAlchemy ⏳ [PENDIENTE]
└── 💾 Proyecto Integrador BD ⏳ [PENDIENTE]

FECHA DE INICIO FASE 3: {fecha_actual}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

=============================================================================
                        3.1 FUNDAMENTOS DE SQL
=============================================================================

¿QUÉ SON LAS BASES DE DATOS?
Una base de datos es un sistema organizado para almacenar, gestionar y 
recuperar información de manera eficiente y estructurada.

TIPOS DE BASES DE DATOS:
1. Relacionales (SQL): MySQL, PostgreSQL, SQLite, SQL Server
2. NoSQL: MongoDB, Redis, Cassandra
3. En memoria: Redis, Memcached
4. Grafos: Neo4j, Amazon Neptune

¿POR QUÉ SQL?
- Estándar industrial desde 1970s
- Lenguaje declarativo (dices QUÉ quieres, no CÓMO)
- Potente para consultas complejas
- Ampliamente compatible

=============================================================================
                           CONCEPTOS FUNDAMENTALES
=============================================================================

📊 ESTRUCTURA DE UNA BASE DE DATOS RELACIONAL:

1. BASE DE DATOS (Database)
   ├── TABLA 1 (Table)
   │   ├── COLUMNA A (Column/Field)
   │   ├── COLUMNA B
   │   └── FILA 1, FILA 2... (Rows/Records)
   ├── TABLA 2
   └── TABLA N

TERMINOLOGÍA CLAVE:
- Tabla (Table): Estructura que contiene datos relacionados
- Fila/Registro (Row/Record): Una entrada individual de datos
- Columna/Campo (Column/Field): Un atributo específico
- Clave Primaria (Primary Key): Identificador único de cada fila
- Clave Foránea (Foreign Key): Referencia a otra tabla
- Índice (Index): Estructura para acelerar búsquedas

=============================================================================
                             TIPOS DE DATOS SQL
=============================================================================

🔢 TIPOS NUMÉRICOS:
- INTEGER / INT: Números enteros (-2147483648 a 2147483647)
- REAL / FLOAT: Números decimales
- DECIMAL(p,s): Decimales con precisión específica

📝 TIPOS DE TEXTO:
- TEXT: Texto de longitud variable
- VARCHAR(n): Texto con longitud máxima n
- CHAR(n): Texto de longitud fija n

📅 TIPOS DE FECHA Y HORA:
- DATE: Solo fecha (YYYY-MM-DD)
- TIME: Solo hora (HH:MM:SS)
- DATETIME: Fecha y hora completa
- TIMESTAMP: Marca de tiempo

✅ OTROS TIPOS:
- BOOLEAN: Verdadero/Falso
- BLOB: Datos binarios (imágenes, archivos)
- NULL: Valor vacío o desconocido

=============================================================================
                          COMANDOS SQL BÁSICOS
=============================================================================

🏗️ DDL (DATA DEFINITION LANGUAGE) - ESTRUCTURA:

CREATE TABLE:
"""

-- Crear una tabla de empleados
CREATE TABLE empleados (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    edad INTEGER,
    salario REAL,
    departamento TEXT,
    fecha_ingreso DATE
);

-- Crear tabla con restricciones
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    precio REAL CHECK (precio > 0),
    stock INTEGER DEFAULT 0,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

"""

ALTER TABLE:
"""

-- Agregar columna
ALTER TABLE empleados ADD COLUMN email TEXT;

-- Modificar columna (depende del SGBD)
ALTER TABLE empleados RENAME COLUMN nombre TO nombre_completo;

-- Eliminar columna
ALTER TABLE empleados DROP COLUMN edad;

"""

DROP TABLE:
"""

-- Eliminar tabla completa
DROP TABLE empleados;

-- Eliminar solo si existe
DROP TABLE IF EXISTS empleados;

"""

📥 DML (DATA MANIPULATION LANGUAGE) - DATOS:

INSERT:
"""

-- Insertar un registro
INSERT INTO empleados (nombre, apellido, edad, salario, departamento) 
VALUES ('Juan', 'Pérez', 30, 50000, 'IT');

-- Insertar múltiples registros
INSERT INTO empleados (nombre, apellido, edad, salario, departamento) 
VALUES 
    ('María', 'García', 25, 45000, 'Marketing'),
    ('Carlos', 'López', 35, 60000, 'IT'),
    ('Ana', 'Rodríguez', 28, 52000, 'Ventas');

-- Insertar desde otra tabla
INSERT INTO empleados_backup 
SELECT * FROM empleados WHERE departamento = 'IT';

"""

SELECT:
"""

-- Seleccionar todos los campos
SELECT * FROM empleados;

-- Seleccionar campos específicos
SELECT nombre, apellido, salario FROM empleados;

-- Ordenar resultados
SELECT * FROM empleados ORDER BY salario DESC;

-- Filtrar con WHERE
SELECT * FROM empleados WHERE departamento = 'IT';

-- Múltiples condiciones
SELECT * FROM empleados 
WHERE departamento = 'IT' AND salario > 50000;

-- Búsqueda con LIKE
SELECT * FROM empleados WHERE nombre LIKE 'Juan%';

-- Limitar resultados
SELECT * FROM empleados LIMIT 5;

"""

UPDATE:
"""

-- Actualizar un campo
UPDATE empleados SET salario = 55000 WHERE id = 1;

-- Actualizar múltiples campos
UPDATE empleados 
SET salario = salario * 1.1, departamento = 'IT Senior'
WHERE departamento = 'IT' AND edad > 30;

"""

DELETE:
"""

-- Eliminar registros específicos
DELETE FROM empleados WHERE departamento = 'Marketing';

-- Eliminar todos los registros (¡CUIDADO!)
DELETE FROM empleados;

"""

🔍 DQL (DATA QUERY LANGUAGE) - CONSULTAS AVANZADAS:

"""

-- FUNCIONES DE AGREGACIÓN
SELECT COUNT(*) as total_empleados FROM empleados;
SELECT AVG(salario) as salario_promedio FROM empleados;
SELECT MAX(salario) as salario_maximo FROM empleados;
SELECT MIN(salario) as salario_minimo FROM empleados;
SELECT SUM(salario) as total_nomina FROM empleados;

-- GROUP BY
SELECT departamento, COUNT(*) as cantidad, AVG(salario) as promedio
FROM empleados 
GROUP BY departamento;

-- HAVING (filtro después de GROUP BY)
SELECT departamento, AVG(salario) as promedio
FROM empleados 
GROUP BY departamento
HAVING AVG(salario) > 50000;

-- SUBCONSULTAS
SELECT * FROM empleados 
WHERE salario > (SELECT AVG(salario) FROM empleados);

-- JOINS (unir tablas)
SELECT e.nombre, e.apellido, d.nombre_departamento
FROM empleados e
INNER JOIN departamentos d ON e.departamento_id = d.id;

"""

=============================================================================
                          RESTRICCIONES Y CONSTRAINTS
=============================================================================

🔒 TIPOS DE RESTRICCIONES:

1. PRIMARY KEY: Identifica únicamente cada fila
2. FOREIGN KEY: Mantiene integridad referencial
3. UNIQUE: Evita valores duplicados
4. NOT NULL: Campo obligatorio
5. CHECK: Validación personalizada
6. DEFAULT: Valor por defecto

EJEMPLOS PRÁCTICOS:
"""

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE CHECK (email LIKE '%@%'),
    edad INTEGER CHECK (edad >= 18),
    activo BOOLEAN DEFAULT TRUE,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    usuario_id INTEGER NOT NULL,
    total REAL CHECK (total > 0),
    estado TEXT DEFAULT 'pendiente',
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

"""

=============================================================================
                             ÍNDICES Y RENDIMIENTO
=============================================================================

🚀 ¿QUÉ SON LOS ÍNDICES?
Estructuras de datos que mejoran la velocidad de las consultas,
similar al índice de un libro.

TIPOS DE ÍNDICES:
- Único (UNIQUE): No permite duplicados
- Compuesto: Múltiples columnas
- Parcial: Solo algunas filas

"""

-- Crear índice simple
CREATE INDEX idx_empleado_apellido ON empleados(apellido);

-- Crear índice único
CREATE UNIQUE INDEX idx_empleado_email ON empleados(email);

-- Crear índice compuesto
CREATE INDEX idx_empleado_dept_salario ON empleados(departamento, salario);

-- Eliminar índice
DROP INDEX idx_empleado_apellido;

"""

BUENAS PRÁCTICAS PARA ÍNDICES:
✅ Crear índices en columnas de búsqueda frecuente
✅ Crear índices en claves foráneas
✅ Usar índices compuestos para consultas múltiples
❌ No crear demasiados índices (ralentizan INSERT/UPDATE)
❌ No crear índices en tablas muy pequeñas

=============================================================================
                          TRANSACCIONES Y ACID
=============================================================================

🔄 ¿QUÉ ES UNA TRANSACCIÓN?
Una secuencia de operaciones que se ejecutan como una unidad atómica.
O se ejecutan TODAS o NO se ejecuta NINGUNA.

PROPIEDADES ACID:
- A (Atomicity): Todo o nada
- C (Consistency): Estado válido siempre
- I (Isolation): Transacciones independientes
- D (Durability): Cambios permanentes

"""

-- Ejemplo de transacción
BEGIN TRANSACTION;

UPDATE cuentas SET saldo = saldo - 1000 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 1000 WHERE id = 2;

-- Si todo está bien
COMMIT;

-- Si algo falla
-- ROLLBACK;

"""

=============================================================================
                            SQLITE ESPECÍFICO
=============================================================================

🗄️ ¿POR QUÉ SQLITE PARA APRENDER?
- No requiere servidor
- Archivo único .db
- Sintaxis SQL estándar
- Ideal para desarrollo y aprendizaje
- Usado en móviles, navegadores, apps locales

CARACTERÍSTICAS ESPECIALES:
- Tipado dinámico
- Soporte completo de transacciones
- Tamaño máximo: 281 TB
- VACUUM para optimizar espacio

"""

-- Comandos específicos de SQLite
.help                   -- Ayuda
.tables                 -- Listar tablas
.schema tabla_nombre    -- Ver estructura de tabla
.headers on             -- Mostrar headers en resultados
.mode column            -- Formato de columnas
.output archivo.txt     -- Exportar a archivo
.read script.sql        -- Ejecutar script
.exit                   -- Salir

"""

=============================================================================
                          PATRONES Y MEJORES PRÁCTICAS
=============================================================================

📋 CONVENCIONES DE NOMENCLATURA:
- Tablas: plural, minúsculas, guiones bajos (usuarios, productos_ventas)
- Columnas: minúsculas, descriptivas (fecha_nacimiento, precio_unitario)
- Índices: prefijo idx_ (idx_usuario_email)
- Claves foráneas: tabla_id (usuario_id, categoria_id)

🏗️ DISEÑO DE ESQUEMAS:
1. Normalización: Evitar redundancia
2. Desnormalización: Optimizar consultas frecuentes
3. Claves primarias auto-incrementales
4. Usar tipos de datos apropiados
5. Definir restricciones desde el diseño

🔍 OPTIMIZACIÓN DE CONSULTAS:
- Usar EXPLAIN QUERY PLAN para analizar
- Filtrar antes de unir (WHERE antes de JOIN)
- Usar LIMIT cuando sea posible
- Evitar SELECT * en producción
- Usar índices apropiados

💡 SEGURIDAD:
- Validar entrada de datos
- Usar parámetros en consultas (evitar SQL injection)
- Principio de menor privilegio
- Respaldos regulares

=============================================================================
                              EJERCICIOS PRÁCTICOS
=============================================================================

🎯 EJERCICIO 1: BIBLIOTECA PERSONAL
Diseña una base de datos para gestionar tu biblioteca personal.

Tablas necesarias:
- autores (id, nombre, apellido, nacionalidad, fecha_nacimiento)
- categorias (id, nombre, descripcion)
- libros (id, titulo, autor_id, categoria_id, año_publicacion, isbn, paginas)
- lecturas (id, libro_id, fecha_inicio, fecha_fin, calificacion, notas)

🎯 EJERCICIO 2: TIENDA ONLINE
Crea el esquema para una tienda online básica.

Tablas:
- usuarios (id, username, email, password_hash, fecha_registro)
- categorias (id, nombre, descripcion)
- productos (id, nombre, descripcion, precio, stock, categoria_id)
- pedidos (id, usuario_id, fecha, total, estado)
- detalle_pedidos (id, pedido_id, producto_id, cantidad, precio_unitario)

🎯 EJERCICIO 3: ANÁLISIS DE DATOS
Usando datos de empleados, crear consultas para:
- Top 5 empleados mejor pagados por departamento
- Promedio de edad por departamento
- Empleados que ganan más que el promedio de su departamento
- Departamentos con más de 10 empleados

=============================================================================
                          PROYECTO INTEGRADOR FASE 3
=============================================================================

🚀 SISTEMA DE GESTIÓN DE INVENTARIO

DESCRIPCIÓN:
Desarrollar un sistema completo de gestión de inventario que incluya:

COMPONENTES:
1. Base de datos SQL bien estructurada
2. Interfaz Python para interactuar
3. Reportes y consultas avanzadas
4. Sistema de alertas por stock bajo
5. Historial de movimientos

TABLAS PRINCIPALES:
- proveedores
- categorias
- productos
- movimientos_inventario
- usuarios_sistema
- alertas

FUNCIONALIDADES:
- CRUD completo de productos
- Registro de entradas/salidas
- Consultas de stock actual
- Reportes de rotación
- Sistema de alertas automatizado

=============================================================================
                                RECURSOS ADICIONALES
=============================================================================

📚 DOCUMENTACIÓN OFICIAL:
- SQLite: https://sqlite.org/docs.html
- SQL Tutorial: https://www.w3schools.com/sql/
- DB-Engines: https://db-engines.com/

🛠️ HERRAMIENTAS RECOMENDADAS:
- DB Browser for SQLite (GUI)
- SQLiteStudio (Multiplataforma)
- VS Code Extension: SQLite Viewer
- DBeaver (Universal DB Tool)

📖 LIBROS RECOMENDADOS:
- "Learning SQL" - Alan Beaulieu
- "SQL in 10 Minutes" - Ben Forta
- "Database Design for Mere Mortals" - Michael Hernandez

=============================================================================
                              PRÓXIMOS PASOS
=============================================================================

📅 ROADMAP DE APRENDIZAJE:

SEMANA 1-2: Fundamentos SQL
- Sintaxis básica (SELECT, INSERT, UPDATE, DELETE)
- Tipos de datos y restricciones
- Práctica con SQLite

SEMANA 3-4: Python + SQLite
- Módulo sqlite3
- Conexiones y cursors
- Manejo de errores

SEMANA 5-6: Consultas Avanzadas
- JOINs complejos
- Subconsultas
- Funciones de ventana

SEMANA 7-8: ORM con SQLAlchemy
- Modelos y relaciones
- Consultas con ORM
- Migraciones

SEMANA 9-10: Proyecto Integrador
- Diseño completo
- Implementación
- Testing y optimización

=============================================================================

✅ CRITERIOS DE CONSOLIDACIÓN DEL MÓDULO 3.1:

1. ✅ Dominar sintaxis SQL básica (CRUD)
2. ✅ Entender conceptos de normalización
3. ✅ Crear esquemas con restricciones apropiadas
4. ✅ Escribir consultas con JOINs y subconsultas
5. ✅ Optimizar consultas con índices
6. ✅ Manejar transacciones correctamente
7. ✅ Completar ejercicios prácticos sin ayuda

=============================================================================

🎯 ESTADO ACTUAL: INICIADO
📝 PRÓXIMO PASO: Práctica con ejemplos básicos
⏰ TIEMPO ESTIMADO: 2-3 semanas para consolidación completa

RECUERDA: No avanzaremos hasta que confirmes la consolidación completa
de este módulo. La base de datos es fundamental para el desarrollo
profesional en Python.

"""
