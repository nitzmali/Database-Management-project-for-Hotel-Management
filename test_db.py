#!/Python27/python

from random import randint
import pymysql
import cgitb
import time
cgitb.enable()
import time
import string
import random

#start_time = time.clock()
# connect to the database
cnx = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='employee')
a = cnx.cursor()
start_time = time.clock()
print start_time
for i in range (100,100000):
    stock = "BDM"
    #v1 = randint(1,100)
    #sql = 'INSERT INTO `employee`.`nitin`(`idnitin`) VALUES(%d)' %(int(v1))
    #sql = 'INSERT INTO `employee`.`nitin`(`idnitin`) VALUES((FLOOR(100+ (RAND() * 20))))'
    #sql = 'INSERT INTO `employee`.`nits` VALUES("%s","%s")' %("name"+str(i),"name"+str(i))
    #sql1 = 'INSERT INTO `employee`.`nits` VALUES("%s","%s")' %(str(stock)+str(i),str(stock)+str(i))
    #sql3 = 'INSERT INTO `employee`.`ids` VALUES("%s","%s","%s","%s","%s")' %(i,i*10,str(stock)+str(i),str(stock)+str(i),str(stock)+str(i))
    sql4 = 'select * from ids where id=606'
    #a.execute(sql)
    a.execute(sql4)

print str(stock)
#countrow = a.execute(sql)
cnx.commit()
#N=2
#print ''.join(random.choice(string.ascii_uppercase) for _ in range(N))
#print(countrow)
data = a.fetchall()

print time.clock()
print time.clock() - start_time, "seconds"
#time.sleep(5)
#start_time = time.clock()

#print time.clock() - start_time, "seconds"
#desc = a.description
#leng = len(desc)
#print leng
