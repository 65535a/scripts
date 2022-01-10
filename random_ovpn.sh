#!/bin/bash

profile=(*.ovpn) 
old_process=$(ps -aux | grep openvpn | grep -v "grep" | awk '{print $2}')

kill $old_process
openvpn ${profile[$((RANDOM % ${#profile[@]}))]}
