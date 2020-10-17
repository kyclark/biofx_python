#!/usr/bin/env python3
""" Generate long sequence """

import argparse
import random
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    seq_len: int
    num_seqs: int
    out_file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Generate long sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-l',
                        '--len',
                        help='Sequence length',
                        metavar='int',
                        type=int,
                        default=1000000)

    parser.add_argument('-n',
                        '--num',
                        help='Number of sequences',
                        metavar='int',
                        type=int,
                        default=100)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='seq.txt')

    args = parser.parse_args()

    return Args(args.len, args.num, args.outfile)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for _ in range(args.num_seqs):
        print(''.join([random.choice('ACGT') for _ in range(args.seq_len)]),
              file=args.out_file)
    print(f'Done, see "{args.out_file.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
