# Locating Restriction Sites

http://rosalind.info/problems/revp/

Write a Python program called "revp.py" that will accept a FASTA-formatted file of a DNA sequence and will print the position and length of every reverse palindrome in the string having length between 4 and 12.

The program should print a "usage" statement for "-h" or "--help" flags:

```
$ ./revp.py -h
usage: revp.py [-h] FILE

Locating Restriction Sites

positional arguments:
  FILE        Input FASTA file

optional arguments:
  -h, --help  show this help message and exit
```

Here is an example input:

```
$ cat tests/inputs/1.fa
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
```

The output given this input file:

```
$ ./revp.py tests/inputs/1.fa
5 4
7 4
17 4
18 4
21 4
4 6
6 6
20 6
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy revp.py tests/revp_test.py
============================ test session starts ============================
...

revp.py::FLAKE8 SKIPPED                                               [  8%]
revp.py::mypy PASSED                                                  [ 16%]
revp.py::test_fst PASSED                                              [ 25%]
revp.py::test_snd PASSED                                              [ 33%]
revp.py::test_find_kmers PASSED                                       [ 41%]
tests/revp_test.py::FLAKE8 SKIPPED                                    [ 50%]
tests/revp_test.py::mypy PASSED                                       [ 58%]
tests/revp_test.py::test_exists PASSED                                [ 66%]
tests/revp_test.py::test_usage PASSED                                 [ 75%]
tests/revp_test.py::test_ok1 PASSED                                   [ 83%]
tests/revp_test.py::test_ok2 PASSED                                   [ 91%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
======================= 10 passed, 2 skipped in 0.95s =======================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
