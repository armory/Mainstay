from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)


@app.route('/')
def index():
 #   return render_template('index.html')

 #Let's get the JSON Payload
    #data = json.loads(request.data)
    #ontent = request.get_json()
    auth_opts = request.headers.get('Authorization')
    print (request.data) 
    request_json = request.get_json()
    # output_string = auth_opts + " and " + request_json
    
    return  auth_opts

@app.route('/test')
def test():
    return "This is the test"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
