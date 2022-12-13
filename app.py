from flask import Flask

app = Flask(__name__)

@app.route("/hello") #listen for this request to slash-hello
def say_hello(): #this is the funcion to execute when that happens
    return "hello there!" #text that will show up

@app.route("/goodbye") #listen for this request to slash-hello
def say_bye(): #this is the funcion to execute when that happens
    return "goodbye!" #text that will show up
