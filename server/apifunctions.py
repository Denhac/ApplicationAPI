import sys
sys.path.insert(0, '../denhacpkg')

from flask import Flask, request, session
from DenhacLdapLibrary import DenhacLdapLibrary



# This is only invoked when run from the command-line from testing:
app = Flask(__name__)
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)




@app.route("/hello")
def hello():
    return "Goodbye, cruel world."





@app.route('/login', methods=['GET', 'POST'])
def login():
	try:
		myLdap = DenhacLdapLibrary()
		myLdap.ldapBind(request.form['user'], request.form['pass'])

		session['logged_in'] = True
		flash('You were logged in')
#        return redirect(url_for('show_entries'))

	except:
		return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

