from flask import Flask, render_template, json


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/post")
def post():
    return render_template('post.html')