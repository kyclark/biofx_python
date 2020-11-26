#!/usr/bin/env python3
"""tests for find_unclustered.py"""

import os.path
import random
import string
import re
from subprocess import getstatusoutput, getoutput
from random import shuffle
from Bio import SeqIO

prg = './find_unclustered.py'
proteins = 'unclustered-proteins/proteins.fa'
cdhit = 'unclustered-proteins/proteins.fa.cdhit.clstr'


# --------------------------------------------------
def test_exists():
    """usage"""

    assert os.path.isfile(prg)
    assert os.path.isfile(proteins)
    assert os.path.isfile(cdhit)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_missing_cdhit():
    """fails on bad input"""

    rv, out = getstatusoutput(f'{prg} -c {proteins}')
    assert rv != 0
    assert re.search('the following arguments are required: -p/--proteins',
                     out)


# --------------------------------------------------
def test_missing_proteins():
    """fails on bad input"""

    rv, out = getstatusoutput(f'{prg} -p {proteins}')
    assert rv > 0
    assert re.search('the following arguments are required: -c/--cdhit', out)


# --------------------------------------------------
def test_bad_protein_file():
    """fails on bad input"""

    bad = random_filename()
    rv, out = getstatusoutput(f'{prg} --cdhit {cdhit} -p {bad}')
    assert rv > 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_cdhit_file():
    """fails on bad input"""

    bad = random_filename()
    rv, out = getstatusoutput(f'{prg} --cdhit {bad} -p {proteins}')
    assert rv > 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input():
    """works on good input"""

    out_file = 'unclustered.fa'
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv, out = getstatusoutput(f'{prg} -c {cdhit} -p {proteins}')
        assert rv == 0
        assert out == ('Wrote 309 of 220,520 unclustered '
                       'proteins to "unclustered.fa"')

        assert os.path.isfile(out_file)

        seqs = list(SeqIO.parse(out_file, 'fasta'))

        assert len(seqs) == 309
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_outfile():
    """works on good input"""

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        cmd = f'{prg} --cdhit {cdhit} --proteins {proteins} -o {out_file}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0

        assert out == ('Wrote 309 of 220,520 unclustered '
                       f'proteins to "{out_file}"')

        assert os.path.isfile(out_file)

        seqs = list(SeqIO.parse(out_file, 'fasta'))
        assert len(seqs) == 309

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
