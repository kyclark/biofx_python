.PHONY: test

test:
	python3 -m pytest -xv --flake8 --pylint --pylint-rcfile=../pylintrc --mypy rna.py tests/rna_test.py

all:
	../bin/all_test.py rna.py
