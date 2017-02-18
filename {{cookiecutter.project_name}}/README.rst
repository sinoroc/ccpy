..


.. contents::

.. sectnum::


Hacking
=======

This project makes extensive use of `tox`_, `pytest`_, and `GNU Make`_.


Development environment
-----------------------

Use following command to create a Python virtual environment with all
necessary dependencies::

    tox -r -e develop

This creates a Python virtual environment in the ``.venv`` directory. It can
be activated with the following command::

    . .venv/bin/activate


Run test suite
--------------

In a Python virtual environment run the following command::

    make review

Outside of a Python virtual environment run the following command::

    tox -r


Build and package
-----------------

In a Python virtual environment run the following command::

    make package

Outside of a Python virtual environment run the following command::

    tox -r -e package


Links
=====

.. target-notes::

.. _`GNU Make`: https://www.gnu.org/software/make/
.. _`pytest`: http://pytest.org/
.. _`tox`: https://tox.readthedocs.io/


.. EOF
