from cgitb import html;
from flask import Flask, render_template;

# __name__ is the name of the app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

app.run('127.0.0.1')