#9-12 = User Module
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