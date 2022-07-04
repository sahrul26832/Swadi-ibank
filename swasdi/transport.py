from sqlalchemy.pool import NullPool, QueuePool
from fastapi_sqlalchemy import DBSessionMiddleware
from swasdi.settings import TRANSPORT, ROUTERS
from kaen.transport.wsFast.fastrans import get_application
from kaen.transport.wsFast.routers import get_router
from swasdi.libs.contrib.db import dbCnn

app = get_application(**TRANSPORT)
# app.add_middleware(DBSessionMiddleware, db_url=dbCnn().connection_string,engine_args={"poolclass":NullPool,"pool_recycle":3600},commit_on_exit=True)
app.add_middleware(DBSessionMiddleware,
                   db_url=dbCnn().connection_string,
                   engine_args={"poolclass": QueuePool, "pool_recycle": 180, "pool_pre_ping": True},
                   commit_on_exit=True,)
app.include_router(get_router(ROUTERS), prefix=TRANSPORT.get('api_prefix', '/api'))
