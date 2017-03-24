import csv, io, itertools, logging, sys, time

sys.path.insert(0, '/var/www/denhacpkg')
sys.path.insert(0, '/var/www/server')
sys.path.insert(0, '/var/www/log')

import envproperties
from logging.handlers import RotatingFileHandler
from flask import Flask, request, session, render_template, redirect#, url_for
from DenhacLdapLibrary import DenhacLdapLibrary
from DenhacJsonLibrary import DenhacJsonLibrary
from DenhacDbLibrary import *

app = Flask(__name__)

####################################################################################
###### This is only invoked when run from the command-line for testing:
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
####################################################################################
###### Used to encrypt the session cookies
app.secret_key = envproperties.session_key
####################################################################################
###### Used to set up formatter for the logfile
if app.debug is not True:
	file_handler = RotatingFileHandler('/var/www/log/apifunctions.log', maxBytes=1024 * 1024 * 100, backupCount=20)
	file_handler.setLevel(logging.DEBUG)
	formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
	file_handler.setFormatter(formatter)
	app.logger.addHandler(file_handler)
####################################################################################


####################################################################################
##########  GLOBAL FUNCTIONS FOR ALL REQUESTS
####################################################################################
## Global function to check if a user is logged in and has permissions
@app.before_request
def before_request():
	"""
		Check for an active session and for proper permissions.

		This function is implicitly called at the beginning of every app.route call below.
		It returns http 500 with a permissions error if the user does not have the proper
		level of access.
	"""
	admin_services   = []
	manager_services = ['memberpaymentreport', 'createMember', 'readMembers', 'readMember', 'createpayment', 'searchmember', 'getopenbalances', 'getmember', 'getmemberbalance', 'importpaypaldata', 'createmember', 'editmember']

	# Ensure member is logged in to access any APIs
	if 'logged_in' not in session and request.endpoint != 'login' and request.endpoint != 'main':
		return DenhacJsonLibrary.ReplyWithError("You must be logged in.")

	# Ensure that admin services have admin privileges
	if request.endpoint in admin_services and not session['isAdmin']:
		return DenhacJsonLibrary.ReplyWithError("You do not have permissions for this service.")

	# Ensure that manager services have manager privileges
	if request.endpoint in manager_services and not session['isManager']:
		return DenhacJsonLibrary.ReplyWithError("You do not have permissions for this service.")
####################################################################################


# Global error handler for Internal Server Errors
@app.errorhandler(500)
def internal_error(exception):
	"""Catch any unhandled error and reply with http 500"""
	app.logger.error(exception)
	return DenhacJsonLibrary.ReplyWithError("Internal Server Error")

# Global error handler - any uncaught exceptions will go here.
@app.errorhandler(Exception)
def exception_handler(error):
	"""Catch any unhandled exception and reply with http 500"""
	app.logger.error(error)
	return DenhacJsonLibrary.ReplyWithError("ERROR: " + repr(error))
####################################################################################

# Main page - login form to enter user/pw
@app.route('/')
def main():
	"""Display the login form to the user."""
#	return render_template('login.html')
# TODO - WHY THE @#$%^ DO TEMPLATES WORK ON THE DEV API SERVER AND NOT THE PROD API SERVER???
	return '''
	<h2>Login</h2>
	<form action="login" method="post">
		<dl>
			<dt>Username:
			<dd><input type="text" name="username">
			<dt>Password:
			<dd><input type="password" name="password">
			<dd><input type="submit" value="Login">
		</dl>
	</form>
	'''

####################################################################################

# Hello world tester (You still can't access this if you aren't logged in though - see @app.before_request)
@app.route("/hello")
def hello():
	"""Simple hello world test service."""
	return DenhacJsonLibrary.ObjToJson(dict(msg = "Goodbye, cruel world."))

####################################################################################

def antiBruteForceLogic():
	"""
	Attempt to detect brute-force guessing of passwords, and force the user to wait.
	"""
	# Force a wait every few consecutive login failures
	session.pop('logged_in', None)
	if 'login_tries' not in session:
		session['login_tries'] = 1
	else:
		session['login_tries'] += 1

	if session['login_tries'] % 3 == 0:
		# Nope, if you're guessing, I'm throttling you to an avg of <1/sec.
		time.sleep(5)
		session.pop('login_tries', None)

