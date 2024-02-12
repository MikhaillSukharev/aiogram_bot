import aiogram
from config import BOT_TOKEN

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot=bot)
