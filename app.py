from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/engineering')
def index():
    return render_template('engineering.html')

@app.route('/science')
def index():
    return render_template('science.html')

@app.route('/medicine')
def index():
    return render_template('medicine.html')

@app.route('/others')
def index():
    return render_template('others.html')

if __name__ == '__main__':
    app.run()
