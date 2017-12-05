# read in the data
with open("five", "r") as f:
	data = f.read()

# put all jumps in a list
jumps = []
for jump in data.split('\n'):
	if len(jump) > 0:
		jumps.append(int(jump))

#
#	Part 1
#

def part1(jumps):
	# tracks the number of jumps taken
	stepCount = 0

	# while still within the list of jumps,
	index = 0
	while index < len(jumps):
		# get the jump, ++ the old jump, jump, increase stepCount
		jump = jumps[index]
		jumps[index] += 1
		index += jump
		stepCount += 1
	
	# print result
	print(stepCount)

# make sure to send in a copy of the list of jumps, due to the way it's passed by reference
part1(list(jumps))

#
#	Part 2
#

def part2(jumps):
	# track the number of jumps taken
	stepCount = 0

	# while still within the list of jumps,
	index = 0
	while index < len(jumps):
		# get the jump, modify the old jump, jump, increase stepCount
		jump = jumps[index]
		jumps[index] += 1 if jump < 3 else -1
		index += jump
		stepCount += 1
	
	# print results
	print(stepCount)

# make sure to send in a copy of the list of jumps, due to the way it's passed by reference
part2(list(jumps))
