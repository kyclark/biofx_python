""" Tests for mrna.py """

import os
from subprocess import getstatusoutput

PRG = './mrna.py'
INPUT1 = './tests/inputs/1.txt'
INPUT2 = './tests/inputs/2.txt'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Usage """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_ok1():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} MA')
    assert rv == 0
    assert out.rstrip() == '12'


# --------------------------------------------------
def test_ok2():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} {INPUT1}')
    assert rv == 0
    assert out.rstrip() == '448832'


# --------------------------------------------------
def test_ok3():
    """ OK """

    rv, out = getstatusoutput(f'{PRG} {INPUT2}')
    assert rv == 0
    assert out.rstrip() == '415872'
