import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)

from db import (
    connect_db,
    create_user,
    get_user,
    get_product_count
)

TOKEN = "8678993710:AAFf84KlsCTbiKd_pVbNbw5NexGxER3sfhc"

ADMINS = [5329713401]

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

    await create_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.full_name
    )

    user = await get_user(
        message.from_user.id
    )

    balance = user["balance"]

    await message.answer(
        f"🛒 Bienvenido a Severino Store\n\n"
        f"💰 Saldo actual: ${balance}\n\n"
        f"Selecciona una opción:",
        reply_markup=main_menu
    )


@dp.message(Command("admin"))
async def admin_panel(message: Message):

    if message.from_user.id not in ADMINS:
        await message.answer(
            "⛔ No tienes acceso a este panel."
        )
        return

    total_products = await get_product_count()

    await message.answer(
        "🛠 Panel Severino Store\n\n"
        f"📦 Productos registrados: {total_products}\n\n"
        "Opciones disponibles:\n"
        "➕ Agregar Producto\n"
        "📦 Ver Productos\n"
        "💰 Ver Recargas\n"
        "📊 Estadísticas"
    )


@dp.message()
async def menu_handler(message: Message):

    if message.text == "👤 Perfil":

        user = await get_user(
            message.from_user.id
        )

        await message.answer(
            f"👤 Perfil\n\n"
            f"🆔 ID: {user['id']}\n"
            f"👤 Nombre: {user['full_name']}\n"
            f"💰 Saldo: ${user['balance']}"
        )

    elif message.text == "💳 Recargar":

        await message.answer(
            "💳 Métodos de pago\n\n"
            "🟡 Binance\n"
            "UID: 584886173\n\n"
            "🏦 Banreservas\n"
            "Tipo: Cuenta de Ahorros\n"
            "Cuenta: 9604451937\n\n"
            "📸 Después de realizar el pago envía el comprobante."
        )

    elif message.text == "🛒 Tienda":

        await message.answer(
            "🛒 Tienda\n\n"
            "Próximamente productos reales."
        )

    elif message.text == "💰 Billetera":

        user = await get_user(
            message.from_user.id
        )

        await message.answer(
            f"💰 Saldo disponible\n\n"
            f"${user['balance']}"
        )

    elif message.text == "📦 Mis Pedidos":

        await message.answer(
            "📦 No tienes pedidos todavía."
        )

    elif message.text == "📞 Soporte":

        await message.answer(
            "📞 Soporte Severino Store\n\n"
            "Contacta al administrador."
        )


async def main():

    await connect_db()

    print("✅ Severino Store iniciada")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
