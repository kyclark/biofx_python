#!/usr/bin/env python3
""" Calculate Fibonacci """

import argparse
from typing import NamedTuple, Callable


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

    parser.add_argument('gen',
                        metavar='generations',
                        type=int,
                        help='Number of generations')

    parser.add_argument('litter',
                        metavar='litter',
                        type=int,
                        help='Size of litter per generation')

    args = parser.parse_args()

    if not 1 <= args.gen <= 40:
        parser.error(f'generations "{args.gen}" must be between 1 and 40')

    if not 1 <= args.litter <= 5:
        parser.error(f'litter "{args.litter}" must be between 1 and 5')

    return Args(generations=args.gen, litter=args.litter)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    def fib(n: int) -> int:
        return 1 if n in (1, 2) else fib(n - 2) * args.litter + fib(n - 1)

    fib = memoize(fib)

    print(fib(args.generations))


# --------------------------------------------------
def memoize(f: Callable) -> Callable:
    """ Memoize a function """

    cache = {}

    def memo(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]

    return memo


# --------------------------------------------------
if __name__ == '__main__':
    main()
