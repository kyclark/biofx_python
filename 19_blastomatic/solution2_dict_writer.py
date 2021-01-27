#!/usr/bin/env python3
""" Annotate BLAST output """

import argparse
import csv
import os
from typing import NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    hits: TextIO
    annotations: TextIO
    outfile: TextIO
    delimiter: str
    pctid: float


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Annotate BLAST output',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--blasthits',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='BLAST -outfmt 6',
                        required=True)

    parser.add_argument('-a',
                        '--annotations',
                        help='Annotations file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required=True)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Output field delimiter',
                        metavar='DELIM',
                        type=str,
                        default='')

    parser.add_argument('-p',
                        '--pctid',
                        help='Minimum percent identity',
                        metavar='PCTID',
                        type=float,
                        default=0.)

    args = parser.parse_args()

    return Args(hits=args.blasthits,
                annotations=args.annotations,
                outfile=args.outfile,
                delimiter=args.delimiter or guess_delimiter(args.outfile.name),
                pctid=args.pctid)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    annots_reader = csv.DictReader(args.annotations, delimiter=',')
    annots = {row['seq_id']: row for row in annots_reader}

    writer = csv.DictWriter(
        args.outfile,
        fieldnames=['qseqid', 'pident', 'depth', 'lat_lon'],
        delimiter=args.delimiter)
    writer.writeheader()

    hits = csv.DictReader(args.hits,
                          delimiter=',',
                          fieldnames=[
                              'qseqid', 'sseqid', 'pident', 'length',
                              'mismatch', 'gapopen', 'qstart', 'qend',
                              'sstart', 'send', 'evalue', 'bitscore'
                          ])

    num_written = 0
    for hit in hits:
        if float(hit.get('pident', -1)) < args.pctid:
            continue

        if seq_id := hit.get('qseqid'):
            if seq := annots.get(seq_id):
                num_written += 1
                writer.writerow({
                    'qseqid': seq_id,
                    'pident': hit.get('pident'),
                    'depth': seq.get('depth'),
                    'lat_lon': seq.get('lat_lon'),
                })

    print(f'Exported {num_written:,} to "{args.outfile.name}".')


# --------------------------------------------------
def guess_delimiter(filename: str) -> str:
    """ Guess the field separator from the file extension """

    ext = os.path.splitext(filename)[1]
    return ',' if ext == '.csv' else '\t'


# --------------------------------------------------
if __name__ == '__main__':
    main()
