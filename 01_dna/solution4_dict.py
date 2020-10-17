#!/usr/bin/env python3
""" Tetranucleotide frequency """

import argparse
import os
from typing import NamedTuple, Tuple


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    count_a, count_c, count_g, count_t = count(args.dna)
    print(f'{count_a} {count_c} {count_g} {count_t}')


# --------------------------------------------------
def count(dna: str) -> Tuple[int, int, int, int]:
    """ Count bases in DNA """

    counts = {}
    for base in dna:
        if base not in counts:
            counts[base] = 0
        counts[base] += 1

    return (counts.get('A', 0),
            counts.get('C', 0),
            counts.get('G', 0),
            counts.get('T', 0))


# --------------------------------------------------
def test_count() -> None:
    """ Test count """

    assert count('') == (0, 0, 0, 0)
    assert count('123XYZ') == (0, 0, 0, 0)
    assert count('A') == (1, 0, 0, 0)
    assert count('C') == (0, 1, 0, 0)
    assert count('G') == (0, 0, 1, 0)
    assert count('T') == (0, 0, 0, 1)
    assert count('ACCGGGTTTT') == (1, 2, 3, 4)


# --------------------------------------------------
if __name__ == '__main__':
    main()
