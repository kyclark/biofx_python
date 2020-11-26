#!/usr/bin/env python3
"""tests for swiss.py"""

import csv
import hashlib
import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput
from random import shuffle
from Bio import SeqIO

prg = './swisstake.py'
input1 = './inputs/swiss1.txt'
input2 = './inputs/swiss2.txt'


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


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
def test_bad_file():
    """fails on bad file"""

    bad = random_filename()
    rv, out = getstatusoutput('{} {} -k foo'.format(prg, bad))
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_missing_keyword():
    """fails on missing keyword"""

    rv, out = getstatusoutput('{} {}'.format(prg, input1))
    assert rv > 0
    assert re.search('are required: -k/--keyword', out)


# --------------------------------------------------
def test_01():
    """works on good input"""

    run({
        'kw': '"complete proteome"',
        'tax': '-s Metazoa FUNGI viridiplantae',
        'skipped': 14,
        'took': 1
    })


# --------------------------------------------------
def test_02():
    """works on good input"""

    run({
        'kw': '"complete proteome"',
        'tax': '-s METAZOA fungi',
        'skipped': 13,
        'took': 2
    })


# --------------------------------------------------
def test_03():
    """works on good input"""

    run({
        'kw': '"complete proteome"',
        'tax': '-s metazoa',
        'skipped': 9,
        'took': 6
    })


# --------------------------------------------------
def test_04():
    """works on good input"""

    run({'kw': '"complete proteome"', 'tax': '', 'skipped': 6, 'took': 9})


# --------------------------------------------------
def test_01():
    """works on good input"""

    run({'kw': 'malaria', 'tax': '', 'skipped': 13, 'took': 2})


# --------------------------------------------------
def run(args):
    """Run and test"""

    out_tmpl = 'Done, skipped {skipped} and took {took}. See output in "{out}".'
    run_tmpl = '{prg} {file} -o {out_file} {skip} -k {keyword}'
    out_file = random_filename()

    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        cmd = run_tmpl.format(prg=prg,
                              file=input2,
                              out_file=out_file,
                              skip=args['tax'],
                              keyword=args['kw'])

        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out.split('\n')[-1] == out_tmpl.format(skipped=args['skipped'],
                                                      took=args['took'],
                                                      out=out_file)

        fasta = list(SeqIO.parse(out_file, 'fasta'))
        assert len(fasta) == args['took']

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)
