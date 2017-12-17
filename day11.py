# read in data
with open("PuzzleInputs/11", "r") as f:
	data = f.read()

path = data.replace('\n', '').split(',')

#
#	Part 1
#

class Coordinate():
	'3-dimensional coordinate data structure'

	def __init__(self):
		self.x = 0
		self.y = 0
		self.z = 0
	
	# resets the coordinate to specified values
	def set(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	# moves the coordinate by the specified values
	def move(self, dX, dY, dZ):
		self.x += dX
		self.y += dY
		self.z += dZ

	def __str__(self):
		return str(self.x) + " " + str(self.y) + " " + str(self.z)

class Hexagon():
	'hexagon data structure'

	def __init__(self):
		self.coord = Coordinate()
	
	# updates the coordinates depending on the direction given
	def move(self, direction):
		if direction == 'n':
			self.coord.move(0, 1, -1)
		if direction == 'ne':
			self.coord.move(1, 0, -1)
		if direction == 'se':
			self.coord.move(1, -1, 0)
		if direction == 's':
			self.coord.move(0, -1, 1)
		if direction == 'sw':
			self.coord.move(-1, 0, 1)
		if direction == 'nw':
			self.coord.move(-1, 1, 0)

	# returns the distance between itself and a different hexagon
	def distance(self, h):
		return max(abs(self.coord.x - h.coord.x), abs(self.coord.y - h.coord.y), abs(self.coord.z - h.coord.z))

	def __str__(self):
		return self.coord.__str__()

# returns the fewest steps needed to get from the origin to the hexagon at the end of the path
def get_fewest_steps(path):
	center = Hexagon()
	end = Hexagon()

	# move the hexagon to the end of the path
	for direction in path:
		end.move(direction)

	return center.distance(end)

fewest_steps = get_fewest_steps(path)
print(fewest_steps)

#
#	Part 2
#

# returns the furthest distance the path reaches from the origin hexagon
def get_furthest_distance(path):
	center = Hexagon()
	end = Hexagon()

	furthest_distance = center.distance(end)

	# move the end hexagon along the path
	for direction in path:
		end.move(direction)

		# check to see if the new distance is the new furthest distance
		distance = center.distance(end)
		if distance > furthest_distance:
			furthest_distance = distance
	
	return furthest_distance

furthest_distance = get_furthest_distance(path)
print(furthest_distance)
