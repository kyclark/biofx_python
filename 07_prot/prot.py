#!/usr/bin/env python3
"""
Author : christopherton <christopherton@localhost>
Date   : 2022-02-05
Purpose: Translate RNA to proteins
"""

import argparse
from typing import NamedTuple, TextIO
from pyspark import SparkContext
import operator
from itertools import takewhile
from typing import NamedTuple, List
from functools import partial


class Args(NamedTuple):
    """ Command-line arguments """
    rna: str


# --------------------------------------------------
def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Translate RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('rna', type=str, metavar='RNA', help='RNA sequence')

    args = parser.parse_args()

    return Args(args.rna)


# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """
    
    #get args
    args = get_args()
    rna = args.rna.upper()

    #initialize spark instance
    sc = SparkContext.getOrCreate()

    codon_to_aa = {
        'AAA': 'K', 'AAC': 'N', 'AAG': 'K', 'AAU': 'N', 'ACA': 'T',
        'ACC': 'T', 'ACG': 'T', 'ACU': 'T', 'AGA': 'R', 'AGC': 'S',
        'AGG': 'R', 'AGU': 'S', 'AUA': 'I', 'AUC': 'I', 'AUG': 'M',
        'AUU': 'I', 'CAA': 'Q', 'CAC': 'H', 'CAG': 'Q', 'CAU': 'H',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P', 'CGA': 'R',
        'CGC': 'R', 'CGG': 'R', 'CGU': 'R', 'CUA': 'L', 'CUC': 'L',
        'CUG': 'L', 'CUU': 'L', 'GAA': 'E', 'GAC': 'D', 'GAG': 'E',
        'GAU': 'D', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'GUA': 'V',
        'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UAC': 'Y', 'UAU': 'Y',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S', 'UGC': 'C',
        'UGG': 'W', 'UGU': 'C', 'UUA': 'L', 'UUC': 'F', 'UUG': 'L',
        'UUU': 'F', 'UAA': '*', 'UAG': '*', 'UGA': '*',
    }

    k_mers = [rna[i:i + 3] for i in range(0, len(rna), 3)]
    rna_par = sc.parallelize(k_mers)
    trans = ''.join(rna_par.map(lambda codon: codon_to_aa.get(codon, '-')).collect())
    print(trans.partition('*')[0])


    '''

    while (l>=0) and (r < len(rna)):
            set = rna[l:r+3]
            if len(set) == 3:
                i = codon_to_aa[set]
                if i == '*':
                    break
                protein+= i
                l+=3
                r+=3
    '''
        
    
# --------------------------------------------------
if __name__ == '__main__':
    main()
