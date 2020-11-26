# FASTX grep

Select sequence records by text.
Currently just FASTA/Q but could be anything parsable by Bio.SeqIO.

```
$ ./fastx_grep.py -h
usage: fastx_grep.py [-h] [-f str] [-O str] [-o FILE] PATTERN FILE [FILE ...]

Grep through FASTX files

positional arguments:
  PATTERN               Search pattern
  FILE                  Input file(s)

optional arguments:
  -h, --help            show this help message and exit
  -f str, --format str  Input file format (default: )
  -O str, --out_format str
                        Output file format (default: )
  -o FILE, --outfile FILE
                        Output file (default: None)
```
