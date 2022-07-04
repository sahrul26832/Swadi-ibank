from sqlalchemy.orm import sessionmaker
from fastapi_sqlalchemy import db
from .dbInit import dbCnn


def get_dbsession(stype='web'):
    try:
        if stype == 'web': return getattr(db, 'session')
    except Exception:
        pass

    cnn = dbCnn()
    cnn.connect()
    db_session = sessionmaker(bind=cnn.engine)
    return db_session()


def get_dbconnection():
    try:
        db_session = getattr(db, 'session')
        return db_session
    except Exception:
        cnn = dbCnn()
        cnn.connect()
        return cnn


def selectDb(sqlcmd, fetch=1, flush=1, **kwargs):
    db_session = get_dbsession(stype='web')
    try:
        # Flush Cache
        if flush == 1:
            sql_flush = "FLUSH QUERY CACHE"
            db_session.execute(sql_flush)

        if fetch > 1:
            sqlcmd = sqlcmd + " LIMIT " + str(fetch)

        cursor = db_session.execute(sqlcmd, **kwargs)

        if fetch == 1:
            dbrc = cursor.fetchone()
        else:
            dbrc = cursor.fetchall()
        return dbrc
    except Exception:
        if fetch == 1:
            return None
        else:
            return []


def executeDb(sqlcmd):
    db_cnn = get_dbconnection()
    return db_cnn.execute(sqlcmd)

    # db_session.flush()
    # return db_session.execute(sqlcmd)
