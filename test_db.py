#!/Python27/python


import pymysql
import cgitb
cgitb.enable()
import time
# connect to the database
cnx = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='stockmarket')
a = cnx.cursor()
sql = 'SELECT * from price'
a.execute(sql)
countrow = a.execute(sql)
#print(countrow)
data = a.fetchall()

desc = a.description
leng = len(desc)
print leng
rowcoun = a.rowcount
print countrow
i = 0
while i<leng:
    print "%s" % desc[i][0],


    i = i+1
print "\n"
#for idx,row in enumerate(data):
    #print(row)
for row in data:
    i=0
    #k=0
    #while j<leng:
        #print("\t")
    while(i<leng-1):
        #if leng==2:
        print "%s %s %s" %row
            #print row[i+1]
        i = i+1
        #elif leng==3:
            #print row[i],
            #print row[i+1],
            #print row[i+2]
            #i = i+1


        #j = j+1
    #while i<1:
        #print "%s %s" % (desc[0][0],desc[1][0])

        #print "%s" % row[i]
        #i = i+1
        #j = j+1
