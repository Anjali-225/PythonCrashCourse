#8-13
#8-17 This code adheres to the styling functions mentioned in this chapter

def build_profile(first, last, **description):
	"""Build a dictionary containing everything we know about a user."""
	description['first_name'] = first
	description['last_name'] = last
	return description
user_profile = build_profile('Anjali', 'Morar', location='Woodmead', field='coding', studies='Code College')
print(user_profile)

#-----------------------------------------------------------------------------------------------