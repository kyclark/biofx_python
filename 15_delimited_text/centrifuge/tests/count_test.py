""" Tests for counts_by_tax.py """

import os
from subprocess import getstatusoutput

PRG = './counts_by_tax.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(PRG, flag))
        assert rv == 0
        assert out.lower().startswith('usage:')
