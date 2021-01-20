#!/usr/bin/env python3
""" Annotate BLAST output """

import argparse
import csv
import sys
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    hits: TextIO
    annotations: TextIO
    outfile: TextIO
    delimiter: str
    quiet: bool


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('hits',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='BLAST output (-outfmt 6)')

    parser.add_argument('-a',
                        '--annotations',
                        help='Annotation file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('-d',
                        '--delimiter',
                        help='Output field delimiter',
                        metavar='DELIM',
                        type=str,
                        default='\t')

    parser.add_argument('-q',
                        '--quiet',
                        help='Do not print missing centroids',
                        action='store_true')

    args = parser.parse_args()

    return Args(args.hits, args.annotations, args.outfile, args.delimiter,
                args.quiet)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()

    annots_reader = csv.DictReader(args.annotations, delimiter=',')
    annots = {}
    for row in annots_reader:
        if centroid := row.get('centroid'):
            annots[centroid] = row

    headers = ['seq_id', 'pident', 'genus', 'species']
    args.outfile.write(args.delimiter.join(headers) + '\n')
    # print(args.delimiter.join(headers), file=args.outfile)

    hits = csv.DictReader(args.hits,
                          delimiter='\t',
                          fieldnames=[
                              'qseqid', 'sseqid', 'pident', 'length',
                              'mismatch', 'gapopen', 'qstart', 'qend',
                              'sstart', 'send', 'evalue', 'bitscore'
                          ])

    for hit in hits:
        if seq_id := hit.get('sseqid'):
            if info := annots.get(seq_id):
                args.outfile.write(
                    args.delimiter.join([
                        seq_id,
                        row.get('pident', 'NA'),
                        info.get('genus', 'NA'),
                        info.get('species', 'NA')
                    ]) + '\n')

                # print(args.delimiter.join([
                #     seq_id,
                #     row.get('pident', 'NA'),
                #     info.get('genus', 'NA'),
                #     info.get('species', 'NA')
                # ]),
                #       file=args.outfile)
            else:
                if not args.quiet:
                    print(f'Missing "{seq_id}"', file=sys.stderr)

    args.outfile.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
