#!/usr/bin/python3 -s

"""
mini-df
-------

Usage:

    ./mini-df [-h] [PATH...]

`mini-df` outputs the file system disk space usage of each entry in
PATH. The information required is: Total Space, Free Space, Used
Space. The result should be in Bytes.

- PATH can be zero or more arguments. IF zero args are given,
  `mini-df` will list the disk space usage of the current directory.
- If given `-h` will output the result in human-readable format.
"""

import argparse
import os.path
import shutil


def main(args):
    #print("{:<20s} {:<20s} {:<20s}\t{:<s}".format('Total', 'Used', 'Free', 'Path'))
    for path in args.Path:
        try:
            df = shutil.disk_usage(path)
        except FileNotFoundError as e:
            print(e)
            continue
        key = 0
        unit = {0: 'B ', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
        usage = {'total': df.total, 'used': df.used, 'free': df.free}
        if args.H:
            while usage.get('total') > 1024 and key <= 4:
                usage['total'] = usage.get('total') / 1024
                usage['used'] = usage.get('used') / 1024
                usage['free'] = usage.get('free') / 1024
                key += 1

        print("{:<.1f} {:s} {:<.1f} {:s} {:<.1f} {:s}\t{:s}".format(usage.get('total'),
                                                                    unit.get(key),
                                                                    usage.get('used'),
                                                                    unit.get(key),
                                                                    usage.get('free'),
                                                                    unit.get(key),
                                                                    path))
    exit(0)


if __name__ == '__main__':
    # Define arguments
    parser = argparse.ArgumentParser(description="mini-df")
    parser.add_argument('-H', action='store_true',
                        help='output the result in human-readable format.')
    parser.add_argument('Path', nargs='*', default=[os.path.abspath(os.curdir)], type=str,
                        help='Path can be zero or more arguments.'
                             ' If zero args are given it will list the disk'
                             'space usage of the current directory')
    args = parser.parse_args()
    main(args)
