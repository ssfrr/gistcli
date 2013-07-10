Writing Command Line Tools in Python
====================================

The following are my notes for the talk on writing command line applications
given to PhillyPUG on July 10, 2013.

Usage Strings
 - uses existing unix conventions (posix!)

Argument Parsing

 - optparse
 - argparse
 - docopt

docopt
 - automatic argument parsing
 - help comes for free
 - arguments
 - options
 - commands
    - constant strings
 - Separate options definitions
 - github.com/docopt/docopt
 - docopt.org
 - Vladimir Keleshev

Shelling Out
 - Writing Interactive Applications
 - use the cmd module

cmd
 - python standard library
 - subclass Cmd
 - set a prompt
 - define operations with do_ functions
 - docstrings become command help
 - help comes for free (again!)

Links:
 - github.com/docopt/docopt
 - docopt.org
