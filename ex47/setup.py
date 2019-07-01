try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Remus M.',
    'url': 'N/A',
    'download_url': 'N/A',
    'author_email': 'remus_c.m@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'testingproject2'
}

setup(**config)
