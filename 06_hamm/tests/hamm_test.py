#!/usr/bin/env python3
""" Tests for hamm.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput

PRG = './hamm.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY = './tests/inputs/empty.txt'
INPUT1 = './tests/inputs/1.txt'
INPUT2 = './tests/inputs/2.txt'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file() -> None:
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(file: str, expected: str) -> None:
    """ Run with input """

    rv, out = getstatusoutput(f'{RUN} {file}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_input1() -> None:
    """ Test with input1 """

    run(INPUT1, '7')


# --------------------------------------------------
def test_input2() -> None:
    """ Test with input2 """

    run(INPUT2, '503')


# --------------------------------------------------
def test_empty_file() -> None:
    """ Empty file """

    rv, out = getstatusoutput(f'{RUN} {EMPTY}')
    assert rv != 0
    assert re.search(f'Input file "{EMPTY}" must have two lines.', out)


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
