from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello',)
def printHelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5001)
