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
def run(file: str, expected: str) -> None:
    """ Run test """

    rv, out = getstatusoutput(f'{RUN} {file}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_1() -> None:
    """ Input 1 """

    expected = '\n'.join([
        'B5ZC00',
        '85 118 142 306 395',
        'P07204_TRBM_HUMAN',
        '47 115 116 382 409',
        'P20840_SAG1_YEAST',
        '79 109 135 248 306 348 364 402 485 501 614',
    ])
    run(INPUT1, expected)


# --------------------------------------------------
def test_2() -> None:
    """ Input 2 """

    expected = """
P13473_LMP2_HUMAN
32 38 49 58 75 101 123 179 229 242 257 275 300 307 317 356
P42098_ZP3_PIG
124 146 179 271
P80069_A45K_MYCBO
7 161
Q13VE3
95
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
P01042_KNH_HUMAN
48 169 205 294
P07204_TRBM_HUMAN
47 115 116 382 409
Q7S432
173
A3DF24
178
P07585_PGS2_HUMAN
211 262 303
Q9QSP4
196 250 326 443
    """.strip()
    run(INPUT2, expected)


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
