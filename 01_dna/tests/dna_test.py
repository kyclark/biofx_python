""" Tests for dna.py """

import os
import platform
from subprocess import getstatusoutput, getoutput

PRG = './dna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.exists(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage with no args or for help """

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{RUN} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_arg() -> None:
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        retval, out = getstatusoutput(f'{RUN} {dna}')
        assert retval == 0
        assert out == expected


# --------------------------------------------------
def test_file() -> None:
    """ Uses file arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        retval, out = getstatusoutput(f'{RUN} {file}')
        assert retval == 0
        assert out == expected
