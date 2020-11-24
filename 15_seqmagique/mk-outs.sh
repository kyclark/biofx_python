#!/usr/bin/env bash

PRG="./seqmagique.py"
DIR="./tests/inputs"
INPUT1="${DIR}/1.fa"
INPUT2="${DIR}/2.fa"
EMPTY="${DIR}/empty.fa"

$PRG $INPUT1 > "${INPUT1}.out"
$PRG $INPUT2 > "${INPUT2}.out"
$PRG $EMPTY > "${EMPTY}.out"
$PRG $INPUT1 $INPUT2 $EMPTY > "$DIR/all.fa.out"

STYLES="plain simple grid pipe orgtbl rst mediawiki latex latex_raw latex_booktabs"

for FILE in $INPUT1 $INPUT2; do
    for STYLE in $STYLES; do
        $PRG -t $STYLE $FILE > "$FILE.${STYLE}.out"
    done
done

echo Done.
