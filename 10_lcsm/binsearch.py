#!/usr/bin/env python3
""" Binary Search """

import argparse
import sys
from typing import NamedTuple, TextIO



class Args(NamedTuple):
    """ Command-line arguments """
    num: int
    max: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Binary Search',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='The number to guess',
                        metavar='int',
                        type=int,
                        required=True)

    parser.add_argument('-m',
                        '--max',
                        help='The maximum range',
                        metavar='int',
                        type=int,
                        required=True)

    args = parser.parse_args()

    return Args(args.num, args.max)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    answer = binary_search(args.num, range(args.max + 1), 0, args.max)
    print('Found' if answer > 0 else 'Not present')


# --------------------------------------------------
def binary_search(x: int, xs: List[int], low: int, high: int) -> int:
    """ Binary search """

    print(f'{low:4} {high:4}', file=sys.stderr)

    if high >= low:
        mid = (high + low) // 2

        if xs[mid] == x:
            return mid
        elif xs[mid] > x:
            return binary_search(x, xs, low, mid - 1)
        else:
            return binary_search(x, xs, mid + 1, high)
    else:
        return -1


# --------------------------------------------------
if __name__ == '__main__':
    main()
