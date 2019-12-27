from getpass import getpass
import hashlib
import sqlite3

from settings import DATABASE


def is_valid_credentials(username: str, password: str, conn) -> bool:
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    c = conn.cursor()
    c.execute(
        "SELECT EXISTS(SELECT 1 FROM users WHERE username = ? AND password_hash = ?)",  # noqa
        (username, hashed_pw),
    )
    return bool(c.fetchone()[0])


if __name__ == "__main__":
    print("\nWelcome! Please sign in:")
    username = str(input("Username: "))
    password = getpass()

    conn = sqlite3.connect(DATABASE)

    if is_valid_credentials(username, password, conn):
        print("\nMy deepest, darkest secret\n")
    else:
        print("\nGet lost\n")
