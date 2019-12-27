from getpass import getpass
import hashlib

from settings import DATABASE


print("\nWelcome! Please make an account:")
username = str(input("Username: "))
password = getpass()
hashed_pw = hashlib.sha256(password.encode()).hexdigest()


conn = sqlite3.connect(DATABASE)
c = conn.cursor()
c.execute('''INSERT INTO users
             VALUES(username, password_hash )''')
c.commit() # check this