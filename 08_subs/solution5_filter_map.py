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

    # Method 5: Same as 4 but L.C. -> map()
    pos = filter(
        lambda pos: pos > 0,
        map(lambda pos: seq.find(subseq, pos) + 1,
            range(len(seq) - len(subseq))))
    print(' '.join(map(str, sorted(set(pos)))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
