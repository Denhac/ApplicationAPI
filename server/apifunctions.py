import sys
sys.path.insert(0, '/var/www/denhacpkg')
sys.path.insert(0, '/var/www/server')
sys.path.insert(0, '/var/www/log')

import envproperties
import itertools
import logging
import time
from logging.handlers import RotatingFileHandler
from flask import Flask, request, session, render_template, redirect, url_for
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
## Global function to check if a user is logged in
@app.before_request
def before_request():
	if 'logged_in' not in session and request.endpoint != 'login' and request.endpoint != 'main':
		return DenhacJsonLibrary.ReplyWithError("You must be logged in.")

	# TODO - roles checks go here.

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
	return render_template('login.html')

# Hello world tester (You still can't access this if you aren't logged in though - see @app.before_request)
@app.route("/hello")
def hello():
	return DenhacJsonLibrary.ObjToJson(dict(msg = "Goodbye, cruel world."))

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
			username = request.form['username']
			password = request.form['password']

		if not username or not password:
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

	# TODO - get roles from DB, store them in session[], and then check them in @app.before_request()
	return DenhacJsonLibrary.ObjToJson(dict(logged_in = "True"))

# Logout method
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return DenhacJsonLibrary.ObjToJson(dict(logged_out = "True"))






# Helper fn to maintain same DB session across same Flask session
#def getMemberDb():
#	if 'member_db' not in session:
#		session['member_db'] = DenhacMemberDb()
#	return session['member_db']
#  TODO - THIS ISN'T WORKING BECAUSE OF SOME FOOL JSON ERROR



# Mark's query - phase 1
@app.route('/pastduemembers')
def pastduemembers():

	memberDb = DenhacMemberDb()

	sql = """
		SELECT c.name, c.id, i.id, i.date_posted, s.value_num, s.action
		FROM invoices i, splits s, customers c
		WHERE i.post_lot = s.lot_guid
		  AND i.owner_guid = c.guid
/*		  AND date_posted > %s AND date_posted < %s
*/
		  AND date_posted > '2015-07-01'
		ORDER BY i.id, s.action;
	"""

	cur = memberDb.executeQueryGetCursor(sql)

	desc = cur.description
	rows = [dict(itertools.izip([col[0] for col in desc], row)) 
		for row in cur.fetchall()]

	return DenhacJsonLibrary.ObjToJson(dict(rows = rows))






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
