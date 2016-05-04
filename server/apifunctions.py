import sys
sys.path.insert(0, '/var/www/denhacpkg')
sys.path.insert(0, '/var/www/server')
sys.path.insert(0, '/var/www/log')

import envproperties
import itertools
import logging
import time
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
	file_handler.setLevel(logging.ERROR)
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
	admin_services   = ['hello']
	manager_services = ['memberpaymentreport', 'createMember', 'readMembers', 'readMember', 'createpayment', 'searchmember', 'getopenbalances']

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
	app.logger.error(exception)
	return DenhacJsonLibrary.ReplyWithError("Internal Server Error")

# Global error handler - any uncaught exceptions will go here.
@app.errorhandler(Exception)
def exception_handler(error):
	app.logger.error(error)
	return DenhacJsonLibrary.ReplyWithError("ERROR: " + repr(error))
####################################################################################

# Main page - login form to enter user/pw
@app.route('/')
def main():
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
	return DenhacJsonLibrary.ObjToJson(dict(msg = "Goodbye, cruel world."))

####################################################################################

def antiBruteForceLogic():
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
	memberDb = DenhacMemberDb()
	resultList = memberDb.getPaymentTypes()
	return DenhacJsonLibrary.ObjToJson(dict(rows = resultList))

@app.route('/getopenbalances')
def getopenbalances():
	memberDb = DenhacMemberDb()
	resultList = memberDb.getOpenBalances()
	return DenhacJsonLibrary.ObjToJson(dict(rows = resultList))






#@app.route('/createmember')
#def createmember():
#	return render_template('createmember.html')




####################################################################################

# TODO - DEPRECATE THIS SERVICE; WE'RE DONE WITH GNUCASH
@app.route('/memberpayment', methods=['GET'])
def memberpaymentreport():
	startDate = None
	endDate = None

	try:
		if request.method == 'GET':
			startDate = request.args['startdate']
			endDate = request.args['enddate']

		if not startDate or not endDate:
			raise KeyError

	except KeyError:
		return DenhacJsonLibrary.ReplyWithError("startdate and enddate are required!")

	gncDb = DenhacGnucashDb()
	results = gncDb.memberPaymentReport(startDate, endDate)
	return DenhacJsonLibrary.ObjToJson(dict(rows = results))













####################################################################################

@app.route('/members', methods=['GET'])
def readMembers():
	try:
		return 'readMembers: invoked';
		# TODO: connect to db from configuration
		# TODO: check role/permissions; only staff can see all members
		# TODO: render a template to display all members
	except:
		# TODO: return to login page or ... ?
		return render_template('login.html', error=error)

@app.route('/members', methods=['POST'])
def createMember():
	try:
		return 'createMember: invoked';
		# TODO: connect to db from configuration
		# TODO: check role/permissions
		# TODO: parse data and create new member record
	except: 
		# TODO: return to login page or ... ?
		return render_template('login.html', error=error)

@app.route('/members/<username>', methods=['GET'])
def readMember(username):
	try:
		return 'readMember: ' + username;
		# TODO: connect to db from configuration
		# TODO: check role/permissions
		# TODO: render a template for member name and balance
	except:
		# TODO: return to login page or ... ?
		return render_template('login.html', error=error)
