from flask import Flask, render_template, redirect, request

# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
import pickle
import pandas as pd
import numpy as np


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


@app.route("/")
def root():
    return render_template("landing.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/heart")
def heart():
    return render_template("heart.html")


@app.route("/predictheart", methods=["POST"])
def predictheart():
    input_features = [float(x) for x in request.form.values()]
    print(input_features)
    features_value = [np.array((input_features))]
    print(features_value)
    features_name = [
        "age",
        "trestbps",
        "chol",
        "thalach",
        "oldpeak",
        "sex",
        "cp",
        "  fbs",
        "restecg",
        "exang",
        "slope",
        "ca",
        "thal",
    ]

    df = pd.DataFrame(features_value, columns=features_name)
    print(df)

    x = df.iloc[::].values
    print(x)
    model1 = pickle.load(open("heart.pkl", "rb"))
    output = model1.predict(x)
    if output == 1:
        res_val = "a high risk of Heart Disease"
    else:
        res_val = "a low risk of Heart Disease"

    return render_template(
        "heart_result.html", prediction_text="Patient has {}".format(res_val)
    )


if __name__ == "__app__":
    app.run(debug=True)
