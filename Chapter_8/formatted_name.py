'''
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"\n{first_name} {last_name}"
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=None):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()
while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")


#8-10

def show_messages(show[:], sent):

	while show_message:
		current_message = show_message.pop()
		print(f"Message: {current_message}")
		sent_mess.append(current_message)

def sent_messages(sent_mess):
	print("\nThe following messages have been sent:")
	for sent in sent_mess:
		print(sent)

show_message = ['Hey!', 'Thanx!', 'C U 2morrow!']
sent_mess = []

show_messages(show_message, sent_mess)
sent_messages(sent_mess)

print(f"\n{show_message}")

print(f"\n{sent_message}")
#------------------------------------------------------------------------
'''
def print_models(unprinted_design[:], completed_model):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)