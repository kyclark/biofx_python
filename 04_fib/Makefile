.PHONY: test

test:
	python3 -m pytest -xv --flake8 --pylint --pylint-rcfile=../pylintrc --mypy fib.py tests/fib_test.py

all:
	../bin/all_test.py fib.py
