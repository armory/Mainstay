from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__)


@app.route('/')
def index():
    
    return "You have reached Flask-app! You Win!"

@app.route('/test')
def test():
    return "This is the test"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
