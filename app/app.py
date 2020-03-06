from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
 #   return render_template('index.html')

 #Let's get the JSON Payload
    #data = json.loads(request.data)
    #ontent = request.get_json()
    print (request.data) 
    return request.data

@app.route('/test')
def test():
    return "This is the test"

if __name__ == '__main__':
    app.run(host='0.0.0.0')