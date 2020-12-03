#!/usr/bin/env python3
""" Turn IUPAC DNA codes into regex """

import argparse
import sys
import re
from itertools import product
from typing import NamedTuple, List


class Args(NamedTuple):
    pattern: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Turn IUPAC DNA codes into regex',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='pattern',
                        type=str,
                        help='IUPAC DNA sequence')

    args = parser.parse_args()

    return Args(args.pattern)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    trans = {
        'A': ['A'],
        'B': ['C', 'G', 'T'],
        'C': ['C'],
        'D': ['A', 'G', 'T'],
        'G': ['G'],
        'H': ['A', 'C', 'T'],
        'K': ['G', 'T'],
        'M': ['A', 'C'],
        'N': ['A', 'C', 'G', 'T'],
        'R': ['A', 'G'],
        'S': ['G', 'C'],
        'T': ['T'],
        'U': ['U'],
        'V': ['A', 'C', 'G'],
        'W': ['A', 'T'],
        'Y': ['C', 'T']
    }

    bases = sorted(trans.keys())
    if not re.search('^[' + ''.join(bases) + ']+$', args.pattern):
        sys.exit(f"Pattern must contain only {', '.join(bases)}.")

    iupac = list(map(lambda base: trans[base], args.pattern))
    regex = '^' + ''.join(map(make_alternatives, iupac)) + '$'

    print('pattern = "{}"'.format(args.pattern))
    print('regex   = "{}"'.format(regex))

    for possibility in sorted(product(*iupac)):
        dna = ''.join(possibility)
        print(dna, 'OK' if re.search(regex, dna) else 'NO')


# --------------------------------------------------
def make_alternatives(choices: List[str]) -> str:
    """ Make alternatives """

    n = len(choices)
    return '' if n == 0 else choices[0] if n == 1 else f"[{''.join(choices)}]"


# --------------------------------------------------
def test_make_alternatives():
    """ Test make_alternatives """

    assert make_alternatives([]) == ''
    assert make_alternatives(['A']) == 'A'
    assert make_alternatives(['A', 'B']) == '[AB]'


# --------------------------------------------------
if __name__ == '__main__':
    main()
