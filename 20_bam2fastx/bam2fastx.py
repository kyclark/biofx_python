#!/usr/bin/env python3
""" BAM to FASTx """

import argparse
import os
from parallelprocs import run
from typing import NamedTuple, List, TextIO


class Args(NamedTuple):
    file: List[TextIO]
    file_format: str
    outdir: str
    num_procs: int
    verbose: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='BAM to FASTx',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rb'),
                        help='Input BAM files')

    parser.add_argument('-f',
                        '--format',
                        help='Output format',
                        metavar='STR',
                        type=str,
                        choices=['fasta', 'fastq'],
                        default='fasta')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='')

    parser.add_argument('-p',
                        '--procs',
                        help='Num procs',
                        metavar='INT',
                        type=int,
                        default=2)

    parser.add_argument('-v', '--verbose', help='Verbose', action='store_true')

    args = parser.parse_args()

    return Args(file=args.file,
                file_format=args.format,
                outdir=args.outdir,
                num_procs=args.procs,
                verbose=args.verbose)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    out_fmt = args.file_format
    out_dir = args.outdir or out_fmt
    out_ext = '.fa' if out_fmt == 'fasta' else '.fq'

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    commands = []
    for i, fh in enumerate(args.file, start=1):
        fh.close()
        basename = os.path.basename(fh.name)
        root, _ = os.path.splitext(basename)
        out_path = os.path.join(out_dir, root + out_ext)
        print(f'{i:3}: {basename}')
        commands.append(f'samtools {out_fmt} "{fh.name}" > {out_path}')

    try:
        ok = run(commands,
                 halt=1,
                 num_procs=args.num_procs,
                 verbose=args.verbose)
        if not ok:
            print('Something went wrong')
    except Exception as e:
        print(e)

    print(f'Done, see output in "{out_dir}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
