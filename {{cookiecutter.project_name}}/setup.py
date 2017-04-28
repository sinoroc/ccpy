""" Setup script
"""


import os

import setuptools


NAME = '{{cookiecutter.project_name}}'
DESCRIPTION = "{{cookiecutter.project_name}} Pyramid application"


INSTALL_REQUIREMENTS = [
    'pyramid',
    'waitress',
]


HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(HERE, 'CHANGELOG.rst')) as f:
    CHANGELOG = f.read()


LONG_DESCRIPTION = README
VERSION = CHANGELOG.splitlines()[4]


SOURCE_DIRECTORY = 'src'
PACKAGES = setuptools.find_packages(
    where=SOURCE_DIRECTORY,
)
PACKAGE_DIRECTORIES = {
    '': SOURCE_DIRECTORY,
}


LICENSE = 'Apache-2.0'  # https://spdx.org/licenses/


ENTRY_POINTS = {
    'paste.app_factory': [
        'main_entry_point={{cookiecutter.main_package_name}}.main:entry_point',
    ],
    'console_scripts': [
        '{}=pyramid.scripts.pserve:main'.format(NAME),
    ],
}


def _do_setup():
    setuptools.setup(
        # metadata
        name=NAME,
        description=DESCRIPTION,
        license=LICENSE,
        long_description=LONG_DESCRIPTION,
        version=VERSION,
        # options
        entry_points=ENTRY_POINTS,
        install_requires=INSTALL_REQUIREMENTS,
        package_dir=PACKAGE_DIRECTORIES,
        packages=PACKAGES,
    )
    return


if __name__ == '__main__':
    _do_setup()


# EOF
