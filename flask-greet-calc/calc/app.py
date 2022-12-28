from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <html>
    <body>
    <h1> Calc Page </h1>
    <p> Welcome to the Calc Page</p>
    <a href="/add">Add Numbers</a>
    </body>
    </html>
    """
    return html

@app.route('/math/<operation>')
def all(operation):
    ops = {'add':add,'sub':sub,'mult':mult,'div':div}
    a = request.args.get('a')
    b = request.args.get('b')
    result = ops[operation](int(a),int(b))
    # if(operation == 'add'):
    #     result = add(int(a),int(b))
    # elif(operation == 'sub'):
    #     result = sub(int(a),int(b))
    # elif(operation == 'mult'):
    #     result = mult(int(a),int(b))
    # elif(operation == 'div'):
    #     result = div(int(a),int(b))    
    return f"{result}"


@app.route('/add')
def addpage():
    a = request.args.get('a')
    b = request.args.get('b')
    result = add(int(a),int(b))
    return f"{result}"

@app.route('/mult')
def multpage():
    a = request.args.get('a')
    b = request.args.get('b')
    result = mult(int(a),int(b))
    return f"{result}"

@app.route('/div')
def divpage():
    a = request.args.get('a')
    b = request.args.get('b')
    result = div(int(a),int(b))
    return f"{result}"

@app.route('/sub')
def subpage():
    a = request.args.get('a')
    b = request.args.get('b')
    result = sub(int(a),int(b))
    return f"{result}"
