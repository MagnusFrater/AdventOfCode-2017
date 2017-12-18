from collections import deque
import re

# read in the data
with open("PuzzleInputs/16", "r") as f:
	data = f.read()

moves = data.replace('\n', '').split(',')

#
#	Part 1
#

# returns a list of all the numbers found within string `s`
def get_all_nums(s):
	return re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", s)

# generates the programs in their initial state
def generate_programs():
	programs = []
	for i in range(0, 16):
		programs.append(chr(97 + i))
	return programs

# makes 'count' programs move from the end to the front, but maintain their order otherwise
def spin(programs, count):
	items = deque(programs)
	items.rotate(count)
	return list(items)

# makes the programs at positions `i` and `j` swap places
def exchange(programs, i, j):
	temp = programs[i]
	programs[i] = programs[j]
	programs[j] = temp

# makes the programs named `a` and `b` swap places
def partner(programs, a, b):
	i = programs.index(a)
	j = programs.index(b)
	exchange(programs, i, j)

# returns the programs' positions at the end of their dance(s)
def dance(moves, dances):
	programs = generate_programs()

	history = []

	# dance FOREVER
	for i in range(0, dances):
		# if dancers were in this position in the past, found dance cycle
		positions = ''.join(programs)
		if positions in history:
			return history[dances % i]
		history.append(positions)

		# haven't had these starting positions before, so do the moves
		for move in moves:
			# spin - "sX"
			if move[:1] == 's':
				programs = spin(programs, int(get_all_nums(move)[0]))
	
			# exchange - "xA/B"
			if move[:1] == 'x':
				nums = get_all_nums(move)
				exchange(programs, int(nums[0]), int(nums[1]))

			# partner - "pA/B"
			if move[:1] == 'p':
				partner(programs, list(move)[1], list(move)[3])
		
	return ''.join(programs)
	
last_dance_position = dance(moves, 1)
print(last_dance_position)

#
#	Part 2
#

# had to make use of memoization to properly solve this - and I shamelessly partook of some Reddit help to do so :P
billion_dances = dance(moves, 1000000000)
print(billion_dances)
