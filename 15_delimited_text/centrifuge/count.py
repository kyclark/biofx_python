#!/usr/bin/env python3
""" Count Centrifuge """

import argparse
import csv
import os
import sys
from collections import defaultdict
from typing import NamedTuple, TextIO, Dict


class Args(NamedTuple):
    """ Command-line arguments """
    counts: TextIO
    names: TextIO
    out_file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Summary file',
                        metavar='SUM',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='OUT',
                        type=argparse.FileType('rt'),
                        default=sys.stdout)

    args = parser.parse_args()

    basename, ext = os.path.splitext(args.file.name)
    if not ext == '.sum':
        parser.error(f'File extention "{ext}" is not ".sum"')

    tsv_file = basename + '.tsv'
    if not os.path.isfile(tsv_file):
        parser.error('Cannot find expected TSV "{}"'.format(tsv_file))

    return Args(args.file, open(tsv_file), args.outfile)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

    tax_name = {}
    names_reader = csv.DictReader(args.names, delimiter='\t')
    for row in names_reader:
        tax_name[row['taxID']] = row['name']

    counts: Dict[str, int] = defaultdict(int)
    counts_reader = csv.DictReader(args.counts, delimiter='\t')
    for row in counts_reader:
        if tax_id := row['taxID']:
            counts[tax_id] += 1

    writer = csv.DictWriter(args.out_file,
                            fieldnames=['count', 'tax'],
                            delimiter='\t')
    writer.writeheader()

    for tax_id, count in counts.items():
        writer.writerow({'count': count, 'tax': tax_name.get(tax_id, 'NA')})


# --------------------------------------------------
if __name__ == '__main__':
    main()
