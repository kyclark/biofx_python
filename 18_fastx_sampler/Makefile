.PHONY = fa clean run pdf test
SYNTH = ../17_synth/synth.py
TRAIN = ../17_synth/tests/inputs/*.fa

run: fasta
	./sampler.py *.fa

test:
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy sampler.py tests/sampler_test.py

all:
	../bin/all_test.py sample.py

fasta: n1k.fa n10k.fa n100k.fa n1m.fa

clean:
	rm -rf *.fa out __pycache__

n1k.fa:
	time $(SYNTH) -n 1000 -o tests/inputs/n1k.fa -m 75 -x 200 $(TRAIN)

n10k.fa:
	time $(SYNTH) -n 10000 -o tests/inputs/n10k.fa -m 75 -x 200 $(TRAIN)

n100k.fa:
	time $(SYNTH) -n 100000 -o tests/inputs/n100k.fa -m 75 -x 200 $(TRAIN)
