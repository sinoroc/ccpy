#


""" Command line interface
"""


import argparse
import logging

from . import _meta


def main():
    """ CLI main function
    """
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser(
        allow_abbrev=False,
    )
    parser.add_argument('--version', action='version', version=_meta.VERSION)
    args = parser.parse_args()
    logger.info("Arguments %s", args)


# EOF
