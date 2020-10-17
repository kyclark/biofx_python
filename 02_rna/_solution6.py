#!/usr/bin/env python3
""" Transcribe DNA into RNA """

import argparse
import os
from typing import NamedTuple, List, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: List[TextIO]
    out_dir: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Transcribe DNA into RNA',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input DNA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='+')

    parser.add_argument('-o',
                        '--outdir',
                        help='Output directory',
                        metavar='DIR',
                        type=str,
                        default='out')

    args = parser.parse_args()

    return Args(file=args.file, out_dir=args.outdir)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    num_files, num_seqs = 0, 0
    for fh in args.file:
        num_files += 1
        out_file = os.path.join(args.out_dir, os.path.basename(fh.name))
        out_fh = open(out_file, 'wt')

        for dna in fh:
            num_seqs += 1
            for base in dna:
                # print('U' if base == 'T' else base,
                #       end='',
                #       flush=False,
                #       file=out_fh)
                out_fh.write('U' if base == 'T' else base)

        out_fh.close()

    print(f'Done, wrote {num_seqs} sequence{"" if num_seqs == 1 else "s"} '
          f'in {num_files} file{"" if num_files == 1 else "s"} '
          f'to directory "{args.out_dir}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
