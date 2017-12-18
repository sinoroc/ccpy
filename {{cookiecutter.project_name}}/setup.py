#!/usr/bin/env python


""" Setup script """


import os

import setuptools


NAME = '{{cookiecutter.project_name}}'
DESCRIPTION = "{{cookiecutter.project_name}} Pyramid application"


AUTHOR = '{{cookiecutter.author}}'
AUTHOR_EMAIL = '{{cookiecutter.author_email}}'
URL = '{{cookiecutter.url}}'


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


REQUIREMENTS_SETUP = [
    'docutils',  # needed for 'setup.py check --restructuredtext'
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


def _do_setup():
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.rst')) as file_:
        readme = file_.read()
    with open(os.path.join(here, 'CHANGELOG.rst')) as file_:
        changelog = file_.read()

    long_description = readme
    version = changelog.splitlines()[4]

    source_directory = 'src'
    packages = setuptools.find_packages(
        where=source_directory,
    )
    package_directories = {
        '': source_directory,
    }

    setuptools.setup(
        name=NAME,
        version=version,
        # metadata
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        long_description=long_description,
        url=URL,
        # options
        entry_points=ENTRY_POINTS,
        extras_require=REQUIREMENTS_EXTRAS,
        install_requires=REQUIREMENTS_INSTALL,
        package_dir=package_directories,
        packages=packages,
        setup_requires=REQUIREMENTS_SETUP,
    )
    return


if __name__ == '__main__':
    _do_setup()


# EOF
