# Inferring mRNA from Protein

http://rosalind.info/problems/mrna/

Write a Python program called `mrna.py` that will accept a protein sequence as a positional argument or a file name along with an optional "modulo" argument that defaults to 1,000,000.

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./mrna.py -h
usage: mrna.py [-h] [-m int] str

Inferring mRNA from Protein

positional arguments:
  str                   Input protein or file

optional arguments:
  -h, --help            show this help message and exit
  -m int, --modulo int  Modulo value (default: 1000000)
```

The output for the program should be number of different RNA strings from which the protein could have been translated, modulo the given argument, e.g.:

```
$ ./mrna.py MA
12
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy mrna.py tests/mrna_test.py
============================ test session starts ============================
...

mrna.py::FLAKE8 PASSED                                                [ 10%]
mrna.py::mypy PASSED                                                  [ 20%]
tests/mrna_test.py::FLAKE8 PASSED                                     [ 30%]
tests/mrna_test.py::mypy PASSED                                       [ 40%]
tests/mrna_test.py::test_exists PASSED                                [ 50%]
tests/mrna_test.py::test_usage PASSED                                 [ 60%]
tests/mrna_test.py::test_ok1 PASSED                                   [ 70%]
tests/mrna_test.py::test_ok2 PASSED                                   [ 80%]
tests/mrna_test.py::test_ok3 PASSED                                   [ 90%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
============================ 10 passed in 0.63s =============================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
