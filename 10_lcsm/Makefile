.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy lcsm.py tests/lcsm_test.py

all:
	../bin/all_test.py lcsm.py

1K.fa:
	./genseq.py -n 1000 -o 1K.fa

100K.fa:
	./genseq.py -n 100000 -o 100K.fa

1M.fa:
	./genseq.py -n 1000000 -o 1M.fa
