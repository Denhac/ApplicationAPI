#!/usr/bin/python

# Python includes
import calendar, logging, sys
from datetime import date, datetime
from logging.handlers import RotatingFileHandler

# Our own includes go here
# insert() makes our path the first searched entry, as opposed to append()
sys.path.insert(0, '/var/www/denhacpkg')
from DenhacDbLibrary import DenhacMemberDb
from DenhacEmailLibrary import DenhacEmail

# SETUP LOGGER
appLogger = logging.getLogger('ImportLogger')
appLogger.propagate = False

# TODO - revert to INFO once we're stable
#appLogger.setLevel(logging.INFO)
appLogger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler = RotatingFileHandler('script_logs/monthly-invoice.log', backupCount=24)
handler.setFormatter(formatter)
handler.doRollover()	# Rotate the file every time we start up (that way we always know what to email at the end)
appLogger.addHandler(handler)

###############################
appLogger.debug("Starting up.")

memberDb = DenhacMemberDb()

# Bill all active members for the current month
notes = "Member Dues: " + str(calendar.month_name[date.today().month])

for member in memberDb.getActiveMembers():
    sql    = "INSERT INTO invoice (member_id, invoice_date, amount, notes) VALUES (%s,NOW(),%s,%s)"
    params = [member['id'], member['paymentAmount'], notes]

    memberDb.executeQueryNoResult(sql, params)
    appLogger.info('Created invoice for $' + str(member['paymentAmount']) + ' for member ' + member['lastName']) + ', ' + member['firstName'])

appLogger.debug("Done!")

with open('script_logs/monthly-invoice.log', 'r') as myfile:
	data = myfile.read()

	DenhacEmail.SendEmail(fromAddr = 'treasurer@denhac.org',
						  toAddr   = ['treasurer@denhac.org'],
						  subject  = 'Monthly Invoicing Program',
						  body     = data)
