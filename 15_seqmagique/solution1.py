#!/usr/bin/env python3
""" Mimic seqmagick, print stats on FASTA sequences """

import argparse
from typing import NamedTuple, TextIO, List
import numpy as np
from tabulate import tabulate
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: List[TextIO]
    tablefmt: str


class FastaInfo(NamedTuple):
    """ FASTA file information """
    filename: str
    min_len: int
    max_len: int
    avg_len: float
    num_seqs: int


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+',
                        help='Input FASTA file(s)')

    parser.add_argument('-t',
                        '--tablefmt',
                        metavar='table',
                        type=str,
                        choices=[
                            'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst',
                            'mediawiki', 'latex', 'latex_raw', 'latex_booktabs'
                        ],
                        default='plain',
                        help='Tabulate table style')

    args = parser.parse_args()

    return Args(args.file, args.tablefmt)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    info = [process(fh) for fh in args.file]
    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    print(tabulate(info, tablefmt=args.tablefmt, headers=headers))


# --------------------------------------------------
def process(fh: TextIO) -> FastaInfo:
    """ Process a file """

    if lengths := [len(rec.seq) for rec in SeqIO.parse(fh, 'fasta')]:
        return FastaInfo(filename=fh.name,
                         min_len=min(lengths),
                         max_len=max(lengths),
                         avg_len=round(np.mean(lengths), 2),
                         num_seqs=len(lengths))

    return FastaInfo(filename=fh.name,
                     min_len=0,
                     max_len=0,
                     avg_len=0,
                     num_seqs=0)


# --------------------------------------------------
if __name__ == '__main__':
    main()
