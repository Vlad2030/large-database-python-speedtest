import sqlite3


async def async_make(
        database_location: str, rows: int,
        columns: int, random_data: bool) -> None:
    with sqlite3.connect(database_location) as database:
        cursor: sqlite3.Cursor = database.cursor()
        if random_data:
            pass
        else:
            pass
    return