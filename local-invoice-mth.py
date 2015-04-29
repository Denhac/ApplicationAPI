#!/usr/bin/python
from DenhacGncLibrary import DenhacGncSession, DenhacGncInvoice

from datetime import datetime, date
import sys
import csv

mySession = DenhacGncSession()

# Read member_ids and amount from file
with open ('members.csv', 'rb') as csvfile:
    today = datetime.today()

    memreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in memreader:
	if (row['Bill'] == "Y"):
            invoice_id = str(today.year) + '-' + str(today.month) + '-' + row['Member ID']
            print "Creating invoice: (", row['Due'], ", ", invoice_id, ")"
            try:
                DenhacGncInvoice.invoiceMemberDues(mySession, row['Member ID'], row['Due'], invoice_id, invoice_date = date(today.year, today.month, 1))
                print "Successfully created"
                mySession.saveSession()
            except:
                print "Error creating:", sys.exc_info()[0], sys.exc_info()[1]
                mySession.cancelSession()
                exit(1)
    mySession.endSession()
