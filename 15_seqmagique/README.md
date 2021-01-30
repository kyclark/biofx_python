# Seqmagique

Write a program called `seqmagique.py` that will accept FASTA input files and will print the minimum/maximum/average sequence lengths and the number of sequence in each file:

```
$ ./seqmagique.py tests/inputs/*.fa
name                     min_len    max_len    avg_len    num_seqs
tests/inputs/1.fa             50         50      50.00           1
tests/inputs/2.fa             49         79      64.00           5
tests/inputs/empty.fa          0          0       0.00           0
```

The program should print a usage:

```
$ ./seqmagique.py -h
usage: seqmagique.py [-h] [-t table] FILE [FILE ...]

Argparse Python script

positional arguments:
  FILE                  Input FASTA file(s)

optional arguments:
  -h, --help            show this help message and exit
  -t table, --tablefmt table
                        Tabulate table style (default: plain)
```

The output table should be formatted with the `tabulate` module and so will accept all the valid table styles, e.g.:

```
$ ./seqmagique.py -t simple tests/inputs/*.fa
name                     min_len    max_len    avg_len    num_seqs
---------------------  ---------  ---------  ---------  ----------
tests/inputs/1.fa             50         50      50.00           1
tests/inputs/2.fa             49         79      64.00           5
tests/inputs/empty.fa          0          0       0.00           0
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--pylint-rcfile=../pylintrc --mypy seqmagique.py tests/seqmagique_test.py
============================= test session starts ==============================
...
collected 12 items

seqmagique.py::FLAKE8 SKIPPED                                            [  7%]
seqmagique.py::mypy PASSED                                               [ 15%]
tests/seqmagique_test.py::FLAKE8 SKIPPED                                 [ 23%]
tests/seqmagique_test.py::mypy PASSED                                    [ 30%]
tests/seqmagique_test.py::test_exists PASSED                             [ 38%]
tests/seqmagique_test.py::test_usage PASSED                              [ 46%]
tests/seqmagique_test.py::test_bad_file PASSED                           [ 53%]
tests/seqmagique_test.py::test_empty_file PASSED                         [ 61%]
tests/seqmagique_test.py::test_input1 PASSED                             [ 69%]
tests/seqmagique_test.py::test_input2 PASSED                             [ 76%]
tests/seqmagique_test.py::test_input_all PASSED                          [ 84%]
tests/seqmagique_test.py::test_styles PASSED                             [ 92%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
======================== 11 passed, 2 skipped in 6.33s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