# Login method - POSTed to here by index.html; could be called from anywhere
@app.route('/login', methods=['POST'])
def login():
	"""
	Login a user against the configured LDAP server, and save session data if valid.

	Access Level:		All
	Accepted methods:	POST

	Inputs:		username
				password
	Returns:	{"logged_in": "True", "username": <username>} or error
	"""
	username = None
	password = None

	try:
		if request.method == 'POST':
			# Will throw KeyError if vars not present
			username = request.form['username']
			password = request.form['password']

		if not username or not password:			# Detect the condition if a var is there but empty
			raise KeyError

	except KeyError:
		return DenhacJsonLibrary.ReplyWithError("Username and Password are required!")

	myLdap = DenhacLdapLibrary()
	try:
		myLdap.ldapBind(username, password)
	except:
		antiBruteForceLogic()
		return DenhacJsonLibrary.ReplyWithError("Invalid username or password.")

	session['logged_in'] = True
	session['username']  = username
	session.pop('login_tries', None)

	# Get this member's permissions from DB, store them in session[], and then check them in @app.before_request()
	memberDb = DenhacMemberDb()
	member   = memberDb.getMemberByADUsername(username)
	session['isAdmin']   = member['isAdmin']
	session['isManager'] = member['isManager']

	return DenhacJsonLibrary.ObjToJson(dict(logged_in = "True", username = username))

####################################################################################

# Logout method
@app.route('/logout')
def logout():
	"""Logout the requested user."""
	session.pop('logged_in', None)
	return DenhacJsonLibrary.ObjToJson(dict(logged_out = "True"))

####################################################################################

# Helper fn to maintain same DB session across same Flask session
#def getMemberDb():
#	if 'member_db' not in session:
#		session['member_db'] = DenhacMemberDb()
#	return session['member_db']
# TODO - THIS ISN'T WORKING BECAUSE OF SOME FOOL JSON ERROR
# See here: http://stackoverflow.com/questions/24035878/fixing-the-class-to-enable-object-storing-in-flask-session
# And here: http://stackoverflow.com/questions/21411497/flask-jsonify-a-list-of-objects

####################################################################################

@app.route('/createpayment', methods=['GET'])
def createpayment():
	"""
	Create a payment against a specific member's account.

	Access Level:		Manager
	Accepted methods:	GET

	Inputs:		member_id			The member ID in the DB
				amount				The amount to credit(+) or debit(-)
				payment_type_id		Links to an ID in the payment_type table
				notes				The memo field for the transaction
	Returns:	{"created": "True"} or error
	"""
	try:
		# Will throw KeyError if vars not present
		member_id       = request.args['member_id']
		amount          = request.args['amount']
		payment_type_id = request.args['payment_type_id']
		notes           = request.args['notes']

		# Will throw KeyError if present but empty
		if not member_id or not amount or not payment_type_id or not notes:
			raise KeyError

	except KeyError:
		return DenhacJsonLibrary.ReplyWithError("member_id and amount and payment_type_id and notes are required!")

	memberDb = DenhacMemberDb()
	memberDb.createPayment(member_id, amount, payment_type_id, notes)
	return DenhacJsonLibrary.ObjToJson(dict(created = "True"))

@app.route('/searchmember', methods=['GET'])
def searchmember():
	"""
	Search for a member in the DB.

	The service searches multiple fields, including first name, last name, and handle.
	Return any matching member in an array.

	Accepted methods: GET

	Inputs:		search_str			The string to search

	Returns: {"rows": [{"firstName": "string", "string": "DFM001", "lastName": "string", "paymentAmount": float, "middleInitial": "string", "contact_email": "string", "onAutoPay": bool, "active": bool, "paypal_email": "string", "id": int}]}
			or error
	"""

	try:
		# Will throw KeyError if vars not present
		search_str = request.args['search_str']

		# Will throw KeyError if present but empty
		if not search_str:
			raise KeyError

	except KeyError:
		return DenhacJsonLibrary.ReplyWithError("search_str is required!")

	memberDb = DenhacMemberDb()
	resultList = memberDb.searchMemberName(search_str)
	return DenhacJsonLibrary.ObjToJson(dict(rows = resultList))

