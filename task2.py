#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

mydata=cgi.FieldStorage()

value = mydata.getvalue("c")

output = subprocess.getoutput("sudo" + value)

print("\n Hello")
print("<br />")
print("<br />")

print("Command: ",value)

print("<br />")
print("<br />")

print("Output:",output)
