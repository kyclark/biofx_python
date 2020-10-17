#!/usr/bin/env python3
""" Tests for hamm.py """

import os
import random
import re
import string
from subprocess import getstatusoutput

PRG = './hamm.py'
INPUT1 = './tests/inputs/1.txt'
INPUT2 = './tests/inputs/2.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """Bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(file, expected):
    """ Run with input """

    rv, out = getstatusoutput(f'{PRG} {file}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_input1():
    """ Test with input1 """

    run(INPUT1, '7')


# --------------------------------------------------
def test_input2():
    """ Test with input2 """

    run(INPUT2, '503')


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
