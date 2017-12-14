# read in the data
with open("PuzzleInputs/09", "r") as f:
	data = f.read()

#
#	Part 1
#

# returns the score for the specified sub-group
def get_score(stream, level, index):
	score = level
	in_garbage = False

	# while there are more characters in the stream
	while index < len(stream):
		# start sub-group
		if not in_garbage and stream[index] == '{':
			sub_score, index = get_score(stream, level+1, index+1)
			score += sub_score
			continue

		# end current sub-group
		if not in_garbage and stream[index] == '}':
			return score, index+1

		# garbage start
		if not in_garbage and stream[index] == '<':
			in_garbage = True

		# garbage end
		if in_garbage and stream[index] == '>':
			in_garbage = False

		# ignore
		if in_garbage and stream[index] == '!':
			index += 1

		# next stream character
		index += 1

score = get_score(data, 1, 1)[0]
print(score)

#
#	Part 2
#

def count_garbage(stream, index):
	in_garbage = False
	garbage_count = 0

	#while there are more characters in the stream
	while index < len(stream):
		# start sub-group
		if not in_garbage and stream[index] == '{':
			sub_garbage_count, index = count_garbage(stream, index+1)
			garbage_count += sub_garbage_count
			continue

		# end current sub_group
		if not in_garbage and stream[index] == '}':
			return garbage_count, index+1

		# garbage start
		if  not in_garbage and stream[index] == '<':
			in_garbage = True
			index += 1
			continue

		# garbage end
		if in_garbage and stream[index] == '>':
			in_garbage = False
			index += 1
			continue

		# ignore
		if in_garbage and stream[index] == '!':
			index += 2
			continue

		# only count random characters if `in_garbage`
		if in_garbage:
			garbage_count += 1

		# get next stream character	
		index += 1

garbage_count = count_garbage(data, 1)[0]
print(garbage_count)
