#!/usr/bin/python3
"""
    module contains a function that runs a Flask app.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """
        function that cloeses the session
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def state():
    """
        function that returns an HTML file contains states.
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
        function that renders an HTML file that displays
        a state by its id.
    """
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode='none')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
