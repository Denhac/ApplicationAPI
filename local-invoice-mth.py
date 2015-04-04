#!/usr/bin/python

from DenhacGncLibrary import DenhacGncSession, DenhacGncInvoice

from datetime import datetime, date

import sys

import csv

#path = 'mysql://gnucash:Hj0rgQ@10.0.101.249/gnucash'
path = 'mysql://gnucash:Hj0rgQ@10.0.101.111/gnucash'

mySession = DenhacGncSession(path)

# Read member_ids and amount from file
with open ('members.csv', 'rb') as csvfile:
    today = datetime.today()
    year = today.year
    #month = today.month
    month = today.strftime('%m')
    memreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in memreader:
	if (row['Bill'] == "Y"):
            invoice_id = str(year) + '-' + str(month) + '-' + row['Member ID']
            print "Creating invoice: (", row['Due'], ", ", invoice_id, ")"
            try:
                DenhacGncInvoice.invoiceMemberDues(mySession, row['Member ID'], row['Due'], invoice_id)
                print "Successfully created"
                mySession.saveSession()
            except:
                print "Error creating:", sys.exc_info()[0], sys.exc_info()[1]
                mySession.cancelSession()
                exit(1)
    mySession.endSession()
