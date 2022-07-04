import os
from acorns.contrib.configYaml import configYaml

CONSOLE_CMD = "swasdi"

APP_ROOT_DIR = os.path.dirname(os.path.abspath(os.path.join(__file__, "..")))
APP_PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = os.getenv('APPS_SETTING_FILE', '')
if not os.path.isfile(CONFIG_FILE): CONFIG_FILE = ''

APPS_CONFIG_PATH = os.getenv('APPS_CONFIG_PATH', '')

if not CONFIG_FILE and APPS_CONFIG_PATH:
    CONFIG_FILE = os.path.join(APPS_CONFIG_PATH, 'setting.yml')
    if not os.path.isfile(CONFIG_FILE): CONFIG_FILE = ''

if not CONFIG_FILE: CONFIG_FILE = os.path.join(APP_ROOT_DIR, 'setting.yml')

cfg = configYaml(CONFIG_FILE)

DATABASES = cfg.get('database')

TRANSPORT = cfg.get('transport')

ROUTERS = [
    ['swasdi.libs.apps.authBase.router', 'authen', '/authen'],
          ] + cfg.get('routers', default=[])

SECRET_KEY = cfg.secret_key
os.environ['secret_key'] = SECRET_KEY

TOKEN_NAME = cfg.get('token_name')

LDAP_CONFIG = cfg.get('ldap')