@app.route('/getpaymenttypes')
def getpaymenttypes():
	"""Return a list of valid payment types from the DB."""
	memberDb = DenhacMemberDb()
	resultList = memberDb.getPaymentTypes()
	return DenhacJsonLibrary.ObjToJson(dict(rows = resultList))

@app.route('/getopenbalances')
def getopenbalances():
	"""
	Return an array of members and the balance owed for each.

	Access Level:		Manager
	Accepted methods:	GET

	Inputs:		none
	Returns:	{"rows": [{"businessNumber": "string", "prox_card_id": "string", "ad_username": "string", "driver_license": "string", "paypal_email": "string", "id": int, "city": "string", "paymentAmount": float, "isAdmin": int, "emerAddress2": "string", "emerAddress1": "string", "phoneNumber": "string", "onAutoPay": int, "emerRelation1": "string", "emerRelation2": "string", "streetAddress2": "string", "streetAddress1": "string", "isManager": int, "zipCode": "string", "contact_email": , "active": int, "emerPhone1": "string", "emerPhone2": "string", "firstName": "string", "gnuCashId": "string", "lastName": "string", "middleInitial": "string", "birthdate": "string", "join_date": "string", "emerContact2": "string", "emerContact1": "string", "balance": float, "medicalConditionList": "string"}]}
				or error
	"""
	memberDb = DenhacMemberDb()
	resultList = memberDb.getOpenBalances()
	return DenhacJsonLibrary.ObjToJson(dict(rows = resultList))

@app.route('/getmember', defaults={'member_id':'-1'})
@app.route('/getmember/<member_id>')
def getmember(member_id):
	"""
	Return a single member row by ID.

	Access Level:		Manager
	Accepted methods:	GET

	Inputs:		member_id
	Returns:	{"row": {"businessNumber": "string", "prox_card_id": "string", "ad_username": "string", "driver_license": "string", "paypal_email": "string", "id": int, "city": "string", "paymentAmount": float, "isAdmin": int, "emerAddress2": "string", "emerAddress1": "string", "phoneNumber": "string", "onAutoPay": int, "emerRelation1": "string", "emerRelation2": "string", "streetAddress2": "string", "streetAddress1": "string", "isManager": int, "zipCode": "string", "contact_email": , "active": int, "emerPhone1": "string", "emerPhone2": "string", "firstName": "string", "gnuCashId": "string", "lastName": "string", "middleInitial": "string", "birthdate": "string", "join_date": "string", "emerContact2": "string", "emerContact1": "string", "balance": float, "medicalConditionList": "string"}}
				or error
	"""
	memberDb = DenhacMemberDb()
	member   = memberDb.getMember(member_id)

	if member:
		return DenhacJsonLibrary.ObjToJson(dict(row = member[0]))

	return DenhacJsonLibrary.ObjToJson(dict())

@app.route('/getmemberbalance', defaults={'member_id':'-1'})
@app.route('/getmemberbalance/<member_id>')
def getmemberbalance(member_id):
	"""
	Return a single member balance by ID with all transaction rows

	Access Level:		Manager
	Accepted methods:	GET

	Inputs:		member_id
	Returns:	{"balance": float, "rows": [{"amount": float, "transaction_date": "string", "type": "string", "notes": "string"}]}
				or error
	"""
	memberDb = DenhacMemberDb()
	resultList = memberDb.getMemberBalance(member_id)

	balance = 0.0
	for row in resultList:
		balance += float(row['amount'])

	return DenhacJsonLibrary.ObjToJson(dict(rows = resultList, balance = balance))

