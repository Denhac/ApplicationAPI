import sys
sys.path.insert(0, '/var/www/denhacpkg')
sys.path.insert(0, '/var/www/server')

from flask import Flask, request, session, flash, abort
from DenhacLdapLibrary import DenhacLdapLibrary

###### This is only invoked when run from the command-line from testing:
app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)
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
#
#		if not user:
#			return "User is required!"
#		if not pass:
#			return "Pass is required!"
#

	except KeyError:
		return "User and Password are required!"


	return "I am here."

	try:
		myLdap = DenhacLdapLibrary()
		myLdap.ldapBind(request.form['user'], request.form['password'])

		session['logged_in'] = True
		flash('You were logged in')
#        return redirect(url_for('show_entries'))

	except:
		return "Some exception somewhere!"


#@app.route('/logout')
#def logout():
#    session.pop('logged_in', None)
#    flash('You were logged out')
#    return redirect(url_for('show_entries'))
#
