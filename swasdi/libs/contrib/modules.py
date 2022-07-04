from acorns.contrib.modules import module_loader
from swasdi import settings

def get_class_module(pack_name='', class_name=''):
    if not pack_name: return
    try:
        appset = getattr(settings, pack_name)
    except Exception:
        return

    if not appset: return
    sts, rc_cls = module_loader(appset, class_name)
    if sts != 0: return
    return rc_cls
