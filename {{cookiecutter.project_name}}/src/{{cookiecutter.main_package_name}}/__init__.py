""" Module initializer
"""


import pkg_resources


# PEP 396
__version__ = pkg_resources.get_distribution(  # pylint: disable=no-member
    '{{cookiecutter.project_name}}',  # http://stackoverflow.com/a/22845276
).version


# EOF
