#!/usr/bin/env python3
""" Annotate BLAST output """

import argparse
import pandas as pd
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
    annots = pd.read_csv(args.annotations)
    hits = pd.read_csv(args.hits,
                       delimiter='\t',
                       names=[
                           'qseqid', 'sseqid', 'pident', 'length', 'mismatch',
                           'gapopen', 'qstart', 'qend', 'sstart', 'send',
                           'evalue', 'bitscore'
                       ])

    def error(msg: str) -> None:
        if not args.quiet:
            print(msg, file=sys.stderr)

    data = []
    for _, hit in hits.iterrows():
        if seq_id := hit.get('sseqid'):
            centroids = annots[annots['centroid'] == seq_id]
            if not centroids.empty:
                for _, centroid in centroids.iterrows():
                    data.append({
                        'seq_id': seq_id,
                        'pident': hit.get('pident', 'NA'),
                        'genus': centroid.get('genus', 'NA'),
                        'species': centroid.get('species', 'NA'),
                    })
            else:
                error(f'Missing "{seq_id}"')

    df = pd.DataFrame.from_records(data=data)
    df.to_csv(args.outfile, index=False, sep=args.delimiter)


# --------------------------------------------------
if __name__ == '__main__':
    main()
