import flask_assetrev

__all__ = [
    'init_app',
]


def init_app(app):
    asset_file = app.config.get('ASSETREV_MANIFEST_FILE', None)

    if asset_file:
        flask_assetrev.AssetRev(app)
