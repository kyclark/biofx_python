# BAM to FASTx in Python

Revisiting the BAM-to-FASTA problem we solved with `bam2fa.sh`, let's look at how we might accomplish this with Python. About half of the Python version is devoted to `get_args` where we define an option for the ouptut `-f|--format` to be constrained to the `choices` of 'fasta' (default) or 'fastq' (which are also the names of the subargument to `samtools`), the `-o|--outdir` directory, and the number of `-p|--procs` processes for `parallel` to run concurrently. I also added a `-v|--verbose` flag to see the output from running `samtools` processes or to keep quite (the default).

The Python version of this code has a few more options but mostly runs just the same. Whereas in the `bash` version, I wrote all the commands to a temporary file, in this version I make a `list` of `commands` that I pass to the `parallelprocs.run` function. This is a module that encapsulates all the logic for run the commands with the `parallel` program if available otherwise to run them serially. This function returns `True` or `False` to indicate whether the processes were run but may also throw an `Exception` so we need to use `try/catch`. 

Most of the details in this program have to do with formulating the output file names by finding the "root" of the basename for each input file. 

````
>>> import os
>>> os.path.basename('/path/to/sample.bam')
'sample.bam'
>>> os.path.splitext('sample.bam')
('sample', '.bam')
````

You have to run `splitext` on the `basename`:

````
>>> os.path.splitext('/path/to/sample.bam')
('/path/to/sample', '.bam')
````

Since `splitext` returns a 2-tuple, we can unpack into two variables; but we don't actually need the 2nd value (the current extension), so we use the underscore (`_`) as a throwaway placeholder:

````
>>> root, _ = os.path.splitext('sample.bam')
>>> root
'sample'
````

It is not necessary to use `_` -- you are welcome to have a named variable, but I like to do this for two reasons:

1. It shows to the reader that I know I'm not using this value.
2. Some linters will complain about unused variables, so I avoid that warning.

If you care to look at the source for `parallelprocs`, it can be found here:

	https://github.com/kyclark/parallelprocs