#

"""Functional tests."""

import unittest

import webtest

import {{cookiecutter.main_package_name}}


class TestFunctional(unittest.TestCase):
    """ Functional test."""

    def setUp(self) -> None:
        wsgi_app = {{cookiecutter.main_package_name}}.main.entry_point({})
        self.test_app = webtest.TestApp(wsgi_app)

    def tearDown(self) -> None:
        pass

    def test_functional(self) -> None:
        """Root URL should return HTPP status code 200."""
        self.test_app.get('/', status=200)


# EOF
