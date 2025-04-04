import os

''' Expected usage:
from dotvars import getvar
x = getvar("db.test.username", default="root")
'''

_vars = {
  "db": {
    "test": {
      "server": "localhost",
      "dbname": "test_db",
      "username": "testuser",
      "password": "tester12#$",
    },
    "dev": {
      "server": "localhost",
      "dbname": "dev_db",
      "username": "devuser",
      "password": "devisdev@1",
    },
    "prod": {
      "server": "db.example.com",
      "dbname": "app",
      "username": "appuser",
      "password": os.getenv("MSQL_PASSWORD"),
    },
  },
  "web": {
    "test": "http://test.example.com",
    "dev": "http://dev.example.com",
    "prod": "https://www.example.com",
  },
  "command": "C:\\Apps\\python.exe" if os.name == "nt" else "python3",
}


def getvar(dotname, default=None):
  val = digvar(dotname)
  return val if val else default
# -- end getvar()


def digvar(dotname, dotdict=_vars):
  if "." in dotname:
    dotname, nextname = dotname.split(".", 1)
    nextdict = dotdict.get(dotname, {})
    val = digvar(nextname, nextdict)
  else:
    val = dotdict.get(dotname, None)
  return val
# -- end digvar()
