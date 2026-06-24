from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒 Tienda"),
            KeyboardButton(text="💰 Billetera")
        ],
        [
            KeyboardButton(text="💳 Recargar"),
            KeyboardButton(text="📦 Mis Pedidos")
        ],
        [
            KeyboardButton(text="👤 Perfil"),
            KeyboardButton(text="📞 Soporte")
        ]
    ],
    resize_keyboard=True
)
