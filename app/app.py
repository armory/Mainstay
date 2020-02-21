from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return "This is the one test for all!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
