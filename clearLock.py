#!/usr/bin/python

from DenhacGncLibrary import DenhacDb

myDb = DenhacDb()
myDb.executeQueryNoResult("DELETE FROM gnclock;")

print "Lock Cleared"