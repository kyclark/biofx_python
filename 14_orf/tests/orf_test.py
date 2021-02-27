""" Tests for orf.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput

PRG = './orf.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
INPUT1 = './tests/inputs/1.fa'
INPUT2 = './tests/inputs/2.fa'
INPUT3 = './tests/inputs/3.fa'
EMPTY = './tests/inputs/empty.fa'


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
def test_bad_file() -> None:
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty_file() -> None:
    """ Prints nothing on empty file """

    rv, out = getstatusoutput(f'{RUN} {EMPTY}')
    assert rv == 0
    assert out.strip() == ''


# --------------------------------------------------
def run(file: str) -> None:
    """ Run with inputs """

    expected_file = file + '.out'
    assert os.path.isfile(expected_file)
    expected = set(open(expected_file).read().splitlines())
    rv, out = getstatusoutput(f'{RUN} {file}')
    assert rv == 0
    assert set(out.splitlines()) == expected


# --------------------------------------------------
def test_ok1() -> None:
    """ OK """

    run(INPUT1)


# --------------------------------------------------
def test_ok2() -> None:
    """ OK """

    run(INPUT2)


# --------------------------------------------------
def test_ok3() -> None:
    """ OK """

    run(INPUT3)


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
