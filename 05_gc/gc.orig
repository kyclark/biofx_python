#!/usr/bin/env python3
"""
Purpose: Calculate GC content
Author : Ken Youens-Clark <kyclark@gmail.com>
"""

import argparse
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input sequence file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    high = (0, '')

    # high = sorted([gc(seq) for seq in SeqIO.parse(args.file, 'fasta')])[-1]
    high = sorted(map(gc, SeqIO.parse(args.file, 'fasta')))[-1]

    print(f'{high[1]} {high[0]:0.06f}')


# --------------------------------------------------
def gc(rec):
    """ Return the GC content, record ID for a sequence """

    seq = str(rec.seq)
    gc = re.findall('[gc]', seq, re.IGNORECASE)
    return ((len(gc) / len(seq)) * 100, rec.id)


# --------------------------------------------------
if __name__ == '__main__':
    main()
