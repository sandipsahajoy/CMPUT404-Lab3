#!/usr/bin/env python3
import os, json, cgi

### Print python env variables as plain text
# print("Content-Type: text/plain")
# print() 
# print(os.environ)

### Print python env variables as json
# print("Content-Type: application/json")
# print()
# print(json.dumps(dict(os.environ), indent=2))

### Print query parameter data in html
# print("Content-Type:text/html")
# print()
# print("<p>QUERY_STRING: {}</p>".format(os.environ['QUERY_STRING']))

### Print user's browser parameter data in html
print("Content-Type:text/html")
print()
print("<p>HTTP_USER_AGENT: {}</p>".format(os.environ['HTTP_USER_AGENT']))
