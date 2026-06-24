import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import (
Message,
ReplyKeyboardMarkup,
KeyboardButton
)
ADMINS = [5329713401]
from db import (
connect_db,
create_user,
get_user
)

TOKEN = os.getenv("BOT_TOKEN")

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

```
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
    f"🛒 Bienvenido a Ruiz Store\n\n"
    f"💰 Saldo actual: ${balance}\n\n"
    f"Selecciona una opción:",
    reply_markup=main_menu
)
```

@dp.message()
async def menu_handler(message: Message):

```
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
        "Binance\n"
        "UID: 123456789\n\n"
        "Transferencia\n"
        "Banco Banreservas\n"
        "Cuenta: XXXXXXXX\n"
        "Titular: Moises Ruiz"
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
        "📞 Soporte Ruiz Store\n\n"
        "Contacta al administrador."
    )
```

async def main():

```
await connect_db()

await dp.start_polling(bot)
```

if **name** == "**main**":
asyncio.run(main())
