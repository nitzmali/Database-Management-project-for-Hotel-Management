#!/Python27/python
import cgi
import pymysql
import cgi, cgitb
cgitb.enable()


def htmltop():

    print"""Content-type: text/html\n\n
          <!DOCTYPE html>
          <html lang="en">
          <head>
          <meta charset="utf-8"/>
          <title> MyPythonWebpage </title>
          </head>
          <body>"""
def connectDB():
    db = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='dbmshotel')
    cursor = db.cursor()
    print "nitin"
    return db,cursor

def stock(db,cursor):
    db=db
    cursor=cursor
    name='shaitaan'
    age=10
    email="nitsmali@hotmail.com"
    dep=10
    #sql = 'INSERT INTO `dbmshotel.dbmscustomer VALUES("%s","%s","%s","%s")' %(name,12,nits@yahoo.com,2)
    #sql = 'INSERT INTO `dbmshotel`.`dbmscustomer`('dbmscustomername`,`dbmscustomerage`,`dbmscustomeremail`,`dependent`)VALUES("mali",11,"nitsmali@hotmail.com",20);'
    sql ='INSERT INTO `dbmshotel`.`dbmscustomer`(`dbmscustomername`,`dbmscustomerage`,`dbmscustomeremail`,`dependent`)VALUES("%s","%d","%s","%d")' %(name,age,email,dep)
    cursor.execute(sql)
    print cursor.fetchall()
    db.commit()
    print "below is"

def htmltail():
     print"""<p> Ending Html tail<p></body>
    </html>"""
if __name__=="__main__":
    try:
        htmltop()
        form = cgi.FieldStorage()
        name = form.getvalue('name')
        age = form.getvalue('age')
        usrtel = form.getvalue('usrtel')
        email = form.getvalue('email')
        #print name
        #print age
        db,cursor = connectDB()
        stock(db,cursor)
        htmltail()

    except:
        cgi_print_exception()
