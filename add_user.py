from getpass import getpass
import hashlib
import sqlite3

from settings import DATABASE, MIN_PASSWORD_LENGTH


# "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
#  ^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$


def is_valid_password(password: str):
    reason = None
    if len(password) < MIN_PASSWORD_LENGTH:
        reason = "Password must be at least 6 characters."

    if reason is None:
        return True
    else:
        print("\n" + reason + " Please try again.")


def get_user_input() -> (str, str):
    username = str(input("Username: "))
    password = getpass()
    hashed_pw = None
    while not is_valid_password(password):
        password = getpass()
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    return username, hashed_pw


print("\nWelcome! Please make an account:")
username, hashed_pw = get_user_input()

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

c.execute("SELECT * FROM users WHERE username = ?", (username,))
matches = c.fetchall()
while len(matches) > 0:
    print("\nUsername already taken. Please retry")
    username, hashed_pw = get_user_input()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    matches = c.fetchall()

params = (username, hashed_pw)
c.execute("INSERT INTO users VALUES(?, ?)", params)
conn.commit()
