import json
from flask import Flask, render_template, request, jsonify, abort
from utils.jinja_filters import newline_to_break

app = Flask(__name__)
app.jinja_env.filters['newline_to_break'] = newline_to_break

with open('articles.json', 'r') as f:
    articles = json.load(f)

@app.route("/")
def home():
    return render_template('index.html', articles=articles)

@app.route("/post/<article_id>")
def get_article(article_id):
    article = next((a for a in articles if a["id"] == article_id), None)
    if not article:
        abort(404)
    return render_template('post.html', article=article)