import os
from flask import Flask, render_template

template_dir = os.path.abspath("build")
static_dir = os.path.abspath("build/assets")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


@app.route('/')
def index():
    return render_template('index.html')