from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/engineering')
def engineering():
    return render_template('engineering.html')

@app.route('/science')
def science():
    return render_template('science.html')

@app.route('/medicine')
def medicine():
    return render_template('medicine.html')

@app.route('/others')
def others():
    return render_template('others.html')

if __name__ == '__main__':
    app.run()
