from getpass import getpass
import hashlib
import sqlite3

from settings import DATABASE


def is_valid_credentials(username: str, password: str) -> bool:
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    hashed_pw = hashlib.sha256(password.encode()).hexdigest()

    c.execute(
        "SELECT EXISTS(SELECT 1 FROM users WHERE username = ? AND password_hash = ?)",  # noqa
        (username, hashed_pw),
    )
    return bool(c.fetchone()[0])


if __name__ == "__main__":
    print("\nWelcome! Please sign in:")
    username = str(input("Username: "))
    password = getpass()

    if is_valid_credentials(username, password):
        print("\nMy deepest, darkest secret\n")
    else:
        print("\nGet lost\n")
