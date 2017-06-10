#!/Python27/python
import cgi
import pymysql

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
    db = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='stockmarket')
    cursor = db.cursor()
    return db,cursor

def selectstock(db,cursor,firstname):
    sql = firstname
    cursor.execute(sql)
    stock = cursor.fetchall()
    return stock

def displaystock(people):
    print("<table border ='1'>")
    print("<tr>")
    print("<th>Room</th>")
    print("<th>Price</th>")
    print("</tr>")
    for each in people:
        print("<tr>")
        print("<td> {0}</td>".format(each[0]))
        print("<td> {0}</td>".format(each[1]))
        print("</tr>")
    print("</table>")

def htmltail():
    print"""</body>
              </html>"""

def getData():
    formData = cgi.FieldStorage()
    firstname = formData.getvalue('firstname')
    return firstname


if __name__=="__main__":
        try:
            htmltop()
            firstname = getData()
            db,cursor = connectDB()
            stock = selectstock(db,cursor,firstname)
            cursor.close()
            displaystock(stock)


            htmltail()
        except:
            cgi_print_exception()
