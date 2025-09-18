import psycopg2

# Conexión a la base de datos con tus datos de Docker
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    dbname="postgres",   # si no definiste POSTGRES_DB, la default es "postgres"
    user="postgres",     # usuario por defecto
    password="contra"    # la clave que pusiste
)
cur = conn.cursor()

# Crear tablas
cur.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id),
    producto VARCHAR(100) NOT NULL
);
""")
print("Tablas creadas ✅")

# DDL: Agregar columnas
cur.execute("ALTER TABLE usuarios ADD COLUMN IF NOT EXISTS edad INT;")
cur.execute("ALTER TABLE pedidos ADD COLUMN IF NOT EXISTS cantidad INT DEFAULT 1;")
print("Columnas agregadas ✅")

# DDL: Renombrar columnas
cur.execute("ALTER TABLE usuarios RENAME COLUMN nombre TO nombre_completo;")
print("Columna renombrada ✅")

# DDL: Eliminar columnas
cur.execute("ALTER TABLE pedidos DROP COLUMN IF EXISTS cantidad;")
print("Columna eliminada ✅")

# DDL: Agregar un CHECK
cur.execute("ALTER TABLE usuarios ADD CONSTRAINT check_edad CHECK (edad >= 0);")
print("Restricción CHECK agregada ✅")

# DDL: Eliminar una tabla
cur.execute("DROP TABLE IF EXISTS pedidos;")
print("Tabla eliminada ✅")

# Guardar cambios y cerrar
conn.commit()
cur.close()
conn.close()
print("Conexión cerrada ✅")
