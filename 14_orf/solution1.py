#!/usr/bin/env python3
""" Find ORFs """

import argparse
import sys
from Bio import Seq, SeqIO
from typing import List, NamedTuple, TextIO


class Args(NamedTuple):
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find ORFs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input FASTA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(lambda s: str(s.seq), SeqIO.parse(args.file, 'fasta')))

    if not seqs:
        sys.exit(f'"{args.file.name}" contains no sequences.')

    rna = seqs[0].replace('T', 'U')
    orfs = set()

    # Process forward and reverse
    for seq in [rna, Seq.reverse_complement(rna)]:
        # Use 0, 1, 2 for frame shifts
        for i in range(3):
            # Try to translate this frame into amino acids
            if aa := translate(seq[i:]):
                # Each ORF has to be individually added to the set
                for orf in find_orfs(aa):
                    orfs.add(orf)

    print('\n'.join(sorted(orfs)))


# --------------------------------------------------
def find_orfs(aa: str) -> List[str]:
    """Find ORFs in AA sequence"""

    # Method 1: Use in/str.index()
    orfs = []
    while 'M' in aa:
        start = aa.index('M')
        if '0' in aa[start + 1:]:
            stop = aa.index('0', start + 1)
            orfs.append(''.join(aa[start:stop]))
            aa = aa[start + 1:]
        else:
            break

    return orfs


# --------------------------------------------------
def test_find_orfs() -> None:
    """Test find_orfs"""

    assert find_orfs('') == []
    assert find_orfs('M') == []
    assert find_orfs('0') == []
    assert find_orfs('MAMAPR0') == ['MAMAPR', 'MAPR']
    assert find_orfs('MAMAPR0M') == ['MAMAPR', 'MAPR']


# --------------------------------------------------
def find_codons(seq: str, k: int) -> List[str]:
    """Find codons/non-overlapping 3-mers"""

    return list(map(lambda i: seq[i:i + k], range(0, len(seq), k)))


# --------------------------------------------------
def test_find_codons() -> None:
    """Test find_codons"""

    assert find_codons('', 3) == []
    assert find_codons('A', 3) == ['A']
    assert find_codons('AA', 3) == ['AA']
    assert find_codons('AAA', 3) == ['AAA']
    assert find_codons('AAAB', 3) == ['AAA', 'B']
    assert find_codons('AAABB', 3) == ['AAA', 'BB']
    assert find_codons('AAABBB', 3) == ['AAA', 'BBB']


# --------------------------------------------------
def translate(seq: str) -> str:
    """Translate RNA in amino acids"""

    codon_to_aa = {
        'AAA': 'K',
        'AAC': 'N',
        'AAG': 'K',
        'AAU': 'N',
        'ACA': 'T',
        'ACC': 'T',
        'ACG': 'T',
        'ACU': 'T',
        'AGA': 'R',
        'AGC': 'S',
        'AGG': 'R',
        'AGU': 'S',
        'AUA': 'I',
        'AUC': 'I',
        'AUG': 'M',
        'AUU': 'I',
        'CAA': 'Q',
        'CAC': 'H',
        'CAG': 'Q',
        'CAU': 'H',
        'CCA': 'P',
        'CCC': 'P',
        'CCG': 'P',
        'CCU': 'P',
        'CGA': 'R',
        'CGC': 'R',
        'CGG': 'R',
        'CGU': 'R',
        'CUA': 'L',
        'CUC': 'L',
        'CUG': 'L',
        'CUU': 'L',
        'GAA': 'E',
        'GAC': 'D',
        'GAG': 'E',
        'GAU': 'D',
        'GCA': 'A',
        'GCC': 'A',
        'GCG': 'A',
        'GCU': 'A',
        'GGA': 'G',
        'GGC': 'G',
        'GGG': 'G',
        'GGU': 'G',
        'GUA': 'V',
        'GUC': 'V',
        'GUG': 'V',
        'GUU': 'V',
        'UAA': '0',
        'UAC': 'Y',
        'UAG': '0',
        'UAU': 'Y',
        'UCA': 'S',
        'UCC': 'S',
        'UCG': 'S',
        'UCU': 'S',
        'UGA': '0',
        'UGC': 'C',
        'UGG': 'W',
        'UGU': 'C',
        'UUA': 'L',
        'UUC': 'F',
        'UUG': 'L',
        'UUU': 'F',
    }

    return ''.join(map(lambda c: codon_to_aa.get(c, '-'), find_codons(seq, 3)))


# --------------------------------------------------
def test_translate() -> None:
    """Test translate"""

    assert translate('') == ''
    assert translate('A') == '-'
    assert translate('XXX') == '-'
    rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    assert translate(rna) == 'MAMAPRTEINSTRING0'


# --------------------------------------------------
if __name__ == '__main__':
    main()
