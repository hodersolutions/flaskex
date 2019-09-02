from flask import Flask

app  = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

@app.route("/home", methods=["GET"])
def home_1():
    return "<h1>Lunch Time </h1>"

app.run()