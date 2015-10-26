#!/usr/bin/python
# Digimonkey
# Oct 2015

import envproperties
import json

class DenhacJsonLibrary:

	def __init__(self):
		pass

	def ObjToJson(obj):
		return json.dumps(obj, default=lambda o: o.__dict__)

	def JsonToObj(jsonStr):
		return json.loads(jsonStr)

	def ReplyWithError(msg):
		return DenhacJsonLibrary.ObjToJson(dict(errorMsg = msg))
		# TODO - abort(500) and create a custom error page template, to pass this errorMsg to.

	# Python 2.x way of declaring static functions
	ObjToJson      = staticmethod(ObjToJson)
	JsonToObj      = staticmethod(JsonToObj)
	ReplyWithError = staticmethod(ReplyWithError)
