#7-9#No Pastrami------------------------------------------------------
sandwiches_order = ['Cheese and tomato','pastrami', 'Chicken mayo','pastrami', 'Tuna','pastrami']
print("The deli has runn out of pastrami")

while 'pastrami' in sandwiches_order:
	sandwiches_order.remove('pastrami')
print(sandwiches_order)

finished_sandwiches = []

while sandwiches_order:
	order = sandwiches_order.pop()
	finished_sandwiches.append(order)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())

#---------------------------------------------------------------------