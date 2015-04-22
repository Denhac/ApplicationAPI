#!/usr/bin/python

# Digimonkey
# Nov 2014

# With thanks to http://current.workingdirectory.net/posts/2011/gnucash-python-bindings/
# and many sample scripts here: http://svn.gnucash.org/trac/browser/gnucash/trunk/src/optional/python-bindings/example_scripts

import MySQLdb

import envproperties

import os
import sys
import warnings

from datetime import datetime, date, timedelta
from decimal import Decimal

from gnucash import Session, GncNumeric
from gnucash.gnucash_business import Customer, Invoice, Entry, BillTerm

class DenhacGncSession:
    _path = None
    _session = None
    _root = None
    _commod = None
    _currency = None

    def __init__(self, path):
        if os.path.exists(path + '.LCK'):
            raise AssertionError("""Lock file exists. Is GNUCash running?\n""")

        self._path = path
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self._session = Session(path, is_new = False)

        self._root = self.getBook().get_root_account()
        self._commod = self.getBook().get_table()
        self._currency = self._commod.lookup('CURRENCY', 'USD')

    def saveAndEndSession(self):
        self._session.save()
        self._session.end()

    def saveSession(self):
        self._session.save()

    def endSession(self):
        self._session.end()

    def cancelSession(self):
        self._session.end()
        self._session.destroy()

    def getBook(self):
        return self._session.book

    def getRoot(self):
        return self._session.book.get_root_account()

    def getCurrency(self):
        return self._currency

class DenhacGncCustomer:

    def getCustomerById(book, customer_id):
        return book.CustomerLookupByID(customer_id)

    def createCustomer(session, customer_id, customer_name):
        assert( isinstance(session, DenhacGncSession) )
        return Customer(session.getBook(), customer_id, session.getCurrency(), customer_name)

    def isExists(book, customer_id):
        if DenhacGncCustomer.getCustomerById(book, customer_id) is None:
            return False
        else:
            return True

    getCustomerById = staticmethod(getCustomerById)
    createCustomer = staticmethod(createCustomer)
    isExists = staticmethod(isExists)

# With further thanks to: svn.gnucash.org/trac/browser/gnucash/trunk/src/optional/python-bindings/example_scripts/simple_invoice_insert.py
class DenhacGncInvoice:

    def gnc_numeric_from_decimal(decimal_value):
        sign, digits, exponent = decimal_value.as_tuple()

        numerator = 0
        TEN = int(Decimal(0).radix()) # this is always 10
        numerator_place_value = 1
        for i in xrange(len(digits)-1,-1,-1):
            numerator += digits[i] * numerator_place_value
            numerator_place_value *= TEN

        if decimal_value.is_signed():
            numerator = -numerator

        if exponent < 0:
            denominator = TEN ** (-exponent)
        else:
            numerator *= TEN ** exponent
            denominator = 1

        return GncNumeric(numerator, denominator)

    def invoiceMemberDues(mySession, member_id, invoice_amount, invoice_id):
        assert( isinstance(mySession, DenhacGncSession) )

        # Find the Customer according to the member_id
        customer = DenhacGncCustomer.getCustomerById(mySession.getBook(), member_id)
        if customer is None:
            raise ValueError("No Customer found!")

        # Set the invoice ID and invoice_date
        # <year>-<month>-<member_id>
        today = datetime.today()
        year = today.year
        month = today.month
#        invoice_id = str(year) + '-' + str(month) + '-' + member_id
        invoice_date = date(year, month, 1)
        due_date = invoice_date+timedelta(days=30)
        print "Inside4."

        # Set invoice date (and due date) to the first of the month
        # TODO - for some reason Gnucash isn't taking this date; it takes whatever date it's created instead.
        invoice = Invoice(mySession.getBook(), invoice_id, mySession.getCurrency(), customer)
        invoice_value = DenhacGncInvoice.gnc_numeric_from_decimal(Decimal(invoice_amount))
        income_account = mySession.getRoot().lookup_by_name("Income - Member Dues")
        asset_account = mySession.getRoot().lookup_by_name("Assets")
        receivables_account = asset_account.lookup_by_name("Accounts Receivable")
        # Python bindings don't allow passthrough call to gncBillTermLookupByName with the right parameters.
        # This site couldn't find a way either https://github.com/cvonkleist/hackerspace-gnucash/blob/master/insert_invoices.py line 123
        # So we'll do the same hacky thing and lookup from an existing invoice
	bill_term = mySession.getBook().InvoiceLookupByID("000200").GetTerms();
        print "Inside5."

        invoice.SetTerms(bill_term)
        invoice_entry = Entry(mySession.getBook(), invoice)
        invoice_entry.SetInvTaxIncluded(False)
        invoice_entry.SetDescription("Member Dues")
        invoice_entry.SetQuantity(GncNumeric(1))
        invoice_entry.SetInvAccount(income_account)
        invoice_entry.SetInvPrice(invoice_value)

        print "asset_account", asset_account
        print "receivables_account", receivables_account
        print "invoice_date", invoice_date
        invoice.PostToAccount(receivables_account, invoice_date, due_date, "", True, False)
        print "Invoice created successfully."

    gnc_numeric_from_decimal = staticmethod(gnc_numeric_from_decimal)
    invoiceMemberDues = staticmethod(invoiceMemberDues)

class DenhacDb:
    _connect = None

    def connect():
        if _connect is None:
            _connect = MySQLdb.connect(envproperties.dbserver, envproperties.dbuser, envproperties.dbpassword, envproperties.dbschema)

    def executeQueryNoResult(sql):
        Connect()

        # TODO - INPUT SANITIZING (LIKE NOW)
        cursor = _connect.cursor()
        cursor.execute(sql)
        db.commit()
