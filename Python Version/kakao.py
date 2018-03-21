from flask import Flask, jsonify, request, make_response
import flask
import json
from functools import wraps

from response import *
from updateDB import *

from command import Command

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello! Dukwon Lunch Bot</br>We have dukwon high school's lunch api.</br>Just connect http://test.jaewon.me/lunchapi/?(parameter)</br></br>:::Description:::</br>Key: key , Value: 조식(1), 중식(2), 석식(3)</br>ex) http://test.jaewon.me/lunchapi?key='조식'</br>ex2) http://test.jaewon.me/lunchapi?key=1</h1>"

#lunchbot commander

@app.route("/lunchapi", methods=['GET'])
def lunchapi():
    key = request.args.get('key')
    
    checkcheck()

    if key == "조식" or key == '1':
        text = breakfast()
    elif key == "중식" or key == '2':
        text = lunch()
    elif key == "석식" or key == '3':
        text = dinner()

    return text

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

    text=text.replace(" ","\n")

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
"""
@app.route("/tests", methods=['GET'])
def api():
    key = request.args.get('key')
    
    checkcheck()

    if key == "조식":
        text = breakfast()
    elif key == "중식":
        text = lunch()
    elif key == "석식":
        text = dinner()

    return key
"""
#blog commander

@app.route("/blog/ls")
def lsCom():
    command = Command()
    result=command.ls2()

    response=''
    for data in result:
        response+=data+"  "

    return response, 200

@app.route("/blog/help")
def helpCom():
    command = Command()
    response = command.help()

    return response, 200

@app.route("/blog/cd")
def cdCom():
    command = Command()
    result = command.cd()

    return response, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
