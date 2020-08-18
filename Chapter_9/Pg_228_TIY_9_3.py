#9-3
class User():
	
	def __init__(self, first_name, last_name, age, username, email):
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.username = username
		self.email = email

	def describe_user(self):
		print(f"\n{self.first_name} {self.last_name}")
		print(f"\tAge: {self.age}")
		print(f"\tUsername: {self.username}")
		print(f"\tEmail: {self.email}")

	def greet_user(self):
		"""Personalized greeting to user."""
		print(f"\nHello {self.first_name}!\n")
#-------------------------------------------------------------------------------
user_1 = User('willie','williams', 26, 'w_williams', 'willie26@gmail.com')

user_1.describe_user()
user_1.greet_user()
#-------------------------------------------------------------------------------
user_2 = User('josh','kim', 45, 'josh_k', 'josh_k@gmail.com')

user_2.describe_user()
user_2.greet_user()
#-------------------------------------------------------------------------------
user_3 = User('lucia','freddy', 35, 'lu_fred', 'lucia.freddy34@yahoo.com')

user_3.describe_user()
user_3.greet_user()
#-------------------------------------------------------------------------------
user_4 = User('claire','delport', 19, 'delport123Claire', 'delport123Claire@hotmail.com')

user_4.describe_user()
user_4.greet_user()
#-------------------------------------------------------------------------------
user_5 = User('tonga','right', 65, 'tongaright', 'tonga.right@outlook.com')

user_5.describe_user()
user_5.greet_user()
#-------------------------------------------------------------------------------