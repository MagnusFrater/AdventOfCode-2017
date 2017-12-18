from day10 import get_data_as_ascii, get_knot_hash
print("(ignore above numbers (from day 10))")

INPUT = "nbysizxe"

#
#	Part 1
#

# returns hexadecimal value in binary
def get_hex_as_binary(hexval):
	# 4 binary digits per 1 hexadecimal digit
	length = len(hexval) * 4
	binary = bin(int(hexval, 16))[2:]

	# add leading (padding) 0's
	while ((len(binary)) < length):
		binary = '0' + binary

	return binary

# returns the number of cells used
def get_used_count(key_string):
	count = 0

	# for each row in disk,
	for i in range(0,128):
		# hash the input, count the 1's	
		hash_input = key_string + "-" + str(i)
		knot_hash = get_knot_hash(get_data_as_ascii(hash_input))
		count += get_hex_as_binary(knot_hash).count("1")
	
	return count

used_count = get_used_count(INPUT)
print(used_count)

#
#	Part 2
#

# returns the disk (128x128 grid)
def generate_disk(key_string):
	disk = []

	# generate each row one by one
	for i in range(0, 128):
		hash_input = key_string + "-" + str(i)
		knot_hash = get_knot_hash(get_data_as_ascii(hash_input))
		disk.append(list(map(int, list(get_hex_as_binary(knot_hash)))))

	return disk

# translates a coordinate into a formatted string - "x:y"
def hash_cell(x, y):
	return str(x) + ":" + str(y)

class DepthFirstSearch2D():
	'custom Depth First Search algorithm for 2d grids'

	def __init__(self, grid, x, y):
		self.visited = []
		self.grid = grid
		self.visit(x, y)
	
	# marks the specified cell as 'visited', then 'visits' all connecting cells
	# connected cells == cells up/down/left/right
	def visit(self, x, y):
		# don't retrace steps
		if hash_cell(x, y) in self.visited:
			return

		# make sure coordinates are within bounds
		if y < 0 or y >= len(self.grid) or x < 0 or x >= len(self.grid[y]):
			return

		# count cell as visited if cell has value of '1', otherwise stop
		if self.grid[y][x] == 1:
			self.visited.append(hash_cell(x, y))
		else:
			return

		# visit all surrounding (up/down/left/right) cells
		self.visit(x-1, y)
		self.visit(x+1, y)
		self.visit(x, y-1)
		self.visit(x, y+1)

# returns the number of regions within the disk
def get_region_count(disk):
	regions = []

	# cycle through every 
	for y in range(0, 128):
		for x in range(0, 128):
			# check if cell is already within a region
			found = False
			cell_hash = hash_cell(x, y)
			for region in regions:
				if cell_hash in region:
					found = True

			# if cell not already found within existing regions,
			if not found:
				# generate it's region
				dfs2d = DepthFirstSearch2D(disk, x, y)

				# only add regions that actually contain cells (lol I'm dumb)
				if len(dfs2d.visited) > 0:
					regions.append(dfs2d.visited)

	return len(regions)

region_count = get_region_count(generate_disk(INPUT))
print(region_count)
