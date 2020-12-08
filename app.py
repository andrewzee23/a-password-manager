import sqlite3
from art import logo, goodbye, success
from sqlite3 import Error

conn = sqlite3.connect('passwords.db')
cur = conn.cursor()
in_session = True

print(logo)
while in_session:
    option = input('What can I help you with? [e]-new entry, [u]-update, [d]-delete [s]-search, [a]-see all, [q]-quit \n').lower()
    if option == "e":
        print("Let's make a new entry")
        website_name = input("What website is it? \n").lower()
        username = input("What's the username? \n")
        email = input("What's the email? \n")
        user_password = input("What's the password? \n")
        data = (website_name, email, username, user_password)
        cur.execute('''INSERT INTO passwords (website, email, username, password) VALUES (?,?,?,?)''', data)
        conn.commit()
        print(success)
        second_chance = input("Would you like to keep going? [y]-yes , [n]-no \n").lower()
        if second_chance == "n":
            print(goodbye)
            in_session = False