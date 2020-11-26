.PHONY: pdf test data

data:
	wget ftp://ftp.imicrobe.us/biosys-analytics/exercises/unclustered-proteins.tgz

pdf:
	asciidoctor-pdf README.adoc

test:
	pytest --disable-pytest-warnings -xv test.py
