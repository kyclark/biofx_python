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
        parser.error(f'generations "{args.n}" must be between 1 and 40')

    if not 1 <= args.k <= 5:
        parser.error(f'litter "{args.k}" must be between 1 and 5')

    return Args(generations=args.n, litter=args.k)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    fib = [0, 1]
    for _ in range(args.generations - 1):
        fib.append((fib[-2] * args.litter) + fib[-1])

    print(fib[-1])

    # def fib(n: int) -> int:
    #     nums = [0, 1]
    #     for i in range(n - 1):
    #         nums.append((nums[-2] * args.litter) + nums[-1])
    #     return nums[-1]

    # print(fib(args.generations))


# --------------------------------------------------
if __name__ == '__main__':
    main()
