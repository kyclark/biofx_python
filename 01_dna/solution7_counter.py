#!/usr/bin/env python3
""" Tetranucleotide frequency """

import argparse
import os
from collections import Counter
from typing import NamedTuple


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
    counts = Counter(args.dna)
    print(counts.get('A', 0), counts.get('C', 0), counts.get('G', 0),
          counts.get('T', 0))


# --------------------------------------------------
if __name__ == '__main__':
    main()
