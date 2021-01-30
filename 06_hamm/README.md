# Hamming Distance

http://rosalind.info/problems/hamm/

Write a Python program called `hamm.py` that takes a single position argument which is a readable file that will contain two lines of DNA sequences and will print the Hamming distance between them.

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./hamm.py -h
usage: hamm.py [-h] FILE

Hamming distance

positional arguments:
  FILE        File input

optional arguments:
  -h, --help  show this help message and exit
```

Here is an example input file:

```
$ cat tests/inputs/1.txt
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
```

The output should be an integer value, for instance, 7 here as 7 bases would need to be changed to transform one sequence to the other:

```
$ ./hamm.py tests/inputs/1.txt
7
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--mypy hamm.py tests/hamm_test.py
============================ test session starts ============================
...

hamm.py::FLAKE8 SKIPPED                                               [  8%]
hamm.py::mypy PASSED                                                  [ 16%]
hamm.py::test_hamming PASSED                                          [ 25%]
tests/hamm_test.py::FLAKE8 SKIPPED                                    [ 33%]
tests/hamm_test.py::mypy PASSED                                       [ 41%]
tests/hamm_test.py::test_exists PASSED                                [ 50%]
tests/hamm_test.py::test_usage PASSED                                 [ 58%]
tests/hamm_test.py::test_bad_file PASSED                              [ 66%]
tests/hamm_test.py::test_input1 PASSED                                [ 75%]
tests/hamm_test.py::test_input2 PASSED                                [ 83%]
tests/hamm_test.py::test_empty_file PASSED                            [ 91%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
======================= 10 passed, 2 skipped in 0.40s =======================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
