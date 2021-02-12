""" Tests for fastx_grep.py """

import os
import platform
import random
import string
import re
from subprocess import getstatusoutput
from typing import Optional, List

PRG = './fastx_grep.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
EMPTY = './tests/inputs/empty.fa'
LSU = './tests/inputs/lsu.fq'
LSU_FA = './tests/inputs/lsu.fa'
BAD_EXT = './tests/inputs/lsu.fx'


# --------------------------------------------------
def test_exists() -> None:
    """exists"""

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
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


# --------------------------------------------------
def test_cannot_guess() -> None:
    """ Dies on unguessable extension """

    pattern = random_string()
    rv, out = getstatusoutput(f'{RUN} {pattern} {BAD_EXT}')
    assert rv != 0
    assert re.search(f'Please specify file format for "{BAD_EXT}"', out)


# --------------------------------------------------
def test_out_file() -> None:
    """ out_file """

    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        flag = '-o' if random.choice([0, 1]) else '--outfile'
        rv, _ = getstatusoutput(f'{RUN} {flag} {out_file} LSU {LSU}')
        assert rv == 0
        assert os.path.isfile(out_file)
        expected = open(LSU + '.upper.out').read().rstrip()
        assert open(out_file).read().rstrip() == expected

    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def run(pattern: str,
        input_file: str,
        expected_file: str,
        opts: Optional[List[str]] = None) -> None:
    """ Runs on command-line input """

    assert os.path.isfile(expected_file)
    expected = open(expected_file).read().rstrip()

    out_file = random_string()
    if os.path.isfile(out_file):
        os.remove(out_file)

    try:
        options = ' '.join(opts) if opts else ''
        cmd = f"{RUN} {options} {pattern} -o {out_file} {input_file}"
        rv, _ = getstatusoutput(cmd)

        assert os.path.isfile(out_file)
        assert rv == 0
        assert open(out_file).read().rstrip() == expected
    finally:
        if os.path.isfile(out_file):
            os.remove(out_file)


# --------------------------------------------------
def test_empty_file() -> None:
    """ Handles empty file """

    pattern = random_string()
    run(pattern, EMPTY, EMPTY + '.out')


# --------------------------------------------------
def test_lsu_uppercase() -> None:
    """ LSU """

    run('LSU', LSU, LSU + '.upper.out')


# --------------------------------------------------
def test_lsu_lowercase() -> None:
    """ lsu """

    run('lsu', LSU, LSU + '.lower.out')


# --------------------------------------------------
def test_lsu_uppercase_insensitive() -> None:
    """ -i LSU """

    run('LSU', LSU, LSU + '.i.upper.out', ['-i'])


# --------------------------------------------------
def test_lsu_lowercase_insensitive() -> None:
    """ -i lsu """

    run('lsu', LSU, LSU + '.i.lower.out', ['--insensitive'])


# --------------------------------------------------
def test_outfmt_fastq_to_fasta() -> None:
    """ outfmt """

    flag = '-O' if random.choice([0, 1]) else '--outfmt'
    run('LSU', LSU, LSU + '.fa.out', [f'{flag} fasta'])


# --------------------------------------------------
def test_outfmt_fastq_to_fasta2line() -> None:
    """ outfmt """

    flag = '-O' if random.choice([0, 1]) else '--outfmt'
    run('LSU', LSU, LSU + '.2fa.out', [f'{flag} fasta-2line'])


# --------------------------------------------------
def random_string() -> str:
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
