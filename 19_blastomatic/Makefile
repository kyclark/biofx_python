.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy blastomatic.py tests/*_test.py

all:
	../bin/all_test.py blastomatic.py
