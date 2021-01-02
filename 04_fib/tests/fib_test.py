""" Tests for fib.py """

import os
import platform
import random
import re
from subprocess import getstatusoutput

PRG = './fib.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    for arg in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {arg}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_generations() -> None:
    """ Dies when generations is bad """

    n = random.choice(list(range(-10, 0)) + list(range(41, 50)))
    k = random.randint(1, 5)
    rv, out = getstatusoutput(f'{RUN} {n} {k}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f'generations "{n}" must be between 1 and 40', out)


# --------------------------------------------------
def test_bad_litter() -> None:
    """ Dies when litter size is bad """

    n = random.randint(1, 40)
    k = random.choice(list(range(-10, 0)) + list(range(6, 20)))
    rv, out = getstatusoutput(f'{RUN} {n} {k}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f'litter "{k}" must be between 1 and 5', out)


# --------------------------------------------------
def test_1() -> None:
    """runs on good input"""

    rv, out = getstatusoutput(f'{RUN} 5 3')
    assert rv == 0
    assert out == '19'


# --------------------------------------------------
def test_2() -> None:
    """runs on good input"""

    rv, out = getstatusoutput(f'{RUN} 30 4')
    assert rv == 0
    assert out == '436390025825'


# --------------------------------------------------
def test_3() -> None:
    """runs on good input"""

    rv, out = getstatusoutput(f'{RUN} 29 2')
    assert rv == 0
    assert out == '178956971'
