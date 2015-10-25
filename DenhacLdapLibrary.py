import envproperties
import ldap

class DenhacLdapLibrary:
	_ldap       = None
	_base       = "ou=Muggles,ou=Humans,ou=Denhac,dc=denhac,dc=local"
	_criteria   = "(objectClass=user)"
	_attributes = ['displayName']

	def __init__(self):
		self._ldap = ldap.initialize(envproperties.ldap_server)
		self._ldap.protocol_version = ldap.VERSION3
		self._ldap.set_option(ldap.OPT_REFERRALS, 0)

	def ldapBind(self, username, password):
		if not username.startswith('DENHAC\\'):
			username = 'DENHAC\\' + username

		bind    = self._ldap.simple_bind_s(username, password)
