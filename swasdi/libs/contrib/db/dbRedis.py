'''
16/3/2020   Jirapong Initial verion
'''
from kaen.contrib.db.cnn.redis import connection
from swasdi.settings import DATABASES


class dbRedisCnn:
    cnn = None

    def __init__(self, db_section='dbredis'):
        self.cnn = connection(config=DATABASES.get(db_section, {}))
        self.cnn.connect()

    def set(self, name, value, ex=None, px=None, nx=False, xx=False):
        if not self.cnn.isConnect: return
        return self.cnn.set(name, value, ex, px, nx, xx)

    def get(self, name):
        if not self.cnn.isConnect: return
        return self.cnn.get(name)

    def scan(self, pattern):
        if not self.cnn.isConnect: return
        return self.cnn.scan(pattern)

    def delete(self, name):
        if not self.cnn.isConnect: return
        if '*' in name:
            scnLst = self.scan(name)
            try:
                scnLst = scnLst[1]
                for key in scnLst:
                    self.cnn.delete(key)
                return len(scnLst)
            except Exception:
                return 0
        else:
            return self.cnn.delete(name)

    @property
    def redisConnection(self):
        return self.cnn


def redisGet(name):
    rd = dbRedisCnn()
    return rd.get(name)


def redisSet(name, value, ex=None, px=None, nx=False, xx=False):
    rd = dbRedisCnn()
    return rd.set(name, value, ex, px, nx, xx)


def redisClear(name):
    rd = dbRedisCnn()
    return rd.delete(name)
