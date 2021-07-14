#!/usr/bin/env bash

if [[ $# -ne 1 ]]; then
    printf "usage: %s FILE\n" $(basename "$0")
    exit 1
fi

OUT_DIR="fasta"

[[ ! -d "$OUT_DIR" ]] && mkdir -p "$OUT_DIR"

while read -r PROT_ID; do
    echo "$PROT_ID"
    URL="http://www.uniprot.org/uniprot/${PROT_ID}.fasta"
    echo $URL
    OUT_FILE="$OUT_DIR/${PROT_ID}.fasta" 
    wget -q -O "$OUT_FILE" "$URL"
done < $1

echo "Done, see output in \"$OUT_DIR\"."
