#7-8#Deli---------------------------------------------------------------------
sandwiches_orders = ['Cheese and tomato', 'Chicken mayo', 'Tuna']
finished_sandwiches = []

while sandwiches_orders:
	order = sandwiches_orders.pop()
	print(f"I made your {order.title()} sandwich")
	finished_sandwiches.append(order)

print("\nThe following sandwiches have been made:")
for finished_sandwich in finished_sandwiches:
	print(finished_sandwich.title())

print("")

#---------------------------------------------------------------------