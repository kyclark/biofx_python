#!/usr/bin/env python3
"""Graph"""

import argparse
import logging
from collections import defaultdict
from Bio import SeqIO
from pprint import pformat


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

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

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    file = args.file
    k = args.overlap

    logging.basicConfig(
        filename='.log',
        filemode='w',
        level=logging.DEBUG if args.debug else logging.CRITICAL)

    beginning = defaultdict(list)
    end = defaultdict(list)

    for rec in SeqIO.parse(file, 'fasta'):
        kmers = find_kmers(rec.seq, k)
        if kmers:
            beginning[kmers[0]].append(rec.id)
            end[kmers[-1]].append(rec.id)

    logging.debug('BEGINNINGS\n{}'.format(pformat(beginning)))
    logging.debug('ENDS\n{}'.format(pformat(end)))

    for kmer in end:
        if kmer in beginning:
            for seq_id in end[kmer]:
                for other in beginning[kmer]:
                    if seq_id != other:
                        print(seq_id, other)


# --------------------------------------------------
def find_kmers(seq, k):
    """Find k-mers in string"""

    seq = str(seq)
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
