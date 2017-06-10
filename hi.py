#!/Python27/python
import mysql.connector
import pymysql




cnx = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='dbmshotel')
a = cnx.cursor()
sql = 'SELECT * from dbmscustomer'
a.execute(sql)
countrow = a.execute(sql)
#print(countrow)
data = a.fetchall()
for row in data:
    for col in row:
        print ("%s," % col)
    print ("\n")
