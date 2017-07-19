# -[ipahttp]-------------------------------------------------------
# Original source: https://github.com/nordnet/python-freeipa-json
# Modified by Scott Fraser and Eric O'Connor for denhac, The Denver Hackerspace
# -----------------------------------------------------------------------------

import logging
import json
import requests

requests.packages.urllib3.disable_warnings()

VERSION = '1.0'

class ipa(object):
    def __init__(self, username, password, server, domain, sslverify=False, logger=None):
        self.username = username
        self.password = password
        self.server = server
        self.domain = domain
        self.sslverify = sslverify
        self.session = requests.Session()
        # self.cert = cert
        self.logger = logger or logging.getLogger(__name__)

        self._setUpLoginSession()

    def _checkCurrentSession(self):
        """
        Check if the IPA ping command works, if not call _setUpLoginSession
        """
        m = {"id": 0, "method": "ping/1", "params": [[] ,{"version": "2.213"} ] }

        try:
            resp = self._makeRequest(m)
        except:
            self.log.info('Session expired; logging in again')
            self._setUpLoginSession()
        else:
            return resp

    def _setUpLoginSession(self):
        """
        Gets valid session from FreeIPA server or raises `FreeIPALoginFailure`
        """
        # Get session variable or raise exception
        self.log.info('Attempting to obtain a valid session.')
        ipaurl = 'https://{0}/ipa/session/login_password'.format(self.server)
        header = {'referer': ipaurl, 'Content-Type':
            'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
        login = {'user': self.username, 'password': self.password}
        resp = self.session.post(ipaurl, headers=header, data=login, verify=self.sslverify)

        if resp.status_code == requests.codes.ok:
            self.log.info('Successfully logged in as {0}'.format(self.username))
            # set login_user for use when changing password for self
            self.login_user = self.username
        else:
            self.log.warning('Failed to log {0} in to {1}'.format(self.username, self.server))
            raise FreeIPALoginFailure('Failed to log {0} in to {1}'.format(self.username, self.server))

    def _makeRequest(self, pdict):
        """
        New function for making requests to FreeIPA
        Special request method for generating a username
        """
        ipaurl = 'https://{0}/ipa'.format(self.server)
        session_url = '{0}/session/json'.format(ipaurl)
        header = {'referer': ipaurl, 'Content-Type': 'application/json',
                  'Accept': 'application/json'}

        data = pdict

        self.log.debug('Making {0} request to {1}'.format(pdict['method'], session_url))

        resp = self.session.post(
                session_url, headers=header,
                data=json.dumps(data),
                verify=self.sslverify
        )

        if resp.status_code == requests.codes.ok:
            return resp.json()
        elif resp == None:
            raise FreeIPARequestFailed('The request returned no data')
        else:
            raise FreeIPARequestFailed('The request failed. General failure')

    def user_add(self, firstname, lastname, fullname, email_list, random_passwd=True, version="2.213", user_login=None, verbose=False):
        """
        Helper function to add user to FreeIPA.
        :param user_login: Username to be used to login
        :type user_login: str
        :param firstname: User's first name
        :type firstname: str
        :param lastname: User's last name
        :type lastname: str
        :param fullname: User's complete name
        :type fullname: str
        :param email_list: User's email in list format
        :type email_list: list
        :param random_passwd: Determine if a random password should be generated
        :type random_passwd: bool
        :param version: Version of the API to use
        :type version: str
        :return: Dictionary of values assigned to the user
        :rtype: dict
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        if user_login == None:
            # Get a valid username
            user_login = self.gen_user_name(firstname=firstname, lastname=lastname)

        m = {"id": 0, "method": "user_add/1", "params": [ [ user_login ], {"cn": fullname, "givenname": firstname, "sn": lastname, "mail": email_list, "random": random_passwd, "version": version}  ] }

        resp = self._makeRequest(m)

        if resp['error'] == None:
            if verbose:
                self.log.debug('Returning entire response')
                return resp
            else:
                self.log.debug('Returning parsed response')
                return resp['result']['result']
        else:
            raise FreeIPAUserError.UserAlreadyExists('A user already exists with {}'.format(user_login))

    def gen_user_name(self, firstname, lastname, version="2.213"):
        """
        Request a valid username from FreeIPA.
        :param firstname: User's first name
        :type firstname: str
        :param lastname: User's last name
        :type lastname: str
        :param version: Version of the API to use
        :type version: str
        :return: A username as a string
        :rtype: str
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        m = {"id": 0, "method": "command_defaults/1", "params": [ ["user_add/1"], {"kw": {"givenname": firstname, "sn": lastname },  "params": [ "uid" ], "version": version } ] }

        resp = self._makeRequest(m)

        if resp['error'] == None:
            return resp['result']['result']['uid']
        else:
            return resp

    def user_status(self, user, verbose= False):
        """
        Get current user's status
        :param user: Username
        :return: Dict with all data inside
        :rtype: dict
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        m = {"id": 0, "method": "user_status/1", "params": [[user], {"version": "2.213"}]}

        resp = self._makeRequest(m)

        if resp['error'] == None:
            if verbose:
                self.log.debug('Returning entire response')
                return resp
            else:
                self.log.debug('Returning parsed response')
                return resp['result']['result']
        else:
            raise FreeIPAUserError.UserNotFound('User \'{}\' was not found'.format(user))

    def user_show(self, user, verbose= False):
        """
        Obtain information about the user including groups

        Example:
        `ipa.user_show('radioboy')['result']['result']['memberof_group']`

        :param user: Username to query on server
        :type user: str
        :param verbose: Return entire json object or just the results data
        :return: Dict of user data
        :rtype: dict
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        m = {"id": 0, "method": "user_show/1", "params": [[user], {"version": "2.213"}]}

        if verbose:
            self.log.debug('Returning entire response')
            return self._makeRequest(m)
        else:
            self.log.debug('Returning parsed response')
            return self._makeRequest(m)['result']['result']

    def user_find(self, user=None, sizelimit=40000):
        # Not providing a user will return all users in FreeIPA
        # Check if there is a valid session
        self._checkCurrentSession()

        m = dict(id=0, method="user_find/1", params=[ [ user ], { "sizelimit": sizelimit, "version": "2.213" } ])

        return self._makeRequest(m)

    def user_disable(self, user, verbose=False):
        """
        Disable an accout with a given username (UID)
        :param user: Username to disable
        :return:
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        m = {"id": 0, "method": "user_disable/1", "params": [[user], { "version": "2.213" } ] }

        resp = self._makeRequest(m)

        if resp['error'] == None:
            if verbose:
                self.log.debug('Returning entire response')
                return resp
            else:
                self.log.debug('Returning parsed response')
                return resp['result']['result']
        else:
            raise FreeIPAUserError.UserAlreadyDisabled('{} is already disabled and cannot be disabled again.'.format(user))

    def user_enable(self, user, verbose= False):
        """
        Enable an account with a given username (UID)
        :param username: Username of account to enable
        :return:
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        m = {"id": 0, "method": "user_enable/1", "params": [[user], {"version": "2.213"}]}

        resp = self._makeRequest(m)

        if resp['error'] is None:
            if verbose:
                self.log.debug('Returning entire response')
                return resp
            else:
                self.log.debug('Returning parsed response')
                return resp['result']['result']
        else:
            raise FreeIPAUserError.UserAlreadyEnabled('{} is already disabled and cannot be disabled again.'.format(user))

    def user_unlock(self, user, verbose= False):
        """
        Unlock account with a given username (UID)
        :param user: Username of account to unlock
        :param verbose: True: Return all data sent by FreeIPA False: return only the data asked for
        :type verbose: bool
        :return: Return 'True' for success.
        :rtype: bool
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        m = {"id": 0, "method": "user_unlock/1", "params": [[user], {"version": "2.213"}]}

        resp = self._makeRequest(m)

        if verbose:
            return resp

        if resp['error'] != None:
            raise FreeIPAUserError.UserNotUnlocked(resp['result']['summary'])

        # return resp

    def user_groups(self, user, verbose= False):
        """
        Help function
        Given a username, return a list of groups
        :param user: Username as string
        :type user: str
        :return: List of groups user is in
        :rtype: list
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        resp = self.user_show(user, verbose=True)

        if verbose:
            return resp
        else:
            return resp['result']['result']['memberof_group']

    def group_show(self, group, verbose= False):
        """
        Return a list of users within a given group

        `ipa.group_show('members', verbose=False)`

        :param group: Group name as string
        :type group: str
        :param verbose: True: Return all data sent by FreeIPA False: return only the data asked for
        :type verbose: bool
        :return: list
        :rtype: list
        """
        # Check if there is a valid session
        self._checkCurrentSession()

        m = {'item': [group], 'method': 'group_show', 'params':
             {'all': True, 'raw': False}}
        results = self._makeReq(m)

        if results['error']:
            raise FreeIPAGroupDoesNotExist(results['error']['message'])

        if verbose:
            return [results]
        else:
            return results['result']['result']['member_user']

    def user_valid(self, username, password):
        """
        Test if user credentials are valid. True for success and False for failure
        This function will not return a normal bind and commands cannot be run against this
        :param username: Username to authenticate with
        :type username: str
        :param password: Password to authenticate with
        :type password: str
        :return: True for success; False for failure
        :rtype: bool
        """

        # Get session variable or raise exception
        self.log.info('Attempting to obtain a valid session.')
        ipaurl = 'https://{0}/ipa/session/login_password'.format(self.server)
        header = {'referer': ipaurl, 'Content-Type':
            'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
        login = {'user': username, 'password': password}
        resp = self.session.post(ipaurl, headers=header, data=login, verify=self.sslverify)

        if resp.status_code == requests.codes.ok:
            self.log.info('Successfully authenticated as{0}'.format(self.username))
            return True
        else:
            self.log.warning('Invalid credentials for {0}'.format(self.username, self.server))
            return False


class FreeIPAUserError(Exception):
    """General exceptions dealing with users"""

    class UserDoesNotExist(Exception):
        """Username does not exist in FreeIPA"""

    class UserAlreadyExists(Exception):
        """A user with that username already exists"""

    class UserNotUnlocked(Exception):
        """Failure to unlock user"""

    class UserAlreadyDisabled(Exception):
        """User is already disabled"""
    class UserAlreadyEnabled(Exception):
        """User is already enabled"""

    class UserNotFound(Exception):
        """Username was not found"""

class FreeIPALoginFailure(Exception):
    """Failure to log into FreeIPA server"""

class FreeIPAGroupDoesNotExist(Exception):
    """Group does not exist"""

class FreeIPARequestFailed(Exception):
    """The request failed. Are you logged in?"""
