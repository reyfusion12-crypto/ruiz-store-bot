import os
import asyncpg

pool = None

async def connect_db():
global pool

```
pool = await asyncpg.create_pool(
    os.getenv("DATABASE_URL")
)

async with pool.acquire() as conn:

    # Usuarios
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id BIGINT PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        balance NUMERIC DEFAULT 0,
        created_at TIMESTAMP DEFAULT NOW()
    )
    """)

    # Productos
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        price NUMERIC NOT NULL,
        active BOOLEAN DEFAULT TRUE
    )
    """)

    # Pedidos
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS orders(
        id SERIAL PRIMARY KEY,
        user_id BIGINT,
        product_id INTEGER,
        status TEXT DEFAULT 'PENDING',
        delivery_data TEXT,
        created_at TIMESTAMP DEFAULT NOW()
    )
    """)

    # Recargas
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS deposits(
        id SERIAL PRIMARY KEY,
        user_id BIGINT,
        amount NUMERIC,
        method TEXT,
        status TEXT DEFAULT 'PENDING',
        photo_id TEXT,
        created_at TIMESTAMP DEFAULT NOW()
    )
    """)
```

async def create_user(user_id, username, full_name):

```
async with pool.acquire() as conn:

    await conn.execute("""
    INSERT INTO users(
        id,
        username,
        full_name
    )
    VALUES($1,$2,$3)
    ON CONFLICT(id)
    DO NOTHING
    """,
    user_id,
    username,
    full_name
    )
```

async def get_user(user_id):

```
async with pool.acquire() as conn:

    return await conn.fetchrow(
        "SELECT * FROM users WHERE id=$1",
        user_id
    )
```

async def update_balance(user_id, amount):

```
async with pool.acquire() as conn:

    await conn.execute("""
    UPDATE users
    SET balance = balance + $1
    WHERE id = $2
    """,
    amount,
    user_id
    )
```
