#!/usr/bin/python
from DenhacGncLibrary import DenhacGncSession, DenhacGncInvoice
from datetime import datetime, date
import sys
import csv

if ((len(sys.argv) < 4) or (len(sys.argv) > 5)):
    sys.exit('Usage: multi-month-invoice [member ID] [amount] [num months] [starting month(optional)]')

memberID = sys.argv[1]
amount = sys.argv[2]
numMths = int(sys.argv[3])
# Compute the starting month
today = datetime.today()
if (len(sys.argv) == 5):
    startMth = int(sys.argv[4])
else:
    startMth = today.month
startYr = today.year
#if (startMth < today.month):
#    # Must mean next year
#    startYr = today.year+1

print "Generating "+str(numMths)+" months of invoices for "+memberID+" beginning in "+str(startMth)+"/"+str(startYr)

mySession = DenhacGncSession()

curMth = startMth
curYr = startYr
while (numMths > 0):
    invoice_id = str(curYr)+'-'+format(curMth, '02')+'-'+memberID
    #TODO: Check if the invoice already exists
    invoice_date = date(curYr, curMth, 1)
    print "Creating invoice: (", invoice_id, ", ", str(amount), ")"
    try:
        DenhacGncInvoice.invoiceMemberDues(mySession, memberID, amount, invoice_id, invoice_date)
        print "Successfully created"
        mySession.saveSession()
    except:
        print "Error creating:", sys.exc_info()[0], sys.exc_info()[1]
        mySession.cancelSession()
        exit(1)
    numMths = numMths-1
    curMth = curMth+1
    if (curMth > 12):
        curMth = 1
        curYr = curYr + 1

mySession.endSession()
