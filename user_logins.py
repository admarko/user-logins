import hashlib
import json

with open("credentials.json", "r") as creds:
	LOGINS = json.load(creds)

def is_valid_credentials(username: str, password: str) -> bool:
	hashed_pw = hashlib.sha256(password.encode()).hexdigest()
	return username in LOGINS and LOGINS[username] == hashed_pw 


if __name__ == "__main__":
	print("\nWelcome! Please sign in:")
	username = str(input("Username: "))
	password = str(input("Password: "))

	if is_valid_credentials(username, password):
		print("\nmy deepest, darkest secret\n")
	else:
		print("\nget lost\n")
