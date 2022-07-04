from pydantic import BaseModel, Field
from swasdi.libs.contrib.routeBase import appHeader


class ldap_request(BaseModel):
    header: appHeader = Field(title='Application header')
    username: str = Field(title='User name')
    password: str = Field(title='Password')
