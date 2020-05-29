#!/bin/sh

dirs=$(ls -v 999bottles)

for f in 999bottles/*;
do
	bp=$(objdump -D $f | grep '38 c2' -B 1 | head -n 1 | awk '{print $10}' | cut -d, -f1)
	value=$(objdump -D $f | grep $bp | grep -v movzbl | tail -n 1 | awk '{print $10}' | cut -d, -f1 | sed 's/\$//g')
	echo $value | xxd -r >> values
	cat values
done
