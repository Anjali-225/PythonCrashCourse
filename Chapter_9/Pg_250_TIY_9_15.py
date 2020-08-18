#9-15
#THIS IS THE VERSION WHICH COUNTS THE LOOP THING			
#HOWEVER BOTH VERSIONS DO WORK and for the first version I did take help from the internet
#-------------------------------------------------------------------------------
from random import choice

#MAKE A FUNCTION TO GET A TICKET THAT IS THE WINNING TICKET
def winning_ticket(chance):
	lottery_winning_ticket = []

	#FOR NO REPITION USE A WHILE LOOP
	while len(lottery_winning_ticket) < 4:
		items_pulled = choice(chance)
		if items_pulled not in lottery_winning_ticket:
			lottery_winning_ticket.append(items_pulled)

	return lottery_winning_ticket
#-------------------------------------------------------------------------------
#MAKE A FUNCTION TO CHECK IF YOUR TICKET MATCHES THE WINNING TICKET
def check_ticket(played_ticket, lottery_winning_ticket):
	for element in played_ticket:
		if element not in lottery_winning_ticket:
			return False

	#WE MUST GET A WINNING TICKET
	return True 
#-------------------------------------------------------------------------------
#GENERATE A RANDOM TICKET
def generate_ticket(chance):
	ticket = []

	#FOR NO REPITITIONS USE A WHILE
	while len(ticket) < 4:
		items_pulled = choice(chance)
		if items_pulled not in ticket:
			ticket.append(items_pulled)

	return ticket 
#-------------------------------------------------------------------------------
chance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
lottery_winning_ticket = winning_ticket(chance)

plays = 0
won = False

#SET MAX NUMBER OF ATTEMPTS
MAX = 100
#-------------------------------------------------------------------------------
while not won:
	new_ticket = generate_ticket(chance)
	won = check_ticket(new_ticket, lottery_winning_ticket)
	plays += 1
	if plays >= MAX:
		break
#-------------------------------------------------------------------------------
if won:
	print('We found the winning ticket!')
	print(f"Your ticket: {new_ticket}")
	print(f"Winning Ticket: {lottery_winning_ticket}")
	print(f"It took {plays} tries to win!")
else:
	print(f"Tried {plays} times, without pulling a winner.")
	print(f"Your ticket: {new_ticket}")
	print(f"Winning Ticket: {lottery_winning_ticket}")
#-------------------------------------------------------------------------------
#THIS IS THE SOLUTION THAT CHECKS IF YOUR TICKET IS THE SAME AND THE WINNING TICKET
'''
from random import choice

chance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
my_ticket = [1, 5, 6, 'd']

lottery_winning_ticket = []

print("Any ticket with the following items pulled is the winner!!")

#for no repeatition i will use a while
while len(lottery_winning_ticket) < 4:
	items_pulled = choice(chance)

	if items_pulled not in lottery_winning_ticket:
		#print(f"Item pulled is a {items_pulled}!")
		lottery_winning_ticket.append(items_pulled)

for winner in range(100):
	if my_ticket == lottery_winning_ticket:
		print("You are the winner!!!") 
	else:
		print("Better luck next time!")
'''
#-------------------------------------------------------------------------------