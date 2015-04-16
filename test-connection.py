#!/usr/bin/python

from DenhacGncLibrary import DenhacGncSession, DenhacGncCustomer
import sys

#path = './xml/denhac_xml.gnucash'
path = 'mysql://gnucash:yourPasswordHere@localhost/gnucash'  #develop

#release : 'mysql://gnucash:Hj0rgQ@10.0.101.249/gnucash'

print "Starting to open session"
mySession = DenhacGncSession(path)
print "Session open"

try:
    member_id = "DM005"

    if DenhacGncCustomer.isExists(mySession.getBook(), member_id):
        customer = DenhacGncCustomer.getCustomerById(mySession.getBook(), member_id)
        print "Got customer: "+member_id
    else:
        print "Connection made, but customer not found!"

    mySession.EndSession()

except:
    mySession.cancelSession()
    exit(1)

