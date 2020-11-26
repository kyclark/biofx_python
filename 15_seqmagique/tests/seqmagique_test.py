""" Tests for seqmagique.py """

import os
import platform
import random
import string
import re
from subprocess import getstatusoutput, getoutput

PRG = './seqmagique.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY = ('./tests/inputs/empty.fa', './tests/inputs/empty.fa.out')
TEST1 = ('./tests/inputs/1.fa', './tests/inputs/1.fa.out')
TEST2 = ('./tests/inputs/2.fa', './tests/inputs/2.fa.out')
ALL = ('./tests/inputs/*.fa', './tests/inputs/all.fa.out')


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{RUN} {flag}')
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
def run(input_file: str, expected_file: str) -> None:
    """ Runs on command-line input """

    expected = open(expected_file).read().rstrip()
    rv, out = getstatusoutput(f'{RUN} {input_file}')
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_empty_file() -> None:
    """ Handles empty file """

    run(*EMPTY)


# --------------------------------------------------
def test_input1() -> None:
    """ Runs on command-line input """

    run(*TEST1)


# --------------------------------------------------
def test_input2() -> None:
    """ Runs on command-line input """

    run(*TEST2)


# --------------------------------------------------
def test_input_all() -> None:
    """ Runs on command-line input """

    run(*ALL)


# --------------------------------------------------
def test_styles() -> None:
    """ Test table styles """

    styles = [
        'plain', 'simple', 'grid', 'pipe', 'orgtbl', 'rst', 'mediawiki',
        'latex', 'latex_raw', 'latex_booktabs'
    ]

    for file in [TEST1[0], TEST2[0]]:
        for style in styles:
            expected_file = file + '.' + style + '.out'
            assert os.path.isfile(expected_file)
            expected = open(expected_file).read().rstrip()
            flag = '--tablefmt' if random.choice([0, 1]) else '-t'
            rv, out = getstatusoutput(f'{RUN} {flag} {style} {file}')
            assert rv == 0
            assert out == expected


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
