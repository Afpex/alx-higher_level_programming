#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status

import urllib.request
url = 'https://alx-intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    content = response.read().decode('utf-8')
print("-" * 20)
print("Body response:")
print("\t- type: {}".format(type(content)))
print("\t- content: {}".format(content))
print("\t- utf8 content: {}".format(content))
print("-" * 20)
