#!/usr/bin/python3
"""
    script that fetches data from db_storage and returns it into HTML
    file data displays it very well.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list')
def list_states():
    """
        list_states function that fetches states from FileStorage
        and returns it as HTML file that dispalys it very well.
    """
    all_states = storage.all(State)
    sorted_states = sorted(all_states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
        app_teardown function that cleans up the app.
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
