""" Tests for lcsm.py """

import os
import random
import re
import string
from subprocess import getstatusoutput

PRG = './lcsm.py'
INPUT1 = './tests/inputs/1.fa'
INPUT2 = './tests/inputs/2.fa'
NO_SHARED = './tests/inputs/none.fa'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage """

    rv, out = getstatusoutput(PRG)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_file() -> None:
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{PRG} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_short() -> None:
    """ Runs OK """

    rv, out = getstatusoutput(f'{PRG} {INPUT1}')
    assert rv == 0
    assert out in ['AC', 'CA', 'TA']


# --------------------------------------------------
def test_long() -> None:
    """ Runs OK """

    rv, out = getstatusoutput(f'{PRG} {INPUT2}')
    assert rv == 0
    expected = ('GCCTTTTGATTTTAACGTTTATCGGGTGTAGTAAGATTGCGCGC'
                'TAATTCCAATAAACGTATGGAGGACATTCCCCGT')
    assert out == expected


# --------------------------------------------------
def test_no_shared() -> None:
    """ Correctly reports when no sequences are shared """

    rv, out = getstatusoutput(f'{PRG} {NO_SHARED}')
    assert rv == 0
    assert out == 'No common subsequence.'


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
