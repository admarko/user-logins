import os
import sqlite3
from urllib.request import pathname2url

from settings import DATABASE


def create_table() -> None:
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("CREATE TABLE users (username VARCHAR, password_hash VARCHAR)")


try:
    db_URI = "file:{}?mode=rw".format(pathname2url(DATABASE))
    conn = sqlite3.connect(db_URI, uri=True)

    if conn is not None:
        c = conn.cursor()
        c.execute('SELECT name from sqlite_master where type= "table"')
        tables = [table[0] for table in c.fetchall()]
        print(
            "\nThe database already exists, with the following table{}: ".format(  # noqa
                "s" if len(tables) > 1 else ""
            )
        )

        for table in tables:
            c.execute("SELECT COUNT(*) FROM {}".format(table))
            num_rows = c.fetchone()[0]
            print("-{} ({} rows)".format(table.capitalize(), num_rows))

        response = str(
            input("\nWould you like to delete it and create a new one [y/n]? ")
        ).lower()
        while response != "y" and response != "n":
            response = str(
                input("Please respond with a [y]es or a [n]o: ")
            ).lower()  # noqa

        if response == "n":
            exit()
        else:
            os.remove(DATABASE)
            create_table()
except sqlite3.OperationalError:
    create_table()
