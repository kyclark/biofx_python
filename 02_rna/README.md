# Transcribing DNA into RNA

http://rosalind.info/problems/rna/

Write a program called `rna.py` that will accepts one or more files, each containing a sequence of DNA on each line and the name of an output directory.
The sequences in each file will be transcribed to RNA in output file located in the output directory.

The program should print a "usage" statement for `-h` or `--help` flags:

```
$ ./rna.py -h
usage: rna.py [-h] [-o DIR] FILE [FILE ...]

Transcribe DNA into RNA

positional arguments:
  FILE                  Input DNA file

optional arguments:
  -h, --help            show this help message and exit
  -o DIR, --outdir DIR  Output directory (default: out)
```

The input files should look like this:

```
$ cat tests/inputs/input1.txt
GATGGAACTTGACTACGTAAATT
```

The default output directory is "out."
Note how all the input files are processed into the output directory and the STDOUT from the program summarizes the actions:

```
$ ./rna.py tests/inputs/*
Done, wrote 5 sequences in 3 files to directory "out".
```

And the output should look like this:

```
$ head -c 20 out/*
==> out/input1.txt <==
GAUGGAACUUGACUACGUAA
==> out/input2.txt <==
UUAGCCCAGACUAGGACUUU
==> out/input3.txt <==
CUUAGGUCAGUGGUCUCUAA
```

A fully passing test suite looks like the following:

```
$ make test
python3 -m pytest -xv --flake8 --pylint --mypy rna.py tests/rna_test.py
============================ test session starts ============================
...

rna.py::FLAKE8 SKIPPED                                                [  8%]
rna.py::mypy PASSED                                                   [ 16%]
tests/rna_test.py::FLAKE8 SKIPPED                                     [ 25%]
tests/rna_test.py::mypy PASSED                                        [ 33%]
tests/rna_test.py::test_exists PASSED                                 [ 41%]
tests/rna_test.py::test_usage PASSED                                  [ 50%]
tests/rna_test.py::test_no_args PASSED                                [ 58%]
tests/rna_test.py::test_bad_file PASSED                               [ 66%]
tests/rna_test.py::test_good_input1 PASSED                            [ 75%]
tests/rna_test.py::test_good_input2 PASSED                            [ 83%]
tests/rna_test.py::test_good_multiple_inputs PASSED                   [ 91%]
::mypy PASSED                                                         [100%]
=================================== mypy ====================================

Success: no issues found in 2 source files
======================= 10 passed, 2 skipped in 0.46s =======================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
