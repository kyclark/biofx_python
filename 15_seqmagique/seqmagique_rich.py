#!/usr/bin/env python3
""" Mimic seqmagick, print stats on FASTA sequences """

import argparse
import numpy as np
from typing import List, NamedTuple, TextIO
from rich.console import Console
from rich.progress import track
from rich.table import Table, Column
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: List[TextIO]


class FastaInfo(NamedTuple):
    """ FASTA file information """
    filename: str
    min_len: int
    max_len: int
    avg_len: int
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
                        help='Input file(s)')

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    table = Table('Name',
                  Column(header='Min. Len', justify='right'),
                  Column(header='Max. Len', justify='right'),
                  Column(header='Avg. Len', justify='right'),
                  Column(header='Num. Seqs', justify='right'),
                  header_style="bold black")

    for fh in track(args.file):
        file = process(fh)
        table.add_row(file.filename, str(file.min_len), str(file.max_len),
                      str(file.avg_len), str(file.num_seqs))

    console = Console()
    console.print(table)


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
