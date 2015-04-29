#!/usr/bin/python

from DenhacGncLibrary import DenhacGncSession, DenhacGncCustomer
import sys

print "Starting to open session"
mySession = DenhacGncSession()
print "Session open"

try:
    member_id = "DM005"

    if DenhacGncCustomer.isExists(mySession, member_id):
        customer = DenhacGncCustomer.getCustomerById(mySession, member_id)
        print "Got customer: "+member_id
    else:
        print "Connection made, but customer not found!"

    mySession.endSession()

except:
    mySession.cancelSession()
    exit(1)
