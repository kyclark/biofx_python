#!/usr/bin/env python3
""" Translate RNA to proteins """

import argparse
from typing import NamedTuple
from Bio import Seq


class Args(NamedTuple):
    """ Command-line arguments """
    rna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Translate RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('rna', type=str, metavar='RNA', help='RNA sequence')

    args = parser.parse_args()

    return Args(args.rna)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    print(Seq.translate(args.rna, to_stop=True))


# --------------------------------------------------
if __name__ == '__main__':
    main()
