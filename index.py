# -*- coding=utf-8 -*-
from flask import url_for, render_template, redirect
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page!'


@app.route('/hello')
def hello():
    return 'Hello Page!'


@app.route('/user/<username>')
def user(username):
    return 'Username is %s' % username


@app.route('/test')
def test():
    print url_for('hello')
    print url_for('index')
    print url_for('user', username='paddy')
    return 'Test Page!'


if __name__ == '__main__':
    app.run()
