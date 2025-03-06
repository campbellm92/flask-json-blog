from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('articles.json', 'r') as f:
    articles = json.load(f)

@app.route("/")
def home():
    return render_template('index.html', articles=articles)

@app.route("/post")
def post():
    return render_template('post.html', articles=articles)