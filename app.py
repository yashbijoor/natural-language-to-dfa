from flask import Flask, render_template, request
from nlq_to_re import *
from re_to_dfa import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        charset = [ch.strip() for ch in (request.form['charset']).split(",")] # Strip whitespaces to obtain charset
        regex = nlq_to_re(charset, request.form['query']) # Obtain Regular Expression for the query
        dfa, image_list = re_to_dfa(charset, regex) # Get dfa in json and diagrams
        return render_template("index.html", dfaJson = str(dfa.transition_table), imgUrls = image_list)
    except:
        return render_template('index.html')

@app.route('/info', methods=['GET'])
def info():
    return render_template('info.html')   

@app.route('/help', methods=['GET'])
def help():
    return render_template('help.html') 