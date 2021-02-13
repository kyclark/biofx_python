.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy blastomatic.py tests/*_test.py

all:
	../bin/all_test.py blastomatic.py

taxdump:
	wget ftp://ftp.ncbi.nih.gov/pub/taxonomy/gi_taxid_nucl.dmp.gz
