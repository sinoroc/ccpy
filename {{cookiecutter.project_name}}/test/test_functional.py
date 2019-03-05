""" Functional test
"""


import unittest

import webtest

import {{cookiecutter.main_package_name}}


class TestFunctional(unittest.TestCase):
    """ Functional test
    """

    def setUp(self):
        wsgi_app = {{cookiecutter.main_package_name}}.main.entry_point({})
        self.test_app = webtest.TestApp(wsgi_app)

    def tearDown(self):
        pass

    def test_functional(self):
        """ Functional test
        """
        self.test_app.get('/', status=200)


# EOF
