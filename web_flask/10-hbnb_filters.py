#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """The page displays hbnb filters"""
    states_list = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    states_list.sort(key=lambda x: x.name)
    amenities.sort(key=lambda x: x.name)
    for state in states_list:
        state.cities.sort(key=lambda x: x.name)
    data = {
        'states': states_list,
        'amenities': amenities
    }
    return render_template('10-hbnb_filters.html', **data)


@app.teardown_appcontext
def flask_teardown(exc):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
