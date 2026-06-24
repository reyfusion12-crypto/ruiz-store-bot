import asyncpg
from config import DATABASE_URL

pool = None

async def connect_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

async def create_user(user_id, username, full_name):
    async with pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO users (id, username, full_name, balance)
            VALUES ($1, $2, $3, 0)
            ON CONFLICT (id) DO NOTHING
        """, user_id, username, full_name)

async def get_user(user_id):
    async with pool.acquire() as conn:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE id=$1",
            user_id
        )
