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
        nums = [0, 1]
        for _ in range(n - 1):
            nums.append((nums[-2] * args.litter) + nums[-1])
        return nums[-1]

    print(fib(args.generations))


# --------------------------------------------------
if __name__ == '__main__':
    main()
