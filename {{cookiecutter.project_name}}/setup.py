""" Setup script
"""


import os

import setuptools


NAME = '{{cookiecutter.project_name}}'
DESCRIPTION = "{{cookiecutter.project_name}} Pyramid application"


LICENSE = 'Apache-2.0'  # https://spdx.org/licenses/


REQUIREMENTS_INSTALL = [
    'pyramid',
    'setuptools',  # needed for 'pkg_resources'
    'waitress',
]


REQUIREMENTS_PACKAGE = [
    'pex',
    'wheel',
]


REQUIREMENTS_TEST = [
    'pytest',
    'pytest-pep8',
    'pytest-pylint',
    'WebTest',
]


REQUIREMENTS_EXTRAS = {
    'package': REQUIREMENTS_PACKAGE,
    'test': REQUIREMENTS_TEST,
}


ENTRY_POINTS = {
    'paste.app_factory': [
        'main_entry_point={{cookiecutter.main_package_name}}.main:entry_point',
    ],
    'console_scripts': [
        '{}=pyramid.scripts.pserve:main'.format(NAME),
    ],
}


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


def _do_setup():
    setuptools.setup(
        name=NAME,
        version=VERSION,
        # metadata
        description=DESCRIPTION,
        license=LICENSE,
        long_description=LONG_DESCRIPTION,
        # options
        entry_points=ENTRY_POINTS,
        extras_require=REQUIREMENTS_EXTRAS,
        install_requires=REQUIREMENTS_INSTALL,
        package_dir=PACKAGE_DIRECTORIES,
        packages=PACKAGES,
    )
    return


if __name__ == '__main__':
    _do_setup()


# EOF
