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

    # Method 3: ugly, moving towards L.C.
    found = []
    seen = set()
    for pos in [
            seq.find(subseq, pos) for pos in range(len(seq) - len(subseq))
    ]:
        if pos == -1:
            break

        if pos not in seen:
            found.append(str(pos + 1))
            seen.add(pos)

    print(' '.join(found))


# --------------------------------------------------
if __name__ == '__main__':
    main()
