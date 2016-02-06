#!/usr/bin/python
from DenhacDbLibrary import *
import csv, sys

if len(sys.argv) != 3:
	msg = """
Usage: ./import-paypal-transactions.py {filename} {notes}

##############################################
# Instructions for use:
# Log in to Paypal and navigate to Activity / Download
# Select "Custom Date Range" and enter your search range
# Choose "Comma Delimited - Completed Payments" in the "File Types for Download" drop down selector
# Save that file and feed it to this script.
##############################################
"""
	raise TypeError(msg)

filename = sys.argv[1]
notes    = sys.argv[2]

# Here's a quick dos2unix on our csv, just in case:
text = open(filename, 'rb').read().replace('\r\n', '\n')
open(filename, 'wb').write(text)

# Payment types to ignore
payment_type_ignore_list = ['Withdraw Funds to Bank Account','Invoice Sent','Request Received','Payment Sent']

# Open a DB connection
memberDb = DenhacMemberDb()

# Read and apply payments
with open(filename, 'rb') as paymentfile:
	memreader = csv.DictReader(paymentfile, delimiter=',', quotechar='"')

	for row in memreader:
		(payment_type, from_email, to_email, name, gross, date) = (str(row[' Type']), str(row[' From Email Address']), str(row[' To Email Address']), str(row[' Name']), str(row[' Gross']), str(row['Date']))

		# Check Payment Type
		if payment_type in payment_type_ignore_list:
			print 'IGNORING Payment of Type: ' + payment_type
			continue

		# Sometimes Paypal has the From and To email addresses backwards; I don't know why.
		email = from_email
		if email == 'treasurer@denhac.org':
			email = to_email

		# Ok, by this point we should have a payment.  Apply it.
		try:
			member = memberDb.getMemberByPaypalEmail(email)
			memberDb.createPayment(member['id'], gross, 3, notes)
			print 'Payment Applied: ' + member['lastName'] + ', Amount: ' + gross


		except IndexError:
			print '================================================'
			print 'Payment UNAPPLIED! Type: ' + payment_type + ', Name: ' + name + ', Amount: ' + gross + ', Date: ' + date
			print 'Better do it manually or someone might be mad...'
			print '================================================'

print 'Done!'
