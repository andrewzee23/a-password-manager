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
    elif option == "q":
        print(goodbye)
        in_session = False
    elif option == "s":
        print("Let's search for that password")
        search_option = input("What would you like to search by? Website? Username? or Email? \n").lower()
        if search_option == 'website':
            site = input("What's the website? \n")
            result = cur.execute("SELECT * from passwords WHERE website = ?", (site,))
            rows = result.fetchall()
            for row in rows:
                print(row)
        elif search_option == 'username':
            name = input("What's the username you're looking for? \n")
            result = cur.execute("SELECT * from passwords WHERE username = ?", (name,))
            rows = result.fetchall()
            for row in rows:
                print(row)
        elif search_option == 'email':
            email = input("What's the email you're looking for? \n")
            result = cur.execute("SELECT * from passwords WHERE email = ?", (email,))
            rows = result.fetchall()
            for row in rows:
                print(row)
        else:
            print("Sorry, that's not a valid entry. Try again.") 
        second_chance = input("Would you like to keep going? [y]-yes , [n]-no \n").lower()
        if second_chance == "n":
            print(goodbye)
            in_session = False
        else:
            pass
    elif option == "a":
        print("Show me everything")
        result = cur.execute("SELECT * from passwords").fetchall()
        for row in result:
            print(row)
        second_chance = input("Would you like to keep going? [y]-yes , [n]-no \n").lower()
        if second_chance == "n":
            print(goodbye)
            in_session = False
        else:
            pass