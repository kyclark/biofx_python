#!/usr/bin/env python3
""" Probabilistically subset FASTA files """

import argparse
import os
import random
import gzip
from Bio import SeqIO
from typing import List, NamedTuple, Optional


class Args(NamedTuple):
    """ Command-line arguments """
    files: List[str]
    file_format: str
    percent: float
    max_reads: int
    seed: Optional[int]
    outdir: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Probabilistically subset FASTA files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=str,
                        nargs='+',
                        help='Input FASTA/Q file(s)')

    parser.add_argument('-f',
                        '--format',
                        help='Input file format',
                        metavar='format',
                        type=str,
                        choices=['fasta', 'fastq'],
                        default='fasta')

    parser.add_argument('-p',
                        '--percent',
                        help='Percent of reads',
                        metavar='reads',
                        type=float,
                        default=.1)

    parser.add_argument('-m',
                        '--max',
                        help='Maximum number of reads',
                        metavar='max',
                        type=int,
                        default=0)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed value',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    if not 0 < args.percent < 1:
        parser.error(f'--percent "{args.percent}" must be between 0 and 1')

    if not os.path.isdir(args.outdir):
        os.makedirs(args.outdir)

    if bad_files := [file for file in args.file if not os.path.isfile(file)]:
        parser.error(f'Invalid file: {", ".join(bad_files)}')

    return Args(files=args.file,
                file_format=args.format,
                percent=args.percent,
                max_reads=args.max,
                seed=args.seed,
                outdir=args.outdir)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    random.seed(args.seed)

    total_num = 0
    for i, file in enumerate(args.files, start=1):
        basename = os.path.basename(file)
        out_file = os.path.join(args.outdir, basename)
        print(f'{i:3}: {basename}')

        ext = os.path.splitext(basename)[1]
        fh = gzip.open(file, 'rt') if ext == '.gz' else open(file, 'rt')
        out_fh = open(out_file, 'wt')
        num_taken = 0

        for rec in SeqIO.parse(fh, args.file_format):
            if random.random() <= args.percent:
                num_taken += 1
                SeqIO.write(rec, out_fh, 'fasta')

            if args.max_reads and num_taken == args.max_reads:
                break

        out_fh.close()
        total_num += num_taken

    num_files = len(args.files)
    print(f'Wrote {total_num:,} sequence{"" if total_num == 1 else "s"} '
          f'from {num_files:,} file{"" if num_files == 1 else "s"} '
          f'to directory "{args.outdir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
