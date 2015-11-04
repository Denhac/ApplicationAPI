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

class DenhacDb:
    __metaclass__   = ABCMeta
    _connect        = None
    _lastUsedCursor = None

    # This method is overrided by the child classes
    @abstractmethod
    def connect(self):
        pass

    def executeQueryNoResult(self, sql, params = None):
        self.connect()
        cursor = self._connect.cursor()
        cursor.execute(sql, params)
        self._connect.commit()
        cursor.close()

    def executeQueryGetCursor(self, sql, params = None):
        self.connect()
        self._lastUsedCursor = self._connect.cursor(MySQLdb.cursors.DictCursor)
        self._lastUsedCursor.execute(sql, params)
        return self._lastUsedCursor

#    def executeQueryReturnList(self, sql, params = None)
#        self.executeQueryGetCursor(sql, params)
#        return self.fetchAllIntoList()
#
#    # Thanks: http://stackoverflow.com/questions/22315919/how-to-get-all-mysql-tuple-result-and-convert-to-json
#    def fetchAllIntoList():
#        """Returns all rows from a cursor as a list of dicts"""
#        desc = self._lastUsedCursor.description
#        return [dict(itertools.izip([col[0] for col in desc], row)) 
#            for row in self._lastUsedCursor.fetchall()]

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

class DenhacGnucashDb(DenhacDb):
    def connect(self):
        if self._connect is None:
            self._connect = MySQLdb.connect(envproperties.gnc_db_server, envproperties.gnc_db_user, envproperties.gnc_db_password, envproperties.gnc_db_schema)
