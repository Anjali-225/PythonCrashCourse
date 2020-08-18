#3-4
guest = ['Joe','Eric','Sarah','Helly']

message = f"{guest[0]}, you are invited to dinner"
print(message)
message = f"{guest[1]}, you are invited to dinner"
print(message)
message = f"{guest[2]}, you are invited to dinner"
print(message)
message = f"{guest[3]}, you are invited to dinner\n"
print(message)

#3-5
print(f"{guest[1]} can not make it to the dinner\n")

del guest[1]

message = f"{guest[0]}, you are invited to dinner"
print(message)
message = f"{guest[1]}, you are invited to dinner"
print(message)
message = f"{guest[2]}, you are invited to dinner\n"
print(message)

#3-6
guest.insert(0, 'Bob')
guest.insert(2, 'James')
guest.append('Shrek')

message = f"{guest[0]}, you are invited to dinner since we have a bigger table"
print(message)
message = f"{guest[1]}, you are invited to dinner since we have a bigger table"
print(message)
message = f"{guest[2]}, you are invited to dinner since we have a bigger table"
print(message)
message = f"{guest[3]}, you are invited to dinner since we have a bigger table"
print(message)
message = f"{guest[4]}, you are invited to dinner since we have a bigger table"
print(message)
message = f"{guest[5]}, you are invited to dinner since we have a bigger table\n"
print(message)

#3-7
print("We can only add two people for dinner")

popped1 = guest.pop()
print(f"Sorry {popped1}, we can not invite you for dinner anymore")

popped2 = guest.pop()
print(f"Sorry {popped2}, we can not invite you for dinner anymore")

popped3 = guest.pop()
print(f"Sorry {popped3}, we can not invite you for dinner anymore")

popped4 = guest.pop()
print(f"Sorry {popped4}, we can not invite you for dinner anymore\n")

print(f"{guest[0]}, you are still invited for dinner")
print(f"{guest[1]}, you are still invited for dinner\n")

#del guest[1]
#del guest[0]

print(guest)



