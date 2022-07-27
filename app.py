from flask import Flask, render_template
from datetime import datetime

app = Flask("hello")

posts = [
    {
        "title": "First post",
        "body": "Here comes the text",
        "author": "Jorns",
        "created": datetime(2022,7,25)
    },
    {
        "title": "Second post",
        "body": "Here comes the text",
        "author": "User 1",
        "created": datetime(2022,7,26)
    },
    {
        "title": "Third post",
        "body": "Here comes the text",
        "author": "User 1",
        "created": datetime(2022,7,26)
    },
    {
        "title": "Fourth post",
        "body": "Here comes the text",
        "author": "User 3",
        "created": datetime(2022,7,26)
    },
    {
        "title": "Fifth post",
        "body": "Here comes the text",
        "author": "User 1",
        "created": datetime(2022,7,26)
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

