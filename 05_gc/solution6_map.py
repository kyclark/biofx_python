#!/usr/bin/env python3
""" Compute GC content """

import argparse
from Bio import SeqIO
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

    for rec in SeqIO.parse(args.file, 'fasta'):
        pct = gc(rec.seq)
        if pct > high.gc:
            high = MySeq(pct, rec.id)

    print(f'{high.name} {high.gc:0.6f}')


# --------------------------------------------------
def gc(seq: str) -> float:
    """ Calculate GC content """

    if not seq:
        return 0

    gc = sum(map(lambda base: base in 'CG', seq.upper()))
    return (gc * 100) / len(seq)


# --------------------------------------------------
def test_gc():
    """ Test gc """

    assert gc('') == 0.
    assert gc('C') == 100.
    assert gc('G') == 100.
    assert gc('CGCCG') == 100.
    assert gc('ATTAA') == 0.
    assert gc('ACGT') == 50.


# --------------------------------------------------
if __name__ == '__main__':
    main()
