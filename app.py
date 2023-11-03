from flask import Flask

app = Flask(__name__)


@app.route("/")
def root():
    return "Hello World"


if __name__ == "__app__":
    app.run(debug=True)
