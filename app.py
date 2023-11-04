from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("landing.html")


@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__app__":
    app.run(debug=True)
