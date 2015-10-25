import sys

from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)


sys.path.insert(0, '../denhacpkg')



@app.route("/hello")
def hello():
    return "Goodbye, cruel world."





@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))



try:
	myLdap = DenhacLdapLibrary()
	myLdap.ldapBind(user, myPass)
	print "SUCCESS!"


except:
	import traceback
	print "Whoops, you fail."
	print '-'*60
	traceback.print_exc(file=sys.stdout)
	print '-'*60
