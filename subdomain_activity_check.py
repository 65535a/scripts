import requests
import sys
import time

requests.packages.urllib3.disable_warnings() 

list = []

active_subdomains = open("active_subdomains.txt", "a")

with open(sys.argv[1]) as f:
    for i in f.read().splitlines():
        list.append(i)

for i in list:
    time.sleep(.3)
    try:
        r = requests.get("https://" + i, verify = False, timeout=5)
        print("Trying " + i)
    except requests.exceptions.RequestException as e:
        print(e)
        continue

    if "not found" not in r.text and r.status_code == 200:
        print ('\033[1m' + "Active subdomain found: " + i + '\033[0m')
        active_subdomains.write(i)
        active_subdomains.write("\n")

active_subdomains.close()
