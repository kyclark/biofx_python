.PHONY = test
SYNTH = ../17_synth/synth.py
TRAIN = ../17_synth/tests/inputs/*.fa

test: fasta
	python3 -m pytest -xv --disable-pytest-warnings --flake8 --pylint --pylint-rcfile=../pylintrc --mypy sampler.py tests/sampler_test.py

all:
	../bin/all_test.py sampler.py

fasta: n1k.fa n10k.fa n100k.fa

n1k.fa:
	$(SYNTH) -s 1 -n 1000 -m 75 -x 200 -o tests/inputs/n1k.fa $(TRAIN)

n10k.fa:
	$(SYNTH) -s 1 -n 10000 -m 75 -x 200 -o tests/inputs/n10k.fa $(TRAIN)

n100k.fa:
	$(SYNTH) -s 1 -n 100000 -m 75 -x 200 -o tests/inputs/n100k.fa $(TRAIN)
