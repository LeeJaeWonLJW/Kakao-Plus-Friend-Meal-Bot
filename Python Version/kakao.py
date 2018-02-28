from flask import Flask, jsonify, request, make_response
import flask
import json
from functools import wraps

from response import *
from checkcheck import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello! Dukwon Lunch Bot</h1>"

@app.route("/keyboard")
def keyboard():
    buttons = ["조식","중식","석식"]

    response = {
        'type': 'buttons',
        'buttons': buttons
    }

    return json.dumps(response, ensure_ascii=False),200

@app.route("/message", methods=['POST'])
def message():
    checkcheck()
    
    values = request.get_json()

    if values['content'] == "조식":
        text=breakfast()
    elif values['content'] == "중식":
        text=lunch()
    elif values['content'] == "석식":
        text=dinner()

    response = {
        'message': {
            'text': text
            },
        'keyboard': {
            'type': 'buttons',
            'buttons': ["조식","중식","석식"]
            }
        }
        
    return json.dumps(response, ensure_ascii=False), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
