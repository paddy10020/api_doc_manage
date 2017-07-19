# -*- coding=utf-8 -*-
from flask import url_for, render_template, redirect
from datetime import datetime

from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/index')
def index_():
    print url_for('index')
    return redirect(url_for('index'))
