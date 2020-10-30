#!/usr/bin/env python3
""" Infer mRNA from Protein """

import argparse
import os
from functools import reduce
from typing import List, NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    protein: str
    modulo: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Infer mRNA from Protein',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein',
                        metavar='protein',
                        type=str,
                        help='Input protein or file')

    parser.add_argument('-m',
                        '--modulo',
                        metavar='int',
                        type=int,
                        default=1000000,
                        help='Modulo value')

    args = parser.parse_args()

    if os.path.isfile(args.protein):
        args.protein = open(args.protein).read().rstrip()

    return Args(args.protein, args.modulo)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    codons = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2, 'G': 4, 'H': 2, 'I': 3,
        'K': 2, 'L': 6, 'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6, 'S': 6,
        'T': 4, 'V': 4, 'W': 1, 'Y': 2, '*': 3,
    }
    print(product(map(codons.get, args.protein + '*')) % args.modulo)


# --------------------------------------------------
def product(xs: List[int]) -> int:
    """ Return the product """

    return reduce(lambda x, y: x * y, xs, 1)


# --------------------------------------------------
def test_product() -> None:
    """ Test product """

    assert product([]) == 1
    assert product([4]) == 4
    assert product([1, 2, 3, 4]) == 24


# --------------------------------------------------
if __name__ == '__main__':
    main()
