#!/usr/bin/env python3
"""tests for yeast/Makefile exercise"""

import os
import re
from subprocess import getstatusoutput


# --------------------------------------------------
def test_files():
    """files exist, have correct answers"""

    files = [('chr-count', '16'), ('chr-size', '12359733'),
             ('gene-count', '6604'), ('verified-genes', '5155'),
             ('uncharacterized-genes', '728')]

    for file, answer in files:
        assert os.path.isfile(file)
        contents = open(file).read().strip()
        assert contents == answer


# --------------------------------------------------
def test_terminated_genes():
    """terminated-genes"""

    file = 'terminated-genes'
    assert os.path.isfile(file)
    lines = open(file).readlines()
    assert len(lines) == 951


# --------------------------------------------------
def test_gene_types():
    """gene-types"""

    file = 'gene-types'
    assert os.path.isfile(file)

    expected = {
        'Dubious': '717',
        'Uncharacterized': '728',
        'Verified': '5155',
        'Verified|silenced_gene': '4',
        'silenced_gene': '2',
    }

    regex = re.compile(r'^\s*(\d+)\s(.+)$')
    for line in open(file):
        match = regex.search(line)
        if match:
            num, gene_type = match.groups()
            if gene_type in expected:
                assert num == expected[gene_type]
