# read in all the data
with open('one') as f:
	data = f.readline()

#
#	Part 1
#

# sum of all doubles
sum = 0

# cycle through pairs
i = 0
while i < len(data) - 1:
	# get the next index (wrap on end)
	j = 0 if i == len(data) - 2 else i + 1

	# if equal, sum
	if data[i] == data[j]:
		sum += int(data[i])
	
	i += 1

# print result
print(sum)

#
#	Part 2
#

sum = 0

# cycle through pairs
i = 0
while i < len(data) - 1:
	# get the next index
	half = int((len(data) - 1) / 2)
	j = i + half if i + half < len(data) - 1 else i - half

	# if equal, sum
	if data[i] == data[j]:
		sum += int(data[i])

	i += 1

# print result
print(sum)
