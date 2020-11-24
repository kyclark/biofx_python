""" Tests for mprt.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput

PRG = './mprt.py'
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
def test_bad_file() -> None:
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(file: str) -> None:
    """ Run test """

    expected_file = file + '.out'
    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f'{RUN} {file}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_1() -> None:
    """ Input 1 """

    run(INPUT1)


# --------------------------------------------------
def test_2() -> None:
    """ Input 2 """

    run(INPUT2)


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
