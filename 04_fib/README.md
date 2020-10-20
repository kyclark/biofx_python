# Rabbits and Recurrence Relations

http://rosalind.info/problems/fib/

Write a program called "fib.py" that accepts two positional arguments which are positive integer values describing the number of generations (<= 40) and the size of each litter (<= 5).

The program should print a "usage" statement for "-h" or "--help" flags:

```
$ ./fib.py -h
usage: fib.py [-h] generations litter

Calculate Fibonacci

positional arguments:
  generations  Number of generations
  litter       Size of litter per generation

optional arguments:
  -h, --help   show this help message and exit
```

The output should be the final number of the Fibonacci sequence up to the given generation using the given litter size:

```
$ ./fib.py 5 3
19
```

A fully passing test suite looks like the following:

```
$ make test
python3 -m pytest -xv --flake8 --pylint --mypy fib.py tests/fib_test.py
============================ test session starts ============================
...

fib.py::FLAKE8 SKIPPED                                                [  8%]
fib.py::mypy PASSED                                                   [ 16%]
tests/fib_test.py::FLAKE8 SKIPPED                                     [ 25%]
tests/fib_test.py::mypy PASSED                                        [ 33%]
tests/fib_test.py::test_exists PASSED                                 [ 41%]
tests/fib_test.py::test_usage PASSED                                  [ 50%]
tests/fib_test.py::test_bad_n PASSED                                  [ 58%]
tests/fib_test.py::test_bad_k PASSED                                  [ 66%]
tests/fib_test.py::test_1 PASSED                                      [ 75%]
tests/fib_test.py::test_2 PASSED                                      [ 83%]
tests/fib_test.py::test_3 PASSED                                      [ 91%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
======================= 10 passed, 2 skipped in 0.43s =======================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
