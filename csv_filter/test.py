#!/usr/bin/env python3
"""tests for csvfilter.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput, getoutput

prg = './csvfilter.py'
titanic = './inputs/titanic.csv'
centroids = './inputs/centroids.tab'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """fails on bad file"""

    bad = random_filename()
    rv, out = getstatusoutput(f'{prg} -f {bad}')
    assert rv > 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_column():
    """works on good input"""

    bad = 'adult_males'
    rv, out = getstatusoutput(f'{prg} -c {bad} -v true --file {titanic}')
    assert rv != 0
    assert re.search(f'--col "{bad}" not a valid column!', out)


# --------------------------------------------------
def test_titanic_any_true():
    """works on good input"""

    out_file = 'out.csv'
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        rv, out = getstatusoutput(f'{prg} --val true --file {titanic}')
        assert rv == 0
        assert out.rstrip() == f'Done, wrote 664 to "{out_file}".'
        assert os.path.isfile(out_file)
        lines = open(out_file).readlines()
        assert len(lines) == 665

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_titanic_adult_male_true():
    """works on good input"""

    out_file = 'out.csv'
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        cmd = f'{prg} --col adult_male -v true -f {titanic}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out.rstrip() == f'Done, wrote 537 to "{out_file}".'
        assert os.path.isfile(out_file)
        lines = open(out_file).readlines()
        assert len(lines) == 538

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_centroids_any_bacteria():
    """works on good input"""

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        cmd = "{} -d $'\t' -o {} -v bacteria -f {}".format(
            prg, out_file, centroids)
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out.rstrip() == f'Done, wrote 493 to "{out_file}".'
        assert os.path.isfile(out_file)
        lines = open(out_file).readlines()
        assert len(lines) == 494

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_centroids_class_bacteria():
    """works on good input"""

    out_file = random_filename()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        tmpl = ("{} --delimiter $'\t' --outfile {} "
                '--col class --val bacteria --file {}')
        cmd = tmpl.format(prg, out_file, centroids)
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        assert out.rstrip() == f'Done, wrote 50 to "{out_file}".'
        assert os.path.isfile(out_file)
        lines = open(out_file).readlines()
        assert len(lines) == 51

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
