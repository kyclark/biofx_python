#!/usr/bin/env python3
""" Create synthetic DNA using Markov chain """

import argparse
import random
from Bio import SeqIO
from collections import defaultdict
from typing import NamedTuple, List, TextIO, Dict


class Args(NamedTuple):
    file: List[TextIO]
    outfile: TextIO
    file_format: str
    num: int
    min_len: int
    max_len: int
    k: int
    seed: int


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

    return Args(file=args.file,
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
    chains = read_training(args.file, args.file_format, args.k)
    seqs = (gen_seq(chains, args.k, args.min_len, args.max_len)
            for _ in range(args.num))

    for i, seq in enumerate(seqs, start=1):
        print(f'>{i}\n{seq}', file=args.outfile)

    print(f'Done, see output in "{args.outfile.name}".')


# --------------------------------------------------
def gen_seq(chains: Dict[str, List[str]], k: int, min_len: int,
            max_len: int) -> str:
    """ Generate a sequence """

    seq = random.choice(list(chains.keys()))
    seq_len = random.randint(min_len, max_len)

    while len(seq) < seq_len:
        prev = seq[-1 * k:]
        choices = chains.get(prev)
        if not choices:
            break

        seq += random.choice(choices)

    return seq


# --------------------------------------------------
def read_training(fhs: List[TextIO], file_format: str,
                  k: int) -> Dict[str, List[str]]:
    """ Read training files, return dict of chains """

    seqs = defaultdict(list)
    for fh in fhs:
        for rec in SeqIO.parse(fh, file_format):
            kmers = find_kmers(str(rec.seq), k)
            for i in range(0, len(kmers) - 1):
                seqs[kmers[i]].append(kmers[i + 1])

    return seqs


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:
    """ Find k-mers in string """

    seq = str(seq)
    n = len(seq) - k + 1
    return list(map(lambda i: seq[i:i + k], range(n)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
