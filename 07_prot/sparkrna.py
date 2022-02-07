#!/usr/bin/env python3
"""
Author : christopherton <christopherton@localhost>
Date   : 2022-02-05
Purpose: Translate RNA to proteins
"""

import argparse
from typing import NamedTuple
from pyspark import SparkContext
from typing import NamedTuple

__all__ = [
    "Args",
    "get_args",
    "codon_dict",
    "sublists",
    "translate"
]

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

    return Args(args.rna).rna.upper()

def codon_dict():
    return ({
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
    })

def sublists(l,k):
    return ([l[i:i + 3] for i in range(0, len(l), k)])


def translate(l,dict):
    #initialize spark instance
    sc = SparkContext.getOrCreate()
    rna_par = sc.parallelize(l)
    trans = ''.join(rna_par.map(lambda codon: dict.get(codon, '-')).collect())
    return (trans.partition('*')[0])




    


   
        
    

