#!/bin/python

import json
import urllib2

# Load our environment config file
myprops = dict(line.strip().split('=') for line in open('./denhac.properties'))
host = myprops['api_server']
print host



data = json.load(urllib2.urlopen(host + "?service=getInvoice&invoice_id=2014-11-999"))
print data
print data["exists"]

data = json.load(urllib2.urlopen(host + "?service=getInvoice&invoice_id=idontexist"))
print data
print data["exists"]
