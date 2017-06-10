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

def stock(db,cursor,nameb):
    db=db
    cursor=cursor
    print nameb

    sql ='select * from dbmshotel.dbmscustomer where dbmscustomername="%s"'%nameb
    cursor.execute(sql)
    x=cursor.fetchall()

    db.commit()
    print "below is"
    return x

def display(data):
    print("<table border ='1'>")
    print("<tr>")
    print("<th>Custid</th>")
    print("<th>Customer Name</th>")
    print("<th>Age</th>")
    print("<th>Email</th>")
    print("<th>Dependent</th>")



    print("</tr>")
    for each in data:
        print("<tr>")
        print("<td> {0}</td>".format(each[0]))
        print("<td> {0}</td>".format(each[1]))
        print("<td> {0}</td>".format(each[2]))
        print("<td> {0}</td>".format(each[3]))
        print("<td> {0}</td>".format(each[4]))
        print("</tr>")
    print("</table>")

def htmltail():

    print"""<p> Ending Html tail<p></body>

    </html>"""
if __name__=="__main__":
    try:
        htmltop()
        form = cgi.FieldStorage()
        nameb = form.getvalue('nameb')

        db,cursor = connectDB()
        x=stock(db,cursor,nameb)
        display(x)

        htmltail()

    except:
        cgi_print_exception()
