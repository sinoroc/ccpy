""" Module initializer
"""


import pkg_resources

from . import main


# PEP 396
__version__ = pkg_resources.get_distribution(
    '{{cookiecutter.project_name}}',  # http://stackoverflow.com/a/22845276
).version


# EOF
