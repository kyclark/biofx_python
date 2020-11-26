from unittest.mock import mock_open
from seqmagique import process


# --------------------------------------------------
def test_process() -> None:
    """ Test process """

    empty = process(mock_open(read_data='')())
    assert empty.min_len == 0
    assert empty.max_len == 0
    assert empty.avg_len == 0
    assert empty.num_seqs == 0

    one = process(mock_open(read_data='>SEQ0\nAAA')())
    assert one.min_len == 3
    assert one.max_len == 3
    assert one.avg_len == 3
    assert one.num_seqs == 1

    two = process(mock_open(read_data='>SEQ0\nAAA\n>SEQ1\nCCCC')())
    assert two.min_len == 3
    assert two.max_len == 4
    assert two.avg_len == 3.5
    assert two.num_seqs == 2
