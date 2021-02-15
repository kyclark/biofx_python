""" Tests for mrna.py """

import os
import platform
from subprocess import getstatusoutput

PRG = './mrna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
TEST1 = ('MA', '12')
TEST2 = ('./tests/inputs/1.txt', '448832')
TEST3 = ('./tests/inputs/2.txt', '415872')
TEST4 = ('./tests/inputs/3.txt', '283264')


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
def run(protein: str, expected: str) -> None:
    """ Run test """

    rv, out = getstatusoutput(f'{RUN} {protein}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_01() -> None:
    """ OK """

    run(*TEST1)


# --------------------------------------------------
def test_02() -> None:
    """ OK """

    run(*TEST2)


# --------------------------------------------------
def test_03() -> None:
    """ OK """

    run(*TEST3)


# --------------------------------------------------
def test_04() -> None:
    """ OK """

    run(*TEST4)
