HARDCODED_USERNAME = "robert"
HARDCODED_PASSWORD = "password123"

def is_valid_credentials(username: str, password: str):
	return username == HARDCODED_USERNAME and password == HARDCODED_PASSWORD
		

if __name__ == "__main__":
	print("\nWelcome! Please sign in:")
	username = str(input("Username: "))
	password = str(input("Password: "))

	if is_valid_credentials(username, password):
		print("\nmy deepest, darkest secret\n")
	else:
		print("\nget lost\n")
