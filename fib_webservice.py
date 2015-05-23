__author__ = 'jgibbs'

from fib_function import fib
from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/fib/<int:n>', methods=['GET'])
def fib_webservice(n):
    return jsonify(sequence=fib(n))

if __name__ == '__main__':
    app.run(debug=True)
