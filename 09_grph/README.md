# Overlap Graphs

http://rosalind.info/problems/grph/

Write a Python program called `grph.py` an input file of sequences and an optional overlap size and will print all the pairs of sequences which can be joined given the overlap size.

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./grph.py -h
usage: grph.py [-h] [-k size] [-d] FILE

Graph through sequences

positional arguments:
  FILE                  FASTA file

optional arguments:
  -h, --help            show this help message and exit
  -k size, --overlap size
                        Size of overlap (default: 3)
  -d, --debug           Debug (default: False)
```

The input file will be in FASTA format:

```
$ cat tests/inputs/1.fa
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
```

The output for this file would look like this:

```
$ ./grph.py tests/inputs/1.fa
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy grph.py tests/grph_test.py
============================ test session starts ============================
...

grph.py::FLAKE8 PASSED                                                [  5%]
grph.py::mypy PASSED                                                  [ 10%]
grph.py::test_find_kmers PASSED                                       [ 15%]
tests/grph_test.py::FLAKE8 PASSED                                     [ 21%]
tests/grph_test.py::mypy PASSED                                       [ 26%]
tests/grph_test.py::test_exists PASSED                                [ 31%]
tests/grph_test.py::test_usage PASSED                                 [ 36%]
tests/grph_test.py::test_bad_k PASSED                                 [ 42%]
tests/grph_test.py::test_bad_file PASSED                              [ 47%]
tests/grph_test.py::test_01 PASSED                                    [ 52%]
tests/grph_test.py::test_02 PASSED                                    [ 57%]
tests/grph_test.py::test_03 PASSED                                    [ 63%]
tests/grph_test.py::test_04 PASSED                                    [ 68%]
tests/grph_test.py::test_05 PASSED                                    [ 73%]
tests/grph_test.py::test_06 PASSED                                    [ 78%]
tests/grph_test.py::test_07 PASSED                                    [ 84%]
tests/grph_test.py::test_08 PASSED                                    [ 89%]
tests/grph_test.py::test_09 PASSED                                    [ 94%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
============================ 19 passed in 4.13s =============================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
