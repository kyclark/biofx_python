# FASTX grep

Select sequence records by text.
Currently just FASTA/Q but could be anything parsable by Bio.SeqIO:

```
$ ./fastx_grep.py -i lsu tests/inputs/lsu.fa
>ITSLSUmock2p.ITS_M01380:138:000000000-C9GKM:1:1101:14440:2042 2:N:0
CAAGTTACTTCCTCTAAATGACCAAGCCTAGTGTAGAACCATGTCGTCAGTGTCAGTCTG
AGTGTAGATCTCGGTGGTCGCCGTATCATTAAAAAAAAAAATGTAATACTACTAGTAATT
ATTAATATTATAATTTTGTCTATTAGCATCTTATTATAGATAGAAGATATTATTCATATT
TCACTATCTTATACTGATATCAGCTTTATCAGATCACACTCTAGTGAAGATTGTTCTTAA
CTGAAATTTCCTTCTTCATACAGACACATTAATCTTACCTA
>ITSLSUmock2p.ITS_M01384:138:000000000-C9GKM:1:1101:14440:2043 2:N:0
ACCCGTCAATTTCTTTAAGTTTTAGCCTTGCGACCGTACTCCCCAGGCGGTGCACTTAGT
GGTTTTCCGGCGACCCGGGCGGCGTCAGAGCCCCCCAAGTCTCGTGCACATCGTTTACGG
CGTGGACTACCAGGGTATCTAATCCTGTTTGATCCCCACGCTTTCGTGCCTCAGCGTCAG
TACCGGCCCAGCCACCCGTCTTCACCTTCGGCGTTCCTGTAGATATCTACGCATTTCACC
GCTACACCTACAGTTCCGGTGGCGCCTACCGGCCTCAAGAAACGCAGTATGCCCAGCTAT
T
```

The program should print a usage:

```
$ ./fastx_grep.py -h
usage: fastx_grep.py [-h] [-f str] [-O str] [-o FILE] [-i] [-v]
                     PATTERN FILE [FILE ...]

Grep through FASTX files

positional arguments:
  PATTERN               Search pattern
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -f str, --format str  Input file format (default: )
  -O str, --outfmt str  Output file format (default: )
  -o FILE, --outfile FILE
                        Output file (default: <_io.TextIOWrapper
                        name='<stdout>' mode='w' encoding='utf-8'>)
  -i, --insensitive     Case-insensitive search (default: False)
  -v, --verbose         Be chatty (default: False)
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--pylint-rcfile=../pylintrc --mypy fastx_grep.py tests/fastx_grep_test.py
============================= test session starts ==============================
...
collected 18 items

fastx_grep.py::FLAKE8 PASSED                                             [  5%]
fastx_grep.py::mypy PASSED                                               [ 10%]
fastx_grep.py::test_guess_format PASSED                                  [ 15%]
tests/fastx_grep_test.py::FLAKE8 SKIPPED                                 [ 21%]
tests/fastx_grep_test.py::mypy PASSED                                    [ 26%]
tests/fastx_grep_test.py::test_exists PASSED                             [ 31%]
tests/fastx_grep_test.py::test_usage PASSED                              [ 36%]
tests/fastx_grep_test.py::test_bad_file PASSED                           [ 42%]
tests/fastx_grep_test.py::test_cannot_guess PASSED                       [ 47%]
tests/fastx_grep_test.py::test_empty_file PASSED                         [ 52%]
tests/fastx_grep_test.py::test_lsu_uppercase PASSED                      [ 57%]
tests/fastx_grep_test.py::test_lsu_lowercase PASSED                      [ 63%]
tests/fastx_grep_test.py::test_lsu_uppercase_insensitive PASSED          [ 68%]
tests/fastx_grep_test.py::test_lsu_lowercase_insensitive PASSED          [ 73%]
tests/fastx_grep_test.py::test_outfile PASSED                            [ 78%]
tests/fastx_grep_test.py::test_outfile_verbose PASSED                    [ 84%]
tests/fastx_grep_test.py::test_outfmt_fastq_to_fasta PASSED              [ 89%]
tests/fastx_grep_test.py::test_outfmt_fastq_to_fasta2line PASSED         [ 94%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 2 source files
======================== 18 passed, 1 skipped in 3.09s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
