#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
flask app entrance
"""

import os
from flask import Flask, render_template, jsonify, request
import os
from configparser import ConfigParser

basedir = os.path.dirname(os.path.abspath(__file__))

config = ConfigParser()
config.read(os.path.join(basedir, 'config.ini'))

app = Flask(__name__, instance_relative_config=True)


@app.route('/')
def index():
    """
    render the index page
    :return: index page
    """

    return render_template("index.html",)


if __name__ == '__main__':
    app.run()
