import hashlib

logins = {
	"robert": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f", 
	"robert_2": "8551667a4e795fc00a174852ea91307e0b01e39789727aa797db4b9876ee0caf",
	"robert_3": "bbb916176aecee96c293b9af79ebdaeb5f9e2a5805cc0787b0632bf8e6e16d20",
}

def is_valid_credentials(username: str, password: str) -> bool:
	return username in logins and logins[username] == password 

def hash_password(password: str) -> str:
	return hashlib.sha256(password.encode()).hexdigest()


if __name__ == "__main__":
	print("\nWelcome! Please sign in:")
	username = str(input("Username: "))
	password = str(input("Password: "))

	hashed_pw = hash_password(password)

	if is_valid_credentials(username, hashed_pw):
		print("\nmy deepest, darkest secret\n")
	else:
		print("\nget lost\n")