@app.route('/importpaypaldata', methods=['POST'])
def importpaypaldata():
	"""DEPRECATING SOON.  DO NOT USE."""
	try:
		# If post, they're sending us the file.
		if request.method == 'POST':
			response = ""
			payment_type_ignore_list = ['Withdraw Funds to Bank Account','Invoice Sent','Request Received','Payment Sent','Temporary Hold','Debit Card Purchase','General Withdrawal']

			memberDb = DenhacMemberDb()
			numPayments  = 0
			numUnapplied = 0
			totalDues    = 0.0
			totalFees    = 0.0

			filedata = request.form['filedata']
			memreader = csv.DictReader(io.StringIO(filedata))

			for row in memreader:
				(payment_type, from_email, to_email, name, gross, date, fee) = (str(row['Type']), str(row['From Email Address']), str(row['To Email Address']), str(row['Name']), str(row['Gross']), str(row['Date']), str(row['Fee']))
				notes = "Paypal Payment: " + str(date)

				# Check Payment Type
				if payment_type in payment_type_ignore_list:
					response += 'IGNORING Payment of Type: ' + payment_type + '\n'
					continue

				# Sometimes Paypal has the From and To email addresses backwards; I don't know why.
				email = from_email
				if email == 'treasurer@denhac.org':
					email = to_email

				# Ok, by this point we should have a payment.  Apply it.
				try:
					# If we're missing the email address (for ex. from a website payment), ignore it and process next row
					if not email:
						raise IndexError

					member = memberDb.getMemberByPaypalEmail(email)
					memberDb.createPayment(member['id'], gross, 3, notes)

					app.logger.error('Payment Applied: ' + member['lastName'] + ', Amount: ' + gross)

					response    += 'Payment Applied: ' + member['lastName'] + ', Amount: ' + gross + '\n'
					totalDues   += float(gross)
					totalFees   += float(fee)
					numPayments += 1

				except IndexError:
					response += '================================================\n'
					response += 'Payment NOT APPLIED! Type: ' + payment_type + ', Name: ' + name + ', Amount: ' + gross + ', Date: ' + date + ', From Email: ' + from_email + '\n'
					response += 'Better do it manually or someone might be mad...\n'
					response += '================================================\n'

					app.logger.error('Payment NOT APPLIED! Type: ' + payment_type + ', Name: ' + name + ', Amount: ' + gross + ', Date: ' + date + ', From Email: ' + from_email)

					numUnapplied += 1
				except:
					return DenhacJsonLibrary.ReplyWithError("ERROR: Something failed for some reason.  Check the server logs for more details. Error: " + sys.exc_info()[0] + sys.exc_info()[1] + sys.exc_info()[2])

			response += 'Done!'
			response += '================================================\n'
			response += '# of Applied Payments: ' + str(numPayments) + '\n'
			response += '# of Unapplied Payments: ' + str(numUnapplied) + ' <--- ****** Enter these transactions into the Member DB manually ******\n'
			response += 'Total Dues Collected: ' + str(totalDues) + '\n'
			response += 'Total Paypal Fees Paid: ' + str(totalFees) + ' <--- ****** Enter this into WaveApps manually ******\n'
			response += '================================================\n'

			return DenhacJsonLibrary.ObjToJson(dict(response = response, numPayments = numPayments, numUnapplied = numUnapplied, totalDues = totalDues, totalFees = totalFees))
	except:
		return DenhacJsonLibrary.ReplyWithError("ERROR: Something failed for some reason.  Check the server logs for more details. Error: " + sys.exc_info()[0] + sys.exc_info()[1] + sys.exc_info()[2])

