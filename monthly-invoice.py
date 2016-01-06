#!/usr/bin/python
from DenhacDbLibrary import DenhacMemberDb

from datetime import date
import calendar
import sys

memberDb = DenhacMemberDb()

notes  = "Member Dues: " + str(calendar.month_name[date.today().month])

for member in memberDb.getActiveMembers():
    sql    = "INSERT INTO invoice (member_id, invoice_date, amount, notes) VALUES (%s,NOW(),%s,%s)"
    params = [member['id'], member['paymentAmount'], notes]

    memberDb.executeQueryNoResult(sql, params)

print 'Done!' #TODO - print this to a log file and cron it once monthly
