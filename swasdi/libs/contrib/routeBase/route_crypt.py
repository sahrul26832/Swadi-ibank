from fastapi import HTTPException
from kaen.route.contrib.api_route import CryptLogRoute
from swasdi.libs.contrib.configapp import getconfig_apps


class DataRouts(CryptLogRoute):
    list_key = []
    encrypt_mode = getconfig_apps("encrypt_mode")
    log_mode = getconfig_apps("log_mode")
    data_request_key = "request"
    data_response_key = "response"

    def route_secret_key(self):
        route_agent = self.get_route_agent()
        keys = getconfig_apps("keyheader|{}".format(route_agent))
        if keys is None:
            raise HTTPException(status_code=500, detail="Invalid Route-Agent headers")
        return keys
