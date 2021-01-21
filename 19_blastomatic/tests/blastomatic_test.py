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

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} --annotations {bad} -b {HITS1}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_input_file() -> None:
    """ Dies on bad input file """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} --blasthits {bad} -a {CENTROIDS}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input() -> None:
    """ Works on good input """

    outfile = 'out.csv'
    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        cmd = f'{RUN} -a {CENTROIDS} -b {HITS1}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == 'Exported 27 to "out.csv".'
        assert os.path.isfile(outfile)

        reader = csv.DictReader(open(outfile), delimiter=',')
        records = list(reader)
        assert len(records) == 27
        assert records[0]['sseqid'] == 'bfb6f5dfb4d0ef0842be8f5df6c86459'
        assert records[-1]['sseqid'] == 'a0952bd2b994a100c0a28a35735cec6b'
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def test_delimiter() -> None:
    """ Specify delimiter """

    outfile = 'out.xxx'
    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        delim = ',' if random.choice([0, 1]) else '\t'
        cmd = f'{RUN} -a {CENTROIDS} -b {HITS1} -d "{delim}" -o {outfile}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == f'Exported 27 to "{outfile}".'
        assert os.path.isfile(outfile)

        reader = csv.DictReader(open(outfile), delimiter=delim)
        records = list(reader)
        assert len(records) == 27
        assert records[0]['sseqid'] == 'bfb6f5dfb4d0ef0842be8f5df6c86459'
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def test_guess_delimiter() -> None:
    """ Guess delimiter """

    tsv_ext = random.choice(['.txt', '.tab', '.tsv'])
    outfile, delim = ('out.csv',
                      ',') if random.choice([0, 1]) else ('out' + tsv_ext,
                                                          '\t')

    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        cmd = f'{RUN} -a {CENTROIDS} -b {HITS2} -o {outfile}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == f'Exported 25 to "{outfile}".'
        assert os.path.isfile(outfile)

        reader = csv.DictReader(open(outfile), delimiter=delim)
        records = list(reader)
        assert len(records) == 25
        assert records[-1]['sseqid'] == '5837cb753f931e6ee8a71937388191fa'
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def test_pctid() -> None:
    """ Filter on percent ID """

    outfile = 'out.tsv'
    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        cmd = f'{RUN} -a {CENTROIDS} -b {HITS2} -p 90 -o {outfile}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out == f'Exported 13 to "{outfile}".'
        assert os.path.isfile(outfile)

        reader = csv.DictReader(open(outfile), delimiter='\t')
        records = list(reader)
        assert len(records) == 13
        assert records[-1]['sseqid'] == 'af77fb5cb5645320672c23f6059fe455'
    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
