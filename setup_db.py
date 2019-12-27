import os
import sqlite3
from urllib.request import pathname2url

from settings import DATABASE


# TODO: lookup difference between os and pathname2url

def create_table():
	conn = sqlite3.connect(DATABASE)
	c = conn.cursor()
	c.execute('''CREATE TABLE users
	             (username VARCHAR, password_hash VARCHAR)''')

try:
    db_URI = 'file:{}?mode=rw'.format(pathname2url(DATABASE))
    conn = sqlite3.connect(db_URI, uri=True)
    
    if conn is not None:
    	# TODO: get consequences of actions
    	response = str(input("\nDatabase already exists. Do you want to delete it and create a new one (y/n)? ")).lower()
    	while response != "y" and response != "n":
    		 response = str(input("Please respond with a (y)es or a (n)o: ")).lower()
    	
    	if response == "n":
    		exit()
    	else:
    		os.remove(DATABASE)
    		create_table()
except sqlite3.OperationalError:
	create_table()
