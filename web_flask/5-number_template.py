#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template


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


@app.route('/number/<int:n>')
def number_page(n):
    """Page displays a number int."""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """display the number_template page."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
