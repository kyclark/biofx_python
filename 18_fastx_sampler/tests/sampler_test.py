""" Tests for sampler.py """

import os
import platform
import random
import re
import string
from subprocess import getstatusoutput
from Bio import SeqIO
from shutil import rmtree

PRG = './sampler.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
N1K = './tests/inputs/n1k.fa'
N10K = './tests/inputs/n10k.fa'
N100K = './tests/inputs/n100k.fa'
FASTQ = '../16_fastx_grep/tests/inputs/lsu.fq'


# --------------------------------------------------
def test_exists():
    """ All the necessary files exist """

    for file in [PRG, N1K, N10K, N100K]:
        assert os.path.isfile(file)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{RUN} {flag}')
        assert rv == 0
        assert re.match('usage:', out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_file():
    """ Dies on bad file """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} {bad}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_bad_pct():
    """ Dies on bad percent """

    bad = random.randint(1, 10)
    rv, out = getstatusoutput(f'{RUN} -p {bad} {N1K}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f'--percent "{float(bad)}" must be between 0 and 1', out)


# --------------------------------------------------
def test_bad_seed():
    """ Dies on bad seed """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} -s {bad} {N1K}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    assert re.search(f"-s/--seed: invalid int value: '{bad}'", out)


# --------------------------------------------------
def test_bad_format():
    """ Dies on bad file format """

    bad = random_string()
    rv, out = getstatusoutput(f'{RUN} -f {bad} {N1K}')
    assert rv != 0
    assert re.match('usage:', out, re.I)
    err = (f"-f/--format: invalid choice: '{bad}' "
           r"\(choose from 'fasta', 'fastq'\)")
    assert re.search(err, out)


# --------------------------------------------------
def test_defaults_one_file():
    """ Runs on good input """

    out_dir = 'out'
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        rv, out = getstatusoutput(f'{RUN} -s 10 {N1K}')
        assert rv == 0
        expected = ('  1: n1k.fa\n'
                    'Wrote 108 sequences from 1 file to directory "out".')
        assert out == expected
        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 1

        out_file = os.path.join(out_dir, os.path.basename(N1K))
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(out_file, 'fasta'))
        assert len(seqs) == 108

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_fastq_input():
    """ FASTQ input """

    out_dir = 'out'
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        rv, out = getstatusoutput(f'{RUN} -s 1 -p .8 -f fastq {FASTQ}')
        assert rv == 0
        expected = ('  1: lsu.fq\n'
                    'Wrote 3 sequences from 1 file to directory "out".')
        assert out == expected
        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 1

        out_file = os.path.join(out_dir, os.path.basename(FASTQ))
        assert os.path.isfile(out_file)

        # correct number of seqs in FASTA format
        seqs = list(SeqIO.parse(out_file, 'fasta'))
        assert len(seqs) == 3

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_defaults_multiple_file():
    """ Runs on good input with many files """

    out_dir = random_string()
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        cmd = f'{RUN} -o {out_dir} -s 1 {N100K} {N10K} {N1K}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0
        status = '\n'.join([
            '  1: n100k.fa',
            '  2: n10k.fa',
            '  3: n1k.fa',
            f'Wrote 11,075 sequences from 3 files to directory "{out_dir}".',
        ])

        assert out == status
        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 3

        expected = [('n1k.fa', 106), ('n10k.fa', 995), ('n100k.fa', 9974)]
        for file, num in expected:
            path = os.path.join(out_dir, file)
            assert os.path.isfile(path)
            seqs = list(SeqIO.parse(path, 'fasta'))
            assert len(seqs) == num

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_max_reads():
    """ Max reads """

    out_dir = 'out'
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        max_reads = random.randint(10, 20)
        rv, out = getstatusoutput(f'{RUN} -s 10 -m {max_reads} {N1K}')
        assert rv == 0
        expected = (
            '  1: n1k.fa\n'
            f'Wrote {max_reads} sequences from 1 file to directory "out".')
        assert out == expected
        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 1

        out_file = os.path.join(out_dir, os.path.basename(N1K))
        assert os.path.isfile(out_file)

        # correct number of seqs
        seqs = list(SeqIO.parse(out_file, 'fasta'))
        assert len(seqs) == max_reads

    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def test_options():
    """ Runs on good input """

    out_dir = random_string()
    try:
        if os.path.isdir(out_dir):
            rmtree(out_dir)

        cmd = f'{RUN} -s 4 -o {out_dir} -p .25 {N1K} {N10K} {N100K}'
        rv, out = getstatusoutput(cmd)
        assert rv == 0

        assert re.search('1: n1k.fa', out)
        assert re.search('2: n10k.fa', out)
        assert re.search('3: n100k.fa', out)
        assert re.search(
            f'Wrote 27,688 sequences from 3 files to directory "{out_dir}".',
            out)

        assert os.path.isdir(out_dir)

        files = os.listdir(out_dir)
        assert len(files) == 3

        seqs_written = 0
        for file in files:
            seqs_written += len(
                list(SeqIO.parse(os.path.join(out_dir, file), 'fasta')))

        assert seqs_written == 27688
    finally:
        if os.path.isdir(out_dir):
            rmtree(out_dir)


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
