#!/bin/bash

profile=(*.ovpn) 
timer=$1
if [ $timer -ge 10 ]; then
while :
  do
    old_process=$(ps -aux | grep openvpn | grep -v "grep" | awk '{print $2}')
    kill $old_process
    openvpn ${profile[$((RANDOM % ${#profile[@]}))]} &
    sleep $timer
done
fi
