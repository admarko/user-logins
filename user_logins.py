import hashlib
import json

logins = {}

def is_valid_credentials(username: str, password: str) -> bool:
	hashed_pw = hashlib.sha256(password.encode()).hexdigest()
	return username in logins and logins[username] == hashed_pw 


if __name__ == "__main__":
	with open("credentials.json", "r") as creds:
		logins = json.load(creds)

	print("\nWelcome! Please sign in:")
	username = str(input("Username: "))
	password = str(input("Password: "))

	if is_valid_credentials(username, password):
		print("\nmy deepest, darkest secret\n")
	else:
		print("\nget lost\n")
