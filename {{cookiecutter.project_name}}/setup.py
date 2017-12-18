""" Setup script
"""


import os

import setuptools


NAME = '{{cookiecutter.project_name}}'
DESCRIPTION = "{{cookiecutter.project_name}} library"


LICENSE = 'Apache-2.0'  # https://spdx.org/licenses/


REQUIREMENTS_INSTALL = [
    'setuptools',  # needed for 'pkg_resources'
]


REQUIREMENTS_PACKAGE = [
    'wheel',
]


REQUIREMENTS_TEST = [
    'pytest',
    'pytest-pep8',
    'pytest-pylint',
]


REQUIREMENTS_EXTRAS = {
    'package': REQUIREMENTS_PACKAGE,
    'test': REQUIREMENTS_TEST,
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
        description=DESCRIPTION,
        license=LICENSE,
        long_description=long_description,
        # options
        extras_require=REQUIREMENTS_EXTRAS,
        install_requires=REQUIREMENTS_INSTALL,
        package_dir=package_directories,
        packages=packages,
    )
    return


if __name__ == '__main__':
    _do_setup()


# EOF
