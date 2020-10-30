""" Tests for revp.py """

import os
from subprocess import getstatusoutput

PRG = './revp.py'
INPUT1 = './tests/inputs/1.fa'
INPUT2 = './tests/inputs/2.fa'


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
    """ Runs ok """

    rv, out = getstatusoutput(f'{PRG} {INPUT1}')
    assert rv == 0
    expected = set(
        ['4 6', '5 4', '6 6', '7 4', '17 4', '18 4', '20 6', '21 4'])
    assert set(out.splitlines()) == expected


# --------------------------------------------------
def test_ok2():
    """ Runs ok """

    expected_file = INPUT2 + '.out'
    assert os.path.isfile(expected_file)

    rv, out = getstatusoutput(f'{PRG} {INPUT2}')
    assert rv == 0

    expected = set(open(expected_file).read().splitlines())
    assert set(out.splitlines()) == expected
