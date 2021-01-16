""" Unit tests for synth.py """

import io
import random
from synth import read_training, find_kmers, gen_seq


# --------------------------------------------------
def test_gen_seq() -> None:
    """ Test gen_seq """

    chain = {
        'ACG': {
            'T': 0.5,
            'C': 0.5
        },
        'CGT': {
            'A': 1.0
        },
        'GTA': {
            'C': 1.0
        },
        'TAC': {
            'G': 1.0
        }
    }

    state = random.getstate()
    random.seed(1)
    assert gen_seq(chain, k=4, min_len=6, max_len=12) == 'CGTACGTACG'
    random.seed(2)
    assert gen_seq(chain, k=4, min_len=5, max_len=10) == 'ACGTA'
    random.setstate(state)


# --------------------------------------------------
def test_read_training() -> None:
    """ Test read_training """

    f1 = io.StringIO('>1\nACGTACGC\n')
    assert read_training([f1], 'fasta', 4) == {
        'ACG': {
            'T': 0.5,
            'C': 0.5
        },
        'CGT': {
            'A': 1.0
        },
        'GTA': {
            'C': 1.0
        },
        'TAC': {
            'G': 1.0
        }
    }

    f2 = io.StringIO('@1\nACGTACGC\n+\n!!!!!!!!')
    assert read_training([f2], 'fastq', 5) == {
        'ACGT': {
            'A': 1.0
        },
        'CGTA': {
            'C': 1.0
        },
        'GTAC': {
            'G': 1.0
        },
        'TACG': {
            'C': 1.0
        }
    }


# --------------------------------------------------
def test_find_kmers() -> None:
    """ Test find_kmers """

    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
