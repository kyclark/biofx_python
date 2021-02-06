#!/usr/bin/env bash

set -u

OUT_DIR="fasta"
[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

URLS=$(mktemp)
echo "http://downloads.yeastgenome.org/sequence/S288C_reference/chromosomes/fasta/chrmt.fsa" > "$URLS"

for i in $(seq 1 16); do
  printf "http://downloads.yeastgenome.org/sequence/S288C_reference/chromosomes/fasta/chr%02d.fsa\n" "$i" >> "$URLS"
done

cd "$OUT_DIR"
wget -nc -i "$URLS"
rm "$URLS"

echo "Done."
