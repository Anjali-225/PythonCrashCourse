#9-5
class User():
	
	def __init__(self, first_name, last_name, age, username, email):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.username = username
		self.email = email
		self.login_attempts = 0


	def describe_user(self):
		print(f"\n{self.first_name} {self.last_name}")
		print(f"\tAge: {self.age}")
		print(f"\tUsername: {self.username}")
		print(f"\tEmail: {self.email}")

	def greet_user(self):
		"""Personalized greeting to user."""
		print(f"\nHello {self.first_name}!\n")


	def increment_login_attempts(self):
		self.login_attempts += 1
		#print(f"Number of login attempts: {self.login_attempts}")

	def reset_login_attempts(self):
		self.login_attempts = 0
		#print(f"Number of login attempts have been resetted")

#-------------------------------------------------------------------------------
user_1 = User('willie','williams', 26, 'w_williams', 'willie26@gmail.com')

user_1.describe_user()
user_1.greet_user()

print("\nMaking 5 login attempts:")
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print("  Login attempts: " + str(user_1.login_attempts))

print("Login attempts have been resetted")
user_1.reset_login_attempts()
print("  Login attempts: " + str(user_1.login_attempts))

#-------------------------------------------------------------------------------
user_2 = User('josh','kim', 45, 'josh_k', 'josh_k@gmail.com')

user_2.describe_user()
user_2.greet_user()

print("\nMaking 4 login attempts:")
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()

print("  Login attempts: " + str(user_2.login_attempts))

print("Login attempts have been resetted")
user_2.reset_login_attempts()
print("  Login attempts: " + str(user_2.login_attempts))

#-------------------------------------------------------------------------------
user_3 = User('lucia','freddy', 35, 'lu_fred', 'lucia.freddy34@yahoo.com')

user_3.describe_user()
user_3.greet_user()

print("\nMaking 3 login attempts:")
user_3.increment_login_attempts()
user_3.increment_login_attempts()
user_3.increment_login_attempts()

print("  Login attempts: " + str(user_3.login_attempts))

print("Login attempts have been resetted")
user_3.reset_login_attempts()
print("  Login attempts: " + str(user_3.login_attempts))

#-------------------------------------------------------------------------------
user_4 = User('claire','delport', 19, 'delport123Claire', 'delport123Claire@hotmail.com')

user_4.describe_user()
user_4.greet_user()

print("\nMaking 2 login attempts:")
user_4.increment_login_attempts()
user_4.increment_login_attempts()

print("  Login attempts: " + str(user_4.login_attempts))

print("Login attempts have been resetted")
user_4.reset_login_attempts()
print("  Login attempts: " + str(user_4.login_attempts))

#-------------------------------------------------------------------------------
user_5 = User('tonga','right', 65, 'tongaright', 'tonga.right@outlook.com')

user_5.describe_user()
user_5.greet_user()

print("\nMaking 1 login attempts:")
user_5.increment_login_attempts()

print("  Login attempts: " + str(user_5.login_attempts))

print("Login attempts have been resetted")
user_5.reset_login_attempts()
print("  Login attempts: " + str(user_5.login_attempts))

#-------------------------------------------------------------------------------'''