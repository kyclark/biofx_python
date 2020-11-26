#!/usr/bin/env python3
"""Grep through FASTX files"""

import argparse
import os
import re
import sys
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Grep through FASTX files',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        metavar='PATTERN',
                        type=str,
                        help='Search pattern')

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('r'),
                        help='Input file(s)')

    parser.add_argument('-f',
                        '--format',
                        help='Input file format',
                        metavar='str',
                        choices=['fasta', 'fastq'],
                        default='')

    parser.add_argument('-O',
                        '--out_format',
                        help='Output file format',
                        metavar='str',
                        choices=['fasta', 'fastq', 'fasta-2line'],
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        default=None)

    args = parser.parse_args()

    if not args.format:
        args.format = guess_format(args.file[0].name)

    if not args.format:
        parser.error(f'Cannot guess --format, please specify')

    return args


# --------------------------------------------------
def guess_format(file):
    """Guess format from extension"""

    _, ext = os.path.splitext(file)
    ext = ext[1:] if ext.startswith('.') else ext

    return 'fasta' if re.match(
        'f(ast|n)?a$', ext) else 'fastq' if re.match('f(ast)?q$', ext) else ''


# --------------------------------------------------
def test_guess_format():
    """Test guess_format"""

    assert guess_format('/foo/bar.fa') == 'fasta'
    assert guess_format('/foo/bar.fna') == 'fasta'
    assert guess_format('/foo/bar.fasta') == 'fasta'
    assert guess_format('/foo/bar.fq') == 'fastq'
    assert guess_format('/foo/bar.fastq') == 'fastq'
    assert guess_format('/foo/bar.fx') == ''


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    regex = re.compile(args.pattern)
    out_fh = args.outfile or sys.stdout
    checked, took = 0, 0

    for fh in args.file:
        for rec in SeqIO.parse(fh, args.format):
            checked += 1
            if any(map(regex.search, [rec.id, rec.description])):
                took += 1
                SeqIO.write(rec, out_fh, args.out_format or args.format)

    print(f'Done, checked {checked}, took {took}.', file=sys.stderr)


# --------------------------------------------------
if __name__ == '__main__':
    main()
