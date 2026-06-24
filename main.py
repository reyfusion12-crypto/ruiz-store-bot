import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from db import connect_db, create_user, get_user
from keyboards import main_menu

# 🔐 TOKEN DIRECTO EN CÓDIGO
BOT_TOKEN = "8678993710:AAFf84KlsCTbiKd_pVbNbw5NexGxER3sfhc"
DATABASE_URL = postgresql://postgres:YTlrNsmmSAGcZOqZMjlyMGLtIMzEntva@reseau.proxy.rlwy.net:29268/railway

if not BOT_TOKEN or ":" not in BOT_TOKEN:
    raise Exception("❌ Token inválido")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):

    await create_user(
        message.from_user.id,
        message.from_user.username,
        message.from_user.full_name
    )

    user = await get_user(message.from_user.id)

    await message.answer(
        f"🛒 Bienvenido\n\n💰 Saldo: {user['balance']}",
        reply_markup=main_menu
    )


@dp.message()
async def handler(message: Message):

    if not message.text:
        return

    if message.text == "👤 Perfil":
        user = await get_user(message.from_user.id)

        await message.answer(
            f"👤 Perfil\n\nID: {user['id']}\nSaldo: {user['balance']}"
        )

    elif message.text == "💳 Recargar":
        await message.answer("Envía comprobante al admin.")

    elif message.text == "🛒 Tienda":
        await message.answer("Tienda en construcción.")

    elif message.text == "💰 Billetera":
        user = await get_user(message.from_user.id)
        await message.answer(f"Saldo: {user['balance']}")


async def main():
    await connect_db()
    print("✅ Bot iniciado correctamente")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
