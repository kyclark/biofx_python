# Open Reading Frames

http://rosalind.info/problems/orf/

Write a Python program called `orf.py` that accepts a FASTA formatted input file as a single positional argument and will print all the possible proteins that could be translated from the open reading frames.

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./orf.py -h
usage: orf.py [-h] FILE

Find ORFs

positional arguments:
  FILE        Input FASTA file

optional arguments:
  -h, --help  show this help message and exit
```

Here is an example input:

```
$ cat tests/inputs/1.fa
>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTC\
TTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
```

The output given this input file

```
$ ./orf.py tests/inputs/1.fa
M
MGMTPRLGLESLLE
MLLGSFRLIPKETLIQVAGSSPCNLS
MTPRLGLESLLE
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--pylint-rcfile=../pylintrc --mypy orf.py tests/orf_test.py
============================= test session starts ==============================
...
collected 13 items

orf.py::FLAKE8 PASSED                                                    [  7%]
orf.py::mypy PASSED                                                      [ 14%]
orf.py::test_truncate PASSED                                             [ 21%]
orf.py::test_find_orfs PASSED                                            [ 28%]
tests/orf_test.py::FLAKE8 SKIPPED                                        [ 35%]
tests/orf_test.py::mypy PASSED                                           [ 42%]
tests/orf_test.py::test_exists PASSED                                    [ 50%]
tests/orf_test.py::test_usage PASSED                                     [ 57%]
tests/orf_test.py::test_bad_file PASSED                                  [ 64%]
tests/orf_test.py::test_empty PASSED                                     [ 71%]
tests/orf_test.py::test_ok1 PASSED                                       [ 78%]
tests/orf_test.py::test_ok2 PASSED                                       [ 85%]
tests/orf_test.py::test_ok3 PASSED                                       [ 92%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
======================== 13 passed, 1 skipped in 1.75s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
