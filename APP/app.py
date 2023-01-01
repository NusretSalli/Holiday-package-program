from flask import Flask, render_template, url_for, request

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__)

@app.route("/")

def hello_world():

    return "hello world!!!"

@app.route("/login")

def login():

    return render_template("login.html")


@app.route("/packages")

def packages():

    return render_template("packages.html")



@app.route("/register")

def register():

    return render_template("register.html")


if __name__ == "__main__":

    app.run(debug=True)

