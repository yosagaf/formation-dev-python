﻿import cgi
import cgitb

form = cgi.FieldStorage()
your_name = form.getvalue('your_name')

comapny_name = form.getvalue('company_name')

print("Content-type:text/html\n")
print("<html>")
print("<head>")
print("<title>First CGI Program</title>")
print("</head>")
print("<body>")
print("<h2>Hello, %s is working in %s</h2>"
      % (your_name, company_name))

print("</body>")
print("</html>")
