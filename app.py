from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/engineering')
def engineering():
    data = pd.read_csv("/home/moonegg/mysite/dataStep/engineer.csv")

    #iterate adding data to mega-nested dict
    programList = {}
    next(data.iterrows())
    for index, row in data.iterrows():
        if not ((row["university"] in programList)):
            programList[row["university"]] = {}
        if not ((row["faculty"] in programList[row["university"]])):
            programList[row["university"]][row["faculty"]] = {}
        if not ((row["round"] in programList[row["university"]][row["faculty"]])):
            programList[row["university"]][row["faculty"]][row["round"]] = {}
        if not ((row["program"] in programList[row["university"]][row["faculty"]][row["round"]])):
            programList[row["university"]][row["faculty"]][row["round"]][row["program"]] = {}
        for column, value in row.items():
            if column not in ["university", "faculty", "round", "program"]:
                programList[row["university"]][row["faculty"]][row["round"]][row["program"]][column] = value
        
    return render_template('engineering.html', programList=programList)

@app.route('/science')
def science():
    data = pd.read_csv("/home/moonegg/mysite/dataStep/science.csv")

    #iterate adding data to mega-nested dict
    programList = {}
    next(data.iterrows())
    for index, row in data.iterrows():
        if not ((row["university"] in programList)):
            programList[row["university"]] = {}
        if not ((row["faculty"] in programList[row["university"]])):
            programList[row["university"]][row["faculty"]] = {}
        if not ((row["round-program"] in programList[row["university"]][row["faculty"]])):
            programList[row["university"]][row["faculty"]][row["round-program"]] = {}
        for column, value in row.items():
            if column not in ["university", "faculty", "round-program"]:
                programList[row["university"]][row["faculty"]][row["round-program"]][column] = value

    return render_template('science.html', programList=programList)

@app.route('/medicine')
def medicine():
    data = pd.read_csv("/home/moonegg/mysite/dataStep/medicine.csv")

    #iterate adding data to mega-nested dict
    programList = {}
    next(data.iterrows())
    for index, row in data.iterrows():
        if not ((row["university"] in programList)):
            programList[row["university"]] = {}
        if not ((row["faculty"] in programList[row["university"]])):
            programList[row["university"]][row["faculty"]] = {}
        if not ((row["round-program"] in programList[row["university"]][row["faculty"]])):
            programList[row["university"]][row["faculty"]][row["round-program"]] = {}
        for column, value in row.items():
            if column not in ["university", "faculty", "round-program"]:
                programList[row["university"]][row["faculty"]][row["round-program"]][column] = value

    return render_template('medicine.html', programList=programList)

@app.route('/others')
def others():
    data = pd.read_csv("/home/moonegg/mysite/dataStep/others.csv")

    #iterate adding data to mega-nested dict
    programList = {}
    next(data.iterrows())
    for index, row in data.iterrows():
        if not ((row["university"] in programList)):
            programList[row["university"]] = {}
        if not ((row["faculty"] in programList[row["university"]])):
            programList[row["university"]][row["faculty"]] = {}
        if not ((row["round-program"] in programList[row["university"]][row["faculty"]])):
            programList[row["university"]][row["faculty"]][row["round-program"]] = {}
        for column, value in row.items():
            if column not in ["university", "faculty", "round-program"]:
                programList[row["university"]][row["faculty"]][row["round-program"]][column] = value

    return render_template('others.html', programList=programList)

if __name__ == '__main__':
    app.run()
