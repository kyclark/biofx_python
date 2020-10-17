#!/usr/bin/env python3
""" Hamming distance """

import argparse
import sys
from itertools import zip_longest
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

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
    """ Make a jazz noise here """

    args = get_args()
    lines = args.file.read().splitlines()

    if len(lines) != 2:
        sys.exit(f'Input file "{args.file.name}" must have two lines.')

    seq1, seq2 = lines
    print(hamming(seq1, seq2))


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
