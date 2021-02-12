#!/usr/bin/env python3
""" Mimic seqmagick """

import argparse
from typing import List, NamedTuple, TextIO
import numpy as np
from tabulate import tabulate
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
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
        description='Mimic seqmagick',
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
    data = [process(fh) for fh in args.files]
    hdr = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    print(tabulate(data, tablefmt=args.tablefmt, headers=hdr, floatfmt='.2f'))


# --------------------------------------------------
def process(fh: TextIO) -> FastaInfo:
    """ Process a file """

    if lengths := [len(rec.seq) for rec in SeqIO.parse(fh, 'fasta')]:
        return FastaInfo(filename=fh.name,
                         min_len=min(lengths),
                         max_len=max(lengths),
                         avg_len=round(float(np.mean(lengths)), 2),
                         num_seqs=len(lengths))

    return FastaInfo(filename=fh.name,
                     min_len=0,
                     max_len=0,
                     avg_len=0.,
                     num_seqs=0)


# --------------------------------------------------
if __name__ == '__main__':
    main()
