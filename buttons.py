from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="button1")],
        [KeyboardButton(text="button2")]
    ],
    resize_keyboard=True
)

location_contact_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lokatsiyani yuborish", request_location=True),
            KeyboardButton(text="Kontaktni yuborish", request_contact=True)
         ]
    ],
    resize_keyboard=True
)
