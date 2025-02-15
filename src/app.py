# app.py
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.config import Config
from commands.start import register_start_handlers
from commands.schedule import register_schedule_handlers

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=Config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

register_start_handlers(dp)
register_schedule_handlers(dp)

if __name__ == '__main__':
    dp.run_polling(bot)