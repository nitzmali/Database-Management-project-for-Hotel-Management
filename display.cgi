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
    return db,cursor



def insertstock(db,cursor,name,age,usrtel,email):
    name = name
    age = age
    usrtel = usrtel
    email= email
    
    print age
    sql = select * from dbmshotel.customer
    #sql = 'INSERT INTO `dbmshotel`.`dbmscustomer` VALUES("%s","%d","%s","%d")' %(name,age,usrtel,email)
    #a.execute(sql)
    cursor.execute(sql)
    db.commit()
    #stock = cursor.fetchall()
    #desc = cursor.description
    #leng = len(desc)
    print "Below is your Queried Table"
    #return stock,desc



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

            #print ticker
            print "\n"
            #print exchange
            htmltail()
            db,cursor = connectDB()
            insertstock(db,cursor,name,age,usrtel,email)

            #stock,desc = selectstock(db,cursor,firstname)
            cursor.close()



        except:
            cgi_print_exception()
