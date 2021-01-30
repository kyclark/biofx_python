# Translating RNA into Protein

http://rosalind.info/problems/prot/

Write a Python program called `prot.py` that takes a sequence of RNA as a single position argument and prints the protein translation.

```
$ ./prot.py AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
MAMAPRTEINSTRING
```

The program should print a "usage" statement for `-h` or `--help` flags:

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
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--mypy prot.py tests/prot_test.py
============================= test session starts ==============================
platform darwin -- Python 3.9.1, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /Library/Frameworks/Python.framework/Versions/3.9/bin/python3
cachedir: .pytest_cache
rootdir: /Users/kyclark/work/bio/code/07_prot
plugins: mypy-0.7.0, flake8-1.0.6, pylint-0.17.0
collected 9 items

prot.py::FLAKE8 SKIPPED                                                  [ 10%]
prot.py::mypy PASSED                                                     [ 20%]
tests/prot_test.py::FLAKE8 SKIPPED                                       [ 30%]
tests/prot_test.py::mypy PASSED                                          [ 40%]
tests/prot_test.py::test_exists PASSED                                   [ 50%]
tests/prot_test.py::test_usage PASSED                                    [ 60%]
tests/prot_test.py::test_input1 PASSED                                   [ 70%]
tests/prot_test.py::test_stop_codon PASSED                               [ 80%]
tests/prot_test.py::test_input2 PASSED                                   [ 90%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
========================= 8 passed, 2 skipped in 1.72s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
