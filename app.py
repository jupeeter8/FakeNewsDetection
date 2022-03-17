from distutils.command.clean import clean
from flask import Flask, render_template, flash, get_flashed_messages, request
from nlp import clean_text
app = Flask(__name__)
app.secret_key="anirudh"

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST", "GET"])
def check():
    cleanT = clean_text(str(request.form['nBody']))
    flash(cleanT)
    return render_template("index.html")
app.run(debug=True)