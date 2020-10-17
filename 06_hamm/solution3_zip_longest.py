#!/usr/bin/env python3
""" Hamming distance """

import argparse
from itertools import zip_longest
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='File input')

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    line1, line2 = args.file.read().splitlines()[:2]

    # Method 3: zip_longest
    distance = 0
    for char1, char2 in zip_longest(line1, line2):
        if char1 != char2:
            distance += 1

    print(distance)


# --------------------------------------------------
if __name__ == '__main__':
    main()
