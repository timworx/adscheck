try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Simple script for checking whether a webpage has has an ad network on it.',
    'author': 'Tim Sherwood',
    'url': 'https://github.com/timworx/adscheck',
    'download_url': 'https://github.com/timworx/adscheck/archive/master.zip',
    'author_email': 'tim@dualmediasolutions.com',
    'version': '0.0.1',
    'install_requires': ['requests>=2.3.0', 'PyYAML==3.11',],
    'packages': ['adscheck',],
    'scripts': [],
    'name': 'adscheck',
    'package_data': {'adscheck': ['*.yml']}
}

setup(**config)
