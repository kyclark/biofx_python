""" Tests for prot.py """

from subprocess import getstatusoutput, getoutput
import os

PRG = './prot.py'
TEST1 = ('./tests/inputs/input1.txt', './tests/inputs/input1.txt.out')


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Usage """

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{PRG} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_input1():
    """ Runs on command-line input """

    rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    rv, out = getstatusoutput(f'{PRG} {rna}')
    assert rv == 0
    assert out == 'MAMAPRTEINSTRING'


# --------------------------------------------------
def test_input2():
    """ Runs on file input """

    file, expected = TEST1
    rna = open(file).read().rstrip()
    rv, out = getstatusoutput(f'{PRG} {rna}')
    assert rv == 0
    assert out.rstrip() == open(expected).read().rstrip()
