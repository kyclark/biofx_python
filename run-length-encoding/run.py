#!/usr/bin/env python3
"""Run-length encoding/data compression"""

import argparse
import os
import sys
from itertools import starmap


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().strip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for line in args.text.splitlines():
        counts = []
        count = 0
        prev = None
        for letter in line:
            # We are at the start
            if prev is None:
                prev = letter
                count = 1
            # This letter is the same as before
            elif letter == prev:
                count += 1
            # This is a new letter, so record the count
            # of the previous letter and reset the counter
            else:
                counts.append((prev, count))
                count = 1
                prev = letter

        # get the last letter after we fell out of the loop
        counts.append((prev, count))

        # for letter, num in counts:
        #     print('{}{}'.format(letter, '' if num == 1 else num), end='')
        # print()

        #print(''.join(['{}{}'.format(c, '' if n == 1 else n) for c, n in counts]))

        fmt = lambda c, n: '{}{}'.format(c, '' if n == 1 else n)
        print(''.join(starmap(fmt, counts)))



# --------------------------------------------------
if __name__ == '__main__':
    main()
