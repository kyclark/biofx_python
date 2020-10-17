#!/usr/bin/env python3
"""Find location of N-glycosylation motif"""

import argparse
import logging
import os
import re
import requests
import sys
from typing import NamedTuple, List, TextIO
from Bio import SeqIO


class Args(NamedTuple):
    file: TextIO
    download_dir: str


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find location of N-glycosylation motif',
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
    """Make a jazz noise here"""

    args = get_args()

    logging.basicConfig(filename='.log', filemode='w', level=logging.DEBUG)
    files = fetch_fasta(args.file, args.download_dir)
    regex = re.compile('(?=(N[^P][ST][^P]))')

    for file in files:
        seqs = list(SeqIO.parse(file, 'fasta'))
        if not seqs:
            print(f'"{file}" contains no sequences.', file=sys.stderr)
            continue

        seq = seqs[0]
        if hits := list(regex.finditer(str(seq.seq))):
            pos = map(lambda m: m.start() + 1, hits)
            name = os.path.basename(file).replace('.fa', '')
            print('\n'.join([name, ' '.join(map(str, pos))]))


# --------------------------------------------------
def fetch_fasta(fh: TextIO, fasta_dir: str) -> List[str]:
    """Fetch the FASTA files into the download directory"""

    if not os.path.isdir(fasta_dir):
        os.makedirs(fasta_dir)

    files = []
    for prot_id in map(str.rstrip, fh):
        fasta = os.path.join(fasta_dir, prot_id + '.fa')
        if not os.path.isfile(fasta):
            # TODO: Make this logging
            logging.debug(f'Fetching "{prot_id}" -> {fasta}')
            url = f'http://www.uniprot.org/uniprot/{prot_id}.fasta'
            response = requests.get(url)
            if response.status_code == 200:
                fh = open(fasta, 'wt')
                fh.write(response.text)
                fh.close()
            else:
                print(f'Error fetching "{url}": "{response.status_code}"',
                      file=sys.stderr)
                continue

        files.append(fasta)

    return files


# --------------------------------------------------
if __name__ == '__main__':
    main()
