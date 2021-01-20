#!/usr/bin/env python3
""" Annotate BLAST output """

import argparse
import pandas as pd
import sys
import numpy as np
from typing import Any, NamedTuple, TextIO


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
    # hits = hits.set_index('sseqid').join(annots.set_index('centroid'))
    joined = pd.merge(hits,
                      annots,
                      left_on='sseqid',
                      right_on='centroid',
                      how='left')

    def error(msg: str) -> None:
        if not args.quiet:
            print(msg, file=sys.stderr)

    data = []
    for _, hit in joined.iterrows():
        print(hit)
        if seq_id := hit.get('sseqid'):
            # genus, species = hit.get('genus'), hit.get('species')
            genus = '' if isnan(hit['genus']) else hit['genus']
            species = '' if isnan(hit['species']) else hit['species']
            # genus = hit['genus'] or ''
            # species = hit['species'] or ''
            print('GENUS "{}"'.format(hit['genus']))
            print('SPECIES "{}"'.format(hit['species']))

            if any([genus, species]):
                data.append({
                    'seq_id': seq_id,
                    'pident': hit.get('pident'),
                    'genus': genus,
                    'species': species,
                })
            else:
                error(f'Missing "{seq_id}"')
        break

    df = pd.DataFrame.from_records(data=data)
    df.to_csv(args.outfile, index=False, sep=args.delimiter)


# --------------------------------------------------
def isnan(val: Any) -> bool:
    """ Detect NaN """

    print(f'VAL "{val}"')
    return isinstance(val, float) and np.nan(val)


# --------------------------------------------------
if __name__ == '__main__':
    main()
