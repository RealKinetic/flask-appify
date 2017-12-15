from werkzeug.utils import import_string

__all__ = [
    'init_app',
]

modules = [
    'appengine',
    'assetrev',
    'cors',
    'seasurf',
    'talisman',
]


def init_ext(app, ext_name):
    ext = import_string('flask_appify.ext.' + ext_name)

    ext.init_app(app)


def init_app(app):
    for module in modules:
        init_ext(app, module)
