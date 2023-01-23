# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import sqlite3
from flask import Flask, render_template

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def index():
    conn = sqlite3.connect("tcascentral.db")
    db = conn.cursor()
    db.execute("SELECT * FROM program")
    program = db.fetchall()
    db.execute("SELECT name FROM PRAGMA_TABLE_INFO('program')")
    header = db.fetchall()
    i = 0
    for row in header:
        header[i] = row[0]
        i += 1
    print(header)
    return render_template("index.html", program=program, header=header)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
