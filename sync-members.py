#!/usr/bin/python

import MySQLdb
import sys
from urlparse import urlparse

server, user, password, db = [""]*4
with open('creds.config') as f:
    for curLine in f.readlines():
        if (curLine[0] != '#'):
            parts = urlparse(curLine.strip())
            server = parts.hostname
            user = parts.username
            password = parts.password
            db = parts.path[1:]
db = MySQLdb.connect(server, user, password, db)
# The DictCursor lets us reference results by column name
cursor = db.cursor(MySQLdb.cursors.DictCursor) 
select_sql = "SELECT * FROM customers"
# Errors will bubble up to console as desired so no need to try/catch
cursor.execute(select_sql)

# Now look up each member and make sure values exist and are in sync
memCheck_sql = "SELECT * FROM dh_members WHERE id=%s"
memInsert_sql = "INSERT INTO dh_members (id, memberType, autoPay) VALUES (%s, %s, %s)"
memUpdate_sql = "UPDATE dh_members SET memberType=%s WHERE id=%s"
memCursor = db.cursor(MySQLdb.cursors.DictCursor)
for gncRow in cursor.fetchall():
    # Both conditions need to know what the member type should be
    memType = ""
    if gncRow["id"].startswith("DM"):
        memType = "M"
    elif gncRow["id"].startswith("DSM"):
        memType = "S"
    elif gncRow["id"].startswith("DFM"):
        memType = "F"
    else:
        print "Invalid member id ".gncRow["id"]
        continue
    memCursor.execute(memCheck_sql, [gncRow["id"]])
    if (memCursor.rowcount == 0):
        # Create a new member row
	memCursor.execute(memInsert_sql, [gncRow["id"], memType, 0])
        print "Created dh_members row for "+gncRow["id"]
    else:
        # Double check the member field but otherwise move on
        memRow = memCursor.fetchone()
        if (memRow["id"] != gncRow["id"]):
            memCursor.execute(memUpdate_sql, [memType, memRow["id"]])
            print "Updated dh_members member type for "+gncRow["id"]

db.commit()

