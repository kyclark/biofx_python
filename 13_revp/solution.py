#!/usr/bin/env python3
"""Locating Restriction Sites"""

import argparse
import sys
from Bio import SeqIO, Seq
from typing import NamedTuple, TextIO, Tuple


class Args(NamedTuple):
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

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
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(lambda s: str(s.seq), SeqIO.parse(args.file, 'fasta')))

    if not seqs:
        sys.exit(f'"{args.file.name}" contains no sequences.')

    seq = seqs[0]

    for k in range(4, 13):
        kmers = find_kmers(seq, k)
        revc = list(map(Seq.reverse_complement, kmers))

        for fwd, rev in zip(enumerate(kmers), enumerate(revc)):
            if snd(fwd) == snd(rev):
                print(fst(fwd) + 1, k)


# --------------------------------------------------
def fst(tup: Tuple):
    """Return second member of tuple"""

    return tup[0]


# --------------------------------------------------
def test_fst():
    """Test fst"""

    assert fst((1, 'A')) == 1
    assert fst(('A', 1)) == 'A'


# --------------------------------------------------
def snd(tup: Tuple):
    """Return second member of tuple"""

    return tup[1]


# --------------------------------------------------
def test_snd():
    """Test snd"""

    assert snd((1, 'A')) == 'A'
    assert snd(('A', 1)) == 1


# --------------------------------------------------
def find_kmers(seq, k):
    """Find k-mers in string"""

    n = len(seq) - k + 1
    return list(map(lambda i: seq[i:i + k], range(n)))


# --------------------------------------------------
def test_find_kmers():
    """Test find_kmers"""

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
