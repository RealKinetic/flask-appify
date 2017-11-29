import flask_seasurf

__all__ = [
    'init_app',
]


def init_app(app):
    flask_seasurf.SeaSurf(app)
