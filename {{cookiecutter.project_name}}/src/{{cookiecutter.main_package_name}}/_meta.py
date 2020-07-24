#

"""Meta information."""

import importlib_metadata

PROJECT_NAME = '{{cookiecutter.project_name}}'

_DISTRIBUTION_METADATA = importlib_metadata.metadata(PROJECT_NAME)

VERSION = _DISTRIBUTION_METADATA['Version']

# EOF
