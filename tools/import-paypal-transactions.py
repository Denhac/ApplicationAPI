#!/usr/bin/python

# Python includes
import csv, sys

# Our own includes go here
# insert() makes our path the first searched entry, as opposed to append()
sys.path.insert(0, '/var/www/denhacpkg')

from DenhacDbLibrary import *

if len(sys.argv) != 3:
	msg = """
Usage: ./import-paypal-transactions.py {filename} {notes}

##############################################
# Instructions for use:
# Log in to Paypal and navigate to Activity / Download
# Select "Custom Date Range" and enter your search range
# Choose "Comma Delimited - Balance Affecting Transactions" in the "File Types for Download" drop down selector
# Save that file and feed it to this script.
# Add notes that make sense for members, such as "Paypal Payment received: Jan"
##############################################
"""
	raise TypeError(msg)

filename = sys.argv[1]
notes    = sys.argv[2]

# Here's a quick dos2unix on our csv, just in case:
text = open(filename, 'rb').read().replace('\r\n', '\n')
open(filename, 'wb').write(text)

# Payment types to ignore
payment_type_ignore_list = ['Withdraw Funds to Bank Account','Invoice Sent','Request Received','Payment Sent','Temporary Hold','Debit Card Purchase']

# Open a DB connection
memberDb = DenhacMemberDb()
memberDb.startTransaction()

try:
	# Create a var to sum total dues collected
	numPayments = 0
	totalDues   = 0.0
	totalFees   = 0.0

	# Read and apply payments
	with open(filename, 'rb') as paymentfile:
		memreader = csv.DictReader(paymentfile, delimiter=',', quotechar='"')

		for row in memreader:
			(payment_type, from_email, to_email, name, gross, date, fee) = (str(row['Type']), str(row['From Email Address']), str(row['To Email Address']), str(row['Name']), str(row['Gross']), str(row['Date']), str(row['Fee']))

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
				totalDues   += float(gross)
				totalFees   += float(fee)
				numPayments += 1

			except IndexError:
				print '================================================'
				print 'Payment UNAPPLIED! Type: ' + payment_type + ', Name: ' + name + ', Amount: ' + gross + ', Date: ' + date + ', From Email: ' + from_email
				print 'Better do it manually or someone might be mad...'
				print '================================================'

	print '================================================'
	print '# of Payments: ' + str(numPayments)
	print 'Total Dues Collected: ' + str(totalDues)
	print 'Total Paypal Fees Paid: ' + str(totalFees) + ' <--- ****** Enter this into WaveApps manually ******'
	print '================================================'
	print 'Committing changes...'
	memberDb.commit()
	print 'Done!'

except:
	print 'We failed... rolling back'
	memberDb.rollback()
	print 'DB Changes rolled back.'
