__all__ = [
    'description',
    'maintainer',
    'maintainer_email',
    'url',
    'version_info',
    'version',
]

version_info = (0, 1)
version = '.'.join(map(bytes, version_info))

maintainer = 'Nick Joyce'
maintainer_email = 'nick.joyce@realkinetic.com'

description = """
Opinionated library that sets up a Flask application with a set of defaults
covering security, CORS, Asset revisioning etc.
""".strip()

url = 'https://github.com/RealKinetic/flask-appify'
