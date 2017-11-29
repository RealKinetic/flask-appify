import functools

from flask_appify.util import request_wants_json

try:
    from google.appengine.api import datastore_errors
except ImportError:
    # not on the AppEngine platform
    datastore_errors = None


__all__ = [
    'init_app',
]


html_response = {
    503: """<!doctype html><html><head><title>503 Service
Unavailable</title></head><body><h1>Service Unavailable</h1><p>Service is
temporarily unavailable. Please try again later.</p></body></html>"""
}

json_response = {
    503: """{"status":"error","code":503,"message":"Service is
temporarily unavailable. Please try again later."}"""
}


def handle_temp_error(app, err):
    """
    This is a Flask `errorhandler` handling `datastore_errors.InternalError`.

    According to `https://cloud.google.com/appengine/docs/standard/python/
    datastore/exceptions` this exception does not necessarily mean that the
    underlying operation failed.

    :param app: The flask app that received the error.
    :param err: The exception that was raised.
    """
    response = app.make_response(
        json_response[503] if request_wants_json() else html_response[503]
    )

    response.status_code = 503

    return response


def init_app(app):
    if datastore_errors:
        app.errorhandler(datastore_errors.InternalError)(
            functools.partial(handle_temp_error, app)
        )
        app.errorhandler(datastore_errors.Timeout)(
            functools.partial(handle_temp_error, app)
        )
        app.errorhandler(datastore_errors.TransactionFailedError)(
            functools.partial(handle_temp_error, app)
        )
