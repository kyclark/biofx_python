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
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Usage """

    rv, out = getstatusoutput(PRG)
    assert rv > 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_k():
    """ Dies on bad k """

    k = random.choice(range(-10, 1))
    rv, out = getstatusoutput(f'{PRG} -k {k} {SAMPLE1}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f'-k "{k}" must be > 0', out)


# --------------------------------------------------
def test_bad_file():
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput('{} {}'.format(PRG, bad))
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run_it(in_file, k):
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

    run_it(SAMPLE1, 3)


# --------------------------------------------------
def test_02():
    """ Runs OK """

    run_it(SAMPLE1, 4)


# --------------------------------------------------
def test_03():
    """ Runs OK """
    run_it(SAMPLE1, 5)


# --------------------------------------------------
def test_04():
    """ Runs OK """
    run_it(SAMPLE2, 3)


# --------------------------------------------------
def test_05():
    """ Runs OK """
    run_it(SAMPLE2, 4)


# --------------------------------------------------
def test_06():
    """ Runs OK """
    run_it(SAMPLE2, 5)


# --------------------------------------------------
def test_07():
    """ Runs OK """
    run_it(SAMPLE3, 3)


# --------------------------------------------------
def test_08():
    """ Runs OK """
    run_it(SAMPLE3, 4)


# --------------------------------------------------
def test_09():
    """ Runs OK """
    run_it(SAMPLE3, 5)


# --------------------------------------------------
def random_string():
    """Generate a random string"""

    return ''.join(
        random.sample(string.ascii_letters + string.digits,
                      k=random.randint(5, 10)))
