#!/usr/bin/env python3
""" Scan for shortest, number using memory """

import argparse
from Bio import SeqIO
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Scan for shortest, number using memory',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='FASTA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    # Get a list of the sequences as strings
    seqs = list(map(lambda s: str(s.seq), SeqIO.parse(args.file, 'fasta')))

    # Find the length of the shortest sequence, total num of sequences
    shortest = min(map(len, seqs))
    num_seqs = len(seqs)

    print(f'shortest = "{shortest}", num = "{num_seqs}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
