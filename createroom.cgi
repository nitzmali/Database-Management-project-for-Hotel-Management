#!/Python27/python
#print("Location:http://localhost/python/rooms.html")
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

def stock(db,cursor,number,type,smoke,floor,photo,price):
    db=db
    cursor=cursor
    photo="null"
    print photo
    print number
    print type
    print smoke
    print floor
    print price

    #sql= 'INSERT INTO dbmshotel.dbmsuniqueroom VALUES("%s","%s","%s","%s","%s","%s")' %(number,type,smoke,floor,photo,price)
    sql = 'select * from dbmshotel.dbmsuniqueroom '


    #sql ='INSERT INTO `dbmshotel`.`dbmscustomer`(`dbmscustomername`,`dbmscustomerage`,`dbmscustomeremail`,`dependent`)VALUES("%s","%s","%s","%s")' %(name,age,email,usrtel)
    cursor.execute(sql)
    x=cursor.fetchall()




    return x

def display(data):
    print("<table border ='1'>")
    print("<tr>")
    print("<th>Number</th>")
    print("<th>type</th>")
    print("<th>smoke</th>")
    print("<th>floor</th>")
    print("<th>photo</th>")
    print("<th>Price</th>")



    print("</tr>")
    for each in data:
        print("<tr>")
        print("<td> {0}</td>".format(each[0]))
        print("<td> {0}</td>".format(each[1]))
        print("<td> {0}</td>".format(each[2]))
        print("<td> {0}</td>".format(each[3]))
        print("<td> {0}</td>".format(each[4]))
        print("<td> {0}</td>".format(each[5]))
        print("</tr>")
    print("</table>")

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
        x=stock(db,cursor,number,type,smoke,floor,photo,price)
        display(x)
        htmltail()

    except:
        cgi_print_exception()
