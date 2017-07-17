from pprint import pprint
from ipahttp import ipahttp_revised


"""
Start a connection to the FreeIPA server
Expects a username and password, the server's IP or hostname and the domain that resides on the target server. 
Optionally, SSL cert checking can be enabled, disabled by default."""
ipa = ipahttp_revised.ipa(username='radioboy', password='Password!', domain='internal.denhac.org', server='ldap.internal.denhac.org', sslverify=False)


"""
Method: user_status
Obtains the user's last login time and number of failed logins.
Expects a valid username and optionally verbose can be set to 'True' for the entire FreeIPA response instead of the parsed response
"""
# pprint(ipa.user_status('radioboy', verbose=True), indent=4)


"""
Method: user_unlock
Unlock account with a given username
Expects username to unlock and returns response from FreeIPA server
"""
# pprint(ipa.user_unlock('radioboy'), indent=4)


"""
Method: user_find
Returns information about a specific user or all users if none are passed in
Optionally define a username or size limit. FreeIPA recommends not querying more than 40,000 users at once
"""
# pprint(ipa.user_find())
# OR
# pprint(ipa.user_find('radioboy'))

"""
Method: user_show
Displays most information about the user including what groups they are in, login shell, etc. Check `group_show` for easy group lookup.
Expects a username to look up. Optionally set verbose = True for the complete response from the server without parsing.
"""
# pprint(ipa.user_show('radioboy'), indent=4)

"""
Method: user_disable
Disable account with a given username.
Expects username to disable and returns response from FreeIPA server
"""
# pprint(ipa.user_disable('radioboy'), indent=4)

"""
Method: user_enable
Enables account with a given username
Expects username to enable and returns response from FreeIPA server
"""
# pprint(ipa.user_enable('radioboy'), indent=4)


"""
Method: user_add
Creates a new user on the FreeIPA host.
Expects firstname as str, lastname as str, fullname as str (Normally just firstname lastname but it doesn't really matter), email_list as list (i.e. [email] ), user_login as str (if left to None, one is generated), verbose as bool
The random_passwd is currently only working when set to True. Its left here for future improvements
"""
# pprint(ipa.user_add('Scott', 'Fraser', 'Scott Fraser', ['radioboy@denhac.org'], user_login='radioboy', verbose=True))

"""
Method: user_groups
Returns a list of groups a given user is a member of
Expects a username
"""
# pprint(ipa.user_groups('radioboy'), indent=4)

"""
Method: user_valid
Test if user credentials are valid. True for success and False for failure
This function will not return a normal bind and commands cannot be run against this return value
Expects a username and password
"""

# pprint(ipa.user_valid('radioboy', 'somekindofpassword'), indent=4)


"""
Method: group_show
----> Currently Broken <----
List all the users in a given group
Expects a valid group name. Returns FreeIPA response
"""
# pprint(ipa.group_show('board'), indent=4)

"""
Method: gen_username
Generates what *should* be a valid username automagically. Requires further testing as FreeIPA gave mixed results
Expects a firstname and a lastname to use as a base for the generation."""
# pprint(ipa.gen_username('Herp', 'Derp'), indent=4)

"""
Method: _setUpLoginSession
Logs into the remote server
Generally internal use but can be called elsewhere to start a session. 
Does not expect any parameters"""
# pprint(ipa._setUpLoginSession(), indent=4)

"""
Method: _checkCurrentSession
Check if the current session is still valid.
This method is run before every call, if session is not valid, it tries to log in and then make the calling request.
This shouldn't be needed outside but its there.
"""
# pprint(ipa._checkCurrentSession())

"""
Method: _makeRequest
Factory function to make requests at the server. 
Expects a dictionary of values to send to the remote server
"""
# pprint(ipa._makeRequest(pdict), indent=4)
