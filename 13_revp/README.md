# Locating Restriction Sites

http://rosalind.info/problems/revp/

Write a Python program called `revp.py` that will accept a FASTA-formatted file of a DNA sequence and will print the position and length of every reverse palindrome in the string having length between 4 and 12.

The program should print a "usage" statement for `-h` or `--help` flags:

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
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--pylint-rcfile=../pylintrc --mypy revp.py tests/revp_test.py
============================= test session starts ==============================
...
collecting ... collected 10 items

revp.py::FLAKE8 PASSED                                                   [  9%]
revp.py::mypy PASSED                                                     [ 18%]
revp.py::test_revp PASSED                                                [ 27%]
tests/revp_test.py::FLAKE8 SKIPPED                                       [ 36%]
tests/revp_test.py::mypy PASSED                                          [ 45%]
tests/revp_test.py::test_exists PASSED                                   [ 54%]
tests/revp_test.py::test_usage PASSED                                    [ 63%]
tests/revp_test.py::test_bad_file PASSED                                 [ 72%]
tests/revp_test.py::test_ok1 PASSED                                      [ 81%]
tests/revp_test.py::test_ok2 PASSED                                      [ 90%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
======================== 10 passed, 1 skipped in 1.29s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
