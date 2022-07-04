from datetime import datetime
from acorns.tools.dictTools import setdictvalue, getdictvalue


class PROCRoute:
    parm_model = None
    parm_dict = {}
    response = {}

    def __init__(self, parm_model=None, **kwargs):
        self.parm_model = parm_model
        if self.parm_model:
            self.parm_dict = parm_model.dict()
            self.response['header'] = self.parm_model.header.dict()
            self.response['header']['request_dt'] = datetime.now()

    def get_request(self, keys='', **kwargs):
        if not keys: return self.parm_dict
        return getdictvalue(self.parm_dict, keys=keys, **kwargs)

    def set_response(self, keys='', value=None):
        if not keys: return
        self.response = setdictvalue(self.response, keys=keys, value=value)

    def get_response(self, keys='', **kwargs):
        if not keys:
            self.response['header']['response_dt'] = datetime.now()
            return self.response
        return getdictvalue(self.response, keys=keys, **kwargs)
