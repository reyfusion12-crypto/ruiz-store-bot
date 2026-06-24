import asyncpg
from config import DATABASE_URL

pool = None


async def connect_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id BIGINT PRIMARY KEY,
            username TEXT,
            full_name TEXT,
            balance NUMERIC DEFAULT 0
        )
        """)

        await conn.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id SERIAL PRIMARY KEY,
            name TEXT,
            price NUMERIC,
            description TEXT
        )
        """)


async def create_user(user_id, username, full_name):
    async with pool.acquire() as conn:
        await conn.execute("""
        INSERT INTO users(id, username, full_name)
        VALUES($1,$2,$3)
        ON CONFLICT(id) DO NOTHING
        """, user_id, username, full_name)


async def get_user(user_id):
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE id=$1",
            user_id
        )


async def get_products():
    async with pool.acquire() as conn:
        return await conn.fetch("SELECT * FROM products ORDER BY id")
