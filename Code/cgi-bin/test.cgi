#!/usr/bin/env python3

import cgi
import subprocess
import cgitb
import webbrowser

print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

success_page = "successful.html"
error_page = "error.html"

if username and password:
	print("past if username<br>")
	command = ['./store_credentials.sh', username, password]
	print(command)
	print("<br>")
	try:
		print("About to run script")
		result = subprocess.run(command, check=True, capture_output=True, text=True)
		print("Script output:", result.stdout)
		print('<meta http-equiv="refresh" content="0; url=../successful.html">')
	except subprocess.CalledProcessError as e:
		print("Error occurred:", e.stderr)
		print('<meta http-equiv="refresh" content="0; url=../error.html">')
else:
	print("<h1>Error!</h1><p>No username provided</p>")
