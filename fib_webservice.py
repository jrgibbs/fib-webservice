__author__ = 'jgibbs'

from fib_function import fib
from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/fib/<int:n>', methods=['GET'])
def fib_webservice(n):
    """ This function provides output from the fib_function

    :param n: A integer greater than or equal to 0
    :return: A dictionary with a list containing all of the numbers that
    make the fibonacci sequence through n positions back to the web browser.
    """
    return jsonify(sequence=fib(n))

@app.errorhandler(404)
def page_not_found(error):
    """ This function generates an error for an invalid webservice call

    :param error: 404: HTTP response code
    :return: An error due to invalid input for the fib_webservice function call
    """
    return jsonify(error=error.description, code=error.code, name=error.name)

if __name__ == '__main__':
    app.run(debug=True)
