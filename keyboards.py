from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👤 Perfil")],
        [KeyboardButton(text="🛒 Tienda")],
        [KeyboardButton(text="💳 Recargar")],
        [KeyboardButton(text="💰 Billetera")]
    ],
    resize_keyboard=True
)
