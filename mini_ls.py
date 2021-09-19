#!/usr/bin/python3 -s

"""
mini-ls
-------

Usage

    ./mini-ls [-r] [FILE...]

`mini-ls` lists information about the paths given in FILE. The
information required are: Owner, Permission, Modified Time.

- FILE can be zero or more arguments. If zero args are given,
  `mini-ls` will list information about the current directory.
- If given, the `-r` option will make `mini-ls` run recursively on any
  directory it comes across.
"""

import argparse
import os
import pwd
import stat
import time


def mini_ls(path, recursive):
    try:
        info = os.stat(path)
    except FileNotFoundError:
        print(path + ': File not found')
        return 2
    print("{:4s} {:8s} {:8s} {:6s}".format(str(oct(info.st_mode))[-3:],
                                           pwd.getpwuid(info.st_uid).pw_name,
                                           time.ctime(info.st_mtime),
                                           path))
    stat.S_ISDIR(info.st_mode)
    if recursive and stat.S_ISDIR(info.st_mode):
        for file in os.listdir(path):
            info = os.stat(path + '/' + file)
            print("{:4s} {:8s} {:8s} {:6s}".format(str(oct(info.st_mode))[-3:],
                                                   pwd.getpwuid(info.st_uid).pw_name,  # E501
                                                   time.ctime(info.st_mtime),
                                                   path + '/' + file))
    return 0


if __name__ == '__main__':
    # Define arguments
    parser = argparse.ArgumentParser(description="mini-grep")
    parser.add_argument('-r', action='store_true',
                        help='run recursively on any directory '
                             'it comes across')
    parser.add_argument('File', nargs='*', default=[os.path.abspath(os.curdir)], type=str,
                        help='can be zero or more arguments. If zero args '
                             'are given, it will list information about '
                             'the current directory.')
    args = parser.parse_args()
    for i in args.File:
        mini_ls(i, args.r)
