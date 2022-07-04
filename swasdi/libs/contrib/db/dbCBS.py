"""
27/04/2018   Jirapong Initial verion
12/03/2020   add execute in cbs
"""

from kaen.contrib.db.cnn.jdbc import connection
from swasdi.settings import DATABASES


class dbCBSCnn:
    cnn = None
    Session = None
    jcnn = None
    cstatmt = None

    def __init__(self, db_section='dbcbs'):
        self.cnn = connection(config=DATABASES.get(db_section, {}))
        self._getJconn()

    def selectDb(self, sqlcmd, fetch=1, **kwargs):
        try:
            # Flush Cache
            if not kwargs: kwargs = {}
            self.cnn.execute(sqlcmd, **kwargs)

            return self._fetch(fetch)
            # if fetch == 1:
            #     dbrc = self.cnn.fetchone()
            # elif fetch > 1:
            #     dbrc = self.cnn.fetchmany(fetch)
            # else:
            #     dbrc = self.cnn.fetchall()
            # return dbrc
        except Exception as e:
            if fetch == 1:
                return None
            else:
                return []

    def executeDb(self, sqlcmd):
        self.cnn.execute(sqlcmd)
        return self._fetch()

    def _fetch(self, fetch=1):
        try:
            if fetch == 1:
                dbrc = self.cnn.fetchone()
            elif fetch > 1:
                dbrc = self.cnn.fetchmany(fetch)
            else:
                dbrc = self.cnn.fetchall()
            return dbrc
        except Exception:
            if fetch == 1:
                return None
            else:
                return []

    def getHeader(self):
        try:
            return self.cnn.rowDefinition()
        except Exception:
            return []

    def _getJconn(self):
        if not self.jcnn:
            self.jcnn = self.cnn.Jconn

    @property
    def Jconn(self):
        self._getJconn()
        return self.jcnn

    def prepareCall(self, msg="{call mrpc(777, ?, ?)}"):
        if msg:
            self.cstatmt = self.jcnn.prepareCall(msg)

    def setString(self, seq=1, parm=''):
        if parm:
            self.cstatmt.setString(seq, parm)

    def registerOutParameter(self, seq=2, types=12):
        self.cstatmt.registerOutParameter(seq, types)

    def jExecuteQuery(self):
        msg_rc = []
        try:
            rs = self.cstatmt.executeQuery()
            while rs.next():
                msg_rc.append(rs.getString(1))
            rc = 0
        except Exception as e:
            rc = -1000
            msg_rc = str(e)

        return rc, msg_rc

    def executeMRPC(self, msg='', parm='', rtnType=12):
        try:
            if not msg: msg = "{call mrpc(777, ?, ?)}"
            self.prepareCall(msg)
            self.setString(1, parm)
            self.registerOutParameter(2, rtnType)
        except Exception as e:
            return -1100, str(e)
        return self.jExecuteQuery()


def selectDb(sqlcmd, fetch=1, **kwargs):
    try:
        db_cnn = dbCBSCnn()
        return db_cnn.selectDb(sqlcmd=sqlcmd, fetch=fetch, **kwargs)
    except Exception as e:
        return None


def executeDb(sqlcmd):
    try:
        db_cnn = dbCBSCnn()
        return db_cnn.executeDb(sqlcmd=sqlcmd)
    except Exception as e:
        return None
