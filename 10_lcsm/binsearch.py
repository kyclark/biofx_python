#!/usr/bin/env python3
""" Binary Search """

import argparse
import sys
from typing import List, NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    num: int
    maximum: int


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
    nums = list(range(args.maximum + 1))
    pos = binary_search(args.num, nums, 0, args.maximum)
    print(f'Found {args.num}!' if pos > 0 else f'{args.num} not present.')


# --------------------------------------------------
def binary_search(x: int, xs: List[int], low: int, high: int) -> int:
    """ Binary search """

    print(f'{low:4} {high:4}', file=sys.stderr)

    if high >= low:
        mid = (high + low) // 2

        if xs[mid] == x:
            return mid

        if xs[mid] > x:
            return binary_search(x, xs, low, mid - 1)

        return binary_search(x, xs, mid + 1, high)

    return -1


# --------------------------------------------------
if __name__ == '__main__':
    main()
