#!/usr/bin/python3 -s

"""
mini-grep
-----------

Usage:

    ./mini-grep [-q] -e PATTERN [FILE...]

`mini-grep` goes through every argument in FILE and prints the whole
line in which PATTERN is found. By default `mini-grep` also outputs
the line number of each printed line.

- PATTERN has to be a valid regex
- FILE can be zero or more arguments. If zero args are given,
  `mini-grep` will parse entries from the standard input.
- If given, the `-q` options only outputs lines but omits the matching
  line numbers.
"""

import argparse
import re


def mini_grep(args):
    for file in args.File:
        line_no = 1
        try:
            with open(file, 'r') as fobj:
                data = fobj.read()
        except FileNotFoundError as e:
            print(e)
            continue
        for line in data.splitlines():
            if args.q:
                if not re.search(args.e, line):
                    print(str(line_no) + ': ' + line)
            else:
                if re.search(args.e, line):
                    print(str(line_no) + ': ' + line)
            line_no += 1
        print('\n' + '---' + '\n')
    return 0


if __name__ == '__main__':
    # Define arguments
    parser = argparse.ArgumentParser(description="mini-grep")
    parser.add_argument('-e', metavar='PATTERN', type=str,
                        help='PATTERN has to be a valid regex')
    parser.add_argument('-q', action='store_true', help='show lines not '
                                                        'matching pattern')
    parser.add_argument('File', type=str, nargs='+',
                        help='can be zero or more arguments. '
                             'If zero args are given')
    args = parser.parse_args()
    mini_grep(args)
