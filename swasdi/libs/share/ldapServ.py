try:
    import ldap3
except Exception:
    ldap3 = None

from swasdi.settings import LDAP_CONFIG


class authLDAP:
    _user = ''
    _pwd = ''
    _host = ''
    _searchBase = ''
    _adDomain = ''
    _is_Update = ''
    _attrMap = ''
    _attrb = []
    error = ''
    attributes_value = None

    def __init__(self, user, pwd, **kwargs):
        self._user = user
        self._pwd = pwd
        self.get_config()

    def get_config(self):
        self._host = LDAP_CONFIG.get('ldap_auth_url', None)
        self._searchBase = LDAP_CONFIG.get('ldap_auth_search_base', None)
        self._adDomain = LDAP_CONFIG.get('ldap_auth_Active_directory_domain', None)
        self._attrMap = LDAP_CONFIG.get('ldap_auth_user_attr_map', {})
        self._attrb = ['cn', 'givenName', 'name', 'sn', 'mailNickname', 'department',
                       'userAccountControl', 'sAMAccountName', 'mail']

    def authen(self):
        if not (self._user and self._pwd):
            self.error = 'User or Password is empty'
            return False

        if not (self._host and self._searchBase):
            self.error = 'Host (LDAP url) or search base is empty'
            return False

        if self._adDomain:
            ldapUser = '{}\\{}'.format(self._adDomain, self._user)
        else:
            ldapUser = self._user

        searchFilter = '(&(|(userPrincipalName={0})(sAMAccountName={0})(mail={0}))(objectClass=person))'.format(self._user)

        try:
            server = ldap3.Server(self._host, get_info=ldap3.ALL)
            conn = ldap3.Connection(server, user=ldapUser, password=self._pwd,
                                    authentication=ldap3.NTLM, auto_bind=True)

            if conn.bound:
                for key, value in self._attrMap.items():
                    if value not in self._attrb:
                        self._attrb.append(value)

            conn.search(search_base=self._searchBase,
                        search_filter=searchFilter,
                        search_scope=ldap3.SUBTREE,
                        attributes=self._attrb,
                        paged_size=5)

            self.attributes_value = {}
            for entry in conn.response:
                attrb_val = entry.get("attributes")
                if attrb_val:
                    self.attributes_value.update(dict(attrb_val))
                    user_ctl = attrb_val.get('userAccountControl')
                    if user_ctl & 0x0002:
                        self.error = 'User disable'
                        return False  # User Disable
                    elif user_ctl & 0x800000:
                        self.error = 'Password expire'
                        return False  # Password expire

            return conn.bound

        except Exception as e:
            self.error = str(e)
            return False
