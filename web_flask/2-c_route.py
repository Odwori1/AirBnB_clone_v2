#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def index():
    """The website home page."""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """The hbnb page."""
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    """Page that display C followed by the value"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
