#!/usr/bin/env python3
""" Create synthetic DNA using Markov chain """

import argparse
import random
import sys
from itertools import count
from Bio import SeqIO
from collections import defaultdict, Counter
from typing import NamedTuple, List, TextIO, Dict, Optional


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[TextIO]
    outfile: TextIO
    file_format: str
    num: int
    min_len: int
    max_len: int
    k: int
    seed: Optional[int]


WeightedChoice = Dict[str, float]
Chain = Dict[str, WeightedChoice]


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Create synthetic DNA using Markov chain',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Training file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    parser.add_argument('-f',
                        '--format',
                        help='Input file format',
                        metavar='format',
                        type=str,
                        choices=['fasta', 'fastq'],
                        default='fasta')

    parser.add_argument('-n',
                        '--num',
                        help='Number of sequences to create',
                        metavar='number',
                        type=int,
                        default=100)

    parser.add_argument('-x',
                        '--max_len',
                        help='Maximum sequence length',
                        metavar='max',
                        type=int,
                        default=75)

    parser.add_argument('-m',
                        '--min_len',
                        help='Minimum sequence length',
                        metavar='min',
                        type=int,
                        default=50)

    parser.add_argument('-k',
                        '--kmer',
                        help='Size of kmers',
                        metavar='kmer',
                        type=int,
                        default=10)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    return Args(files=args.file,
                outfile=args.outfile,
                file_format=args.format,
                num=args.num,
                min_len=args.min_len,
                max_len=args.max_len,
                k=args.kmer,
                seed=args.seed)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    random.seed(args.seed)
    if chain := read_training(args.files, args.file_format, args.k):
        seqs = (gen_seq(chain, args.k, args.min_len, args.max_len)
                for _ in count())

        for i, seq in enumerate(filter(None, seqs), start=1):
            print(f'>{i}\n{seq}', file=args.outfile)
            if i == args.num:
                break

        print(f'Done, see output in "{args.outfile.name}".')
    else:
        sys.exit(f'No {args.k}-mers in input sequences.')


# --------------------------------------------------
def read_training(fhs: List[TextIO], file_format: str, k: int) -> Chain:
    """ Read training files, return dict of chains """

    counts: Dict[str, Dict[str, int]] = defaultdict(Counter)
    for fh in fhs:
        for rec in SeqIO.parse(fh, file_format):
            for kmer in find_kmers(str(rec.seq), k):
                counts[kmer[:k - 1]][kmer[-1]] += 1

    def weight(freqs: Dict[str, int]) -> Dict[str, float]:
        total = sum(freqs.values())
        return {base: freq / total for base, freq in freqs.items()}

    return {kmer: weight(freqs) for kmer, freqs in counts.items()}


# --------------------------------------------------
def gen_seq(chain: Chain, k: int, min_len: int, max_len: int) -> Optional[str]:
    """ Generate a sequence """

    seq = random.choice(list(chain.keys()))
    seq_len = random.randint(min_len, max_len)

    while len(seq) < seq_len:
        prev = seq[-1 * (k - 1):]
        if choices := chain.get(prev):
            seq += random.choices(population=list(choices.keys()),
                                  weights=list(choices.values()),
                                  k=1)[0]
        else:
            break

    return seq if len(seq) >= min_len else None


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:
    """ Find k-mers in string """

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
