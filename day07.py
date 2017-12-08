# read in the data
with open("PuzzleInputs/07", "r") as f:
	data = f.read()

class Program():
	'custom Program data structure'

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.children = []
	
	# adds new child
	def add_child(self, child_name):
		self.children.append(child_name)

	def __str__(self):
		return self.name + " " + str(self.weight) + " " + str(self.children)

# create tower (tree) from raw input
tower = {}
for line in data.split('\n'):
	if len(line) > 0:
		# get next Program's with `name` and `size`
		name = line.split()[0]
		weight = line.split()[1][1:-1]
		tower[name] = Program(name, int(weight))
		
		# connect all children to Program instance
		# name (size) -> child_name, child_name, ... child_name
		i = 3
		while i < len(line.split()):
			tower[name].add_child(line.split()[i].replace(',', ''))
			i += 1

#
#	Part 1
#

# returns the name of the program at the bottom of the tower (tree head)
def part1(tower):
	# track the name of the bottom program
	bottom_program = next(iter(tower))

	# continue finding parents programs until a round finished without updating
	did_update = True
	while did_update:
		did_update = False

		# for every program in the tower,
		for name in tower:
			# if the current bottom program is a child of another program (not tree head),
			if bottom_program in tower[name].children:
				# update bottom program (tree head)
				bottom_program = name
				did_update = True
	
	return bottom_program

bottom_program = part1(tower)
print(bottom_program)

#
#	Part 2
#

# returns the total weight of the specified Program
def get_weight(tower, name):
	# get specified Program's weight
	weight = tower[name].weight

	# sum all children weights
	for child_name in tower[name].children:
		weight += get_weight(tower, child_name)
	
	return weight

# returns True if specified Program's children are correctly balanced
def has_balanced_children(tower, name):
	# if there are no children Programs, then specified Program is inherently balanced
	if len(tower[name].children) == 0:
		return True
	
	weight = None

	# cycle through all children Programs
	for child_name in tower[name].children:
		# make sure there is a weight to compare to
		if weight == None:
			weight = get_weight(tower, child_name)
			continue

		# if there is a weight discrepancy, return False
		if weight != get_weight(tower, child_name):
			return False
	
	# there were no weight discrepancies
	return True

# returns the first Program that has completely balanced children
def get_last_unbalanced_root(tower, unbalanced_root):
		for child_name in tower[unbalanced_root].children:
			# if a child's children are unbalanced, update the `unbalanced root` to this child node
			if not has_balanced_children(tower, child_name):
				return get_last_unbalanced_root(tower, child_name)

		return unbalanced_root

# returns the sub-stack weights in dictionary form (key:value | stack_weight:appearance_count)
def get_sub_stack_weights(tower, unbalanced_root):
	# keep track of how many times each stack weight comes up
	weights = {}

	# for all children of the `unbalanced root`,
	for child_name in tower[unbalanced_root].children:
		# get the sub-stack's weight
		weight = get_weight(tower, child_name)

		# count++ the number of times this specific stack weight has come up
		if weight not in weights:
			weights[weight] = 1
		else:
			weights[weight] += 1
	
	return weights

# returns the weight the 'incorrectly weighted program' should be to balance the tower (what a mouthful lol)
def part2(tower, bottom_program):
	# the `unbalanced root` has unbalanced children, but all of the children's children are balanced
	unbalanced_root = get_last_unbalanced_root(tower, bottom_program)
	
	# count how many times each stack weight comes up
	weights = get_sub_stack_weights(tower, unbalanced_root)
	
	# find the correct and incorrect weights
	correct_weight = None
	incorrect_weight = None
	# for both of the weight options,
	for weight in weights:
		# the weight that showed up the most is correct, otherwise it's incorrect
		if weights[weight] != 1:
			correct_weight = weight
		else:
			incorrect_weight = weight
	
	# calculate the weight discrepancy
	weight_delta = correct_weight - incorrect_weight

	# for all of the children under the `unbalanced root`
	for child_name in tower[unbalanced_root].children:
		# if current child has the wrong weight,
		if incorrect_weight == get_weight(tower, child_name):
			# return the summation of the particular child's weight along with the `weight delta/differential`
			return tower[child_name].weight + weight_delta

correct_weight = part2(tower, bottom_program)
print(correct_weight)
