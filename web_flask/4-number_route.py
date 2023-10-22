#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Display Hello HBNB! as text"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB as text"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def display_c_files(text):
    """Display C followed by the value of the text variable as text"""
    return 'C ' + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """display Python followed by the value of the text variable as text"""
    return 'Python ' + text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """display n is a number as text"""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
