from time import sleep

# read in the data
with open("PuzzleInputs/18", "r") as f:
	data = f.read()

instructions = data.split('\n')
del instructions[len(instructions) - 1]

#
#	Part 1
#

# returns True if specified value is a lowercase letter; False otherwise
def is_register(value):
	possible_registers = []
	for i in range(26):
		possible_registers.append(chr(97 + i))
	return True if value in possible_registers else False

# initializes a register in memory if it doesn't already exist
def init_memory(memory, register):
	if register not in memory:
		memory[register] = 0

# returns the value to set as the 'last emitted sound' (used by 'rcv')
def snd(memory, instruction):
	value = instruction.split()[1]
	print("snd " + value + "->", end="")

	if is_register(value):
		init_memory(memory, value)
		value = memory[value]
	else:
		value = int(value)
	
	print(value)
	return value

# sets a register to the specified value/different register's value
def set(memory, instruction):
	register = instruction.split()[1]
	value = instruction.split()[2]
	print("set " + register + " " + value + "->", end="")

	if is_register(value):
		init_memory(memory, value)
		value = memory[value]
	else:
		value = int(value)
	
	print(value)
	init_memory(memory, register)
	memory[register] = value

# adds to a register the specified value/different register's value
def add(memory, instruction):
	register = instruction.split()[1]
	value = instruction.split()[2]
	print("add " + register + " " + value + "->", end="")

	if is_register(value):
		init_memory(memory, value)
		value = memory[value]
	else:
		value = int(value)
	
	print(value)
	init_memory(memory, register)
	memory[register] = memory[register] + value

# multiples to a register the specified value/different register's value
def mul(memory, instruction):
	register = instruction.split()[1]
	value = instruction.split()[2]
	print("mul " + register + " " + value + "->", end="")

	if is_register(value):
		init_memory(memory, value)
		value = memory[value]
	else:
		value = int(value)

	print(value)
	init_memory(memory, register)
	memory[register] = memory[register] * value

# sets a register to the remainder of itself against the specified value/different register's value
def mod(memory, instruction):
	register = instruction.split()[1]
	value = instruction.split()[2]
	print("mod " + register + " " + value + "->", end="")

	if is_register(value):
		init_memory(memory, value)
		value = memory[value]
	else:
		value = int(value)

	print(value)
	init_memory(memory, register)
	memory[register] = memory[register] % value

# returns True if specified value/register's value isn't 0; False otherwise
def rcv(memory, instruction):
	value = instruction.split()[1]
	print("rcv " + value + "->", end="")

	if is_register(value):
		init_memory(memory, value)
		value = memory[value]
	else:
		value = int(value)

	print(str(value) + " (?) != 0")
	return True if value != 0 else False

# returns True if specified value/register's value is greater than 0; False otherwise
def jgz(memory, instruction):
	value = instruction.split()[1]
	print("jgz " + value + "->", end="")

	if is_register(value):
		init_memory(memory, value)
		value = memory[value]
	else:
		value = int(value)
	
	print(str(value) + " (?) > 0")
	return True if value > 0 else False

# returns the first value received from a successful 'recieve' function
def get_first_receive(instructions):
	memory = {}
	last_sound = -1

	index = 0
	while index < len(instructions):
		instruction = instructions[index]
		command = instruction.split()[0]

		# 'snd X' - play sound
		if command == "snd":
			last_sound = snd(memory, instruction)

		# 'set X Y' - set register value
		if command == "set":
			set(memory, instruction)

		# 'add X Y' - increase register value
		if command == "add":
			add(memory, instruction)

		# 'mul X Y' - multiply register value
		if command == "mul":
			mul(memory, instruction)

		# 'mod X Y' - modulo remainder
		if command == "mod":
			mod(memory, instruction)

		# 'rcv X' - recover last played sound (if X isn't zero)
		if command == "rcv":
			if rcv(memory, instruction):
				print(memory)
				return last_sound

		# 'jgz X Y' - jump (if X is greater than zero)
		if command == "jgz":
			if jgz(memory, instruction):
				value = instruction.split()[2]
				print("jgz " + value + "->", end="")

				if is_register(value):
					init_memory(memory, value)
					value = memory[value]
				else:
					value = int(value)

				print(value)
				index += value

		index += 1
		print(memory, end="")
		print(" " + str(last_sound))
		# sleep(1)

first_receive = get_first_receive(instructions)
print(first_receive)

