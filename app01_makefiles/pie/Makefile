all: crust.txt filling.txt meringue.txt
	./combine.sh pie.txt crust.txt filling.txt meringue.txt
	./cook.sh pie.txt 375 45

filling.txt:
	./combine.sh filling.txt lemon butter sugar

meringue.txt:
	./combine.sh meringue.txt eggwhites sugar

crust.txt:
	./combine.sh crust.txt flour butter water

clean:
	rm -f crust.txt meringue.txt filling.txt pie.txt
