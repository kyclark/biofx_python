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
    print(hamming(args.seq1, args.seq2))


# --------------------------------------------------
def hamming(seq1: str, seq2: str) -> int:
    """ Calculate Hamming distance """

    # Method 2: The base distance is the difference in their lengths
    distance = abs(len(seq1) - len(seq2))

    # Use zip to pair up the letters
    for char1, char2 in zip(seq1, seq2):
        if char1 != char2:
            distance += 1

    return distance


# --------------------------------------------------
def test_hamming() -> None:
    """ Test hamming """

    assert hamming('', '') == 0
    assert hamming('AC', 'ACGT') == 2
    assert hamming('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT') == 7


# --------------------------------------------------
if __name__ == '__main__':
    main()
