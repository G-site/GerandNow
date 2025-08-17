import aiosqlite


DB_PATH = "database.db"


async def data_create():
    async with aiosqlite.connect(DB_PATH) as db:
        query = """
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tg_id INTEGER NOT NULL,
                username VARCHAR(100) DEFAULT 'Пользователь не имеет Username',
                name VARCHAR(100),
                status TEXT NOT NULL DEFAULT 'User'
            )
        """
        await db.execute(query)
        await db.commit()


async def set_user(tg_id: int, username: str, first_name: str):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT tg_id FROM users WHERE tg_id = ?", (tg_id,))
        result = await cursor.fetchone()
        if result is None:
            await db.execute(
                "INSERT INTO users (tg_id, username, name) VALUES (?, ?, ?)",
                (tg_id, username, first_name)
            )
        await db.commit()


async def get_users():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT tg_id FROM users")
        users = [row[0] for row in await cursor.fetchall()]
        return users


async def check_admin(tg_id):
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT status FROM users WHERE tg_id = ?", (tg_id,))
        result = await cursor.fetchone()
        status = result[0]
        return status
