import asyncpg


class PostgreDB:
    def __init__(self, config):
        self.pool=None
        self.db_name = config.DBNAME
        self.user_db = config.USER
        self.password_db = config.PASSWORD
        self.host_db = config.HOST
        self.port_db = config.PORT


    async def create_pool(self):

        self.pool=await asyncpg.create_pool(port=self.port_db, user=self.user_db, database=self.db_name, password=self.password_db,
                                     host=self.host_db)


