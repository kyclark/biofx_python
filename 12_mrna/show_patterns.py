#!/usr/bin/env python3
""" Generate the mRNA sequences for a protein """

import argparse
import os
from functools import reduce
from itertools import product


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Generate the mRNA sequences for a protein',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein',
                        metavar='protein',
                        type=str,
                        help='Input protein or file')

    parser.add_argument('-m',
                        '--modulo',
                        metavar='int',
                        type=int,
                        default=1000000,
                        help='Modulo value')

    args = parser.parse_args()

    if os.path.isfile(args.protein):
        args.protein = open(args.protein).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    aa_to_codon = {
        'A': ['GCA', 'GCC', 'GCG', 'GCU'],
        'C': ['UGC', 'UGU'],
        'D': ['GAC', 'GAU'],
        'E': ['GAA', 'GAG'],
        'F': ['UUC', 'UUU'],
        'G': ['GGA', 'GGC', 'GGG', 'GGU'],
        'H': ['CAC', 'CAU'],
        'I': ['AUA', 'AUC', 'AUU'],
        'K': ['AAA', 'AAG'],
        'L': ['CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'],
        'M': ['AUG'],
        'N': ['AAC', 'AAU'],
        'P': ['CCA', 'CCC', 'CCG', 'CCU'],
        'Q': ['CAA', 'CAG'],
        'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
        'S': ['AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'],
        'T': ['ACA', 'ACC', 'ACG', 'ACU'],
        'V': ['GUA', 'GUC', 'GUG', 'GUU'],
        'W': ['UGG'],
        'Y': ['UAC', 'UAU'],
        '*': ['UAA', 'UAG', 'UGA'],
    }

    pool = map(aa_to_codon.get, args.protein + '*')
    for i, codons in enumerate(product(*pool), start=1):
        # print(f"{i:5}: {''.join(codons)}")
        print(f"{''.join(codons)}")


# --------------------------------------------------
if __name__ == '__main__':
    main()
