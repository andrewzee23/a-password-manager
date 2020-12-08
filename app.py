import sqlite3
from art import logo, goodbye
from sqlite3 import Error

conn = sqlite3.connect('passwords.db')
cur = conn.cursor()
in_session = True