import flask_cors

__all__ = [
    'init_app',
]


def init_app(app):
    flask_cors.CORS(app, resources={
        r"/*": {
            "origins": "*"
        }
    })
