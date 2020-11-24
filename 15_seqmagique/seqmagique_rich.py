#!/usr/bin/env python3
""" Mimic seqmagick, print stats on FASTA sequences """

import argparse
import os
import sys
import numpy as np
from typing import NamedTuple, TextIO, List, Optional
from rich.console import Console
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

    if info := list(filter(None, [process(fh) for fh in args.file])):
        table = Table('Name', Column(header='Min. Len', justify='right'),
                      Column(header='Max. Len', justify='right'),
                      Column(header='Avg. Len', justify='right'),
                      Column(header='Num. Seqs', justify='right'))

        for row in info:
            table.add_row(row.filename, str(row.min_len), str(row.max_len),
                          str(row.avg_len), str(row.num_seqs))

        Console().print(table)
    else:
        sys.exit('Error processing input.')


# --------------------------------------------------
def process(fh: TextIO) -> Optional[FastaInfo]:
    """ Process a file """

    if lengths := [len(rec.seq) for rec in SeqIO.parse(fh, 'fasta')]:
        return FastaInfo(filename=os.path.basename(fh.name),
                         min_len=min(lengths),
                         max_len=max(lengths),
                         avg_len=round(np.mean(lengths)),
                         num_seqs=len(lengths))
    else:
        return None


# --------------------------------------------------
if __name__ == '__main__':
    main()
