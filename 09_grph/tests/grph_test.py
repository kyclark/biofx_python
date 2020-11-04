""" Tests for grph.py """

from subprocess import getstatusoutput
import os
import random
import re
import string

PRG = './grph.py'
SAMPLE1 = './tests/inputs/1.fa'
SAMPLE2 = './tests/inputs/2.fa'
SAMPLE3 = './tests/inputs/3.fa'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    rv, out = getstatusoutput(PRG)
    assert rv > 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_k() -> None:
    """ Dies on bad k """

    k = random.choice(range(-10, 1))
    rv, out = getstatusoutput(f'{PRG} -k {k} {SAMPLE1}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f'-k "{k}" must be > 0', out)


# --------------------------------------------------
def test_bad_file() -> None:
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput('{} {}'.format(PRG, bad))
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(in_file: str, k: int) -> None:
    """ Run with args """

    out_file = '.'.join([in_file, str(k), 'out'])
    assert os.path.isfile(out_file)

    expected = open(out_file).read().rstrip()
    cmd = '{} -k {} {} | sort'.format(PRG, k, in_file)
    rv, out = getstatusoutput(cmd)
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_01():
    """ Runs OK """

    run(SAMPLE1, 3)


# --------------------------------------------------
def test_02() -> None:
    """ Runs OK """

    run(SAMPLE1, 4)


# --------------------------------------------------
def test_03() -> None:
    """ Runs OK """

    run(SAMPLE1, 5)


# --------------------------------------------------
def test_04() -> None:
    """ Runs OK """

    run(SAMPLE2, 3)


# --------------------------------------------------
def test_05() -> None:
    """ Runs OK """

    run(SAMPLE2, 4)


# --------------------------------------------------
def test_06() -> None:
    """ Runs OK """

    run(SAMPLE2, 5)


# --------------------------------------------------
def test_07() -> None:
    """ Runs OK """

    run(SAMPLE3, 3)


# --------------------------------------------------
def test_08() -> None:
    """ Runs OK """

    run(SAMPLE3, 4)


# --------------------------------------------------
def test_09() -> None:
    """ Runs OK """

    run(SAMPLE3, 5)


# --------------------------------------------------
def random_string() -> str:
    """Generate a random string"""

    return ''.join(
        random.sample(string.ascii_letters + string.digits,
                      k=random.randint(5, 10)))
