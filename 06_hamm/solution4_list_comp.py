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

    # Method 4: list comprehension
    # distance = [1 if c1 != c2 else 0 for c1, c2 in zip_longest(line1, line2)]

    # Use guard
    # distance = [1 for c1, c2 in zip_longest(line1, line2) if c1 != c2]

    # Use bool->int coercion
    distance = [c1 != c2 for c1, c2 in zip_longest(line1, line2)]

    print(sum(distance))


# --------------------------------------------------
if __name__ == '__main__':
    main()
