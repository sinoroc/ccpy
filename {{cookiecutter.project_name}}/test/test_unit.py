#

"""Unit tests."""

import unittest

import {{cookiecutter.main_package_name}}


class TestProjectVersion(unittest.TestCase):
    """Project version string."""

    def test_project_has_version_string(self):
        """Project should have a vesion string."""
        self.assertIn('__version__', dir({{cookiecutter.main_package_name}}))
        self.assertIsInstance({{cookiecutter.main_package_name}}.__version__, str)


# EOF
