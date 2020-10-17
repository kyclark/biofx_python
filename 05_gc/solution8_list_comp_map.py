#!/usr/bin/env python3
""" Compute GC content """

import argparse
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


class MySeq(NamedTuple):
    """ Sequence """
    gc: float
    name: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Compute GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input sequence file')

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    high = MySeq(0., '')
    for seq in map(gc, SeqIO.parse(args.file, 'fasta')):
        if seq.gc > high.gc:
            high = seq

    print(f'{high.name} {high.gc:0.6f}')


# --------------------------------------------------
def gc(rec: SeqRecord) -> MySeq:
    """ Return the GC content, record ID for a sequence """

    pct = 0.
    if seq := str(rec.seq):
        gc = len(re.findall('[GC]', seq.upper()))
        pct = (gc * 100) / len(seq)

    return MySeq(pct, rec.id)


# --------------------------------------------------
def test_gc() -> None:
    """ Test gc """

    assert gc(SeqRecord(Seq(''), id='123')) == (0.0, '123')
    assert gc(SeqRecord(Seq('C'), id='ABC')) == (100.0, 'ABC')
    assert gc(SeqRecord(Seq('G'), id='XYZ')) == (100.0, 'XYZ')
    assert gc(SeqRecord(Seq('ACTG'), id='ABC')) == (50.0, 'ABC')
    assert gc(SeqRecord(Seq('GGCC'), id='XYZ')) == (100.0, 'XYZ')


# --------------------------------------------------
if __name__ == '__main__':
    main()
