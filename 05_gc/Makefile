.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy cgc.py tests/cgc_test.py

all:
	../bin/all_test.py cgc.py

seqs.fa:
	./genseq.py -n 1000

bench: seqs.fa
	./bench.sh
