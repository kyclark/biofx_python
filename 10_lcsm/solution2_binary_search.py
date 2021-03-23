#!/usr/bin/env python3
""" Longest Common Substring """

import argparse
import random
from collections import Counter
from functools import partial
from itertools import chain
from typing import Callable, List, NamedTuple, TextIO
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

    # Find a starting point
    common = partial(common_kmers, seqs)
    start = binary_search(common, 1, shortest)

    if start >= 0:
        # Hill climb to find max
        candidates = []
        for k in range(start, shortest + 1):
            if kmers := common(k):
                candidates.append(random.choice(kmers))
            else:
                break

        # Print the longest candidate
        print(max(candidates, key=len))
    else:
        print('No common subsequence.')


# --------------------------------------------------
def binary_search(f: Callable, low: int, high: int) -> int:
    """ Binary search """

    hi, lo = f(high), f(low)
    mid = (high + low) // 2

    if hi and lo:
        return high

    if lo and not hi:
        return binary_search(f, low, mid)

    if hi and not lo:
        return binary_search(f, mid, high)

    return -1


# --------------------------------------------------
def test_binary_search() -> None:
    """ Test binary_search """

    seqs1 = ['GATTACA', 'TAGACCA', 'ATACA']
    f1 = partial(common_kmers, seqs1)
    assert binary_search(f1, 1, 5) == 2

    seqs2 = ['GATTACTA', 'TAGACTCA', 'ATACTA']
    f2 = partial(common_kmers, seqs2)
    assert binary_search(f2, 1, 6) == 3


# --------------------------------------------------
def common_kmers(seqs: List[str], k: int) -> List[str]:
    """ Find k-mers common to all elements """

    kmers = [set(find_kmers(seq, k)) for seq in seqs]
    counts = Counter(chain.from_iterable(kmers))
    n = len(seqs)
    return [kmer for kmer, freq in counts.items() if freq == n]


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
