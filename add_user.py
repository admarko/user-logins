from getpass import getpass
import hashlib
import sqlite3

from settings import DATABASE, MIN_PASSWORD_LENGTH, SPECIAL_CHARS


def check_or_x(truth_value: bool) -> str:
    return u"\u2713" if truth_value else "X"


def is_valid_password(password: str) -> bool:
    has_lower = True
    has_upper = True
    has_number = True
    has_special = True
    has_length = True

    if not any(char.islower() for char in password):
        has_lower = False
    if not any(char.isupper() for char in password):
        has_upper = False
    if not any(char.isdigit() for char in password):
        has_number = False
    if not any(char in SPECIAL_CHARS for char in password):
        has_special = False
    if len(password) < MIN_PASSWORD_LENGTH:
        has_length = False

    if has_lower and has_upper and has_number and has_special and has_length:
        print("Password accepted. Account created!")
        return True
    else:
        print(
            "\nPassword invalid. Your password must have:\n[{}] At least 1 \
            lowercase letter\n[{}] At least 1 uppercase letter\n[{}] At least \
            1 number\n[{}] At least 1 special character\n[{}] Be at least {} \
            characters long. \nPlease try again\n".format(
                check_or_x(has_lower),
                check_or_x(has_upper),
                check_or_x(has_number),
                check_or_x(has_special),
                check_or_x(has_length),
                MIN_PASSWORD_LENGTH,
            )
        )
        return False


def get_user_input() -> (str, str):
    username = str(input("Username: "))
    password = getpass()
    return username, password


print("\nWelcome! Please make an account:")
username, hashed_pw = get_user_input()

conn = sqlite3.connect(DATABASE)
c = conn.cursor()

c.execute("SELECT * FROM users WHERE username = ?", (username,))
matches = c.fetchone()
type(matches)
while matches is not None:
    print("\nUsername already taken. Please retry")
    username, password = get_user_input()
    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    matches = c.fetchone()

while not is_valid_password(password):
    password = getpass()
hashed_pw = hashlib.sha256(password.encode()).hexdigest()

params = (username, hashed_pw)
c.execute("INSERT INTO users VALUES(?, ?)", params)
conn.commit()
