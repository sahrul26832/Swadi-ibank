from acorns.contrib.cryptvalue import decrypt_value_withkey
from kaen.route.contrib.auth import jwtAuthen
from swasdi.libs.share.ldapServ import authLDAP
from swasdi.settings import SECRET_KEY


class jwtAppAuthen(jwtAuthen):
    def auth_ldap(self):
        ldap_auth = authLDAP(user=self.user_login.username, pwd=self.user_login.password)
        rc = ldap_auth.authen()
        return rc


def decrypt_login(value=''):
    val_crypt = value.split(':')
    if len(val_crypt) < 2: return value
    if val_crypt[0] != 'enc': return value
    val_crypt = ':'.join(val_crypt[1:])
    return decrypt_value_withkey(value=val_crypt, keys=SECRET_KEY)
