.PHONY: test

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy grph.py tests/grph_test.py

all:
	../bin/all_test.py grph.py

out1:
	./solution2_graph.py -o 1.txt tests/inputs/1.fa

out2:
	./solution2_graph.py -o 2.txt tests/inputs/2.fa
