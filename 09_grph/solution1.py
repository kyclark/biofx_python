#!/usr/bin/env python3
"""Graph"""

import argparse
import logging
import operator as op
from iteration_utilities import starfilter
from collections import defaultdict
from itertools import product
from Bio import SeqIO
from pprint import pformat
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO
    k: int
    debug: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Graph through sequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='FASTA file')

    parser.add_argument('-k',
                        '--overlap',
                        help='Size of overlap',
                        metavar='size',
                        type=int,
                        default=3)

    parser.add_argument('-d', '--debug', help='Debug', action='store_true')

    args = parser.parse_args()

    if args.overlap < 1:
        parser.error(f'-k "{args.overlap}" must be > 0')

    return Args(args.file, args.overlap, args.debug)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    k = args.k
    start, end = defaultdict(list), defaultdict(list)
    for rec in SeqIO.parse(args.file, 'fasta'):
        seq = str(rec.seq)
        if len(seq) >= k:
            start[seq[:k]].append(rec.id)
            end[seq[-k:]].append(rec.id)

        # if kmers := find_kmers(str(rec.seq), args.k):
        #     start[kmers[0]].append(rec.id)
        #     end[kmers[-1]].append(rec.id)

    logging.debug('STARTS\n{}'.format(pformat(start)))
    logging.debug('ENDS\n{}'.format(pformat(end)))

    # for kmer in end:
    #     if kmer in start:
    #         for seq_id in end[kmer]:
    #             for other in start[kmer]:
    #                 if seq_id != other:
    #                     print(seq_id, other)

    # for [kmer in end if kmer in start]:
    #     for seq_id in end[kmer]:
    #         for other in start[kmer]:
    #             if seq_id != other:
    #                 print(seq_id, other)

    # for kmer in set(start).intersection(set(end)):
    #     print(kmer)
    #     for seq_id in end[kmer]:
    #         # for other in [other in start[kmer] if other != seq_id]:
    #         for other in filter(lambda s: s != seq_id, start[kmer]):
    #             print(seq_id, other)

    for kmer in set(start).intersection(set(end)):
        # pairs = filter(lambda t: op.ne(*t), product(end[kmer], start[kmer]))

        for pair in starfilter(op.ne, product(end[kmer], start[kmer])):
            print(*pair)


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else list(map(lambda i: seq[i:i + k], range(n)))


# --------------------------------------------------
def test_find_kmers() -> None:
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
