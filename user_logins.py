def get_user_input():
	username = str(raw_input("\nUsername: \n"))
	password = str(raw_input("\nPassword: \n"))
	return username, password

def is_valid_credentials(username: str, password: str):
	if username == "robert" and password == "password123":
		print("my deepest, darkest secret")
	else:
		print("get lost")


if __name__ == "__main__":
	username: str, password: str = get_user_input()
	is_valid_credentials(username, password)
