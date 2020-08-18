#9-14
from random import choice

chance = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

lottery_winning_ticket = []

print("Any ticket with the following items pulled is the winner!!")

#for no repeatition i will use a while
while len(lottery_winning_ticket) < 4:
	items_pulled = choice(chance)

	if items_pulled not in lottery_winning_ticket:
		print(f"Item pulled is a {items_pulled}!")
		lottery_winning_ticket.append(items_pulled)

print(f"Ticket with the follow items is the winner" + str(lottery_winning_ticket))

#-----------------------------------------------------------------------------------