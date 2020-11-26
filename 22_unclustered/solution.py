#!/usr/bin/env python3
""" Find unclustered proteins """

import argparse
import re
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find proteins not clustered by CD-HIT',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--cdhit',
                        help='Output file from CD-HIT (clustered proteins)',
                        metavar='cdhit',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-p',
                        '--proteins',
                        help='Proteins FASTA',
                        metavar='proteins',
                        type=argparse.FileType('r'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='outfile',
                        type=argparse.FileType('wt'),
                        default='unclustered.fa')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Record all the protein IDs that were clustered
    clustered = set()
    for line in args.cdhit:
        if line.startswith('>'):
            continue

        match = re.search(r'>(\d+)', line)
        if match:
            clustered.add(match.group(1))

    # Write out the sequence for IDs that were not clustered
    num_total = 0
    num_unclustered = 0
    for rec in SeqIO.parse(args.proteins, 'fasta'):
        num_total += 1
        prot_id = re.sub(r'\|.*', '', rec.id)
        if prot_id not in clustered:
            num_unclustered += 1
            SeqIO.write(rec, args.outfile, 'fasta')

    print('Wrote {:,d} of {:,d} unclustered proteins to "{}"'.format(
        num_unclustered, num_total, args.outfile.name))


# --------------------------------------------------
if __name__ == '__main__':
    main()
