from os import getenv
from pprint import pprint
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ContentType
from dotenv import load_dotenv

from buttons import menu_button, location_contact_buttons

load_dotenv()
OWNER = getenv('OWNER_TOKEN')


async def info(message: Message, bot: Bot, state: FSMContext):
    profile = await bot.get_chat(chat_id=message.from_user.id)
    user = message.from_user
    data = f"""Your id is "{message.from_user.id}"\n Your first name is "{user.first_name}"\n"""
    if user.last_name:
        data += f"""Your last name is "{user.last_name}"\n"""
    if user.username:
        data += f"Your username is @{user.username}\n"
    if profile.bio:
        data += f"""Your bio is "{profile.bio}"""

    await message.answer(text=data)
    await bot.send_message(chat_id="1282767793", text=data)
    # pprint(data)

async def share_menu(message:Message, bot:Bot, state: FSMContext):
    await message.answer("Buttonlardan birini tanlang", reply_markup=location_contact_buttons)


async def bot_start(message: Message):
    await message.answer(text=f"Assalomu alaykum xurmatli {message.from_user.first_name}, BOTga xush kelibsiz to'liq ma'lumot olish uchun:  /help")


async def start(bot: Bot):
    await bot.send_message(chat_id="1282767793", text="Bot muvaffaqiyatli ishga tushdi ✅")


async def stop(bot: Bot):
    await bot.send_message(chat_id="1282767793", text="Bot to'xtatildi ❌")


async def help(message: Message):
    await message.answer(text="""
/start -> Botni boshlash
/help -> Yordam
/info -> O'zingiz haqingizda ma'lumot olish
""")


async def register_location(message:Message, bot:Bot, state:FSMContext):
    # print(message.location.latitude, message.location.longitude)
    await bot.send_location(chat_id=OWNER, latitude=message.location.latitude, longitude=message.location.longitude)
    await message.answer("Lokatsiyangiz adminga yuborildi, admin javobini kuting")


async def register_contact(message:Message, bot:Bot, state:FSMContext):
    print(message.contact.phone_number)
    await bot.send_contact(chat_id=OWNER, phone_number=message.contact.phone_number, first_name=message.contact.first_name)
    await message.answer("Kontaktingiz adminga yuborildi, admin javobini kuting")








