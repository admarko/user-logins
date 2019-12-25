HARDCODED_USERNAME = "robert"
HARDCODED_PASSWORD = "password123"

logins = {
	HARDCODED_USERNAME: HARDCODED_PASSWORD, 
	"robert_2": "password123_2",
	"robert_3": "password123_3",
}

def is_valid_credentials(username: str, password: str):
	return logins[username] == password
		

if __name__ == "__main__":
	print("\nWelcome! Please sign in:")
	username = str(input("Username: "))
	password = str(input("Password: "))

	if is_valid_credentials(username, password):
		print("\nmy deepest, darkest secret\n")
	else:
		print("\nget lost\n")
