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


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
