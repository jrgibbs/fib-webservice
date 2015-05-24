Fibonacci Sample
===================

## Purpose ##
Provide a webservice that accepts a number, n, as input and returns the first n Fibonacci numbers.
[Fibonacci Numbers](http://en.wikipedia.org/wiki/Fibonacci_number) are a specific mathematical
integer sequence.  Although there are many methods to generate the Fibonacci sequence, this example
is a demonstration of python software development concepts.

## Installation ##
`$ pip -r requirements.txt`

## Usage ##
* Running the webservice
 * `$ python fib_webservice.py`
* Access the webservice by pointing a browser to:
  http://127.0.0.1:5000/fib/n
  * replace n with any integer to view the fibonacci sequence through through n places. 
  * Modify the url to get other examples of output from the function

* http://127.0.0.1:5000/fib/6
* http://127.0.0.1:5000/fib/42
* http://127.0.0.1:5000/fib/118
* http://127.0.0.1:5000/fib/-37
* http://127.0.0.1:5000/fib/2.2

## Testing ##
`$ pip -r test-requirements.txt`

Run the tests:
`$ nosetests -v`
