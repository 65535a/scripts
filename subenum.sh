#!/bin/bash

domains=$(cat $1)

for i in $(echo $domains)
do
	echo "Enumerating subdomains in:"
	echo $i
	item=$(amass enum -passive -d $i)
	final=$(dig +noall +answer $item)
	echo "found:"
	echo "$final"
	echo "$final" >> output.txt
done
