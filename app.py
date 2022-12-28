from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():

    print (request.args)
    term = request.args.get("term","")
    return f"WELCOME TO THE SEARCH PAGE YOU SEARCHED THIS TIME FOR {term}"

@app.route('/')
def home_page():
    html = """
    <html>
    <body>
    <h1> Home Page </h1>
    <p> Welcome to my simple app!</p>
    <a href="/hello"> Go to Hello page </a>
    </body>
    </html>
    """
    return html

@app.route("/welcome") #listen for this request to slash-hello
def welcome(): #this is the funcion to execute when that happens
    return "Welcome!"

@app.route("/welcome/home") #listen for this request to slash-hello
def welcomehome(): #this is the funcion to execute when that happens
    return "Welcome home!"

@app.route("/welcome/back") #listen for this request to slash-hello
def welcomeback(): #this is the funcion to execute when that happens
    return "Welcome back!"

# @app.route(”/post”,methods=[”POST”])
# def post_demo():
#     return "YOU MADE A POST REQUEST"

@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment"""
    return """
    <html>
        <body>
            <form method="POST">
                <input name="comment" placeholder="comment">
                <button>Submit</button>
            </form>
        </body>
    </html>
    """

@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""
    comment = request.form.get("comment","")
    #TODO save this into a DB
    return f"<h1>Received your comment {comment}</h1>"


@app.route("/goodbye") #listen for this request to slash-hello
def say_bye(): #this is the funcion to execute when that happens
    return "goodbye!" #text that will show up

USERS = {
    "whiskey": "Whiskey The Dog",
    "spike": "Spike the Porcupine"
}

@app.route('/user/<username>') #<> brackets include space for a variable
def show_user_profile(username):
    """Show user profile for user"""
    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"

@app.route('/r/<subreddit>') #<> brackets include space for a variable
def show_subreddit(subreddit):
    return f"<h1>Welcome to the {subreddit} Subreddit!</h1>"

POSTS = {
    1: "I'm the first post",
    2: "Blargh blargh blargh",
    3: "I'm Corry and I hate this"
}

@app.route('/posts/<int:id>')
def get_post(id):
    comment = POSTS.get(id,"Post Not Found")
    return f"{comment}"

@app.route('/posts/<username>/<int:id>')
def usercomment(username,id):
    name = USERS[username]
    comment = POSTS.get(id,"Post Not Found")
    return f"""
    <h1>This is {name}'s page</h1>
    <h2>Their comment is {comment}</h2>
    """


    