#9-12 = Import
from Admin_9_12_Pg_249 import Admin, Privileges

#-------------------------------------------------------------------------------
admin_1 = Admin('willie','williams', 26, 'w_williams', 'willie26@gmail.com')
admin_1.describe_user()

admin_1.privileges.show_privileges()

print("\nAdding Privileges:")

#Filling the variable admin_1_privileges up with a list of privileges
admin_1_privileges =['can add post', 'can delete post', 'can ban user']

admin_1.privileges.privileges = admin_1_privileges

admin_1.privileges.show_privileges()
#-------------------------------------------------------------------------------
admin_2 = Admin('josh','kim', 45, 'josh_k', 'josh_k@gmail.com')
admin_2.describe_user()

admin_2.privileges.show_privileges()

print("\nAdding Privileges:")

#Filling the variable admin_1_privileges up with a list of privileges
admin_2_privileges =['can hack passwords', 'can reset passwords', 'can ban users']

admin_2.privileges.privileges = admin_2_privileges

admin_2.privileges.show_privileges()
#-------------------------------------------------------------------------------
admin_3 = Admin('lucia','freddy', 35, 'lu_fred', 'lucia.freddy34@yahoo.com')
admin_3.describe_user()

admin_3.privileges.show_privileges()

print("\nAdding Privileges:")

#Filling the variable admin_1_privileges up with a list of privileges

admin_3_privileges=['can create apps', 'can delete apps', 'can ban apps']

admin_3.privileges.privileges = admin_3_privileges

admin_3.privileges.show_privileges()
#-------------------------------------------------------------------------------