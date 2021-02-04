#!/usr/bin/env python3
""" Compute GC content """

import argparse
import sys
from typing import NamedTuple, TextIO, List
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
    seqs: List[MySeq] = []

    for rec in SeqIO.parse(args.file, 'fasta'):
        seqs.append(MySeq(find_gc(rec.seq), rec.id))

    high = max(seqs)
    print(f'{high.name} {high.gc:0.6f}')


# --------------------------------------------------
def find_gc(seq: str) -> float:
    """ Calculate GC content """

    if not seq:
        return 0

    gc = 0
    for base in seq.upper():
        if base in ('C', 'G'):
            gc += 1

    return (gc * 100) / len(seq)


# --------------------------------------------------
def test_find_gc() -> None:
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
