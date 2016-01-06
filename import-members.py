#!/usr/bin/python
#from DenhacDbLibrary import DenhacDb, DenhacGnucashDb, DenhacMemberDb
from DenhacDbLibrary import *
import csv

memberDb = DenhacMemberDb()

# Read member_ids and amount from file
# Columns: Id,Name,GncId,Amount,Active
with open ('members.csv', 'rb') as csvfile:

	memreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

	for row in memreader:
		sql = """
			INSERT INTO `member`
				(`lastName`,
				`gnuCashId`,
				`paymentAmount`,
				`active`)
				VALUES
				(%s,%s,%s,%s);
		"""

		active = 1
		if row['Active'] == 'N':
			active = 0

		params = [row['Name'], row['GncId'], row['Amount'], active]
		memberDb.executeQueryNoResult(sql, params)

	print 'Done'