#!/usr/bin/env bash

PRG='./synth.py'
SAMPLE1='./tests/inputs/CAM_SMPL_GS108.fa'
SAMPLE2='./tests/inputs/CAM_SMPL_GS112.fa'
SAMPLE3='./tests/inputs/lsu.fq'

rm -r ./tests/inputs/*.out

$PRG -s 1 -n 1 -o "$SAMPLE1.n1.out" $SAMPLE1
$PRG -s 1 -m 20 -x 40 -n 1 -o "$SAMPLE1.n1.m20.x40.out" $SAMPLE1
$PRG -s 1 -n 1 -k 4 -o "$SAMPLE1.n1.k4.out" $SAMPLE1
$PRG -s 1 -n 1 -k 5 -o "$SAMPLE1.n1.k5.out" $SAMPLE1
$PRG -s 1 -o "$SAMPLE1.default.out" $SAMPLE1

$PRG -s 1 -n 1 -f fastq -o "$SAMPLE3.n1.out" $SAMPLE3

$PRG -s 1 -n 10 -o "./tests/inputs/mult.n10.out" $SAMPLE1 $SAMPLE2
