#9-7
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
class Admin(User):

	def __init__(self, first_name, last_name, age, username, email):
		super().__init__(first_name, last_name, age, username, email)
		self.privileges = []

	def show_privileges(self):
		#Display the flavours that are available
		print("\nPrivileges: ")
		for privilege in self.privileges:
			print(f"- {privilege}")

#-------------------------------------------------------------------------------
admin_1 = Admin('willie','williams', 26, 'w_williams', 'willie26@gmail.com')
admin_1.describe_user()

admin_1.privileges =['can add post', 'can delete post', 'can ban user']

admin_1.show_privileges()
#-------------------------------------------------------------------------------
admin_2 = Admin('josh','kim', 45, 'josh_k', 'josh_k@gmail.com')
admin_2.describe_user()

admin_2.privileges =['can hack passwords', 'can reset passwords', 'can ban users']

admin_2.show_privileges()
#-------------------------------------------------------------------------------
admin_3 = Admin('lucia','freddy', 35, 'lu_fred', 'lucia.freddy34@yahoo.com')
admin_3.describe_user()

admin_3.privileges =['can create apps', 'can delete apps', 'can ban apps']

admin_3.show_privileges()
#-------------------------------------------------------------------------------