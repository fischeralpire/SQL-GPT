import mysql.connector

def connect(database_type, credentials):
    db_connection = None
    if database_type == "MySQL":
        db_connection = connect_mysql(
            credentials["host"], 
            credentials["user"], 
            credentials["password"], 
            credentials["database"]
        )
    else:
        print(f"{database_type} connection not implemented")
    return db_connection

def connect_mysql(host, user, password, database):
    """Verbindung zur MySQL-Datenbank herstellen."""
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def query(db_connection, query_text):
    """
    Führt eine SQL-Abfrage auf der MySQL-Datenbank aus und gibt das Ergebnis zurück.
    """
    cursor = db_connection.cursor()
    cursor.execute(query_text)
    result = cursor.fetchall()
    cursor.close()
    return result

def get_schema(db_connection):
    """
    Ruft das Schema (Tabellen und ihre Struktur) der MySQL-Datenbank ab.
    """
    cursor = db_connection.cursor()
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    schema = {}
    for (table_name,) in tables:
        cursor.execute(f"DESCRIBE {table_name};")
        schema[table_name] = cursor.fetchall()

    cursor.close()
    return schema

def seed_db(db_connection, db_seed):
    """
    Füllt die MySQL-Datenbank mit vorgegebenen SQL-Befehlen (`db_seed`).
    """
    cursor = db_connection.cursor()
    for s in db_seed:
        cursor.execute(s)
    db_connection.commit()  # Änderungen speichern
    cursor.close()
