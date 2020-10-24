#!/usr/bin/env python3
""" Find subsequences """

import argparse
from itertools import starmap
from typing import NamedTuple, Iterator


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
    k = len(subseq)
    kmers = enumerate(seq[i:i + k] for i in range(len(seq) - k + 1))
    found: Iterator[int] = filter(
        None, starmap(lambda i, kmer: i + 1
                      if kmer == subseq else None, kmers))
    print(*found)


# --------------------------------------------------
if __name__ == '__main__':
    main()
