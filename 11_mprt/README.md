# Finding a Protein Motif 

http://rosalind.info/problems/mprt/

Write a Python program called "mprt.py" that will accept file of sequence IDs, will download the sequences from UniProt, and will print each protein containing the N-glycosylation motif and a list of the locations where the motif can be found.

The program should print a "usage" statement for "-h" or "--help" flags:

```
$ ./mprt.py -h
usage: mprt.py [-h] [-d DIR] FILE

Find location of N-glycosylation motif

positional arguments:
  FILE                  Input text file of UniProt IDs

optional arguments:
  -h, --help            show this help message and exit
  -d DIR, --download_dir DIR
                        Directory for downloads (default: fasta)
```

The input file will list the sequence IDs:

```
$ cat tests/inputs/1.txt
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST
```

The output for this file would look like this:

```
$ ./mprt.py tests/inputs/1.txt
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy mprt.py tests/mprt_test.py
============================= test session starts ==============================
...

mprt.py::FLAKE8 PASSED                                                   [ 10%]
mprt.py::mypy PASSED                                                     [ 20%]
tests/mprt_test.py::FLAKE8 PASSED                                        [ 30%]
tests/mprt_test.py::mypy PASSED                                          [ 40%]
tests/mprt_test.py::test_exists PASSED                                   [ 50%]
tests/mprt_test.py::test_usage PASSED                                    [ 60%]
tests/mprt_test.py::test_bad_file PASSED                                 [ 70%]
tests/mprt_test.py::test_1 PASSED                                        [ 80%]
tests/mprt_test.py::test_2 PASSED                                        [ 90%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
============================= 10 passed in 23.58s ==============================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
