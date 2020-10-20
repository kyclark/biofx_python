# Finding a Shared Motif 

http://rosalind.info/problems/lcsm/

Write a Python program called "lcsm.py" that will accept FASTA file of sequences as a single positional argument and will print the longest common subsequence shared by all the sequences.

The program should print a "usage" statement for "-h" or "--help" flags:

```
$ ./lcsm.py -h
usage: lcsm.py [-h] FILE

Longest Common Substring

positional arguments:
  FILE        Input FASTA

optional arguments:
  -h, --help  show this help message and exit
```

The input file will be in FASTA format:

```
$ cat tests/inputs/1.fa
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
```

The output for this file would look like this:

```
$ ./lcsm.py tests/inputs/1.fa
CA
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy lcsm.py tests/lcsm_test.py
============================ test session starts ============================
...

lcsm.py::FLAKE8 PASSED                                                [  8%]
lcsm.py::mypy PASSED                                                  [ 16%]
lcsm.py::test_kmers PASSED                                            [ 25%]
tests/lcsm_test.py::FLAKE8 PASSED                                     [ 33%]
tests/lcsm_test.py::mypy PASSED                                       [ 41%]
tests/lcsm_test.py::test_exists PASSED                                [ 50%]
tests/lcsm_test.py::test_usage PASSED                                 [ 58%]
tests/lcsm_test.py::test_bad_file PASSED                              [ 66%]
tests/lcsm_test.py::test_empty PASSED                                 [ 75%]
tests/lcsm_test.py::test_short PASSED                                 [ 83%]
tests/lcsm_test.py::test_long PASSED                                  [ 91%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
============================ 12 passed in 42.35s ============================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
