#!/bin/sh

# arg1 = file containing ip addresses. Don't worry if there's other stuff included. IP's will be grepped.

if [ -z "$1"  ]
then
        echo "Usage: ipinfo.sh [file]"
        exit 0
fi
LIST=$(cat $1 | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}")

for i in $LIST
        do curl https://ipinfo.io/$i
done


