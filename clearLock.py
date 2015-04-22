#!/usr/bin/python

#import MySQLdb
#from urlparse import urlparse

from DenhacGncLibrary import DenhacDb

#server, user, password, db = [""]*4
#with open('creds.config') as f:
#    for curLine in f.readlines():
#        if (curLine[0] != '#'):
#            parts = urlparse(curLine.strip())
#            server = parts.hostname
#            user = parts.username
#            password = parts.password
#            db = parts.path[1:]


#db = MySQLdb.connect(server, user, password, db)

#cursor = db.cursor()
#deleteLock_sql = "DELETE FROM gnclock;"

# Errors will bubble up to console as desired so no need to try/catch
#cursor.execute(deleteLock_sql)
#db.commit()

myDb = DenhacDb()
DenhacDb.executeQueryNoResult("DELETE FROM gnclock;")

print "Lock Cleared"
