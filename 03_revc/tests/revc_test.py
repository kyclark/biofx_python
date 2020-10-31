#!/usr/bin/env python3
""" Tests for revc.py """

from subprocess import getstatusoutput
import os
import re

PRG = './revc.py'
TEST1 = ('./tests/inputs/input1.txt', './tests/inputs/output1.txt')
TEST2 = ('./tests/inputs/input2.txt', './tests/inputs/output2.txt')


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage """

    for arg in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_no_args() -> None:
    """ Dies on no args """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_uppercase() -> None:
    """ Runs on uppercase input """

    rv, out = getstatusoutput(f'{PRG} AAAACCCGGT')
    assert rv == 0
    assert out == 'ACCGGGTTTT'


# --------------------------------------------------
def test_lowercase() -> None:
    """ Runs on lowercase input """

    rv, out = getstatusoutput(f'{PRG} aaaaCCCGGT')
    assert rv == 0
    assert out == 'ACCGGGtttt'


# --------------------------------------------------
def test_input1() -> None:
    """ Runs on file input """

    file, expected = TEST1
    rv, out = getstatusoutput(f'{PRG} {file}')
    assert rv == 0
    assert out == open(expected).read().rstrip()


# --------------------------------------------------
def test_input2() -> None:
    """ Runs on file input """

    file, expected = TEST2
    rv, out = getstatusoutput(f'{PRG} {file}')
    assert rv == 0
    assert out == open(expected).read().rstrip()
