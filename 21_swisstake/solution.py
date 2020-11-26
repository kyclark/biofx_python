#!/usr/bin/env python3
"""
Author : Ken Youens-Clark<kyclark@gmail.com>
Date   : 2020-04-30
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='Swiss file')

    parser.add_argument('-k',
                        '--keyword',
                        help='Keywords to take',
                        metavar='keyword',
                        type=str,
                        nargs='+',
                        required=True)

    parser.add_argument('-s',
                        '--skiptaxa',
                        help='Taxa to skip',
                        metavar='taxa',
                        type=str,
                        nargs='*')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # wanted_kw = set([kw.lower() for kw in args.keyword])
    wanted_kw = set(map(str.lower, args.keyword))
    skip_taxa = set(map(str.lower, args.skiptaxa or []))
    num_taken, num_skipped = 0, 0

    for rec in SeqIO.parse(args.file, 'swiss'):
        annots = rec.annotations

        taxa = annots.get('taxonomy')
        if taxa:
            taxa = set(map(str.lower, taxa))
            if skip_taxa.intersection(taxa):
                num_skipped += 1
                continue

        keywords = annots.get('keywords')
        if keywords:
            keywords = set(map(str.lower, keywords))
            if wanted_kw.intersection(keywords):
                num_taken += 1
                SeqIO.write(rec, args.outfile, 'fasta')
            else:
                num_skipped += 1

    print(f'Done, skipped {num_skipped} and took {num_taken}. '
          f'See output in "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
