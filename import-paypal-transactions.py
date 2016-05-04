#!/usr/bin/python
from DenhacDbLibrary import *
import csv, sys

from datetime import date, datetime
import calendar

if len(sys.argv) != 2:
	msg = """
Usage: ./import-paypal-transactions.py {filename}

##############################################
# Instructions for use:
# Log in to Paypal and navigate to Activity / Download
# Select "Custom Date Range" and enter your search range
# Choose "Comma Delimited - Balance Affecting Transactions" in the "File Types for Download" drop down selector
# Save that file and feed it to this script.
##############################################
"""
	raise TypeError(msg)

# Open the csv file
filename = sys.argv[1]
notes = 'Paypal payment received: ' + str(calendar.month_name[date.today().month]) + ' ' + str(date.today().year)

# Here's a quick dos2unix on our csv, just in case
text = open(filename, 'rb').read().replace('\r\n', '\n')
open(filename, 'wb').write(text)

# Set the log file name to current time
logFileName = datetime.now().strftime('script_logs/import-paypal-transactions_%Y_%m_%d_%H_%M_%S.log')
logFile  = open(logFileName, 'w')

def log(msg):
    logFile.write(msg + '\n')
    print msg

# List of Payment types to ignore
payment_type_ignore_list = ['Withdraw Funds to Bank Account','Invoice Sent','Request Received','Payment Sent','Temporary Hold','Debit Card Purchase']

# Open a DB connection
memberDb = DenhacMemberDb()

# Create a var to sum total dues and fees collected
totalDues = 0.0
totalFees = 0.0
unappliedDues = 0.0

# Array to store subtotals for all payment types
subtotals = dict()

def addToSubtotal(payment_type, amount):
	if payment_type not in subtotals:
		subtotals[payment_type] = 0.0
	subtotals[payment_type] += float(amount)

# Read and apply payments
with open(filename, 'rb') as paymentfile:
	memreader = csv.DictReader(paymentfile, delimiter=',', quotechar='"')

	for row in memreader:
		(payment_type, from_email, to_email, name, gross, date, fee) = (str(row[' Type']), str(row[' From Email Address']), str(row[' To Email Address']), str(row[' Name']), str(row[' Gross']), str(row['Date']), str(row[' Fee']))

		addToSubtotal(payment_type, gross)

		# Check Payment Type
		if payment_type in payment_type_ignore_list:
			log('IGNORING Payment of Type: ' + payment_type)
			continue

		# Sometimes Paypal has the From and To email addresses backwards; I don't know why.
		email = from_email
		if email == 'treasurer@denhac.org':
			email = to_email

		# Ok, by this point we should have a payment.  Apply it.
		try:
			member = memberDb.getMemberByPaypalEmail(email)
			memberDb.createPayment(member['id'], gross, 3, notes)
			log('Payment Applied: ' + member['lastName'] + ', Amount: ' + gross)
			totalDues += float(gross)
			totalFees += float(fee)

		except IndexError:
			log('================================================')
			log('Payment UNAPPLIED! Type: ' + payment_type + ', Name: ' + name + ', Amount: ' + gross + ', Date: ' + date + ', From Email: ' + from_email)
			log('Better do it manually or someone might be mad...')
			log('================================================')
			unappliedDues += float(gross)

log('Done!')
log('SUBTOTALS:')
log('================================================')
for key, value in subtotals.items():
	log(key + ': ' + str(value))
log('================================================')
log('Total Dues Collected: ' + str(totalDues))
log('Total Unapplied Dues: ' + str(unappliedDues))
log('Total Paypal Fees Paid: ' + str(totalFees))
log('================================================')
