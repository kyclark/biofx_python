#!/usr/bin/env python3
""" K-mer tiler """

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    """ Command-line arguments """
    text: str
    k: int


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Kmer tiler',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='A positional argument')

    parser.add_argument('-k',
                        '--kmer_size',
                        help='Size of the k-mers',
                        metavar='int',
                        type=int,
                        default=3)

    args = parser.parse_args()

    return Args(args.text, args.kmer_size)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    num = len(args.text) - args.k + 1
    num = 0 if num < 0 else num
    verb = 'is' if num == 1 else 'are'
    plural = '' if num == 1 else 's'

    print(f'There {verb} {num} {args.k}-mer{plural} in "{args.text}."')

    if num:
        print(args.text)
        for i in range(num):
            print(' ' * i + args.text[i:i + args.k])


# --------------------------------------------------
if __name__ == '__main__':
    main()
