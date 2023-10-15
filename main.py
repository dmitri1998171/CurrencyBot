import asyncio
import logging
import sys

from module import *

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, StateFilter
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.utils.keyboard import ReplyKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class States(StatesGroup):
    startState = State()
    currencyRateState = State()
    forexState = State()


TOKEN = "6143261117:AAHR55UQvlPiAqXz7PCAYkkCbAMlrN6YCzA"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    kb = [
        [types.KeyboardButton(text="Currency rate")],
        [types.KeyboardButton(text="Forex")]
    ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", reply_markup=keyboard)
    await state.set_state(States.startState)

@dp.message(StateFilter(States.currencyRateState))
async def currencyRateGetting(message: Message):
    if(currencyPairValidation(message.text) == False):
            await message.answer("Wrong currency pair! Please, type another one")
    else:
        curr_rate = getCurrencyRate(message.text)
        await message.answer(f"{message.text} rate's {curr_rate}")

@dp.message(StateFilter(States.forexState))
async def forexFunc(message: Message):
    pass

@dp.message()
async def echo_handler(message: types.Message, state: FSMContext) -> None:
    if(message.text == "Currency rate"):
        print("Currency rate button was pressed")
        await state.set_state(States.currencyRateState)
        await message.answer("Please, type a currency pair")

    if(message.text == "Forex"):
        print("Forex button was pressed")
        await state.set_state(States.forexState)

async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())