#!/usr/bin/env python3
""" Find subsequences """

import argparse
import re
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

    # Method 8: Regex to handle overlaps
    # pattern = '(?=(' + args.subseq + '))'
    # found = []
    # for match in re.finditer(pattern, args.seq):
    #     found.append(str(match.start() + 1))
    # print(' '.join(found))

    # Shorter
    # pattern = '(?=(' + args.subseq + '))'
    # found = [str(m.start() + 1) for m in re.finditer(pattern, args.seq)]
    # print(' '.join(found))

    # Or
    pattern = '(?=(' + args.subseq + '))'
    matches = map(lambda m: str(m.start() + 1), re.finditer(pattern, args.seq))
    print(' '.join(matches))


# --------------------------------------------------
if __name__ == '__main__':
    main()
