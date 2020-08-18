#8-11

def show_messages(show, sent):

	for current_message in show:
		print(f"Message: {current_message}")
		sent.append(current_message)
		

def sent_messages(sent_mess):
	print("\nThe following messages have been sent:")
	for sent in sent_mess:
		print(sent)

show_message = ['Hey!', 'Thanx!', 'C U 2morrow!']
sent_message = []

show_messages(show_message, sent_message)
sent_messages(sent_message)

print(f"\n{show_message}")

print(f"\n{sent_message}")

#------------------------------------------------------------------------
###*****THIS DID NOT WORK****###
'''
#8-11

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