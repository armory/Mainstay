from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "This is the root context!"

@app.route('/text')
def test():
    return "This is the test"

if __name__ == '__main__':
    app.run(host='0.0.0.0')