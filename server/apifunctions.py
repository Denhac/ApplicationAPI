import sys
sys.path.insert(0, '/var/www/denhacpkg')
sys.path.insert(0, '/var/www/server')

import envproperties
import time
from flask import Flask, request, session, render_template, redirect, url_for
from DenhacLdapLibrary import DenhacLdapLibrary
from DenhacJsonLibrary import DenhacJsonLibrary

app = Flask(__name__)

##########################################
###### This is only invoked when run from the command-line for testing:
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
##########################################
###### Used to encrypt the session cookies
app.secret_key = envproperties.session_key
##########################################

##########################################
## Global function to check if a user is logged in, and redirect him/her to /login if not
@app.before_request
def before_request():
	if 'logged_in' not in session and request.endpoint != 'login' and request.endpoint != 'main':
		return render_template('login.html', error = "You must be logged in to continue.")

	# TODO - roles checks go here.

##########################################

# Main page - login form to enter user/pw
@app.route('/')
def main():
	return render_template('login.html')

# Global error handler - any uncaught exceptions will go here.
@app.errorhandler(Exception)
def exception_handler(error):
	return DenhacJsonLibrary.ReplyWithError("ERROR: " + repr(error))

# Hello world tester (You still can't access this if you aren't logged in though - see @app.before_request)
@app.route("/hello")
def hello():
	return DenhacJsonLibrary.ObjToJson(dict(msg = "Goodbye, cruel world."))

# Login method - POSTed to here by index.html; could be called from anywhere
@app.route('/login', methods=['POST'])
def login():
	user     = None
	password = None

	try:
		if request.method == 'POST':
			user     = request.form['user']
			password = request.form['password']

		if not user or not password:
			raise KeyError

	except KeyError:
		return DenhacJsonLibrary.ReplyWithError("User and Password are required!")

	try:
		myLdap = DenhacLdapLibrary()
		myLdap.ldapBind(user, password)
	except:
		# Anti-bruteforcing; force a wait every few consecutive login failures
		session.pop('logged_in', None)
		if 'login_tries' not in session:
			session['login_tries'] = 1
		else:
			session['login_tries'] += 1

		if session['login_tries'] % 3 == 0:
			# Nope, if you're guessing, I'm throttling you to an avg of <1/sec.
			time.sleep(5)
			session.pop('login_tries', None)

		# Ok finally tell the user he/she failed
		return DenhacJsonLibrary.ReplyWithError("Invalid user name or password.")

	session['logged_in'] = True
	session['user']      = user
	session.pop('login_tries', None)
	return DenhacJsonLibrary.ObjToJson(dict(logged_in = "True"))

	# TODO - get roles from DB, store them here, and then check them in @app.before_request()



# Logout method
@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	return DenhacJsonLibrary.ObjToJson(dict(logged_out = "True"))










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
