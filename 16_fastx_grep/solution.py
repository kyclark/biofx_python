#!/usr/bin/env python3
"""Grep through FASTX files"""

import argparse
import os
import re
import sys
from Bio import SeqIO
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    """ Command-line arguments """
    pattern: str
    files: List[TextIO]
    input_format: str
    output_format: str
    outfile: TextIO
    insensitive: bool


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

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
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-f',
                        '--format',
                        help='Input file format',
                        metavar='str',
                        choices=['fasta', 'fastq'],
                        default='')

    parser.add_argument('-O',
                        '--outfmt',
                        help='Output file format',
                        metavar='str',
                        choices=['fasta', 'fastq', 'fasta-2line'],
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        type=argparse.FileType('wt'),
                        metavar='FILE',
                        default=sys.stdout)

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search',
                        action='store_true')

    args = parser.parse_args()

    return Args(pattern=args.pattern,
                files=args.file,
                input_format=args.format,
                output_format=args.outfmt,
                outfile=args.outfile,
                insensitive=args.insensitive)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()
    regex = re.compile(args.pattern, re.IGNORECASE if args.insensitive else 0)

    for fh in args.files:
        input_format = args.input_format or guess_format(fh.name)

        if not input_format:
            sys.exit(f'Please specify file format for "{fh.name}"')

        output_format = args.output_format or input_format

        for rec in SeqIO.parse(fh, input_format):
            if any(map(regex.search, [rec.id, rec.description])):
                SeqIO.write(rec, args.outfile, output_format)


# --------------------------------------------------
def guess_format(filename: str) -> str:
    """ Guess format from extension """

    ext = re.sub('^[.]', '', os.path.splitext(filename)[1])

    return 'fasta' if re.match('f(ast|a|n)?a$', ext) else 'fastq' if re.match(
        'f(ast)?q$', ext) else ''


# --------------------------------------------------
def test_guess_format() -> None:
    """ Test guess_format """

    assert guess_format('/foo/bar.fa') == 'fasta'
    assert guess_format('/foo/bar.fna') == 'fasta'
    assert guess_format('/foo/bar.faa') == 'fasta'
    assert guess_format('/foo/bar.fasta') == 'fasta'
    assert guess_format('/foo/bar.fq') == 'fastq'
    assert guess_format('/foo/bar.fastq') == 'fastq'
    assert guess_format('/foo/bar.fx') == ''


# --------------------------------------------------
if __name__ == '__main__':
    main()
