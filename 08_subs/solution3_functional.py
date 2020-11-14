#!/usr/bin/env python3
""" Find subsequences """

import argparse
import operator
from functools import partial
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
    r = list(range(len(seq) - len(subseq)))
    ok = partial(operator.le, 0)
    find = partial(seq.find, subseq)
    add1 = partial(operator.add, 1)
    print(*sorted(map(add1, set(filter(ok, map(find, r))))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
