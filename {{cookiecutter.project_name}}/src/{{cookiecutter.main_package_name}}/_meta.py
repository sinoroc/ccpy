#

"""Meta information."""

import importlib.metadata

PROJECT_NAME = '{{cookiecutter.project_name}}'

_DISTRIBUTION_METADATA = importlib.metadata.metadata(PROJECT_NAME)

VERSION = _DISTRIBUTION_METADATA['Version']

# EOF
