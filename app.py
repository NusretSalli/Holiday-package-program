from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")

def login():

    return render_template("login.html")


@app.route("/packages")

def packages():

    return render_template("packages.html")


if __name__ == "__main__":

    app.run(debug=True)

