# DNA Synthesizer: Creating Synthetic Data with Markov Chains

A Markov chain is a model for representing a sequence of possibilities found in a given data set. 
It is a machine learning (ML) algorithm because it discovers or learns
patterns from input data. 
In this exercise, I’ll show how to use Markov chains trained on a set of DNA sequences to generate novel DNA sequences.
In this exercise, you will:

* Read some number of input sequence files to find all the unique k-mers for a
given k.
* Create a Markov chain using these k-mers to produce some number of novel
sequences of lengths bounded by a minimum and maximum.
* Learn about generators.
* Use a random seed to replicate random selections.

Write a program `synth.py` that uses Markov chains trained on input DNA files to create novel DNA sequences:

```
$ ./synth.py tests/inputs/CAM_SMPL_GS108.fa -n 2
Done, see output in "out.fa".
$ cat out.fa
>1
GGGCTTTATACCTAGAGGACGAGCATTAGATCTTGCCAGCATAGGCACTAAAGGTACATTC
>2
TCCAGTTCCAGGGTCAAGATATACCTAAGATATATATTTAGCTAGTTTTATTAAGATTGGAATGT
```

The program should print a usage:

```
$ ./synth.py -h
usage: synth.py [-h] [-o FILE] [-f format] [-n number] [-x max] [-m min]
                [-k kmer] [-s seed]
                FILE [FILE ...]

Create synthetic DNA using Markov chain

positional arguments:
  FILE                  Training file(s)

optional arguments:
  -h, --help            show this help message and exit
  -o FILE, --outfile FILE
                        Output filename (default: out.fa)
  -f format, --format format
                        Input file format (default: fasta)
  -n number, --num number
                        Number of sequences to create (default: 100)
  -x max, --max_len max
                        Maximum sequence length (default: 75)
  -m min, --min_len min
                        Minimum sequence length (default: 50)
  -k kmer, --kmer kmer  Size of kmers (default: 10)
  -s seed, --seed seed  Random seed value (default: None)
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--pylint-rcfile=../pylintrc --mypy synth.py tests/unit_test.py tests/synth_test.py
============================= test session starts ==============================
...
collected 22 items

synth.py::FLAKE8 SKIPPED                                                 [  4%]
synth.py::mypy PASSED                                                    [  8%]
tests/unit_test.py::FLAKE8 SKIPPED                                       [ 13%]
tests/unit_test.py::mypy PASSED                                          [ 17%]
tests/unit_test.py::test_gen_seq PASSED                                  [ 21%]
tests/unit_test.py::test_read_training PASSED                            [ 26%]
tests/unit_test.py::test_find_kmers PASSED                               [ 30%]
tests/synth_test.py::FLAKE8 SKIPPED                                      [ 34%]
tests/synth_test.py::mypy PASSED                                         [ 39%]
tests/synth_test.py::test_exists PASSED                                  [ 43%]
tests/synth_test.py::test_usage PASSED                                   [ 47%]
tests/synth_test.py::test_bad_file PASSED                                [ 52%]
tests/synth_test.py::test_bad_seed PASSED                                [ 56%]
tests/synth_test.py::test_bad_format PASSED                              [ 60%]
tests/synth_test.py::test_sample1_num1 PASSED                            [ 65%]
tests/synth_test.py::test_sample1_num1_outfile PASSED                    [ 69%]
tests/synth_test.py::test_sample1_num1_min20_max40 PASSED                [ 73%]
tests/synth_test.py::test_sample1_num1_kmer4 PASSED                      [ 78%]
tests/synth_test.py::test_sample1_num1_kmer5 PASSED                      [ 82%]
tests/synth_test.py::test_sample3_num1_format PASSED                     [ 86%]
tests/synth_test.py::test_sample1_defaults PASSED                        [ 91%]
tests/synth_test.py::test_multiple_inputs PASSED                         [ 95%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 3 source files
======================== 20 passed, 3 skipped in 5.01s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
