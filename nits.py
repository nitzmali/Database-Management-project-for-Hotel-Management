#!/Python27/python

from random import randint
import pymysql
import cgitb
import time
cgitb.enable()
import time
import string
import random
print "Content-type: text/html"
print
print "<html><head>"
print "</head><body>"
print "<title> MyPythonWebpage </title>"
print "Whatever you would like to print goes here, preferably  between tags "
print "</body></html>"

N=2
print ''.join(random.choice(string.ascii_uppercase) for _ in range(N))
