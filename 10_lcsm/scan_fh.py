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
    args.file.close()

    def seqs():
        return [str(rec.seq) for rec in SeqIO.parse(args.file.name, 'fasta')]

    shortest, num_seqs = 0, 0
    for seq_len in map(len, seqs()):
        if shortest == 0:
            shortest = seq_len

        if seq_len < shortest:
            shortest = seq_len

        num_seqs += 1

    print(f'shortest = "{shortest}", num = "{num_seqs}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
