#!/usr/bin/python
from DenhacLdapLibrary import DenhacLdapLibrary
import getpass
import sys


user   = raw_input("Username: ")
myPass = getpass.getpass(stream=None)


try:
	myLdap = DenhacLdapLibrary()
	myLdap.ldapBind(user, myPass)
	print "SUCCESS!"


except:
	import traceback
	print "Whoops, you fail."
	print '-'*60
	traceback.print_exc(file=sys.stdout)
	print '-'*60
