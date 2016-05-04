#!/usr/bin/python
from DenhacDbLibrary import DenhacMemberDb

from datetime import date, datetime
import calendar

# Set filename to today's date
fileName = datetime.now().strftime('script_logs/monthly-invoice_%Y_%m_%d.log')
logFile  = open(fileName, 'w')

def log(msg):
    logFile.write(msg + '\n')
    print msg

memberDb = DenhacMemberDb()

notes  = "Member Dues: " + str(calendar.month_name[date.today().month])

for member in memberDb.getActiveMembers():
    sql    = "INSERT INTO invoice (member_id, invoice_date, amount, notes) VALUES (%s,NOW(),%s,%s)"
    params = [member['id'], member['paymentAmount'], notes]

    memberDb.executeQueryNoResult(sql, params)
    log('Created invoice for $' + str(member['paymentAmount']) + ' for member ' + member['lastName'])

log('Done!')

#TODO - cron it once monthly, and email us when it completes (either success or fail)
