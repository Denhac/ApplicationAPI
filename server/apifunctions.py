import sys
sys.path.insert(0, '/var/www/denhacpkg')
sys.path.insert(0, '/var/www/server')

import envproperties
from flask import Flask, request, session, flash, abort
from DenhacLdapLibrary import DenhacLdapLibrary


###### This is only invoked when run from the command-line from testing:
app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
######
###### Used to encrypt the session cookies
app.secret_key = envproperties.secret_key
######


@app.route("/hello")
def hello():
    return "Goodbye, cruel world."


@app.route("/abort")
def abort():
	abort(401)

@app.route("/flash")
def flash():
	flash("I am the Flash!")



@app.route('/login', methods=['GET', 'POST'])
def login():
	user     = None
	password = None

	try:
		if request.method == 'POST':
			user   = request.form['user']
			password = request.form['password']
		elif request.method == 'GET':
			user   = request.args.get("user")
			password = request.args.get("password")

	except KeyError:
		return "User and Password are required!"

#	try:
	myLdap = DenhacLdapLibrary()
	myLdap.ldapBind(user, password)

	session['logged_in'] = True
	return "You were logged in!!"

#	except:
#		return "You FAIL!"


#@app.route('/logout')
#def logout():
#    session.pop('logged_in', None)
#    flash('You were logged out')
#    return redirect(url_for('show_entries'))
#

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
