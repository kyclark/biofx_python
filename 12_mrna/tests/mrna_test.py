""" Tests for mrna.py """

import os
import platform
from subprocess import getstatusoutput

PRG = './mrna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
INPUT1 = './tests/inputs/1.txt'
INPUT2 = './tests/inputs/2.txt'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_ok1() -> None:
    """ OK """

    rv, out = getstatusoutput(f'{RUN} MA')
    assert rv == 0
    assert out.rstrip() == '12'


# --------------------------------------------------
def test_ok2() -> None:
    """ OK """

    rv, out = getstatusoutput(f'{RUN} {INPUT1}')
    assert rv == 0
    assert out.rstrip() == '448832'


# --------------------------------------------------
def test_ok3() -> None:
    """ OK """

    rv, out = getstatusoutput(f'{RUN} {INPUT2}')
    assert rv == 0
    assert out.rstrip() == '415872'
