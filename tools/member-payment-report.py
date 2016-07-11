#!/usr/bin/python

# Python includes
import sys

# Our own includes go here
# insert() makes our path the first searched entry, as opposed to append()
sys.path.insert(0, '/var/www/denhacpkg')
from DenhacDbLibrary import DenhacMemberDb

def xstr(s):
    if s is None:
        return ''
    return str(s)

def istr(s):
    if s is None:
        return '0'
    return str(s)

memberDb = DenhacMemberDb()

print "ID, Name, Balance"

for member in memberDb.getActiveMembers():
	bal = memberDb.getBalance(member['id'])
	print xstr(member['id']) + ', ' + xstr(member['firstName']) + ' ' + xstr(member['lastName']) + ', ' + istr(bal)
