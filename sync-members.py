#!/usr/bin/python
from DenhacGncLibrary import DenhacDb
import sys

myDb = DenhacDb()

custCursor = myDb.executeQueryGetCursor("SELECT * FROM customers")

for gncRow in cursor.fetchall():
    # Both conditions need to know what the member type should be
    # TODO - GET THIS FROM THE DB?
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

    memCursor = myDb.executeQueryGetCursor("SELECT * FROM dh_members WHERE id=%s", [gncRow["id"]])
    if (memCursor.rowcount == 0):
        # Create a new member row
        myDb.executeQueryNoResult("INSERT INTO dh_members (id, memberType, autoPay) VALUES (%s, %s, %s)", [gncRow["id"], memType, 0])
        print "Created dh_members row for "+gncRow["id"]
    else:
        # Double check the member field but otherwise move on
        memRow = memCursor.fetchone()
        if (memRow["id"] != gncRow["id"]):

            myDb.executeQueryNoResult("UPDATE dh_members SET memberType=%s WHERE id=%s", [memType, memRow["id"]])
            print "Updated dh_members member type for "+gncRow["id"]
