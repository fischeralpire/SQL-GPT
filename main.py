from flask import Flask, render_template, request

app = Flask(__name__)

# @app.route("/")
# def start_page():
#    return "Hallo"

# @app.route("/index.html")
# def home():
#    return render_template("index.html")

@app.route("/conection.html")
def conection():
   return render_template("conection.html")

@app.route("/query.html", methods=['POST', 'GET'])
def query():
   print(request.form['database_name'])
   return render_template("query.html")

@app.route("/table.html", methods=['POST', 'GET'])
def table():
   print(request.form['anfrage'])
   return render_template("table.html")

if __name__ == "__main__":
    app.run(debug=True)
