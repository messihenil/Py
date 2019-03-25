class InvalidPasswordException(Exception):
	pass
try:
	password = input("Enter the password: ")
	cnt = len(password);
	if(cnt<=8):
		raise InvalidPasswordException
except InvalidPasswordException:
	print("You have entered invalid input")