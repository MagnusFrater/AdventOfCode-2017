# read in the data
with open("PuzzleInputs/08", "r") as f:
	data = f.read()

# instantiates a register if it doesn't exist already
def create_register(registers, *args):
	for reg in args:
		if reg not in registers:
			registers[reg] = 0

# returns the largest value found within any register
def get_largest_register_value(registers):
	largest_value = registers[next(iter(registers))]
	for reg in registers:
		if registers[reg] > largest_value:
			largest_value = registers[reg]
	return largest_value

class Condition():
	'custom Condition data structure'

	def __init__(self, register, inequality, amount):
		self.register = register
		self.inequality = inequality
		self.amount = amount

	# returns True if condition passes, false otherwise
	def passes(self, registers):
		# make sure needed registers exist/are instantiated
		create_register(registers, self.register)

		# handle all inequality permutations :(((((( (there has to be a better way I haven't thought of yet...)
		if self.inequality == ">":
			return True if registers[self.register] > self.amount else False
		if self.inequality == "<":
			return True if registers[self.register] < self.amount else False
		if self.inequality == "==":
			return True if registers[self.register] == self.amount else False
		if self.inequality == "!=":
			return True if registers[self.register] != self.amount else False
		if self.inequality == ">=":
			return True if registers[self.register] >= self.amount else False
		if self.inequality == "<=":
			return True if registers[self.register] <= self.amount else False

	def __str__(self):
		return self.register + " " + self.inequality + " " + self.amount

# register_name inc/dec amount 'if' register_name condition integer
class Instruction():
	'custom Instruction data structure'

	def __init__(self, line):
		parts = line.split()
		self.register = parts[0] 
		self.amount = int(parts[2])
		self.amount *= 1 if parts[1] == "inc" else -1
		self.condition = Condition(parts[4], parts[5], int(parts[6]))

	# executes the instruction if the condition passes
	def run(self, registers):
		if self.condition.passes(registers):
			# make sure needed registers exist/are instantiated
			create_register(registers, self.register)

			# inc/dec register by specified amount
			registers[self.register] += self.amount

	def __str__(self):
		return self.register + " " + str(self.amount) + " if " + self.condition

# parse instructions from raw input
instructions = []
for line in data.split('\n'):
	if len(line) > 0:
		instructions.append(Instruction(line))

#
#	Part 1
#

# infinite (lol) registers all starting at value `0`
registers = {}

# returns the largest value in any register
def part1(instructions, registers):
	# cycle through each instruction
	for instr in instructions:
		# execute the instruction
		instr.run(registers)

	# check each register, find the largest value
	return get_largest_register_value(registers)

largest_register_value = part1(instructions, registers)
print(largest_register_value)

#
# Part 2
#

# same as part 1
registers = {}

# returns the highest value ever held in a register at any point during instruction
def part2(instructions, registers):
	largest_value_ever = 0
	
	# cycle through each instruction
	for instr in instructions:
		# execute the instruction
		instr.run(registers)

		# get current largest value held within the registers
		current_largest_register_value = get_largest_register_value(registers)
		if current_largest_register_value > largest_value_ever:
			# update largest value ever if that's what needed
			largest_value_ever = current_largest_register_value
	
	return largest_value_ever

largest_value_ever = part2(instructions, registers)
print(largest_value_ever)
