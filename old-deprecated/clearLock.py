#!/usr/bin/python
from DenhacDbLibrary import DenhacDb, DenhacGnucashDb

myDb = DenhacGnucashDb()
myDb.executeQueryNoResult("DELETE FROM gnclock")

print "Lock Cleared"