from flask import Flask, render_template, request, url_for, redirect
from nlq_to_re import *
from re_to_dfa import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        charset = [ch.strip() for ch in (request.form['charset']).split(",")]
        regex = nlq_to_re(charset, request.form['query'])
        dfa, base64_dfa = re_to_dfa(charset, regex)
        return render_template("index.html", dfaJson = str(dfa.transition_table), imgUrl = "data:image/png;base64,"+base64_dfa)
    except:
        return render_template('index.html')    