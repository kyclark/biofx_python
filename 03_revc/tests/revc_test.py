#!/usr/bin/env python3
""" Tests for revc.py """

from subprocess import getstatusoutput
import platform
import os
import re

PRG = './revc.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
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
        rv, out = getstatusoutput(f'{RUN} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_no_args() -> None:
    """ Dies on no args """

    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_uppercase() -> None:
    """ Runs on uppercase input """

    rv, out = getstatusoutput(f'{RUN} AAAACCCGGT')
    assert rv == 0
    assert out == 'ACCGGGTTTT'


# --------------------------------------------------
def test_lowercase() -> None:
    """ Runs on lowercase input """

    rv, out = getstatusoutput(f'{RUN} aaaaCCCGGT')
    assert rv == 0
    assert out == 'ACCGGGtttt'


# --------------------------------------------------
def test_input1() -> None:
    """ Runs on file input """

    file, expected = TEST1
    rv, out = getstatusoutput(f'{RUN} {file}')
    assert rv == 0
    assert out == open(expected).read().rstrip()


# --------------------------------------------------
def test_input2() -> None:
    """ Runs on file input """

    file, expected = TEST2
    rv, out = getstatusoutput(f'{RUN} {file}')
    assert rv == 0
    assert out == open(expected).read().rstrip()
