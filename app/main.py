from app.tg.tg_func import dp,bot
import asyncio
from app.utils.logger import set_log


set_log()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())