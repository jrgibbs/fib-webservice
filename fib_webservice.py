__author__ = 'jgibbs'

from fib_function import fib
from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/fib/<int:n>', methods=['GET'])
def fib_webservice(n):
    return jsonify(sequence=fib(n))

@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error=error.description, code=error.code, name=error.name)

if __name__ == '__main__':
    app.run(debug=True)
