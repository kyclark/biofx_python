.PHONY: all fasta features test clean

FEATURES = http://downloads.yeastgenome.org/curation/$\
	chromosomal_feature/SGD_features.tab

all: fasta genome chr-count chr-size features gene-count verified-genes uncharacterized-genes gene-types terminated-genes test

clean:
	find . \( -name \*gene\* -o -name chr-\* \) -exec rm {} \;
	rm -rf fasta SGD_features.tab

fasta:
	./download.sh

genome: fasta
	(cd fasta && cat *.fsa > genome.fa)

chr-count: genome
	grep -e '^>' "fasta/genome.fa" | grep 'chromosome' | wc -l > chr-count

chr-size: genome
	grep -ve '^>' "fasta/genome.fa" | wc -c > chr-size

features:
	wget -nc $(FEATURES)

gene-count: features
	cut -f 2 SGD_features.tab | grep ORF | wc -l > gene-count

verified-genes: features
	awk -F"\t" '$$3 == "Verified" {print}' SGD_features.tab | \
		wc -l > verified-genes

uncharacterized-genes: features
	awk -F"\t" '$$2 == "ORF" && $$3 == "Uncharacterized" {print $$2}' \
		SGD_features.tab | wc -l > uncharacterized-genes

gene-types: features
	awk -F"\t" '{print $$3}' SGD_features.tab | sort | uniq -c > gene-types

terminated-genes: 
	grep -o '/G=[^ ]*' palinsreg.txt | cut -d = -f 2 | \
		sort -u > terminated-genes

test:
	pytest -xv ./test.py
