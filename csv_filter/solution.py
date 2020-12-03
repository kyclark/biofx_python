#!/usr/bin/env python3
""" Filter delimited records """

import argparse
import csv
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Filter delimited records',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file',
                        required=True)

    parser.add_argument('-v',
                        '--val',
                        help='Value for filter',
                        metavar='val',
                        type=str,
                        required=True)

    parser.add_argument('-c',
                        '--col',
                        help='Column for filter',
                        metavar='col',
                        type=str,
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        type=argparse.FileType('wt'),
                        default='out.csv')

    parser.add_argument('-d',
                        '--delimiter',
                        help='Input delimiter',
                        metavar='delim',
                        type=str,
                        default=',')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    search_for = args.val
    search_col = args.col
    reader = csv.DictReader(args.file, delimiter=args.delimiter)

    if search_col and search_col not in reader.fieldnames:
        print(f'--col "{search_col}" not a valid column!', file=sys.stderr)
        print(f'Choose from {", ".join(reader.fieldnames)}')
        sys.exit(1)

    writer = csv.DictWriter(args.outfile, fieldnames=reader.fieldnames)
    writer.writeheader()

    num_written = 0
    for rec in reader:
        text = rec.get(search_col) if search_col else ' '.join(rec.values())

        if re.search(search_for, text, re.IGNORECASE):
            num_written += 1
            writer.writerow(rec)
            # args.outfile.write(text + '\n')

    print(f'Done, wrote {num_written:,} to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
