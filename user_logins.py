def get_user_input():
	print("\nWelcome! Please sign in:")
	username = str(input("Username: "))
	password = str(input("Password: "))
	return username, password

def is_valid_credentials(username: str, password: str):
	if username == "robert" and password == "password123":
		print("\nmy deepest, darkest secret\n")
	else:
		print("\nget lost\n")


if __name__ == "__main__":
	username, password = get_user_input()
	is_valid_credentials(username, password)
