""" Module initializer
"""


import pkg_resources


# PEP 396
__version__ = pkg_resources.get_distribution(
    '{{cookiecutter.project_name}}',  # https://stackoverflow.com/a/22845276
).version


# EOF
