""" Tests for rna.py """

from subprocess import getstatusoutput
import platform
import os.path
import re
import string
import random
import shutil

PRG = './rna.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else PRG
INPUT1 = './tests/inputs/input1.txt'
INPUT2 = './tests/inputs/input2.txt'
INPUT3 = './tests/inputs/input3.txt'


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Usage """

    for flag in ['-h', '--help']:
        retval, out = getstatusoutput(f'{RUN} {flag}')
        assert retval == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_no_args() -> None:
    """ Dies on no args """

    retval, out = getstatusoutput(RUN)
    assert retval != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_bad_file() -> None:
    """ Die on missing input """

    bad = random_filename()
    retval, out = getstatusoutput(f'{RUN} {bad}')
    assert retval != 0
    assert re.match('usage:', out, re.IGNORECASE)
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1() -> None:
    """ Runs on good input """

    out_dir = 'out'
    try:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)

        retval, out = getstatusoutput(f'{RUN} {INPUT1}')
        assert retval == 0
        assert out == 'Done, wrote 1 sequence in 1 file to directory "out".'
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'input1.txt')
        assert os.path.isfile(out_file)
        assert open(out_file).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'

    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def test_good_input2() -> None:
    """ Runs on good input """

    out_dir = random_filename()
    try:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)

        retval, out = getstatusoutput(f'{RUN} -o {out_dir} {INPUT2}')
        assert retval == 0
        assert out == (f'Done, wrote 2 sequences in 1 file to '
                       f'directory "{out_dir}".')
        assert os.path.isdir(out_dir)
        out_file = os.path.join(out_dir, 'input2.txt')
        assert os.path.isfile(out_file)
        assert open(out_file).read().rstrip() == '\n'.join(
            ['UUAGCCCAGACUAGGACUUU', 'AACUAGUCAAAGUACACC'])

    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def test_good_multiple_inputs():
    """ Runs on good inputs """

    out_dir = random_filename()
    try:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)

        retval, out = getstatusoutput(
            f'{RUN} --out_dir {out_dir} {INPUT1} {INPUT2} {INPUT3}')
        assert retval == 0
        assert out == (f'Done, wrote 5 sequences in 3 files to '
                       f'directory "{out_dir}".')
        assert os.path.isdir(out_dir)
        out_file1 = os.path.join(out_dir, 'input1.txt')
        out_file2 = os.path.join(out_dir, 'input2.txt')
        out_file3 = os.path.join(out_dir, 'input3.txt')
        assert os.path.isfile(out_file1)
        assert os.path.isfile(out_file2)
        assert os.path.isfile(out_file3)
        assert open(out_file1).read().rstrip() == 'GAUGGAACUUGACUACGUAAAUU'
        assert open(out_file2).read().rstrip() == '\n'.join(
            ['UUAGCCCAGACUAGGACUUU', 'AACUAGUCAAAGUACACC'])
        assert open(out_file3).read().rstrip() == output3().rstrip()

    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)


# --------------------------------------------------
def output3() -> str:
    """ Output for 3rd input """

    return '\n'.join([('CUUAGGUCAGUGGUCUCUAAACUUUCGGUUCUGUCGUCUUCAUAGGCAAA'
                       'UUUUUGAACCGGCAGACAAGCUAAUCCCUGUGCGGUUAGCUCAAGCAACA'
                       'GAAUGUCCGAUCUUUGAACUUCCUAACGAACCGAACCUACUAUAAUUACA'
                       'UACGAAUAAUGUAUGGGCUAGCGUUGGCUCAUCAUCAAGUCUGCGGUGAA'
                       'AUGGGAACAUAUUCGCAUUGCAUAUAGGGCGUAUCUGACGAUCGAUUCGA'
                       'GUUGGCUAGUCGUACCAAAUGAUUAUGGGCUGGAGGGCCAAUGUAUACGU'
                       'CAGCCAGGCUAAACCACUGGACCGCUUGCAAUCCAUAGGAAGUAAAAUUA'
                       'CCCUUUUUAAACUCUCUAAGAUGUGGCGUCUCGUUCUUAAGGAGUAAUGA'
                       'GACUGUGACAACAUUGGCAAGCACAGCCUCAGUAUAGCUACAGCACCGGU'
                       'GCUAAUAGUAAAUGCAAACACCGUUUCAAGAGCCGAGCCUUUUUUUAAUG'
                       'CAAGGUGACUUCAGAGGGAGUAAAUCGUGGCCGGGGACUGUCCAGAGCAA'
                       'UGCAUUCCCGAGUGCGGGUACCCGUGGUGUGAGAGGAAUCGAUUUCGCGU'
                       'GUGAUACCAUUAAUGGUCCUGUACUACUGUCAGUCAGCUUGAUUUGAAGU'
                       'CGGCCGACAAGGUUGGUACAUAAUGGGCUUACUGGGAGCUUAGGUUAGCC'
                       'UCUGGAAAACUUUAGAAUUUAUAUGGGUGUUUCUGUGUUCGUACAGGCCC'
                       'CAGUCGGGCCAUCGUUGUUGAGCAUAGACCGGUGUAACCUUAAUUAUUCA'
                       'CAGGCCAAUCCCCGUAUACGCAUCUGAAAGGCACACCGCCUAUUACCAAU'
                       'UUGCGCUUCCUUACAUAGGAGGACCUGUUAUCGUCUUCUCAAUCGCUGAG'
                       'UUACCUUAAAACUAGGAUC'),
                      ('ACCGAGUAAAAGGCGACGGUUCGUUUCCGAACCUAUUUGCUCUUAUUUCU'
                       'ACGGGCUGCUAGUGUUGUAGGCUGCAAAACCUACGUAGUCCCAUCUAUCA'
                       'UGCUCGACCCUACGAGGCUAAUGUCUUGUCAGAGGCCCGUCAUGUGCCAC'
                       'GUACAUACACCAAUGUAUACCGCUCUAGCGGUUUGGUGUAGUAGGACUUG'
                       'UGUAUGCACGCUACAGCGAACAACGUUGAUCCCUAACUGAAGUCGGGCUC'
                       'CGCAGGCCUACUCACGCCGUUUCUAUAGGUUGAGCCGCAUCAAACAUUGG'
                       'GUUGAGUCUCGAGUAUAGAGGAAGGCUCUGGUGGCAGGCGCGACGUUGAU'
                       'CGGGAGGAGUAUGGAUGGUGAUCAAUCCCCGUGCCAAUCGCGAGUACUAC'
                       'AGGAGGAGGGGGCGGCUCUGUUCAAUCAUCACCCGUUCCAUCACACGGGC'
                       'AGCACAGUUGACCUCCCGAGCCGUCUCACGGACCUAGUGGCAACAGGUGU'
                       'AUUGAAGCGCCGGGAAUAGUCAUACCCGUGGGCUUGAUUGAGAGACCGAA'
                       'AUUCCGACCGCCAAAACUGCUGAUAUCGUACGCCUUACUACAAAACAAAU'
                       'GACGUCACUACCGGCCAGGGACAAGCUUAUUAAUUAAGUAGGAACCCUAU'
                       'ACCUUGCACAUCCUAAAUCUAGCAGCGGGUCCAGGAUUGGUUCCAGUCCA'
                       'ACGCGCGAUGCGCGUCAAGCUAGGCGAAUGACCACGGUCGAAACACCACU'
                       'UAUGUGACCCACCUUGGCCAACUCUCCCGAUUCUCCUCGCUACUAUCUUG'
                       'AAGGUCACUGAGAAUAUCCCUUAUGGGUCGCAUACGGAGACAGCCGCAGG'
                       'AGCCUUAACGGAGAAUACGCCAAUACUAUGUUCUGGGUCGGUGGGUGUAA'
                       'UGCGAUGCAAUCCGAUCGUGCGAACGUUCCCUUUGAUGACUAUAGGGUCU'
                       'AGUGAUCGUACAUGUGC')])


# --------------------------------------------------
def random_filename() -> str:
    """ Generate a random filename """

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
