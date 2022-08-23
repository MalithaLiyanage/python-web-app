from cgitb import html;
from flask import Flask, render_template, request;

# __name__ is the name of the app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def home_post():
    length = request.form['length']
    width = request.form['width']
    height = request.form['height']
    volume = float(length) * float(width) * float(height)
    return render_template('index.html', volume=volume)

app.run('127.0.0.1')