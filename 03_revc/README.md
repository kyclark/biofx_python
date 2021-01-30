# Complementing a Strand of DNA

http://rosalind.info/problems/revc/

Write a program called `revc.py` that will accept a string of DNA either or a filename containing the DNA and will print the reverse complement.
The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./revc.py -h
usage: revc.py [-h] DNA

Print the reverse complement of DNA

positional arguments:
  DNA         Input sequence or file

optional arguments:
  -h, --help  show this help message and exit
```

The program can accept the DNA as a command-line argument:

```
$ ./revc.py AAAACCCGGT
ACCGGGTTTT
```

Or as the name of an input file such as:

```
$ cat tests/inputs/input1.txt
AAAACCCGGT
$ ./revc.py tests/inputs/input1.txt
ACCGGGTTTT
```

A fully passing test suite looks like the following:

```
$ make test
python3 -m pytest -xv --flake8 --pylint --pylint-rcfile=../pylintrc 
--mypy revc.py tests/revc_test.py
============================= test session starts ==============================
...
collected 11 items

revc.py::FLAKE8 SKIPPED                                                  [  8%]
revc.py::mypy PASSED                                                     [ 16%]
tests/revc_test.py::FLAKE8 SKIPPED                                       [ 25%]
tests/revc_test.py::mypy PASSED                                          [ 33%]
tests/revc_test.py::test_exists PASSED                                   [ 41%]
tests/revc_test.py::test_usage PASSED                                    [ 50%]
tests/revc_test.py::test_no_args PASSED                                  [ 58%]
tests/revc_test.py::test_uppercase PASSED                                [ 66%]
tests/revc_test.py::test_lowercase PASSED                                [ 75%]
tests/revc_test.py::test_input1 PASSED                                   [ 83%]
tests/revc_test.py::test_input2 PASSED                                   [ 91%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
======================== 10 passed, 2 skipped in 1.73s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
