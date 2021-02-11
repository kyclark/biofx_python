#!/usr/bin/env python3
""" Hamming distance """

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    seq1: str
    seq2: str


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq1', metavar='str', help='Sequence 1')

    parser.add_argument('seq2', metavar='str', help='Sequence 2')

    args = parser.parse_args()

    return Args(args.seq1, args.seq2)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    seq1, seq2 = args.seq1, args.seq2

    # Method 1: The base distance is the difference in their lengths
    l1, l2 = len(seq1), len(seq2)
    distance = abs(l1 - l2)

    # Use the length of the shortest word
    # Check the letters at each position
    for i in range(min(l1, l2)):
        if seq1[i] != seq2[i]:
            distance += 1

    print(distance)


# --------------------------------------------------
if __name__ == '__main__':
    main()
