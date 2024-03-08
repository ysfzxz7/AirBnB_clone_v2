#!/usr/bin/python3
"""
    module contains a function that returns all states and its
    states from database, in an HTML file.
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/cities_by_states')
def states_list():
    """
        states_list function that renders an HTML file contains
        all states with its cities.
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
        function that cleans up the SQLAlchemy's session.
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
