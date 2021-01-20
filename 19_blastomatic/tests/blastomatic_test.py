""" Tests for blastomatic.py """

import csv
import os
import platform
import random
import re
import string
from subprocess import getstatusoutput

PRG = './blastomatic.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
HITS1 = './tests/inputs/hits1.tab'
HITS2 = './tests/inputs/hits2.tab'
CENTROIDS = './tests/inputs/centroids.csv'


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
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_annotations() -> None:
    """ Dies on bad annotations file """

    bad = random_filename()
    rv, out = getstatusoutput(f'{RUN} -a {bad} {HITS1}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_input_file() -> None:
    """ Dies on bad input file """

    bad = random_filename()
    rv, out = getstatusoutput(f'{RUN} {bad} -a {CENTROIDS}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input() -> None:
    """ Works on good input """

    err = random_filename()
    if os.path.isfile(err):
        os.remove(err)

    try:
        annots_flag = '--annotations' if random.choice([0, 1]) else '-a'
        cmd = f'{RUN} {annots_flag} {CENTROIDS} {HITS1} 2>{err}'
        print(cmd)
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert len(out.split('\n')) == 28

        err_lines = open(err).readlines()
        assert len(err_lines) == 223
    finally:
        if os.path.isfile(err):
            os.remove(err)


# --------------------------------------------------
def test_outfile_delimiter_quiet() -> None:
    """ Works on good input """

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        quiet_flag = '--quiet' if random.choice([0, 1]) else '-q'
        delim_flag = '--delimiter' if random.choice([0, 1]) else '-d'
        delim = ',' if random.choice([0, 1]) else ':'
        out_flag = '--outfile' if random.choice([0, 1]) else '-o'
        cmd = (f'{RUN} -a {CENTROIDS} {HITS2} {out_flag} {out_file} '
               f'{quiet_flag} {delim_flag} "{delim}"')
        print(cmd)

        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == ''

        out_lines = open(out_file).readlines()
        assert len(out_lines) == 26

        with open(out_file) as fh:
            reader = csv.DictReader(fh, delimiter=delim)
            assert reader.fieldnames == [
                'seq_id', 'pident', 'genus', 'species'
            ]

            for row in reader:
                if row['seq_id'] == '26cbd1b8b6fcd255774f4f79be2f259c':
                    assert row['pident'] == '98.701'
                    assert row['genus'] == 'Prochlorococcus MIT9313'
                    assert row['species'] == 'NA'
                    break
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# # --------------------------------------------------
# def test_delimiter() -> None:
#     """ Uses output delimiter """

#     err = random_filename()
#     if os.path.isfile(err):
#         os.remove(err)

#     try:
#         cmd = f'{PRG} --annotations {CENTROIDS} {HITS1} 2>{err}'
#         rv, out = getstatusoutput(cmd)
#         assert rv == 0
#         assert len(out.split('\n')) == 28
#     finally:
#         if os.path.isfile(err):
#             os.remove(err)


# --------------------------------------------------
def random_filename() -> str:
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
