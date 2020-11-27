.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy fastx_grep.py tests/fastx_grep_test.py

all:
	../bin/all_test.py fastx_grep.py
