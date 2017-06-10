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
          </head><style>
body {
    background-color: #93B874;
}
</style>
          <body>"""
def connectDB():
    db = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='dbmshotel')
    cursor = db.cursor()

    return db,cursor

def stock(db,cursor,checkindate,checkoutdate,quantity):
    db=db
    cursor=cursor
    #print checkindate
    #print checkoutdate
    #print quantity
    sql ='select dbmsroomno,dbmsprice,dbms_type from dbmshotel.dbmsuniqueroom where dbmsroomno not in (select room_no from dbmshotel.reservedroom where checkout_date <"%s" and  checkin_date >"%s")' %(checkoutdate,checkindate)

    cursor.execute(sql)
    x = cursor.fetchall()
    db.commit()
    return x

def display(data):
    print("<table border ='1'>")
    print("<tr>")
    print("<th>Room Number</th>")
    print("<th>Price</th>")
    print("<th>Room Type</th>")
    print("</tr>")
    for each in data:
        print("<tr>")
        print("""<td><a href="http://localhost/python/images/nits.png"> {0}</td></a>""".format(each[0]))
        print("""<td><a href="http://localhost/python/payments.html"> {0}</td></a>""".format(each[1]))
        print("<td> {0}</td>".format(each[2]))
        print("</tr>")
    print("</table>")

def disp():
    print("""<p> Look below for the Photos of Specific Type<p>""")
    print("""<p>An absolute URL: <a href="http://localhost/python/images/">Images</a></p>""")
    print("""<img src="http://localhost/python/images/nits.png" alt="Smiley face" width="200" height="200">""")



def htmltail():

    print"""<p> <p></body>

    </html>"""
if __name__=="__main__":
    try:
        htmltop()
        form = cgi.FieldStorage()
        checkindate = form.getvalue('checkindate')
        checkoutdate = form.getvalue('checkoutdate')
        quantity = form.getvalue('quantity')

        #print name
        #print age
        db,cursor = connectDB()
        x = stock(db,cursor,checkindate,checkoutdate,quantity)
        display(x)
        disp()

        htmltail()

    except:
        cgi_print_exception()
