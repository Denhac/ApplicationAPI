#!/usr/bin/python
import smtplib, socket
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

import envproperties

class DenhacEmail:

	def __init__(self):
		pass

	# TODO - Enhance to send an attachment
	def SendEmail(fromAddr, toAddr, subject, body):

		# Ensure TO is a list...
		assert isinstance(toAddr, list)

		# Denhac logic - if on the dev server; append and prepend to Subject line
		if socket.gethostname() == 'devAPI.denhac.local':
			subject = '*TEST*TEST* ' + subject + ' *TEST*TEST*'

		# Build the message
		msg = MIMEMultipart()
		msg['From'] = fromAddr
		msg['To'] = COMMASPACE.join(toAddr)
		msg['Date'] = formatdate(localtime=True)
		msg['Subject'] = subject

		msg.attach(MIMEText(body))

#		# Send the email
		smtp = smtplib.SMTP(envproperties.smtp_server)

		# Login & Send
		smtp.starttls()
		smtp.login(envproperties.smtp_user, envproperties.smtp_password)

		smtp.sendmail(fromAddr, toAddr, msg.as_string())
		smtp.close()

	# Python 2.x way of declaring static functions
	SendEmail = staticmethod(SendEmail)
