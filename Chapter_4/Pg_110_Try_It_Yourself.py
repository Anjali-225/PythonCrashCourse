#4-3
for value in range(1, 21):
	print(value)

print("")

#4-4
million = list(range(1, 1_000_001))
#print(million)
#for millions in million:
	#print(millions)

print("")

#4-5
print(min(million))
print(max(million))
print(sum(million))

print("")

#4-6
odd = list(range(1, 21, 2))
print(odd)

print("")

for oddNum in odd:
	print(oddNum)

print("")

#4-7
multiples = [value*3 for value in range(1, 31)]
print(multiples)

print("")

for multiple in multiples:
	print(multiple)

print("")

#4-8
Cube = []
for value in range(1, 11): 
	Cube.append(value ** 3)
print(Cube)

print("")

for Cubex in Cube:
	print(Cubex)

print("")

#4-9
cubes = [value**3 for value in range(1, 11)]
print(cubes)

print("")

for cub in cubes:
	print(cub)

print("")