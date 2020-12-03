#!/usr/bin/env bash

set -u

PRG="./fastx_grep.py"
EMPTY="./tests/inputs/empty.fa"
LSU="./tests/inputs/lsu.fq"
LSU_FA="./tests/inputs/lsu.fa"

rm -f ./tests/inputs/*.out

"$PRG" -o "$EMPTY.out" XXX "$EMPTY" 

"$PRG" -o "$LSU.upper.out" LSU "$LSU"
"$PRG" -o "$LSU.lower.out" lsu "$LSU"

"$PRG" -o "$LSU.i.upper.out" -i LSU "$LSU"
"$PRG" -o "$LSU.i.lower.out" -i lsu "$LSU"

"$PRG" -O fasta -o "$LSU.fa.out" LSU "$LSU"
"$PRG" -O fasta-2line  -o "$LSU.2fa.out" LSU "$LSU"

echo "Done."
