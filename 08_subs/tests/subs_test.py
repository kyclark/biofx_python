#!/usr/bin/env python3
""" Tests for subs.py """

from subprocess import getstatusoutput
import os

PRG = './subs.py'
TEST1 = ('./tests/inputs/input1.txt', './tests/inputs/input1.txt.out')


# --------------------------------------------------
def test_exists():
    """usage"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for arg in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_input1():
    """ Runs on command-line input """

    rv, out = getstatusoutput(f'{PRG} GATATATGCATATACTT ATAT')
    assert rv == 0
    assert out == '2 4 10'


# --------------------------------------------------
def test_input2():
    """ Runs on file input """

    file, expected = TEST1
    seq, sub = open(file).read().split()
    rv, out = getstatusoutput(f'{PRG} {seq} {sub}')
    assert rv == 0
    assert out.rstrip() == open(expected).read().rstrip()
