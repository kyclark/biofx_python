#!/usr/bin/env python3
"""tests for explode.py"""

import os
import re
from subprocess import getstatusoutput, getoutput

prg = './explode.py'
sample1 = 'samples/sample1.txt'
sample2 = 'samples/sample2.txt'

expected1 = """
ATTTACAATAATTTAATAAAATTAACTAGAAATAAAATATTGTATGAAAATATGTTAAAT
AATGAAAGTTTTTCAGATCGTTTAATAATATTTTTCTTCCATTTTGCTTTTTTCTAAAAT
TGTTCAAAAACAAACTTCAAAGGAAAATCTTCAAAATTTACATGATTTTATATTTAAACA
AATAGAGTTAAGTATAAGAGAAATTGGATATGGTGATGCTTCAATAAATAAAAAAATGAA
AGAGTATGTCAATGTGATGTACGCAATAATTGACAAAGTTGATTCATGGGAAAATCTTGA
TTTATCTACAAAAACTAAATTCTTTTCTGAATTTATTAATGTCGATAAGGAATCTACATT
""".strip()

expected2 = """
TTTGTAAAGTCTGGATTAACTGCTATAAAATCGGAAACCATAACACCTTTTAGAGTTAAA
GAATCTCCTGTTCAAATGGAATGTATTGTTAATGATGTTATTGAACTTGGAGACCAAGGT
GGAGCAGGAAATTTAGTAGTATGTGAAATAAAAATGATTCACATTAATGAAGATATTCTT
GATGATGAAGGAATTATTGATCCAAATAAAATTAAATTAGTCGGACGCATGGGTGGAAAC
TGGTATTGTAAAACTACCAACGAATCTATCTTTGAAGTTGTTAAACCTATCCGTAATTTA
GGTATTGGTGTTGATCAGATTCCTAAACGAATTAAAAATAGCTATATTCTTAGTGGAAAT
GATTTAGGTATGCTAGGAAATATAGAAGCCTTACCTACCATCGAAGAGGTTGAAGAATAC
AAAAAAGAAAACTAACACTATAAAATGAAATAATTAAATTTTAAGTAGTGAAGATGAAGA
CAATGCTGAATTTGAATAATTTCCATGTGAATTGGTGGAATATTGTTCTAACAGTGCACG
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

    run('AT3ACA2TA2T3A2TA4T2A2CTAGA3TA4TAT2GTATGA4TATGT2A3T',
        'ATTTACAATAATTTAATAAAATTAACTAGAAATAAAATATTGTATGAAAATATGTTAAAT')


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
