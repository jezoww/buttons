from asyncio import *
from os import getenv
from aiogram import *
from aiogram.filters import Command
from aiogram.types import Message, BotCommand
from dotenv import load_dotenv

from buttons import location_contact_buttons
from functions import *

load_dotenv()

TOKEN = getenv('BOT_TOKEN')

dp = Dispatcher()


async def main(dp):
    bot = Bot(token=TOKEN)
    await bot.set_my_commands(
        [
            BotCommand(command="/start", description="Start the bot"),
            BotCommand(command="/help", description="Help"),
            BotCommand(command="/info", description="Get info about yourself!"),
            BotCommand(command="/share", description="Share contact or location")
        ]
    )

    dp.startup.register(start)
    dp.message.register(start_menu, Command("start"))
    dp.message.register(location_contact_buttons, Command("share"))
    dp.message.register(bot_start, Command("start"))
    dp.message.register(help, Command("help"))
    dp.message.register(info, Command("info"))
    dp.shutdown.register(stop)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main(dp))

