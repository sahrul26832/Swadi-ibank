from acorns.contrib.configYaml import configYaml
# from saphan.apps.appbase.funct.fconfigbase import appConfigAll
from swasdi.settings import CONFIG_FILE


class config_apps(configYaml):
    def __init__(self, cFile="", dbCfg=True):
        super().__init__(cFile)
        # if dbCfg:
        #     self.updateConfig(appConfigAll())

    def updateConfig(self, cfg=None):
        if cfg:
            if self.config:
                self.config.update(cfg)
            else:
                self.config = cfg.copy()


def getconfig_apps(key='', default=None, file='', dbCfg=True):
    if not key:
        return None
    if not file:
        file = CONFIG_FILE
    cfg = config_apps(cFile=file, dbCfg=dbCfg)
    return cfg.get(key, default)