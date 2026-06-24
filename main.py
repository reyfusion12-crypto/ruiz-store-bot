import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)

TOKEN = "8678993710:AAFf84KlsCTbiKd_pVbNbw5NexGxER3sfhc"


bot = Bot(token=TOKEN)
dp = Dispatcher()


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


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🛒 Bienvenido a Ruiz Store\n\n"
        "Tu tienda de servicios digitales.\n\n"
        "Selecciona una opción:",
        reply_markup=main_menu
    )


@dp.message()
async def menu_handler(message: Message):

    if message.text == "👤 Perfil":
        await message.answer(
            f"👤 Usuario: @{message.from_user.username}\n"
            f"🆔 ID: {message.from_user.id}\n"
            f"💰 Saldo: $0"
        )

    elif message.text == "📞 Soporte":
        await message.answer(
            "📞 Soporte Ruiz Store\n\n"
            "Escribe directamente al administrador."
        )

    elif message.text == "💳 Recargar":
        await message.answer(
            "💳 Métodos de pago\n\n"
            "Binance\n"
            "UID: 584886173\n\n"
            "Transferencia\n"
            "Banco Banreservas\n"
            "Cuenta: 9604451937\n"
            "Titular: Moises Ruiz"
        )

    elif message.text == "🛒 Tienda":
        await message.answer(
            "🛒 Productos disponibles\n\n"
            "1. ChatGPT Plus - $8\n"
            "2. Canva Pro - $5"
        )

    elif message.text == "💰 Billetera":
        await message.answer(
            "💰 Saldo actual\n\n$0 USD"
        )

    elif message.text == "📦 Mis Pedidos":
        await message.answer(
            "📦 No tienes pedidos todavía."
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
