#!/usr/bin/env python3
""" Infer mRNA from Protein """

import argparse
import os
from functools import reduce
from typing import NamedTuple, List


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
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    codon_to_aa = {
        'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T',
        'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S',
        'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M',
        'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R',
        'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L',
        'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
        'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
        'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAC': 'Y', 'UAU': 'Y',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 'UGC': 'C',
        'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L',
        'UUU': 'F', 'UAA': '*', 'UAG': '*', 'UGA': '*',
    }

    possible = [
        len([c for c, res in codon_to_aa.items() if res == aa])
        for aa in args.protein + '*'
    ]
    print(modprod(possible, args.modulo))


# --------------------------------------------------
def mulmod(a: int, b: int, mod: int) -> int:
    """ Multiplication with modulo """

    # Cf. https://www.geeksforgeeks.org/
    # how-to-avoid-overflow-in-modular-multiplication

    def maybemod(x):
        ret = (x % mod) if (mod > 1 and x > mod) else x
        return ret or x  # avoid return 0

    res = 0
    a = maybemod(a)
    while b > 0:
        if b % 2 == 1:
            res = maybemod(res + a)

        a = maybemod(a * 2)
        b //= 2

    return res


# --------------------------------------------------
def test_mulmod() -> None:
    """ Text mulmod """

    assert mulmod(2, 4, 3) == 2
    assert mulmod(9223372036854775807, 9223372036854775807, 1000000) == 501249


# --------------------------------------------------
def modprod(xs: List[int], modulo: int) -> int:
    """ Return the product modulo a value """

    return reduce(lambda x, y: mulmod(x, y, modulo), xs, 1)


# --------------------------------------------------
def test_modprod() -> None:
    """ Test modprod """

    assert modprod([], 3) == 1
    assert modprod([1, 4, 3], 1000000) == 12
    n = 9223372036854775807
    assert modprod([n, n], 1000000) == 501249


# --------------------------------------------------
if __name__ == '__main__':
    main()
