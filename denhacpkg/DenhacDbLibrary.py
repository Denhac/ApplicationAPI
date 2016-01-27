#!/usr/bin/python
# Digimonkey
# Apr 2015

# Import Python mysql bindings
import MySQLdb

# File that stores environment-specific configs like URLs, usernames, etc.
import envproperties

# The Python 2.6-and-later way to define abstract base classes
# See http://dbader.org/blog/abstract-base-classes-in-python for further details why you want this.
from abc import ABCMeta, abstractmethod

# Other imports
from collections import defaultdict

class DenhacDb:
    __metaclass__   = ABCMeta
    _connect        = None
    _lastUsedCursor = None

    # This method is overrided by the child classes
    @abstractmethod
    def connect(self):
        pass

    def executeQueryNoResult(self, sql, params):
        self.connect()
        cursor = self._connect.cursor()
        cursor.execute(sql, params)
        self._connect.commit()
        cursor.close()

    def executeQueryGetCursor(self, sql, params):
        self.connect()
        self._lastUsedCursor = self._connect.cursor(MySQLdb.cursors.DictCursor)
        self._lastUsedCursor.execute(sql, params)
        return self._lastUsedCursor

    def executeQueryGetAllRows(self, sql, params):
        cur = self.executeQueryGetCursor(sql, params)
        return cur.fetchall()

    # Best practice to always explicitly close!
    def __del__(self):
        if self._lastUsedCursor is not None:
            self._lastUsedCursor.close()
        if self._connect is not None:
            self._connect.close()

class DenhacMemberDb(DenhacDb):
    def connect(self):
        if self._connect is None:
            self._connect = MySQLdb.connect(envproperties.member_db_server, envproperties.member_db_user, envproperties.member_db_password, envproperties.member_db_schema)

    def getActiveMembers(self):
        sql = "SELECT * FROM member WHERE active = 1"
        return self.executeQueryGetAllRows(sql, None)

    def getMemberByADUsername(self, username):
        sql    = "SELECT * FROM member WHERE ad_username = %s"
        params = [username]
        return self.executeQueryGetAllRows(sql, params)[0]

    def createPayment(self, member_id, amount, payment_type_id, notes):
        sql = "INSERT INTO payment (member_id, payment_date, amount, payment_type_id, notes) VALUES (%s,NOW(),%s,%s,%s)"
        params = [member_id, amount, payment_type_id, notes]
        self.executeQueryNoResult(sql, params)

    def getBalance(self, member_id):
        sql = """select inv_total.a - pmnt_total.a as balance
              from
              (select coalesce(sum(amount), 0.0) a
              from member m, invoice i
              where m.id = i.member_id
              and m.id = %s) inv_total,
              (select coalesce(sum(amount), 0.0) a
              from member m, payment p
              where m.id = p.member_id
              and m.id = %s) pmnt_total"""
        params = [member_id, member_id]
        return self.executeQueryGetAllRows(sql, params)[0]['balance']


# Not tested yet
#    def getMember(self, id):
#        sql    = "SELECT * FROM member WHERE id = %s"
#        params = [id]
#        return self.executeQueryGetAllRows(sql, params)[0]






# TODO - DEPRECATE THIS CLASS
class DenhacGnucashDb(DenhacDb):
    def connect(self):
        if self._connect is None:
            self._connect = MySQLdb.connect(envproperties.gnc_db_server, envproperties.gnc_db_user, envproperties.gnc_db_password, envproperties.gnc_db_schema)

    # Mark's query - automated!
    def memberPaymentReport(self, startDate, endDate):
        sql = """
            /* For invoices created via API */
            SELECT c.name as name, c.id as customer_id, i.id as invoice_id,
                    cast(i.date_posted as char) as date_posted,
                    s.value_num as value, s.action as action
            FROM invoices i, splits s, customers c
            WHERE i.post_lot = s.lot_guid
              AND i.owner_guid = c.guid
              AND date_posted > %s AND date_posted < %s
            UNION
            /* For invoices created via the UI */
            SELECT c.name as name, c.id as customer_id, i.id as invoice_id,
                    cast(i.date_posted as char) as date_posted,
                    s.value_num as value, s.action as action
            FROM invoices i, splits s, customers c, jobs j
            WHERE i.post_lot = s.lot_guid
            AND i.owner_guid = j.guid
            AND j.owner_guid = c.guid
            AND date_posted > %s AND date_posted < %s
            ORDER BY customer_id, action;
        """

        params = [startDate, endDate, startDate, endDate]
        rows = self.executeQueryGetAllRows(sql, params)

        resultHash = defaultdict(dict)  # Hash(with autovivication) to hold each invoice event

        # tabulatePayments
        for row in rows:
            entry      = {}
            memberName = row['name']
            postdate   = row['date_posted'][:7]   # First 7 characters = "yyyy-mm"
            action     = row['action']
            if ((action == "Lot Link") or (action == "Payment")):
                entry['paid']=1
            resultHash[memberName][postdate]=entry

        return resultHash