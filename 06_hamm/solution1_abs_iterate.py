#!/usr/bin/env python3
""" Hamming distance """

import argparse
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

    # Method 1: The base distance is the difference in their lengths
    l1, l2 = len(line1), len(line2)
    distance = abs(l1 - l2)

    # Use the length of the shortest word
    # Check the letters at each position
    for i in range(min(l1, l2)):
        if line1[i] != line2[i]:
            distance += 1

    print(distance)


# --------------------------------------------------
if __name__ == '__main__':
    main()
