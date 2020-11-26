#!/usr/bin/env python3
"""Annotate BLAST output"""

import argparse
import csv
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('hits',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        help='BLAST output (-outfmt 6)')

    parser.add_argument('-a',
                        '--annotations',
                        help='Annotation file',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    lookup = {}
    reader = csv.DictReader(args.annotations, delimiter=',')
    for row in reader:
        lookup[row['centroid']] = row

    blast_flds = [
        'qseqid', 'sseqid', 'pident', 'length', 'mismatch', 'gapopen',
        'qstart', 'qend', 'sstart', 'send', 'evalue', 'bitscore'
    ]

    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write('\t'.join(['seq_id', 'pident', 'genus', 'species']) + '\n')

    reader = csv.DictReader(args.hits, delimiter='\t', fieldnames=blast_flds)
    for row in reader:
        seq_id = row['sseqid']
        if seq_id not in lookup:
            print('Cannot find seq "{}" in lookup'.format(seq_id),
                  file=sys.stderr)
            continue

        info = lookup[seq_id]
        out_fh.write('\t'.join([
            row['sseqid'], row['pident'], info['genus'] or 'NA',
            info['species'] or 'NA'
        ]) + '\n')

    out_fh.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
