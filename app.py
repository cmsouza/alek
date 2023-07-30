from flask import Flask
from flask import render_template

from aleksay import alek

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('alek.html', alek=alek())
