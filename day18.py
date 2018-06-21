# read in the data
with open("PuzzleInputs/18", "r") as f:
	data = f.read()

instructions = data.split('\n')
del instructions[len(instructions) - 1]
#
#	Part 1
#

def create_memory(

# takes the value, or value at a memory location, and sets it to a different memory location
def set(memory, instruction):
	register = instruction.split()[1]
	value = instruction.split()[2]

	if not value.isnumeric():
		value = memory[value]
	
	memory[register] = value

# returns the first value received from a successful 'recieve' function
def get_first_receive(instructions):
	memory = {}
	
	for instruction in instructions:
		command = instruction.split()[0]

		# 'snd X' - play sound
		if command == "snd":
			continue

		# 'set X Y' - set register value
		if command == "set":
			continue

		# 'add X Y' - increase register value
		if command == "add":
			continue

		# 'mul X Y' - multiply register value
		if command == "mul":
			continue

		# 'mod X Y' - modulo remainder
		if command == "mod":
			continue

		# 'rcv X' - recover last played sound (if X isn't zero)
		if command == "rcv":
			continue

		# 'jgz X Y' - jump (if X is greater than zero)
		if command == "jgz":
			continue

first_receive = get_first_receive(commands)
print(first_receive)
