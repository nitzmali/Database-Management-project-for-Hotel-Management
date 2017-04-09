#!/Python27/python
import mysql.connector
import pymysql




cnx = pymysql.connect(user='root', password='1234', host='127.0.0.1',database='stockmarket')
a = cnx.cursor()
sql = 'SELECT * from stock'
a.execute(sql)
countrow = a.execute(sql)
#print(countrow)
data = a.fetchall()
for row in data:
    for col in row:
        print ("%s," % col)
    print ("\n")




cnx.close()
import webbrowser
f = open('helloworld.html','w')

message = """<html>
<head></head>
<body><p>Hello World!</p>
<br>
<form>
<input type="text" name="first name">
<input type="submit" value="submit">
</form>
<br>
<table>
  {% for row in data %}
  <tr>
    <th> {{ row[0] }}</th>
  </tr>
  {% endfor %}
</table>
<a href = "http://www.nytimes.com"><img src = "C:/Users/nitsm/Desktop/Nitin S Mali (@nitzmali) • Instagram photos and videos_files/nits.jpg" alt="www.google.com" width="104" height="102"> </a>
</body>
</html>"""

f.write(message)
f.close()

filename = 'C:/Users/nitsm/Documents/Django/pythonsql/' + 'helloworld.html'
#filename2='C:/Users/nitsm/Desktop/Nitin S Mali (@nitzmali) • Instagram photos and videos_files/nits.jpg'
webbrowser.open_new_tab(filename)
#webbrowser.open_new_tab(filename2)
