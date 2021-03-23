#!/usr/bin/env bash

# Benchmark all the solutions
hyperfine -m 1000 -L prg ./solution1_for.py,./solution2_unit.py,\
./solution3_list_comp_slice.py,./solution4_map_takewhile.py,\
./solution5_bio_seq.py \
'{prg} AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA' \
--prepare 'rm -rf __pycache__'
