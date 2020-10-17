#!/usr/bin/env python3
"""Find location of N-glycosylation motif"""

import argparse
import logging
import os
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

    for file in files:
        seqs = list(SeqIO.parse(file, 'fasta'))
        if not seqs:
            print(f'"{file}" contains no sequences.', file=sys.stderr)
            continue

        seq = seqs[0]
        if hits := find_motif(str(seq.seq)):
            pos = map(lambda p: p + 1, hits)
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
def find_motif(text: str):
    """Find a pattern in some text"""

    # pos = []
    # for i, kmer in enumerate(find_kmers(text, 4)):
    #     if kmer[0] == 'N' and kmer[1] != 'P' and kmer[
    #             2] in 'ST' and kmer[3] != 'P':
    #         pos.append(i)

    # return pos

    return [
        i for i, kmer in enumerate(find_kmers(text, 4)) if kmer[0] == 'N'
        and kmer[1] != 'P' and kmer[2] in 'ST' and kmer[3] != 'P'
    ]

    # def is_match(pos, kmer):
    #     return (kmer[0] == 'N' and kmer[1] != 'P' and kmer[2] in 'ST'
    #             and kmer[3] != 'P', pos)

    # def filter_map(f, i):
    #     return list(
    #         map(lambda tup: tup[1], filter(lambda tup: tup[0],
    #                                        starmap(f, i))))

    # return filter_map(is_match, enumerate(find_kmers(text, 4)))


# --------------------------------------------------
def test_find_motif():
    """Test find_pattern"""

    assert find_motif('') == []
    assert find_motif('NPTX') == []
    assert find_motif('NXTP') == []
    assert find_motif('NXSX') == [0]
    assert find_motif('NXTX') == [0]
    assert find_motif('XNXSX') == [1]
    assert find_motif('XNXTX') == [1]


# --------------------------------------------------
def find_kmers(seq, k):
    """Find k-mers in string"""

    seq = str(seq)
    n = len(seq) - k + 1
    return list(map(lambda i: seq[i:i + k], range(n)))


# --------------------------------------------------
def test_find_kmers():
    """Test find_kmers"""

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
