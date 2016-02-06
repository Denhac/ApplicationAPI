#!/usr/bin/python

from DenhacGncLibrary import DenhacGncSession, DenhacGncInvoice

from datetime import datetime, date

import sys

#path = './xml/denhac_xml.gnucash'
#path = 'mysql://gnucash:Hj0rgQ@10.0.100.136/gnucash'
path = 'mysql://gnucash:Hj0rgQ@10.0.101.249/gnucash'

mySession = DenhacGncSession(path)

try:
    member_id = "999"
#    member_name = "Script Mackdaddy"

#    invoice_id = "1002"
	# Generate Invoice ID
    today = datetime.today()
    year = today.year
    month = today.month
    invoice_id = str(year) + '-' + str(month) + '-' + member_id

    print "Invoice ID: ", invoice_id
    DenhacGncInvoice.invoiceMemberDues(mySession, member_id, 50, invoice_id)
    print "Blah2."



    mySession.saveAndEndSession()


except:
    print "Unexpected error:", sys.exc_info()[0]
    mySession.cancelSession()
    exit(1)
