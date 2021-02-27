""" Tests for revp.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput

PRG = './revp.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
INPUT1 = './tests/inputs/1.fa'
INPUT2 = './tests/inputs/2.fa'
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
def run(file: str) -> None:
    """ Run the test """

    expected_file = file + '.out'
    assert os.path.isfile(expected_file)

    rv, out = getstatusoutput(f'{RUN} {file}')
    assert rv == 0

    expected = set(open(expected_file).read().splitlines())
    assert set(out.splitlines()) == expected


# --------------------------------------------------
def test_ok1() -> None:
    """ Runs ok """

    run(INPUT1)


# --------------------------------------------------
def test_ok2() -> None:
    """ Runs ok """

    run(INPUT2)


# --------------------------------------------------
def test_mepty() -> None:
    """ Runs ok """

    run(EMPTY)


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
