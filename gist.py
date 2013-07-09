#!/usr/bin/env python

'''gist.py

A command-line gist poster in Python.

This project is mainly a demo of docopt and cmd, two great python libraries for
making beautiful and functional command-line programs. This utility can be used
as a quick way to post gists from the command line, or if the user does not
provide a filename then a command prompt is opened.

Usage: gist.py [-d <desc>] [<filename>]

Options:
    -d <desc>   A short description of this gist [default: ]
    <filename>  A file to be posted as a gist.'''

from __future__ import print_function
from docopt import docopt
import requests
import json
from cmd import Cmd

GIST_API_URL = 'https://api.github.com/gists'


def main(args):
    gist_filename = args['<filename>']
    gist_desc = args['-d']
    if gist_filename is not None:
        gist_url = post_gist(gist_filename, gist_desc)
        print(gist_url)
    else:
        app = GistCmd()
        app.cmdloop()


def post_gist(filename, description):
    gist_file = open(filename)

    new_gist = {
        'description': description,
        'public': True,
        'files': {
            filename: {
                'content': gist_file.read()
            }
        }
    }
    response = requests.post(GIST_API_URL, data=json.dumps(new_gist))
    return response.json()['html_url']


class GistCmd(Cmd):
    prompt = 'gist> '

    def do_list(self, line):
        '''Shows a list of the most recent gists posted'''
        gists_response = requests.get(GIST_API_URL)
        for gist in gists_response.json():
            api_id = gist['id']
            user = gist['user']['login']
            desc = gist['description']
            print('%s: %s - %s' % (api_id, user, desc))

    def do_show(self, line):
        '''Displays the given gist'''
        gist = requests.get(GIST_API_URL + '/' + line).json()
        if gist['user']:
            user = gist['user']['login']
        else:
            user = 'Anonymous'
        desc = gist['description']
        gist_files = gist['files']

        print('User: ' + user)
        print('Description: ' + desc)
        for filename, info in gist_files.iteritems():
            print('\n' + filename + '\n--')
            raw_file_response = requests.get(info['raw_url'])
            raw_file = raw_file_response.text
            print(raw_file)

    def do_quit(self, line):
        '''Quits'''
        return True


if __name__ == '__main__':
    args = docopt(__doc__)
    main(args)
