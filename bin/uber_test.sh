#!/usr/bin/env bash

# Run all the tests for the entire repo

set -eu -o pipefail

ROOT=$(cd "$(dirname "$0")/.." && pwd)
echo "ROOT $ROOT"

PYLINTRC="$ROOT/.pylintrc"
[[ -f "$PYLINTRC" ]] && export PYLINTRC

DIRS=$(find "$ROOT" -mindepth 1 -maxdepth 1 -type d -name \[01\]\* | sort)
for DIR in $DIRS; do
    BASE=$(basename "$DIR")
    echo "==> $BASE <=="
    cd "$DIR" 
    [[ -f Makefile ]] && make all
    cd "$ROOT"
done
