#!/usr/bin/python

from DenhacGncLibrary import DenhacGncSession, DenhacGncCustomer
import sys

mySession = DenhacGncSession()

try:
    member_id = "999"
    member_name = "Script Mackdaddy"

    if DenhacGncCustomer.isExists(mySession.getBook(), member_id):
        print "OMG member already exists as a Customer! Getting Customer..."
        customer = DenhacGncCustomer.getCustomerById(mySession.getBook(), member_id)
        print "Got customer."
    else:
        DenhacGncCustomer.createCustomer(mySession, member_id, member_name)
        print "New member created!"

    mySession.saveAndEndSession()

except:
    mySession.cancelSession()
    exit(1)
