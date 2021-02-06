#!/bin/bash

if [[ $# -gt 1 ]]; then
    FILE=$1
    shift 1
    echo "Will combine $@" > "$FILE"
else
    echo "usage: $(basename "$0") FILE ingredients"
fi
