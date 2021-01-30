# Counting tetranucleotide frequency

http://rosalind.info/problems/dna/

Create a program called `dna.py` that will accept a sequence of DNA as a single positional argument.
The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./dna.py -h
usage: dna.py [-h] DNA

Tetranucleotide frequency

positional arguments:
  DNA         Input DNA sequence

optional arguments:
  -h, --help  show this help message and exit
```

The program should print the frequencies of the bases A, C, G, and T:

```
$ ./dna.py AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
20 12 17 21
```

The `make test` target will run the complete test suite:

```
$ make test
python3 -m pytest -xv --flake8 --pylint --mypy dna.py tests/dna_test.py
============================ test session starts ============================
...

dna.py::FLAKE8 PASSED                                                 [ 11%]
dna.py::mypy PASSED                                                   [ 22%]
tests/dna_test.py::FLAKE8 SKIPPED                                     [ 33%]
tests/dna_test.py::mypy PASSED                                        [ 44%]
tests/dna_test.py::test_exists PASSED                                 [ 55%]
tests/dna_test.py::test_usage PASSED                                  [ 66%]
tests/dna_test.py::test_arg PASSED                                    [ 77%]
tests/dna_test.py::test_file PASSED                                   [ 88%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
======================= 8 passed, 1 skipped in 0.87s ========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
