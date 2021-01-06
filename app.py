from flask import Flask, render_template
from query import search

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/<query>/<banyak>')
def api_search(query, banyak):
    return search(query, int(banyak))

app.run()
