""" Common functions """

from typing import Any, List, Tuple


# --------------------------------------------------
def fst(tup: Tuple[Any, Any]) -> Any:
    """ Return first member of tuple """

    return tup[0]


# --------------------------------------------------
def test_fst() -> None:
    """Test fst"""

    assert fst((1, 'A')) == 1
    assert fst(('A', 1)) == 'A'


# --------------------------------------------------
def snd(tup: Tuple[Any, Any]) -> Any:
    """ Return second member of tuple """

    return tup[1]


# --------------------------------------------------
def test_snd() -> None:
    """ Test snd """

    assert snd((1, 'A')) == 'A'
    assert snd(('A', 1)) == 1


# --------------------------------------------------
def find_kmers(seq: str, k: int) -> List[str]:
    """ Find k-mers in string """
    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers() -> None:
    """ Test find_kmers """

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 1) == ['A', 'C', 'T', 'G']
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []
