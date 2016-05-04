#!/usr/bin/python
# Digimonkey
# Oct 2015

import envproperties
import datetime, json

class DenhacJsonLibrary:

	def __init__(self):
		pass

	def JsonDefaultMappings(value):
		if isinstance(value, datetime.date):
			return dict(year=value.year, month=value.month, day=value.day)
		else:
			return value.__dict__

	def ObjToJson(obj):
		#return json.dumps(obj, default=lambda o: o.__dict__)
		return json.dumps(obj, default=DenhacJsonLibrary.JsonDefaultMappings)

	def JsonToObj(jsonStr):
		return json.loads(jsonStr)

	def ReplyWithError(msg):
		return DenhacJsonLibrary.ObjToJson(dict(errorMsg = msg))
		# TODO - abort(500) and create a custom error page template, to pass this errorMsg to.

	# Python 2.x way of declaring static functions
	JsonDefaultMappings = staticmethod(JsonDefaultMappings)
	ObjToJson           = staticmethod(ObjToJson)
	JsonToObj           = staticmethod(JsonToObj)
	ReplyWithError      = staticmethod(ReplyWithError)
