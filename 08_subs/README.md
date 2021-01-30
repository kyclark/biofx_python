# Finding a Motif in DNA

http://rosalind.info/problems/subs/

Write a Python program called `subs.py` that accepts two positional arguments, a sequence and a possible subsequence.
The output should be all the start positions where the subsequence can be found in the sequence:

```
$ ./subs.py GATATATGCATATACTT ATAT
2 4 10
```

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./subs.py -h
usage: subs.py [-h] seq subseq

Find subsequences

positional arguments:
  seq         Sequence
  subseq      Sub-sequence

optional arguments:
  -h, --help  show this help message and exit
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--mypy subs.py tests/subs_test.py
============================ test session starts ============================
...

subs.py::FLAKE8 SKIPPED                                               [ 11%]
subs.py::mypy PASSED                                                  [ 22%]
tests/subs_test.py::FLAKE8 SKIPPED                                    [ 33%]
tests/subs_test.py::mypy PASSED                                       [ 44%]
tests/subs_test.py::test_exists PASSED                                [ 55%]
tests/subs_test.py::test_usage PASSED                                 [ 66%]
tests/subs_test.py::test_input1 PASSED                                [ 77%]
tests/subs_test.py::test_input2 PASSED                                [ 88%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
======================= 7 passed, 2 skipped in 0.28s ========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
