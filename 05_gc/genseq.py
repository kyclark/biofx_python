#!/usr/bin/env python3
""" Generate long sequence """

import argparse
import numpy as np
import random
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    seq_len: int
    num_seqs: int
    sigma: float
    out_file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Generate long sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-l',
                        '--len',
                        help='Average sequence length',
                        metavar='int',
                        type=int,
                        default=500)

    parser.add_argument('-n',
                        '--num',
                        help='Number of sequences',
                        metavar='int',
                        type=int,
                        default=1000)

    parser.add_argument('-s',
                        '--sigma',
                        help='Sigma/STD',
                        metavar='sigma',
                        type=float,
                        default=0.1)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='seqs.fa')

    args = parser.parse_args()

    return Args(args.len, args.num, args.sigma, args.outfile)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for i in range(args.num_seqs):
        seq_len = int(np.random.normal(args.seq_len, args.sigma))
        seq = ''.join([random.choice('ACGT') for _ in range(seq_len)])
        args.out_file.write(f'>SEQ{i}\n{seq}\n')

    print(f'Wrote {args.num_seqs:,} sequences of avg length {args.seq_len:,} '
          f'to "{args.out_file.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
