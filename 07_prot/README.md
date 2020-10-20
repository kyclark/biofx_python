# Translating RNA into Protein

http://rosalind.info/problems/prot/

Write a Python program called "prot.py" that takes a sequence of RNA as a single position argument and prints the protein translation.

```
$ ./prot.py AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
MAMAPRTEINSTRING
```

The program should print a "usage" statement for "-h" or "--help" flags:

```
$ ./prot.py -h
usage: prot.py [-h] RNA

Translate RNA to proteins

positional arguments:
  RNA         RNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy prot.py tests/prot_test.py
============================ test session starts ============================
...

prot.py::FLAKE8 SKIPPED                                               [ 11%]
prot.py::mypy PASSED                                                  [ 22%]
tests/prot_test.py::FLAKE8 SKIPPED                                    [ 33%]
tests/prot_test.py::mypy PASSED                                       [ 44%]
tests/prot_test.py::test_exists PASSED                                [ 55%]
tests/prot_test.py::test_usage PASSED                                 [ 66%]
tests/prot_test.py::test_input1 PASSED                                [ 77%]
tests/prot_test.py::test_input2 PASSED                                [ 88%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
======================= 7 passed, 2 skipped in 0.53s ========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
