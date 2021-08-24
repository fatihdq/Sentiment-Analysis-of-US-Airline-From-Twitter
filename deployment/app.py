from flask import Flask, render_template, request, jsonify
from predictor import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/sentiment", methods=['POST'])
def sentiment_prediction():
    tweet = request.form['text']
    sentiment,prob = prediction(tweet)
    if sentiment == 0:
        sent = 'Negative (' + str(round(prob*100,2)) +'%)'
    else:
        sent = 'Positive (' + str(round(prob*100,2)) +'%)'
    return jsonify({'result':sent})
        

        

if __name__ == '__main__':
    app.run(debug=True)