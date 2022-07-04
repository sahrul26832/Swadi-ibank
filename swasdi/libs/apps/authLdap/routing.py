from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from swasdi.libs.contrib import routeBase
from swasdi.libs.apps.authLdap import serializer
from swasdi.libs.contrib.routeBase.route_crypt import DataRouts
from swasdi.libs.share.ldapServ import authLDAP

router = APIRouter(route_class=DataRouts)


@router.post('/ldap-auth', response_model=routeBase.appResponse, **routeBase.base_response_parm)
async def ldap_authen(requestinfo: serializer.ldap_request, Authorize: AuthJWT = Depends()):
    Authorize.jwt_required()
    proc = routeBase.PROCRoute(requestinfo)
    request_value = proc.get_request()
    username = request_value.get('username')
    password = request_value.get('password')
    ldap_cls = authLDAP(user=username, pwd=password)
    ldap_rc = ldap_cls.authen()
    result = {"status":ldap_rc}
    if not ldap_rc:
        result['error'] = ldap_cls.error
    proc.set_response('response|result', result)
    return proc.get_response()
