from flask import Flask, render_template, request, redirect, url_for, session
from datenbank import connect
import mysql.connector

app = Flask(__name__)
app.secret_key = 'geheimer_schluessel'

@app.route("/conection.html", methods=['POST', 'GET'])
def conection():
    if request.method == "POST":
        # MySQL-Datenbankverbindungseinstellungen
        database_name = request.form.get("database_name")
        credentials = {
            "host": "localhost",
            "user": "",
            "password": "",
            "database": database_name
        }

        # Versuchen, eine Verbindung zur Datenbank herzustellen
        try:
            db_connection = connect("MySQL", credentials)
            if db_connection.is_connected():
                print(f"Verbindung erfolgreich zu: {database_name}")
                session['db_connection'] = True  # Markiere Verbindung als erfolgreich
                session['database_name'] = database_name
                db_connection.close()
                return redirect(url_for("query"))
            else:
                print("Verbindung fehlgeschlagen.")
                session['db_connection'] = False
                return "Verbindung fehlgeschlagen, bitte versuchen Sie es erneut."
        except mysql.connector.Error as err:
            print(f"Fehler bei der Verbindung zur Datenbank: {err}")
            session['db_connection'] = False
            return f"Verbindung zur Datenbank fehlgeschlagen: {err}"

    return render_template("conection.html")

@app.route("/query.html", methods=['POST', 'GET'])
def query():
    if session.get('db_connection'):
        message = f"Verbindung zur Datenbank '{session['database_name']}' erfolgreich hergestellt!"
    else:
        message = "Keine Verbindung zur Datenbank."

    return render_template("query.html", message=message)

@app.route("/table.html", methods=['POST', 'GET'])
def table():
    print(request.form['anfrage'])
    return render_template("table.html")

if __name__ == "__main__":
    app.run(debug=True)
