from fastapi import APIRouter, Depends
from fastapi_jwt_auth import AuthJWT
from kaen.route.serializer import User, Settings
from swasdi.libs.apps.authBase.funct.fauth import jwtAppAuthen
# from swasdi.libs.apps.funct.fauth import decrypt_login
from swasdi.settings import TOKEN_NAME
router = APIRouter()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.post('/token-login')
async def token_login(user: User, Authorize: AuthJWT = Depends()):
    token = jwtAppAuthen(Authorize=Authorize)
    if TOKEN_NAME:
        token.set_token_name(**TOKEN_NAME)
    return token.login_token(user=user)


@router.post('/token-refresh')
def token_refresh(Authorize: AuthJWT = Depends()):
    token = jwtAppAuthen(Authorize=Authorize)
    if TOKEN_NAME:
        token.set_token_name(**TOKEN_NAME)
    return token.refresh_token()
