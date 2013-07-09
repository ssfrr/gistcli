#!/usr/bin/env python

'''gist.py

A command-line gist poster in Python.

This project is mainly a demo of docopt and cmd, two great python libraries for
making beautiful and functional command-line programs.

Usage: gist.py'''

from __future__ import print_function
from docopt import docopt
import requests
import json

GIST_API_URL = 'https://api.github.com/gists'


def main(args):
    new_gist = {
        'description': 'A Test Gist',
        'public': True,
        'files': {
            'testfile.txt': {
                'content': 'Wow, this file is the best!'
            }
        }
    }
    response = requests.post(GIST_API_URL, data=json.dumps(new_gist))
    print(response.json()['html_url'])


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
