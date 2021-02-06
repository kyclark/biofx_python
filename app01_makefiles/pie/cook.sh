#!/bin/bash

if [[ $# -eq 3 ]]; then
    ITEM=$1
    TEMP=$2
    TIME=$3
    echo "Will cook \"${ITEM}\" at ${TEMP} degrees for ${TIME} minutes."
else
    echo "usage: $(basename $0) ITEM TEMP TIME"
fi
