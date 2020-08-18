dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Tuples are like lists constants that can not be changed or modified
#dimensions[0] = 250
print("")

dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

print("")

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)