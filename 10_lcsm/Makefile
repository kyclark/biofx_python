.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --mypy lcsm.py tests/lcsm_test.py

all:
	../bin/all_test.py lcsm.py
