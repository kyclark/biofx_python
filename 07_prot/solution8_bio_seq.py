#!/usr/bin/env python3
""" Translate RNA to proteins """

import argparse
from Bio.Seq import Seq
from typing import NamedTuple


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
    print(str(Seq(args.rna).translate()).replace('*', ''))


# --------------------------------------------------
if __name__ == '__main__':
    main()
