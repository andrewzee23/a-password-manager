import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('passwords.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS passwords (
    id integer primary key,
    website text not null,
    email text not null,
    username text not null,
    password text not null
);
'''
)
conn.commit()
conn.close()
print("Table created")
