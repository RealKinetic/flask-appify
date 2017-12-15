import flask_talisman

__all__ = [
    'init_app',
]


def init_app(app):
    allow_from = app.config.get(
        'TALISMAN_FRAME_OPTIONS_ALLOW_FROM',
        None
    )

    if isinstance(allow_from, (list, tuple)):
        allow_from = " " .join(allow_from)

    if allow_from:
        frame_options = flask_talisman.ALLOW_FROM
    else:
        frame_options = flask_talisman.SAMEORIGIN

    flask_talisman.Talisman(
        app,
        content_security_policy=app.config.get(
            'TALISMAN_CONTENT_SECURITY_POLICY',
            flask_talisman.DEFAULT_CSP_POLICY
        ),
        force_https_permanent=app.config.get(
            'TALISMAN_FORCE_HTTPS_PERMANENT',
            True,
        ),
        frame_options=frame_options,
        frame_options_allow_from=allow_from,
    )
