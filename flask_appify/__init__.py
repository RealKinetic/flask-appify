"""
This is the main entry point for all AppEngine requests in to the application.
This module is divided up in to a 1:1 relationship of AppEngine module to WSGI
application.

Each python module must expose an ``app`` object.
"""

import imp
import os.path

from flask import Flask

from flask_appify import ext

__all__ = [
    'create_app',
]


def create_app(import_name, config_loader=None, **kwargs):
    """
    Create and return a Flask application object that is given some sane
    defaults.

    :param config_loader: A func that takes the app and configures it
    """
    if 'template_folder' not in kwargs:
        _, path, _ = imp.find_module(import_name)

        kwargs['template_folder'] = os.path.realpath(
            os.path.join(
                path,
                'templates'
            )
        )

    app = Flask(import_name, **kwargs)

    if config_loader:
        config_loader(app)

    ext.init_app(app)

    return app
