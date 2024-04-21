#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
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


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    """Page that display Python followed by the value"""
    return f'Python {text.replace("_", " ")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
