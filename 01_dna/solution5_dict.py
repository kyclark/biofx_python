#!/usr/bin/env python3
""" Tetranucleotide frequency """

import argparse
import os
from typing import NamedTuple, Dict


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
    counts = count(args.dna)
    print('{} {} {} {}'.format(counts['A'], counts['C'], counts['G'],
                               counts['T']))


# --------------------------------------------------
def count(dna: str) -> Dict[str, int]:
    """ Count bases in DNA """

    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in dna:
        if base in counts:
            counts[base] += 1

    return counts


# --------------------------------------------------
def test_count() -> None:
    """ Test count """

    assert count('') == {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    assert count('123XYZ') == {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    assert count('A') == {'A': 1, 'C': 0, 'G': 0, 'T': 0}
    assert count('C') == {'A': 0, 'C': 1, 'G': 0, 'T': 0}
    assert count('G') == {'A': 0, 'C': 0, 'G': 1, 'T': 0}
    assert count('T') == {'A': 0, 'C': 0, 'G': 0, 'T': 1}
    assert count('ACCGGGTTTT') == {'A': 1, 'C': 2, 'G': 3, 'T': 4}


# --------------------------------------------------
if __name__ == '__main__':
    main()
