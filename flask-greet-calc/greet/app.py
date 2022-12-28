from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
    <body>
    <h1> Greet Page </h1>
    <p> Welcome to the Greet Page</p>
    <a href="/welcome"> Go to Welcome page </a>
    </body>
    </html>
    """
    return html

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcomehome():
    return "welcome home"

@app.route('/welcome/back')
def welcomeback():
    return "welcome back"
