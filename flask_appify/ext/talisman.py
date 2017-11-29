import flask_talisman

__all__ = [
    'init_app',
]


def init_app(app):
    flask_talisman.Talisman(
        app,
        content_security_policy=app.config.get(
            'TALISMAN_CONTENT_SECURITY_POLICY',
            flask_talisman.DEFAULT_CSP_POLICY
        ),
        force_https_permanent=app.config.get(
            'TALISMAN_FORCE_HTTPS_PERMANENT',
            True,
        )
    )
