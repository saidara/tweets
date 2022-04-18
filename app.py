import string
from flask import Flask, request,render_template,jsonify
import joblib
import os
import numpy as np
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")



@app.route('/', methods=['POST', 'GET'])
def result():
    enter_tweet =(request.form['siblings'])
    


    X = []
    X.append(enter_tweet)

    print(X)


    model_path = r'/Users/saidaraogonuguntla/Downloads/titanic-main/tweets/model/model.pkl'

    model = joblib.load(model_path)

    Y = model.predict(X)
    pred = "disaster tweet " if Y[0]==1 else "nondisaster tweet"
    print(pred)
    print(Y)
    return render_template('index.html', prediction_text = pred)


if __name__ =="__main__":
    app.run(debug=True, port=5623)
