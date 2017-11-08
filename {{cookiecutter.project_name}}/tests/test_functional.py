""" Functional test
"""


import unittest

import {{cookiecutter.main_package_name}}


class TestFunctional(unittest.TestCase):
    """ Functional test
    """

    def setUp(self):
        return

    def tearDown(self):
        return

    def test_functional(self):  # pylint: disable=no-self-use
        """ Functional test
        """
        hasattr({{cookiecutter.main_package_name}}, '__version__')
        return


# EOF
