.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy subs.py tests/subs_test.py

all:
	../bin/all_test.py subs.py
