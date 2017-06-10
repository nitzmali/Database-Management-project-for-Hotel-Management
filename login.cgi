#!/Python27/python
#print("Location:http://localhost/python/rooms.html")
import cgi
import pymysql
import cgi, cgitb
cgitb.enable()
def login()

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

    return db,cursor

def stock(db,cursor,number,type,smoke,floor,photo,price):
    db=db
    cursor=cursor

    print photo
    print number
    print type
    print smoke
    print floor

    sql= 'INSERT INTO `dbmshotel`.`dbmsuniqueroom`(`dbmsroomno`,`dbms_type`,`dbms_smoking`,`dbmsfloor`,`dbmsphotos`,`dbmsprice`)VALUES("%s","%s","%s","%s","%s","%s")' %(number,type,smoke,floor,photo,price)

    #sql ='INSERT INTO `dbmshotel`.`dbmscustomer`(`dbmscustomername`,`dbmscustomerage`,`dbmscustomeremail`,`dependent`)VALUES("%s","%s","%s","%s")' %(name,age,email,usrtel)
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
        number = form.getvalue('number')
        type = form.getvalue('type')
        smoke = form.getvalue('smoke')
        floor = form.getvalue('floor')
        photo = form.getvalue('photo')
        price = form.getvalue('price')
        #print name
        #print age
        db,cursor = connectDB()
        stock(db,cursor,number,type,smoke,floor,photo,price)

        htmltail()

    except:
        cgi_print_exception()
