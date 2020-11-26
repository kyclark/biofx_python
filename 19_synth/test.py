#!/usr/bin/env python3
""" tests for synth.py """

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './synth.py'


# --------------------------------------------------
def test_exists():
    """ exists """

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """ usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """ bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_seed():
    """ not int for seed """

    bad = random_string()
    opt = random.choice(['-s', '--seed'])
    rv, out = getstatusoutput(f'{prg} {opt} {bad} ./inputs/*')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_01():
    """ works """

    outfile = 'out.fa'
    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        cmd  = f'{prg} -m 10 -x 30 -s 1 -o {outfile} -n 2 inputs/*'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert os.path.isfile(outfile)
        expected = [
            '>1',
            'TAGTATAATTAGTATAATTTGTATAATTTT',
            '>2',
            'TGTGGAAAACGTGGAAAACATGGAAAACAA',
        ]
        assert open(outfile).read().strip() == '\n'.join(expected)
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
