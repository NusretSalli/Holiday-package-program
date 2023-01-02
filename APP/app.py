from flask import Flask, render_template, url_for, request

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])

def hello_world():

    return "HEHE"

@app.route("/login", methods = ["GET","POST"])

def login():

    if request.method == 'POST':
        if request.form.get('action1') == 'VALUE1':
            pass # do something
        
        elif  request.form.get('action2') == 'VALUE2':
            pass # do something else
        
        else:
            pass # unknown
        
    elif request.method == 'GET':
        return render_template('login.html')

    return render_template("login.html")


@app.route("/packages")

def packages():

    return render_template("packages.html")



@app.route("/register")

def register():

    return render_template("register.html")


if __name__ == "__main__":

    app.run(debug=True)

