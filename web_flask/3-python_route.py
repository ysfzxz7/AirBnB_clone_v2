#!/usr/bin/python3

"""
    Flask module, for creating a sample script that running on
    https://0.0.0.0:5000
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """
        hello function returns a string contains 'Hello HBNB!'
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """
        hbnb function returns a string contains 'HBNB'
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_function(text=None):
    """
        c_function is a function that returns a text like
        C <text>
    """
    return f'C {text.replace("_", " ")}'


@app.route('/python/')
def python_cool():
    """
        python_cool is a function that returns a text contains
        Python is cool
    """
    return 'Python is cool'


@app.route('/python/<text>')
def python_function(text=None):
    """
        python_function is a function that returns a text like
        Python <text>
    """
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
