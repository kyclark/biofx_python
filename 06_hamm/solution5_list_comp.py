#!/usr/bin/env python3
""" Hamming distance """

import argparse
from itertools import zip_longest
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

    # Method 4: list comprehension
    # return sum([1 if c1 != c2 else 0 for c1, c2 in zip_longest(seq1, seq2)])

    # Use guard
    # return sum([1 for c1, c2 in zip_longest(seq1, seq2) if c1 != c2])

    # Use bool->int coercion
    return sum([c1 != c2 for c1, c2 in zip_longest(seq1, seq2)])


# --------------------------------------------------
def test_hamming() -> None:
    """ Test hamming """

    assert hamming('', '') == 0
    assert hamming('AC', 'ACGT') == 2
    assert hamming('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT') == 7


# --------------------------------------------------
if __name__ == '__main__':
    main()
