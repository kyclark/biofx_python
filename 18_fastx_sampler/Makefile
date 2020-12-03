.PHONY = fa clean run pdf test

MOOG = "../08_synthetic_dna/moog.py"

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
	time $(MOOG) -n 1000 -o n1k.fa -t dna -m 75 -x 200

n10k.fa:
	time $(MOOG) -n 10000 -o n10k.fa -t dna -m 75 -x 200

n100k.fa:
	time $(MOOG) -n 100000 -o n100k.fa -t dna -m 75 -x 200

n1m.fa:
	time $(MOOG) -n 1000000 -o n1m.fa -t dna -m 75 -x 200

pdf:
	asciidoctor-pdf README.adoc
