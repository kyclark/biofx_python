#!/usr/bin/env python3
""" Find locations of N-glycosylation motif """

import argparse
import os
import re
import sys
from typing import NamedTuple, List, TextIO
import requests
from Bio import SeqIO


class Args(NamedTuple):
    """ Command-line arguments """
    file: TextIO
    download_dir: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Find locations of N-glycosylation motif',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input text file of UniProt IDs',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    parser.add_argument('-d',
                        '--download_dir',
                        help='Directory for downloads',
                        metavar='DIR',
                        type=str,
                        default='fasta')

    args = parser.parse_args()

    return Args(args.file, args.download_dir)


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    files = fetch_fasta(args.file, args.download_dir)
    regex = re.compile('(?=(N[^P][ST][^P]))')

    for file in files:
        prot_id, _ = os.path.splitext(os.path.basename(file))
        recs = SeqIO.parse(file, 'fasta')
        if rec := next(recs):
            if matches := list(regex.finditer(str(rec.seq))):
                print(prot_id)
                print(*[match.start() + 1 for match in matches])


# --------------------------------------------------
def fetch_fasta(fh: TextIO, fasta_dir: str) -> List[str]:
    """ Fetch the FASTA files into the download directory """

    if not os.path.isdir(fasta_dir):
        os.makedirs(fasta_dir)

    files = []
    for prot_id in map(str.rstrip, fh):
        fasta = os.path.join(fasta_dir, prot_id + '.fasta')
        if not os.path.isfile(fasta):
            url = f'http://www.uniprot.org/uniprot/{prot_id}.fasta'
            response = requests.get(url)
            if response.status_code == 200:
                print(response.text, file=open(fasta, 'wt'))
            else:
                print(f'Error fetching "{url}": "{response.status_code}"',
                      file=sys.stderr)
                continue

        files.append(fasta)

    return files


# --------------------------------------------------
if __name__ == '__main__':
    main()
