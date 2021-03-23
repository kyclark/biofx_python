#!/usr/bin/env bash

# Benchmark all the solutions
hyperfine -m 1000 -L prg ./solution1_str_find.py,./solution2_str_index.py,\
./solution3_functional.py,./solution4_kmers_functional.py,\
./solution4_kmers_imperative.py,./solution5_re.py \
'{prg} GATATATGCATATACTT ATAT' --prepare 'rm -rf __pycache__'
