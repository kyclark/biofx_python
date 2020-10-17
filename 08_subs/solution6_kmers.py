#!/usr/bin/env python3
""" Find subsequences """

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    seq: str
    subseq: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find subsequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='seq', help='Sequence')

    parser.add_argument('subseq', metavar='subseq', help='Sub-sequence')

    args = parser.parse_args()

    return Args(args.seq, args.subseq)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    seq, subseq = args.seq, args.subseq

    # Method 6: kmers
    found = []
    k = len(subseq)
    for i, sub in [(i, seq[i:i + k]) for i in range(len(seq) - k + 1)]:
        if sub == subseq:
            found.append(str(i + 1))

    print(' '.join(found))


# --------------------------------------------------
if __name__ == '__main__':
    main()
