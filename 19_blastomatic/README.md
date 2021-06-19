# Blastomatic: Parsing Delimited Text Files

Delimited text files are a standard way to encode columnar data. You are likely familiar with spreadsheets like Microsoft Excel or Google Sheets where each worksheet may hold a data set with columns across the top and records running down. You can export this data to a text file where the columns of data are delimited, or separated by a character. 
Quite often the delimiter is a comma, and the file will have an extension
of .csv. 
This format is called CSV for comma-separated values. 
When the delimiter is a Tab, the extension may be .tab, .txt, or .tsv for tab-separated values. 
The first line of the file usually will contain the names of the columns. Notably, this is not the case with the tabular output from BLAST (Basic Local Alignment Search Tool), one of the most popular tools in bioinformatics used to compare sequences. 
In this chapter, I will show you how to parse this output and merge the BLAST results with metadata from another delimited text file using the csv and pandas modules.

In this exercise, you will:

* Learn how to use csvkit and csvchk to view delimited text files
* Learn how to use the csv and pandas modules to parse delimited text files

Write a program called `blastomatic.py` that will select BLAST hits above a given percent ID and will merge them with annotations and print the query sequence ID, the percent ID, the depth, and the lat/lon:

```
$ ./blastomatic.py -a tests/inputs/meta.csv -b tests/inputs/hits1.csv -p 99
Exported 22 to "out.csv".
$ head out.csv
qseqid,pident,depth,lat_lon
"JCVI_READ_1095913011720","100.000","12","41.485832,-71.35111"
"JCVI_READ_1095900076806","100.000","32","41.09111,-71.60222"
"JCVI_READ_1095900076806","100.000","32","41.09111,-71.60222"
"JCVI_READ_1095901257294","100.000","32","41.09111,-71.60222"
"JCVI_READ_1095899227776","100.000","25","38.946945,-76.41722"
"JCVI_READ_1093012135235","100.000","20","36.003887,-75.39472"
"JCVI_READ_1093012135235","100.000","20","36.003887,-75.39472"
"JCVI_READ_1093012135235","100.000","20","36.003887,-75.39472"
"JCVI_READ_1093012135235","100.000","20","36.003887,-75.39472"
```

The program should produce a usage:

```
$ ./blastomatic.py -h
usage: blastomatic.py [-h] -b FILE -a FILE [-o FILE] [-d DELIM] [-p PCTID]

Annotate BLAST output

optional arguments:
  -h, --help            show this help message and exit
  -b FILE, --blasthits FILE
                        BLAST -outfmt 6 (default: None)
  -a FILE, --annotations FILE
                        Annotations file (default: None)
  -o FILE, --outfile FILE
                        Output file (default: out.csv)
  -d DELIM, --delimiter DELIM
                        Output field delimiter (default: )
  -p PCTID, --pctid PCTID
                        Minimum percent identity (default: 0.0)
```

A passing test suite looks like this:

```
$ make test
python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint 
--mypy blastomatic.py tests/*_test.py
============================= test session starts ==============================
...
collected 15 items

blastomatic.py::FLAKE8 SKIPPED                                           [  6%]
blastomatic.py::mypy PASSED                                              [ 12%]
tests/blastomatic_test.py::FLAKE8 SKIPPED                                [ 18%]
tests/blastomatic_test.py::mypy PASSED                                   [ 25%]
tests/blastomatic_test.py::test_exists PASSED                            [ 31%]
tests/blastomatic_test.py::test_usage PASSED                             [ 37%]
tests/blastomatic_test.py::test_bad_annotations PASSED                   [ 43%]
tests/blastomatic_test.py::test_bad_input_file PASSED                    [ 50%]
tests/blastomatic_test.py::test_good_input PASSED                        [ 56%]
tests/blastomatic_test.py::test_delimiter PASSED                         [ 62%]
tests/blastomatic_test.py::test_guess_delimiter PASSED                   [ 68%]
tests/blastomatic_test.py::test_pctid PASSED                             [ 75%]
tests/unit_test.py::FLAKE8 SKIPPED                                       [ 81%]
tests/unit_test.py::mypy PASSED                                          [ 87%]
tests/unit_test.py::test_guess_delimiter PASSED                          [ 93%]
::mypy PASSED                                                            [100%]
===================================== mypy =====================================

Success: no issues found in 3 source files
======================== 13 passed, 3 skipped in 2.84s =========================
```

## Author

Ken Youens-Clark <kyclark@gmail.com>
