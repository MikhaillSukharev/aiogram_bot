import re
import aiogram
from loader import dp

@dp.message_handler(regexp=re.compile(pattern='[!/]h+e+l+p+.*', flags=re.IGNORECASE))
async def cmd_help(message: aiogram.types.Message):
    await message.answer("Чем могу помочь?")

@dp.message_handler()
async def acho(message: aiogram.types.Message):
    await message.answer(message.text or message.caption)

