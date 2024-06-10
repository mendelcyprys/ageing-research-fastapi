import sqlite3

DB_PATH = "data/data.db"

create_table = """CREATE TABLE IF NOT EXISTS posts (
    slug TEXT PRIMARY KEY NOT NULL,
    title TEXT,
    introduction TEXT,
    content TEXT,
    thumbnail BLOB,
    image BLOB,
    year INTEGER,
    publish_date TEXT
)"""

def db_init():
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()
    cursor.execute(create_table)
    connection.commit()
    connection.close()
