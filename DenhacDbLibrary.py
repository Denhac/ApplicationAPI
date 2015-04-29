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
    __metaclass__ = ABCMeta
    _connect = None
    _lastUsedCursor = None

    @abstractmethod
    def connect(self):
        pass

    def executeQueryNoResult(self, sql):
        self.connect()
        cursor = self._connect.cursor()
        cursor.execute(sql)
        self._connect.commit()
        cursor.close()

    def executeQueryGetCursor(self, sql):
        self.connect()
        cursor = self._connect.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(sql)
        self._lastUsedCursor = cursor
        return cursor

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
