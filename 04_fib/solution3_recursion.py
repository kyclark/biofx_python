#!/usr/bin/env python3
""" Calculate Fibonacci """

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    generations: int
    litter: int


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('n',
                        metavar='generations',
                        type=int,
                        help='Number of generations')

    parser.add_argument('k',
                        metavar='litter',
                        type=int,
                        help='Size of litter per generation')

    args = parser.parse_args()

    if not 1 <= args.n <= 40:
        parser.error(f'n "{args.n}" must be between 1 and 40')

    if not 1 <= args.k <= 5:
        parser.error(f'k "{args.k}" must be between 1 and 5')

    return Args(generations=args.n, litter=args.k)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    def fib(n: int) -> int:
        return 1 if n == 1 or n == 2 \
            else fib(n - 2) * args.litter + fib(n - 1)

    print(fib(args.generations))


# --------------------------------------------------
if __name__ == '__main__':
    main()
