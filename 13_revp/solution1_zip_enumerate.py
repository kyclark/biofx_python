#!/usr/bin/env python3
""" Locating Restriction Sites """

import argparse
from typing import NamedTuple, TextIO
from Bio import SeqIO, Seq
from common import find_kmers, fst, snd


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Locating Restriction Sites',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input FASTA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    for rec in SeqIO.parse(args.file, 'fasta'):
        for k in range(4, 13):
            kmers = find_kmers(str(rec.seq), k)
            revc = list(map(Seq.reverse_complement, kmers))

            for pos, pair in enumerate(zip(kmers, revc)):
                if fst(pair) == snd(pair):
                    print(pos + 1, k)


# --------------------------------------------------
if __name__ == '__main__':
    main()
