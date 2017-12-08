# read in the memory banks as a int list
with open("PuzzleInputs/06", "r") as f:
	memory_banks = list(map(int, f.read().split()))

#
#	Part 1
#

# returns the index of the bank with the most blocks
def get_bank_with_most_blocks(memory_banks):
	# track the index of the bank with the most blocks
	bank_with_most_index = 0

	# looping through all banks, check if there is a new bank_with_most
	for i in range(len(memory_banks)):
		if memory_banks[i] > memory_banks[bank_with_most_index]:
			bank_with_most_index = i

	return bank_with_most_index

# returns a string that represents the current state of the memory bank counts
def get_configuration_string(memory_banks):
	configuration = ""

	# basically just build "num_blocks|num_blocks|...|num_blocks"
	for i in range(len(memory_banks) - 1):
		configuration += str(memory_banks[i]) + "|"
	configuration += str(memory_banks[len(memory_banks) - 1])

	return configuration

# returns the number of redistribution cycles that must be completed . . .
# before a configuration is produced that has already been seen
def part1(memory_banks):
	# container for retrieved configurations, cycle counter
	configurations = []
	cycles = 0

	# continue storing configurations until a duplicate is found
	while True:
		# find the bank that currently has the most blocks, pull them from the bank
		bank_with_most_index = get_bank_with_most_blocks(memory_banks)
		blocks_to_redistribute = memory_banks[bank_with_most_index]
		memory_banks[bank_with_most_index] = 0
		
		# find the index of the bank to start redistribution with
		current_bank = bank_with_most_index + 1 if bank_with_most_index + 1 < len(memory_banks) else 0

		# until there are no more blocks to redistribute,
		while blocks_to_redistribute > 0:
			# insert block into current memory bank, find next bank
			memory_banks[current_bank] += 1
			blocks_to_redistribute -= 1
			current_bank = current_bank + 1 if current_bank + 1 < len(memory_banks) else 0
		
		# woot, another cycle done
		cycles += 1

		# if configuration has already been produced return the cycle count, otherwise store new configuration
		configuration = get_configuration_string(memory_banks)
		if configuration in configurations:
			return cycles
		else:
			configurations.append(configuration)

# retrieve cycle count, print result
cycles = part1(memory_banks)
print(cycles)

#
#	Part 2
#

# returns the number of cycles needed to reproduce that first duplicate configuration found in part 1
# assumes parameter `memory_banks` is still in the configuration of part 1's first duplicate configuration
def part2(memory_banks):
	# retrieve the first duplicate configuration left over from part 1
	# container for configurations, loop cycle counter
	first_duplicate_configuration = get_configuration_string(memory_banks)
	configurations = []
	cycle_loop_length = 0

	# continue storing configurations until part 1's duplicate configuration is produced a third time
	while first_duplicate_configuration not in configurations:
		# again, find the bank with the most blocks, pull them from the bank
		bank_with_most_index = get_bank_with_most_blocks(memory_banks)
		blocks_to_redistribute = memory_banks[bank_with_most_index]
		memory_banks[bank_with_most_index] = 0

		# again, find the bank to start redistribution with
		current_bank = bank_with_most_index + 1 if bank_with_most_index + 1 < len(memory_banks) else 0

		# again, until there are no more blocks to redistribute,
		while blocks_to_redistribute > 0:
			# insert block into current memory bank, find next bank
			memory_banks[current_bank] += 1
			blocks_to_redistribute -= 1
			current_bank = current_bank + 1 if current_bank + 1 < len(memory_banks) else 0

		# woot, another cycle done
		cycle_loop_length += 1

		# store configuration
		configurations.append(get_configuration_string(memory_banks))

	return cycle_loop_length

# retrieve cycle loop count, print result
# assume parameter `memory_banks` is still in the configuration of part 1's first duplicate configuration
cycle_loop_length = part2(memory_banks)
print(cycle_loop_length)
