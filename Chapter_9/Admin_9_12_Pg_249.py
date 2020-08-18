#9-12 = Admin and Privileges Module
from User_9_12_pg_249 import User
#-------------------------------------------------------------------------------

class Admin(User):

	def __init__(self, first_name, last_name, age, username, email):
		super().__init__(first_name, last_name, age, username, email)
		#self.privileges = []
		self.privileges = Privileges()
			
#-------------------------------------------------------------------------------
class Privileges:

	def __init__(self, privileges = []):
		self.privileges = privileges

	def show_privileges(self):
			#Display the flavours that are available
			print("\nPrivileges: ")
			if self.privileges:
				for privilege in self.privileges:
					print(f"- {privilege}")
			else:
				print('This user has no privileges')
#-------------------------------------------------------------------------------