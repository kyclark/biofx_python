# Finding a Shared Motif 

http://rosalind.info/problems/lcsm/

Write a Python program called `lcsm.py` that will accept FASTA file of sequences as a single positional argument and will print the longest common subsequence shared by all the sequences.

The program should print a "usage" statement for `-h` or `--help` flags:

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
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--pylint-rcfile=../pylintrc --mypy lcsm.py tests/lcsm_test.py
============================= test session starts ==============================
...
collected 13 items

lcsm.py::FLAKE8 SKIPPED                                                  [  7%]
lcsm.py::mypy PASSED                                                     [ 14%]
lcsm.py::test_binary_search PASSED                                       [ 21%]
lcsm.py::test_common_kmers PASSED                                        [ 28%]
lcsm.py::test_find_kmers PASSED                                          [ 35%]
tests/lcsm_test.py::FLAKE8 SKIPPED                                       [ 42%]
tests/lcsm_test.py::mypy PASSED                                          [ 50%]
tests/lcsm_test.py::test_exists PASSED                                   [ 57%]
tests/lcsm_test.py::test_usage PASSED                                    [ 64%]
tests/lcsm_test.py::test_bad_file PASSED                                 [ 71%]
tests/lcsm_test.py::test_short PASSED                                    [ 78%]
tests/lcsm_test.py::test_long PASSED                                     [ 85%]
tests/lcsm_test.py::test_no_shared PASSED                                [ 92%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
======================== 12 passed, 2 skipped in 2.13s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
