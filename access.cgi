#!/Python27/python
print("Location:http://localhost/python/rooms.html")
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




def htmltail():

    print"""<p> Ending Html tail<p></body>

    </html>"""
if __name__=="__main__":
    try:
        htmltop()
        form = cgi.FieldStorage()
        name = form.getvalue('uname')
        psw = form.getvalue('psw')
        x1="nitin"
        y1=123
        x2="mohit"
        y2=123
        print name,psw
        if (x1 is name):
            print "okay"
        else:
            print "not okay"







        htmltail()

    except:
        cgi_print_exception()
