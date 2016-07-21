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

    def getMemberByPaypalEmail(self, paypal_email):
        sql    = "SELECT * FROM member WHERE paypal_email = %s"
        params = [paypal_email]
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

    def searchMemberName(self, search_str):
        search_str = '%' + search_str + '%'
        sql = "SELECT id, lastName, firstName, middleInitial, gnuCashId, paymentAmount, active, onAutoPay, contact_email, paypal_email FROM member WHERE firstName like %s or lastName like %s or ad_username like %s"
        params = [search_str, search_str, search_str]
        return self.executeQueryGetAllRows(sql, params)

    def getPaymentTypes(self):
        sql = "SELECT * FROM payment_type"
        return self.executeQueryGetAllRows(sql, [])

    def getOpenBalances(self):
        sql = """select inv_total.a - pmt_total.a as balance, m2.*
                from
                (select m.id, coalesce(sum(amount), 0.0) a
                from member m, invoice i
                where m.id = i.member_id
                group by m.id) inv_total,
                (select m.id, coalesce(sum(amount), 0.0) a
                from member m, payment p
                where m.id = p.member_id
                group by m.id) pmt_total,
                member m2
                where m2.id = inv_total.id
                and   m2.id = pmt_total.id
                and (inv_total.a - pmt_total.a) > 0
                order by (inv_total.a - pmt_total.a) desc"""
        return self.executeQueryGetAllRows(sql, [])

    def getMember(self, id):
        sql    = "SELECT * FROM member WHERE id = %s"
        params = [id]
        return self.executeQueryGetAllRows(sql, params)

    def getMemberBalance(self, member_id):
        sql = """select invoice_date as transaction_date, amount, 'Invoice' as type, notes
                from invoice where member_id = %s
                union all
                select payment_date, -amount, pt.description as type, notes
                from payment p, payment_type pt
                where member_id = %s
                and pt.id = p.payment_type_id
                order by transaction_date desc"""
        return self.executeQueryGetAllRows(sql, [member_id,member_id])

    def setMemberFieldDefaults(self, fields):
        # Check for all required fields
        if  ('lastName' not in fields or
            'firstName' not in fields or
            'birthdate' not in fields or
            'streetAddress1' not in fields or
            'zipCode' not in fields or
            'phoneNumber' not in fields or
            'paymentAmount' not in fields or
            'contact_email' not in fields or
            'paypal_email' not in fields or
            'join_date' not in fields or
            'prox_card_id' not in fields):

            raise ValueError("Missing a required field.")

        # Fill in any empty non-default, non-required values in our fields array
        if 'middleInitial' not in fields:
            fields['middleInitial'] = ''
        if 'streetAddress2' not in fields:
            fields['streetAddress2'] = ''
        if 'city' not in fields:
            fields['city'] = ''
        if 'businessPhone' not in fields:
            fields['businessPhone'] = ''
        if 'emerContact1' not in fields:
            fields['emerContact1'] = ''
        if 'emerPhone1' not in fields:
            fields['emerPhone1'] = ''
        if 'emerAddress1' not in fields:
            fields['emerAddress1'] = ''
        if 'emerRelation1' not in fields:
            fields['emerRelation1'] = ''
        if 'emerContact2' not in fields:
            fields['emerContact2'] = ''
        if 'emerPhone2' not in fields:
            fields['emerPhone2'] = ''
        if 'emerAddress2' not in fields:
            fields['emerAddress2'] = ''
        if 'emerRelation2' not in fields:
            fields['emerRelation2'] = ''
        if 'medicalHealthProblems' not in fields:
            fields['medicalHealthProblems'] = ''
        if 'gnuCashId' not in fields:
            fields['gnuCashId'] = ''
        if 'active' not in fields:
            fields['active'] = '1'
        if 'onAutoPay' not in fields:
            fields['onAutoPay'] = '0'
        if 'isManager' not in fields:
            fields['isManager'] = '0'
        if 'isAdmin' not in fields:
            fields['isAdmin'] = '0'
        if 'ad_username' not in fields:
            fields['ad_username'] = ''
        if 'prox_card_id' not in fields:
            fields['prox_card_id'] = ''

        return fields

    def createMember(self, fields):
        # Check for required fields and fill in any default values not specified
        fields = self.setMemberFieldDefaults(fields)

        sql = """INSERT INTO `memberdb`.`member`
                (`lastName`,`firstName`,`middleInitial`,`birthdate`,`streetAddress1`,`streetAddress2`,`city`,
                `zipCode`,`phoneNumber`,`businessNumber`,`emerContact1`,`emerPhone1`,`emerAddress1`,`emerRelation1`,
                `emerContact2`,`emerPhone2`,`emerAddress2`,`emerRelation2`,`medicalConditionList`,`paymentAmount`,`active`,
                `onAutoPay`,`isManager`,`isAdmin`,`ad_username`,`contact_email`,`paypal_email`,`join_date`,`prox_card_id`)
                VALUES
                (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                """

        params = [fields['lastName'], fields['firstName'], fields['middleInitial'], fields['birthdate'], fields['streetAddress1'], fields['streetAddress2'], fields['city'],
                  fields['zipCode'], fields['phoneNumber'], fields['businessPhone'], fields['emerContact1'], fields['emerPhone1'], fields['emerAddress1'], fields['emerRelation1'],
                  fields['emerContact2'], fields['emerPhone2'], fields['emerAddress2'], fields['emerRelation2'], fields['medicalHealthProblems'], fields['paymentAmount'], fields['active'],
                  fields['onAutoPay'], fields['isManager'], fields['isAdmin'], fields['ad_username'], fields['contact_email'], fields['paypal_email'], fields['join_date'], fields['prox_card_id']]

        self.executeQueryNoResult(sql, params)

    def editMember(self, member_id, fields):
        # Check for required fields and fill in any default values not specified
        fields = self.setMemberFieldDefaults(fields)

        sql = """UPDATE `memberdb`.`member`
                SET
                `lastName` = %s,
                `firstName` = %s,
                `middleInitial` = %s,
                `birthdate` = %s,
                `streetAddress1` = %s,
                `streetAddress2` = %s,
                `city` = %s,
                `zipCode` = %s,
                `phoneNumber` = %s,
                `businessNumber` = %s,
                `emerContact1` = %s,
                `emerPhone1` = %s,
                `emerAddress1` = %s,
                `emerRelation1` = %s,
                `emerContact2` = %s,
                `emerPhone2` = %s,
                `emerAddress2` = %s,
                `emerRelation2` = %s,
                `medicalConditionList` = %s,
                `paymentAmount` = %s,
                `active` = %s,
                `onAutoPay` = %s,
                `isManager` = %s,
                `isAdmin` = %s,
                `ad_username` = %s,
                `contact_email` = %s,
                `paypal_email` = %s,
                `join_date` = %s,
                `prox_card_id` = %s
                WHERE `id` = %s
                """

        params = [fields['lastName'], fields['firstName'], fields['middleInitial'], fields['birthdate'], fields['streetAddress1'], fields['streetAddress2'], fields['city'],
                  fields['zipCode'], fields['phoneNumber'], fields['businessPhone'], fields['emerContact1'], fields['emerPhone1'], fields['emerAddress1'], fields['emerRelation1'],
                  fields['emerContact2'], fields['emerPhone2'], fields['emerAddress2'], fields['emerRelation2'], fields['medicalHealthProblems'], fields['paymentAmount'], fields['active'],
                  fields['onAutoPay'], fields['isManager'], fields['isAdmin'], fields['ad_username'], fields['contact_email'], fields['paypal_email'], fields['join_date'], fields['prox_card_id'],
                  member_id]

        self.executeQueryNoResult(sql, params)
