#!/usr/bin/env python3
""" tests for iupac.py """

import os
import re
import random
import string
from subprocess import getstatusoutput, getoutput

prg = './iupac.py'


# --------------------------------------------------
def test_exists():
    """ exists """

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_accept_01():
    out = getoutput('{} AYG'.format(prg))
    expected = """
pattern = "AYG"
regex   = "^A[CT]G$"
ACG OK
ATG OK
    """.strip()
    assert out.strip() == expected

# --------------------------------------------------
def test_accept_02():
    out = getoutput('{} MRY'.format(prg))
    expected = """
pattern = "MRY"
regex   = "^[AC][AG][CT]$"
AAC OK
AAT OK
AGC OK
AGT OK
CAC OK
CAT OK
CGC OK
CGT OK
    """.strip()
    assert out.strip() == expected
