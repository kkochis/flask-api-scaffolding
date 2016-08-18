# -*- coding: utf-8 -*-
"""Application setup and bootstrap

This module sets up the application, loads controller (and routes) and includes
any flask extensions and blueprints.

"""
from flask import Flask

app = None  # pylint: disable=invalid-name


def create_app(name):
    """create_app instantiates flask application and routing

    Sets up the flask application and returns that instance. This also imports
    the registered controllers which define the routes.
    """
    global app  # pylint: disable=global-statement,invalid-name
    if app is None:
        app = Flask(name)
        import controllers  # noqa: F401 pylint: disable=unused-variable

    return app
