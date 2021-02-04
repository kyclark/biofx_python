#!/usr/bin/env python3
""" Compute GC content """

import argparse
import sys
from typing import NamedTuple, TextIO
from Bio import SeqIO


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
                        nargs='?',
                        default=sys.stdin,
                        help='Input sequence file')

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    high = MySeq(0., '')

    for rec in SeqIO.parse(args.file, 'fasta'):
        pct = find_gc(rec.seq)
        if pct > high.gc:
            high = MySeq(pct, rec.id)

    print(f'{high.name} {high.gc:0.6f}')


# --------------------------------------------------
def find_gc(seq: str) -> float:
    """ Calculate GC content """

    if not seq:
        return 0

    gc = sum(map(lambda base: base in 'CG', seq.upper()))
    return (gc * 100) / len(seq)


# --------------------------------------------------
def test_find_gc():
    """ Test find_gc """

    assert find_gc('') == 0.
    assert find_gc('C') == 100.
    assert find_gc('G') == 100.
    assert find_gc('CGCCG') == 100.
    assert find_gc('ATTAA') == 0.
    assert find_gc('ACGT') == 50.


# --------------------------------------------------
if __name__ == '__main__':
    main()
