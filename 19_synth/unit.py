import io
import random
from synth import read_training, find_kmers, gen_seq


# --------------------------------------------------
def test_gen_seq() -> None:
    """ Test gen_seq """

    chains = {
        'AAC': ['ACC'],
        'ACC': ['CCG'],
        'CCG': ['CGG'],
        'CGG': ['GGT'],
        'GGT': ['GTT']
    }

    state = random.getstate()
    random.seed(1)
    assert gen_seq(chains, 3, 5, 10) == 'ACCCCGCGG'
    random.seed(2)
    assert gen_seq(chains, 3, 6, 12) == 'AACACC'
    random.setstate(state)


# --------------------------------------------------
def test_read_training() -> None:
    """ Test read_training """

    f1 = io.StringIO('>1\nAACCGGTT\n')

    assert read_training([f1], 'fasta', 3) == {
        'AAC': ['ACC'],
        'ACC': ['CCG'],
        'CCG': ['CGG'],
        'CGG': ['GGT'],
        'GGT': ['GTT']
    }


# --------------------------------------------------
def test_find_kmers() -> None:
    """ Test find_kmers """

    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
