# given input
input = 289326

#
#	Part 1
#

# object to represent the experimental new type of memory
class Onion (object):
	layer = 0
	smallestIndex = 1

	# returns the number of indices within the given layer
	def getLayerSize (self):
		return self.layer * 8 if self.layer > 0 else 1

	# returns the largest index found within the given layer
	def getLargestIndex (self):
		return self.getLayerSize() + self.smallestIndex - 1 if self.getLayerSize() > 1 else self.smallestIndex

	# returns the inner side length of the onion (discluding corners)
	def getSideLength (self):
		return int((self.getLayerSize() - 4) / 4)

	# moves to the next layer
	def nextLayer (self):
		self.smallestIndex = self.getLargestIndex() + 1
		self.layer += 1

	# prints string representation of an Onion instance
	def toString (self):
		print("layer", self.layer, "smallestIndex", self.smallestIndex, "largestIndex", self.getLargestIndex(), "size", self.getLayerSize())

# returns the Manhattan Distance (taxi geometry) of the given index within the Onion
def getManhattanDistance (index, onion):
	# get the Onion instance's layer's minimum index's 'x,y' coordinate (how does one English...)
	x = onion.layer
	y = (onion.layer - 1) * -1 if onion.smallestIndex > 2 else 0
	sideLength = onion.getSideLength()

	# start at the smallest index within the Onion instance's current layer,
	# then move through the layer until you find the correct index (using an 'x,y' coordinate)
	currentIndex = onion.smallestIndex

	# check right-wall indices
	for i in range(sideLength):
		if index == currentIndex:
			return abs(x) + abs(y)
		else:
			currentIndex += 1
			y += 1

	# check top-wall indices
	for i in range(sideLength + 1):
		if index == currentIndex:
			return abs(x) + abs(y)
		else:
			currentIndex += 1
			x -= 1
	
	# check left-wall indices
	for i in range(sideLength + 1):
		if index == currentIndex:
			return abs(x) + abs(y)
		else:
			currentIndex += 1
			y -= 1
	
	# check bottom-wall indices
	for i in range(sideLength + 1):
		if index == currentIndex:
			return abs(x) + abs(y)
		else:
			currentIndex += 1
			x += 1

def part1 (index):
	onion = Onion()

	# find which layer the index is on
	while index > onion.getLargestIndex():
		onion.nextLayer()

	# find the given index within the layer, as represented by an 'x,y' coordinate
	return getManhattanDistance(index, onion)

distance = part1(input)
print(distance)

#
#	Part 2
#

# returns the memory's key given a Cartesian coordinate
def getKey (x, y):
	return str(x) + "|" + str(y)

# writes the sum of all surrounding memory units (that have been written already) into the memory at the given Cartesian coordinate
# returns the sum
def write (memory, x, y):
	sum = 0

	sum += memory.get(getKey(x, y+1), 0)	# above
	sum += memory.get(getKey(x, y-1), 0)	# below
	sum += memory.get(getKey(x-1, y), 0)	# left
	sum += memory.get(getKey(x+1, y), 0)	# right

	sum += memory.get(getKey(x-1, y+1), 0)	# top-left
	sum += memory.get(getKey(x+1, y+1), 0)	# top-right
	sum += memory.get(getKey(x-1, y-1), 0)	# bottom-left
	sum += memory.get(getKey(x+1, y-1), 0)	# bottom-right

	memory[getKey(x, y)] = sum

	return sum

def part2 (input):
	# prepare the Onion
	onion = Onion()
	x = y = 0
	currentIndex = 1
	memory = {}

	# handle the first index
	memory[getKey(x,y)] = 1
	x += 1
	onion.nextLayer()

	# handle each layer of the Onion
	while True:
		sideLength = onion.getSideLength()

		# write right-wall values
		for i in range(sideLength):
			if write(memory, x, y) > input:
				return memory[getKey(x,y)]
			y += 1

		# write top-wall values
		for i in range(sideLength + 1):
			if write(memory, x, y) > input:
				return memory[getKey(x,y)]
			x -= 1

		# write left-wall values
		for i in range(sideLength + 1):
			if write(memory, x, y) > input:
				return memory[getKey(x,y)]
			y -= 1

		# write bottom-wall values
		for i in range(sideLength + 2):
			if write(memory, x, y) > input:
				return memory[getKey(x,y)]
			x += 1

		onion.nextLayer()

firstLargerValue = part2(input)
print(firstLargerValue)
