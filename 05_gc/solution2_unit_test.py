#!/usr/bin/env python3
""" Compute GC content """

import argparse
from Bio import SeqIO
from typing import NamedTuple, TextIO, List


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
    seqs: List[MySeq] = []

    for rec in SeqIO.parse(args.file, 'fasta'):
        seqs.append(MySeq(gc(rec.seq), rec.id))

    high = sorted(seqs)[-1]
    print(f'{high.name} {high.gc:0.6f}')


# --------------------------------------------------
def gc(seq: str) -> float:
    """ Calculate GC content """

    if not seq:
        return 0

    gc = 0
    for base in seq.upper():
        if base == 'C' or base == 'G':
            gc += 1

    return (gc * 100) / len(seq)


# --------------------------------------------------
def test_gc() -> None:
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
