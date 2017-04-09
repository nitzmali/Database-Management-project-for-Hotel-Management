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
    db = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='stockmarket')
    cursor = db.cursor()
    return db,cursor

def selectstock(db,cursor,firstname):
    sql = firstname
    cursor.execute(sql)
    stock = cursor.fetchall()
    desc = cursor.description
    leng = len(desc)
    print "Below is your Queried Table"
    return stock,desc

def displaystock(people,desc):

    print("<table border ='1.5'>")


    if len(desc)==1:
        print("<tr>")
        print("<th>{0}</th>".format(desc[0][0]))
        print("</tr>")

        for row in people:

            print("<tr>")
            print("<td> {0}</td>".format(row[0]))
            print("</tr>")


    elif len(desc)==2:
        print("<tr>")
        print("<th>{0}</th>".format(desc[0][0]))
        print("<th>{0}</th>".format(desc[1][0]))
        print("</tr>")

        for row in people:

            print("<tr>")
            print("<td> {0}</td>".format(row[0]))
            print("<td> {0}</td>".format(row[1]))
            print("</tr>")
    elif len(desc)==3:
        print("<tr>")
        print("<th>{0}</th>".format(desc[0][0]))
        print("<th>{0}</th>".format(desc[1][0]))
        print("<th>{0}</th>".format(desc[2][0]))
        print("</tr>")

        for row in people:

            print("<tr>")
            print("<td> {0}</td>".format(row[0]))
            print("<td> {0}</td>".format(row[1]))
            print("<td> {0}</td>".format(row[2]))
            print("</tr>")
    else :
            print("<tr>")
            print("<th>{0}</th>".format(desc[0][0]))
            print("<th>{0}</th>".format(desc[1][0]))
            print("<th>{0}</th>".format(desc[2][0]))
            print("<th>{0}</th>".format(desc[3][0]))
            print("<th>{0}</th>".format(desc[4][0]))
            print("</tr>")

            for row in people:

                print("<tr>")
                print("<td> {0}</td>".format(row[0]))
                print("<td> {0}</td>".format(row[1]))
                print("<td> {0}</td>".format(row[2]))
                print("<td> {0}</td>".format(row[3]))
                print("<td> {0}</td>".format(row[4]))
                print("</tr>")

    print("</table>")

def htmltail():
    print"""<p> Hello<p></body>
              </html>"""

def getData():

    firstname = form.getvalue('firstname')
    return firstname




if __name__=="__main__":
        try:
            htmltop()

            form = cgi.FieldStorage()
            firstname = getData()
            htmltail()
            db,cursor = connectDB()
            stock,desc = selectstock(db,cursor,firstname)
            cursor.close()
            displaystock(stock,desc)


        except:
            cgi_print_exception()
