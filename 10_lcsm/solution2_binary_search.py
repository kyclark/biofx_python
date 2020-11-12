#!/usr/bin/env python3
""" Longest Common Substring """

import argparse
import collections
import random
from functools import partial
from itertools import starmap
from typing import Callable, Counter, List, NamedTuple, TextIO
from Bio import SeqIO


class Args(NamedTuple):
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
    f = partial(common_kmers, seqs)
    start = binary_search(f, 1, shortest)

    if start >= 0:
        # Hill climb to find max
        candidates = []
        for k in range(start, shortest + 1):
            if kmers := f(k):
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
    elif not hi and lo:
        return binary_search(f, low, mid)
    elif hi and not lo:
        return binary_search(f, mid, high)
    else:
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
def common_kmers(xs: List[str], k: int) -> List[str]:
    """ Find k-mers common to all elements """

    counts: Counter[str] = collections.Counter()

    for kmers in map(lambda x: set(find_kmers(x, k)), xs):
        counts.update(kmers)

    n = len(xs)

    def f(s, i):
        return s if i == n else None

    return list(filter(None, starmap(f, counts.items())))


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
