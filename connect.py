#!/Python27/python
import cgi
import mysql.connector
import pymysql
import cgitb

cgitb.enable()
print "Content-type: text/html"
print
print "<html><head>"
print ""
print "</head><body>"
form=cgi.FieldStorage()
name=form["t1"].value
print "Hello. %s" %name
print "hai"
print '<input type="submit"/>'
Cnx = pymysql.Connect(host="127.0.0.1", port=3306, user="root", passwd="pwd", db="db1")
cursor = Cnx.cursor()
sql="SELECT * FROM rec"
cursor.execute(sql)
data = cursor.fetchone()
print "%s" %data
print "</body></html>"
