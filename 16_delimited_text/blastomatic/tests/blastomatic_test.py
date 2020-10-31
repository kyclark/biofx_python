""" Tests for blastomatic.py """

import csv
import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

PRG = './blastomatic.py'
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

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(PRG, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input() -> None:
    """ Dies on bad input """

    bad = random_filename()
    rv1, out1 = getstatusoutput(f'{PRG} -a {bad} {HITS1}')
    assert rv1 != 0
    assert re.search(f"No such file or directory: '{bad}'", out1)

    rv2, out2 = getstatusoutput(f'{PRG} {bad} -a {CENTROIDS}')
    assert rv2 != 0
    assert re.search(f"No such file or directory: '{bad}'", out2)


# --------------------------------------------------
def test_good_input1() -> None:
    """ Works on good input """

    err = random_filename()
    if os.path.isfile(err):
        os.remove(err)

    try:
        print('{} --annotations {} {} 2>{}'.format(PRG, CENTROIDS, HITS1, err))
        rv1, out1 = getstatusoutput('{} --annotations {} {} 2>{}'.format(
            PRG, CENTROIDS, HITS1, err))
        assert rv1 == 0
        assert len(out1.split('\n')) == 28

        err_lines = open(err).readlines()
        assert len(err_lines) == 223
    finally:
        if os.path.isfile(err):
            os.remove(err)


# --------------------------------------------------
def test_good_input2() -> None:
    """ Works on good input """

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv1, out1 = getstatusoutput('{} -a {} --outfile {} {}'.format(
            PRG, CENTROIDS, out_file, HITS2))
        assert rv1 == 0
        assert len(out1.split('\n')) == 225

        out_lines = open(out_file).readlines()
        assert len(out_lines) == 26

        with open(out_file) as fh:
            reader = csv.DictReader(fh, delimiter='\t')
            assert reader.fieldnames == [
                'seq_id', 'pident', 'genus', 'species'
            ]

            for row in reader:
                if row['seq_id'] == '26cbd1b8b6fcd255774f4f79be2f259c':
                    assert row['pident'] == '98.701'
                    assert row['genus'] == 'Prochlorococcus MIT9313'
                    assert row['species'] == 'NA'
                    break

        # out_contents = open(out_file, 'rb').read()
        # md5_sum = hashlib.md5(out_contents).hexdigest()
        # assert md5_sum == '333544d443be7724a6c1d3ee9e59f799'
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def random_filename() -> str:
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
