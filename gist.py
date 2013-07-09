#!/usr/bin/env python

'''gist.py

A command-line gist poster in Python.

This project is mainly a demo of docopt and cmd, two great python libraries for
making beautiful and functional command-line programs.

Usage: gist.py'''

from docopt import docopt


def main(args):
    pass


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
