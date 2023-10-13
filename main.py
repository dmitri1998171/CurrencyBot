import asyncio
import logging
import sys

from module import *

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

TOKEN = "6143261117:AAHR55UQvlPiAqXz7PCAYkkCbAMlrN6YCzA"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!\n\
                           Please, type a currency pair")

@dp.message()
async def echo_handler(message: types.Message) -> None:
    print(message.text)
    try:
        if(len(message.text) > 7):
            await message.answer("Wrong currency pair! Please, type another one")
        else:
            curr_rate = getCurrencyRate(message.text)
            await message.answer(f"{message.text} rate's {curr_rate}")

    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())