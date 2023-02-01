#!/bin/python3

# PwndPasswd
## J. Avery Reed
## @jarreed0
## http://jar.ylimaf.com
## 2/1/2023

from hashlib import sha1
import requests

def check(passwd):
   hashed = sha1(passwd.encode()).hexdigest()
   pre = hashed[0:5]
   post = hashed[5:].upper()
   api = "https://api.pwnedpasswords.com/range/" + pre
   response = requests.request("GET", api, headers={}, data={})
   for pwnd in response.text.split("\r\n"):
      if pwnd.split(":")[0] == post:
          return int(pwnd.split(":")[1])
   return 0
