from kaen.contrib.db.cnn.mysql import connection
from swasdi.settings import DATABASES


class dbCnn(connection):
    def __init__(self, db_section='default'):
        super().__init__(config=DATABASES.get(db_section, {}))
