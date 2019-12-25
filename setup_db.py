import sqlite3
from urllib.request import pathname2url

try:
    db_URI = 'file:{}?mode=rw'.format(pathname2url('ppab6.db'))
    conn = sqlite3.connect(db_URI, uri=True)
    
    # if conn is not None:
    	

except sqlite3.OperationalError:
	# Create table
	conn = sqlite3.connect('ppab6.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE users
	             (username VARCHAR, password_hash VARCHAR)''')
