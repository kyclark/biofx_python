""" Tests for synth.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from typing import Optional, List

PRG = './synth.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
SAMPLE1 = './tests/inputs/CAM_SMPL_GS108.fa'
SAMPLE2 = './tests/inputs/CAM_SMPL_GS112.fa'
SAMPLE3 = './tests/inputs/lsu.fq'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_seed():
    """ not int for seed """

    bad = random_string()
    opt = random.choice(['-s', '--seed'])
    rv, out = getstatusoutput(f'{RUN} {opt} {bad} ./tests/inputs/*')
    assert rv != 0
    assert re.search(f"invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_format():
    """ Dies on bad file format """

    bad = random_string()
    opt = random.choice(['-f', '--format'])
    rv, out = getstatusoutput(f'{RUN} {opt} {bad} ./tests/inputs/*')
    assert rv != 0
    assert re.search(f"argument -f/--format: invalid choice: '{bad}'", out)


# --------------------------------------------------
def run(input_files: List[str],
        outfile: str,
        expected_file: str,
        opts: Optional[List[str]] = None) -> None:
    """ Runs on command-line input """

    assert all(map(os.path.isfile, input_files))
    assert os.path.isfile(expected_file)

    if os.path.isfile(outfile):
        os.remove(outfile)

    try:
        expected = open(expected_file).read().rstrip()
        options = ' '.join(opts) if opts else ''
        cmd = f"{RUN} {options} {' '.join(input_files)}"
        rv, _ = getstatusoutput(cmd)

        assert rv == 0
        assert os.path.isfile(outfile)
        assert open(outfile).read().strip() == expected

    finally:
        if os.path.isfile(outfile):
            os.remove(outfile)


# --------------------------------------------------
def test_sample1_num1() -> None:
    """ test """

    run([SAMPLE1], 'out.fa', SAMPLE1 + '.n1.out', ['-s 1', '-n 1'])


# --------------------------------------------------
def test_sample1_num1_outfile() -> None:
    """ test """

    filename = random_string()
    run([SAMPLE1], filename, SAMPLE1 + '.n1.out',
        ['-s 1', '-n 1', f'-o {filename}'])


# --------------------------------------------------
def test_sample1_num1_min20_max40() -> None:
    """ test """

    run([SAMPLE1], 'out.fa', SAMPLE1 + '.n1.m20.x40.out',
        ['-s 1', '-n 1', '-m 20', '-x 40'])


# --------------------------------------------------
def test_sample1_num1_kmer4() -> None:
    """ test """

    run([SAMPLE1], 'out.fa', SAMPLE1 + '.n1.k4.out', ['-s 1', '-n 1', '-k 4'])


# --------------------------------------------------
def test_sample1_num1_kmer5() -> None:
    """ test """

    run([SAMPLE1], 'out.fa', SAMPLE1 + '.n1.k5.out', ['-s 1', '-n 1', '-k 5'])


# --------------------------------------------------
def test_sample3_num1_format() -> None:
    """ test """

    run([SAMPLE3], 'out.fa', SAMPLE3 + '.n1.out', ['-s 1', '-n 1', '-f fastq'])


# --------------------------------------------------
def test_sample1_defaults() -> None:
    """ test """

    run([SAMPLE1], 'out.fa', SAMPLE1 + '.default.out', ['-s 1'])


# --------------------------------------------------
def test_multiple_inputs() -> None:
    """ test """

    run([SAMPLE1, SAMPLE2], 'out.fa', './tests/inputs/mult.n10.out',
        ['-s 1', '-n 10'])


# --------------------------------------------------
def random_string():
    """generate a random string"""

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
