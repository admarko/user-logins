from getpass import getpass
import hashlib
import sqlite3

from settings import DATABASE


print("\nWelcome! Please make an account:")
username = str(input("Username: "))
password = getpass()
hashed_pw = hashlib.sha256(password.encode()).hexdigest()


conn = sqlite3.connect(DATABASE)
c = conn.cursor()
params = (username, hashed_pw)
c.execute("INSERT INTO users VALUES(?, ?)", params)

conn.commit()
