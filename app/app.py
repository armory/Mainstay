from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'GET':
        auth_opts = request.headers.get('Authorization')
        print (request.data) 
        request_json = request.get_json()
    # output_string = auth_opts + " and " + request_json
    
    #return  auth_opts
    return "this is the top context path"

@app.route('/test')
def test():
    return "This is the test"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
