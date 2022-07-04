from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional, Dict


class appHeader(BaseModel):
    sysid: str = Field(title='System ID')
    requestID: str = Field(title='Request ID')
    clientIP: Optional[str] = Field(title='Client ID')


class respHeader(appHeader):
    request_dt: datetime = datetime.now()
    response_dt: datetime = datetime.now()


class appResponse(BaseModel):
    header: respHeader
    response: Optional[Dict] = None
