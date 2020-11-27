""" Tests for fastx_grep.py """

import os
import platform
import random
import string
import re
from subprocess import getstatusoutput

PRG = './fastx_grep.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY = './tests/inputs/empty.fa'
LSU = './tests/inputs/lsu.fq'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_file() -> None:
    """ Dies on bad file """

    pattern = random_string()
    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {pattern} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# # --------------------------------------------------
# def run(input_file: str, expected_file: str) -> None:
#     """ Runs on command-line input """

#     expected = open(expected_file).read().rstrip()
#     rv, out = getstatusoutput(f'{RUN} {input_file}')
#     assert rv == 0
#     assert out == expected


# # --------------------------------------------------
# def test_empty_file() -> None:
#     """ Handles empty file """

#     run(*EMPTY)

# # --------------------------------------------------
# def test_input1() -> None:
#     """ Runs on command-line input """

#     run(*TEST1)


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
