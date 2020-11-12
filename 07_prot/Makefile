.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy prot.py tests/prot_test.py

all:
	../bin/all_test.py prot.py
