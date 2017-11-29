import flask_assetrev

__all__ = [
    'init_app',
]


def init_app(app):
    app.config.setdefault('ASSETREV_MANIFEST_FILE', 'asset-manifest.json')
    app.config.setdefault('ASSETREV_BASE_URL', None)
    app.config.setdefault('ASSETREV_BASE_PATH', None)
    app.config.setdefault('ASSETREV_RELOAD', app.debug)

    flask_assetrev.AssetRev(app)
