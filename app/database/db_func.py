import logging
from app.ai.func_ai import ask_ai
from app.database.connector import PostgreDB


class DBfunc:
    def __init__(self,config):
        self.config=config
        self.db=PostgreDB(config)

    async def find_data(self,user_message):

        sql_command=f"""SELECT answers FROM data WHERE LOWER(responces)=LOWER($1)"""

        if not self.db.pool:
            await self.db.create_pool()

        async with self.db.pool.acquire() as conn:
                users = await conn.fetchrow(sql_command,user_message)
                if users:
                    logging.info("Success, data find")
                    return users["answers"]
                else: return await self.save_data(user_message)


    async def save_data(self, user_message):

        sql_command = f"""INSERT INTO data (responces,answers) VALUES($1,$2)"""
        ai_response=await ask_ai(user_message)

        if not self.db.pool:
            await self.db.create_pool()

        try:
            async with self.db.pool.acquire() as conn:
                 await conn.execute(sql_command, user_message,ai_response)
                 logging.info("Success, data saved")

            return ai_response
        except IndexError:
            logging.error("Пустой список")
            return None





