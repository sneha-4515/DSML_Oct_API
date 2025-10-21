from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/panda")
def hello_panda():
    return "<p>Hello, panda!</p>"
@app.route("/ping")
def hello_ping():
    return "{'message': 'Hi I am JSON reply'}"