#!/usr/bin/env python3
"""tests for run.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './run.py'
sample1 = 'samples/sample1.txt'
sample2 = 'samples/sample2.txt'

expected1 = """
AT3ACA2TA2T3A2TA4T2A2CTAGA3TA4TAT2GTATGA4TATGT2A3T
A2TGA3GT5CAGATCGT3A2TA2TAT5CT2C2AT4GCT6CTA4T
TGT2CA5CA3CT2CA3G2A4TCT2CA4T3ACATGAT4ATAT3A3CA
A2TAGAGT2A2GTATA2GAGA3T2G2ATATG2TGATGCT2CA2TA3TA7TGA2
AGAGTATGTCA2TGTGATGTACGCA2TA2T2GACA3GT2GAT2CATG3A4TCT2GA
T3ATCTACA5CTA3T2CT4CTGA2T3AT2A2TGTCGATA2G2A2TCTACAT2
""".strip()

expected2 = """
T3GTA3GTCTG2AT2A2CTGCTATA4TCG2A3C2ATA2CAC2T4AGAGT2A3
GA2TCTC2TGT2CA3TG2A2TGTAT2GT2A2TGATGT2AT2GA2CT2G2AGAC2A2G2T
G2AGCAG2A3T3AGTAGTATGTGA3TA5TGAT2CACAT2A2TGA2GATAT2CT2
GATGATGA2G2A2T2AT2GATC2A3TA4T2A3T2AGTCG2ACGCATG3TG2A3C
TG2TAT2GTA4CTAC2A2CGA2TCTATCT3GA2GT2GT2A3C2TATC2GTA2T3A
G2TAT2G2TGT2GATCAGAT2C2TA3CGA2T2A5TAGCTATAT2CT2AGTG2A3T
GAT3AG2TATGCTAG2A3TATAGA2GC2T2AC2TAC2ATCGA2GAG2T2GA2GA2TAC
A6GA4CTA2CACTATA4TGA3TA2T2A3T4A2GTAGTGA2GATGA2GA
CA2TGCTGA2T3GA2TA2T3C2ATGTGA2T2G2TG2A2TAT2GT2CTA2CAGTGCACG
""".strip()


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def run(dna, expected):
    """run"""

    rv, out = getstatusoutput(f'{prg} {dna}')
    assert rv == 0
    assert out.strip() == expected


# --------------------------------------------------
def test_text():
    """string"""

    run('ATTTACAATAATTTAATAAAATTAACTAGAAATAAAATATTGTATGAAAATATGTTAAAT',
        'AT3ACA2TA2T3A2TA4T2A2CTAGA3TA4TAT2GTATGA4TATGT2A3T')


# --------------------------------------------------
def test_file1():
    """file"""

    assert os.path.isfile(sample1)
    run(sample1, expected1)


# --------------------------------------------------
def test_file2():
    """file"""

    assert os.path.isfile(sample2)
    run(sample2, expected2)
