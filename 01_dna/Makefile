.PHONY: test

test:
	python3 -m pytest -xv --flake8 --pylint --pylint-rcfile=../pylintrc --mypy dna.py tests/dna_test.py

all:
	../bin/all_test.py dna.py