def setFieldsArray():
	"""
	Read POSTed form data and return a cleaned-up dict() of the fields that actually have data.

	This function is called from both the createmember and editmember services.
	"""
	fields = dict()

	# Required fields
	if 'lastName' in request.form and request.form['lastName'] != '':
		fields['lastName'] = request.form['lastName']
	if 'firstName' in request.form and request.form['firstName'] != '':
		fields['firstName'] = request.form['firstName']
	if 'birthdate' in request.form and request.form['birthdate'] != '':
		fields['birthdate'] = request.form['birthdate']
	if 'streetAddress1' in request.form and request.form['streetAddress1'] != '':
		fields['streetAddress1'] = request.form['streetAddress1']
	if 'zipCode' in request.form and request.form['zipCode'] != '':
		fields['zipCode'] = request.form['zipCode']
	if 'phoneNumber' in request.form and request.form['phoneNumber'] != '':
		fields['phoneNumber'] = request.form['phoneNumber']
	if 'paymentAmount' in request.form and request.form['paymentAmount'] != '':
		fields['paymentAmount'] = request.form['paymentAmount']
	if 'contact_email' in request.form and request.form['contact_email'] != '':
		fields['contact_email'] = request.form['contact_email']
	if 'paypal_email' in request.form and request.form['paypal_email'] != '':
		fields['paypal_email'] = request.form['paypal_email']
	if 'join_date' in request.form and request.form['join_date'] != '':
		fields['join_date'] = request.form['join_date']
	if 'prox_card_id' in request.form and request.form['prox_card_id'] != '':
		fields['prox_card_id'] = request.form['prox_card_id']

	# Non-required fields
	if 'middleInitial' in request.form and request.form['middleInitial'] != '':
		fields['middleInitial'] = request.form['middleInitial']
	if 'streetAddress2' in request.form and request.form['streetAddress2'] != '':
		fields['streetAddress2'] = request.form['streetAddress2']
	if 'city' in request.form and request.form['city'] != '':
		fields['city'] = request.form['city']
	if 'businessPhone' in request.form and request.form['businessPhone'] != '':
		fields['businessPhone'] = request.form['businessPhone']
	if 'emerContact1' in request.form and request.form['emerContact1'] != '':
		fields['emerContact1'] = request.form['emerContact1']
	if 'emerPhone1' in request.form and request.form['emerPhone1'] != '':
		fields['emerPhone1'] = request.form['emerPhone1']
	if 'emerAddress1' in request.form and request.form['emerAddress1'] != '':
		fields['emerAddress1'] = request.form['emerAddress1']
	if 'emerRelation1' in request.form and request.form['emerRelation1'] != '':
		fields['emerRelation1'] = request.form['emerRelation1']
	if 'emerContact2' in request.form and request.form['emerContact2'] != '':
		fields['emerContact2'] = request.form['emerContact2']
	if 'emerPhone2' in request.form and request.form['emerPhone2'] != '':
		fields['emerPhone2'] = request.form['emerPhone2']
	if 'emerAddress2' in request.form and request.form['emerAddress2'] != '':
		fields['emerAddress2'] = request.form['emerAddress2']
	if 'emerRelation2' in request.form and request.form['emerRelation2'] != '':
		fields['emerRelation2'] = request.form['emerRelation2']
	if 'medicalHealthProblems' in request.form and request.form['medicalHealthProblems'] != '':
		fields['medicalHealthProblems'] = request.form['medicalHealthProblems']
	if 'active' in request.form and request.form['active'] != '':
		fields['active'] = request.form['active']
	if 'onAutoPay' in request.form and request.form['onAutoPay'] != '':
		fields['onAutoPay'] = request.form['onAutoPay']
	if 'isManager' in request.form and request.form['isManager'] != '':
		fields['isManager'] = request.form['isManager']
	if 'isAdmin' in request.form and request.form['isAdmin'] != '':
		fields['isAdmin'] = request.form['isAdmin']
	if 'ad_username' in request.form and request.form['ad_username'] != '':
		fields['ad_username'] = request.form['ad_username']

	return fields

@app.route('/createmember', methods=['POST'])
def createmember():
	"""
	Create a new member in the DB.

	Access Level:		Manager
	Accepted methods:	POST

	Inputs:		***See the function setFieldsArray() above***
	Returns:	{"success": "True"}
				or error
	"""
	fields = setFieldsArray()

	memberDb = DenhacMemberDb()
	memberDb.createMember(fields)

	return DenhacJsonLibrary.ObjToJson(dict(success = True))

@app.route('/editmember/<member_id>', methods=['POST'])
def editmember(member_id):
	"""
	Edit a member in the DB.

	Access Level:		Manager
	Accepted methods:	POST

	Inputs:		***See the function setFieldsArray() above***
	Returns:	{"success": "True"}
				or error
	"""
	fields = setFieldsArray()

	memberDb = DenhacMemberDb()
	memberDb.editMember(member_id, fields)

	return DenhacJsonLibrary.ObjToJson(dict(success = True))
