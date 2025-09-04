from aiogram.filters import Command
from aiogram import Bot, Dispatcher, types
from app.config import env
import logging
from app.database.db_func import DBfunc
from app import config


TOKEN_TG=env["TOKEN"]
bot=Bot(token=TOKEN_TG)
dp = Dispatcher()
db_func=DBfunc(config)

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.reply("Привет! Напиши мне любой вопрос и я на него отвечу")
    logging.info(f" {message.from_user.first_name} write message ({str(message.text)})")

@dp.message()
async def handle_message(message: types.Message):
    try:
        await bot.send_chat_action(message.chat.id, "typing")
        prompt_user= message.text.strip()
        res= await db_func.find_data(prompt_user)
        await message.reply(f" Answer:\n{res}")
        logging.info(f" {message.from_user.first_name} write message ({str(message.text)})")

    except Exception as e:
        await message.reply(f" Error: {str(e)}")




