#!/usr/bin/env python

'''gist.py

A command-line gist poster in Python.

This project is mainly a demo of docopt and cmd, two great python libraries for
making beautiful and functional command-line programs.

Usage: gist.py [-d <desc>] <filename>

Options:
    -d <desc>   A short description of this gist [default: ]'''

from __future__ import print_function
from docopt import docopt
import requests
import json

GIST_API_URL = 'https://api.github.com/gists'


def main(args):
    gist_filename = args['<filename>']
    gist_desc = args['-d']
    gist_file = open(gist_filename)

    new_gist = {
        'description': gist_desc,
        'public': True,
        'files': {
            gist_filename: {
                'content': gist_file.read()
            }
        }
    }
    response = requests.post(GIST_API_URL, data=json.dumps(new_gist))
    print(response.json()['html_url'])


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
