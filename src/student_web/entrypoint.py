import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='build', static_folder='build/assets')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')