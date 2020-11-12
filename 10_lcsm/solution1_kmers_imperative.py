#!/usr/bin/env python3
""" Longest Common Substring """

import argparse
import random
import sys
from itertools import chain
from collections import Counter
from typing import List, NamedTuple, TextIO
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Longest Common Substring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input FASTA',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    # Get a list of the sequences as strings
    seqs = [str(rec.seq) for rec in SeqIO.parse(args.file, 'fasta')]

    # Find the length of the shortest sequence
    shortest = min(map(len, seqs))

    for k in range(shortest, 0, -1):
        if kmers := common_kmers(seqs, k):
            print(random.choice(kmers))
            sys.exit(0)

    print('No common subsequence.')


# --------------------------------------------------
def common_kmers(seqs: List[str], k: int) -> List[str]:
    """ Find k-mers common to all sequences """

    kmers = [set(find_kmers(seq, k)) for seq in seqs]
    counts = Counter(chain.from_iterable(kmers))
    n = len(seqs)
    candidates = []

    for kmer, count in counts.items():
        if count == n:
            candidates.append(kmer)

    return candidates


# --------------------------------------------------
def test_common_kmers() -> None:
    """ Test common_kmers """

    seqs = ['GATTACA', 'TAGACCA', 'ATACA']
    assert common_kmers(seqs, 5) == []
    assert sorted(common_kmers(seqs, 2)) == ['AC', 'CA', 'TA']


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers() -> None:
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
