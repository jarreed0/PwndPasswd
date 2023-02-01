#!/bin/python3

# PwndPasswd test
## J. Avery Reed
## @jarreed0
## http://jar.ylimaf.com
## 2/1/2023

from PwndPasswd import check
import sys

passwd = ""

if len(sys.argv) > 1:
   passwd = sys.argv[1]
else:
   passwd = input("Type your password: ")

print("Your password was found {} times.".format(str(check(passwd))))
