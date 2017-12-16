# read in the data
with open("PuzzleInputs/10", "r") as f:
	data = f.read()

#
#	Part 1
#

# returns the `data` input as a list of ints
def get_data_as_ints(data):
	return list(map(int, data.replace('\n', '').split(',')))

# reverses the region specified within `num_list` starting at `index` and ending at `index + length`
def reverse(num_list, index, length):
	# while the length of swaps is greater than 0,
	while length > 0:
		# swap the two values at the left/right edges of the reversal bounds
		temp = num_list[index]
		num_list[index] = num_list[(index + length - 1) % len(num_list)]
		num_list[(index + length - 1) % len(num_list)] = temp

		# move the index inwards by 1, decrease the reversal bounds by 2 (since two numbers got swapped)
		index = (index + 1) % len(num_list)
		length -= 2

# returns the result of a single round of a 'Knot Hash' algorithm
# uses list of ints as lengths, list of values between [0,256), starting index, skip value
def get_hash(lengths, num_list, index, skip):
	# for every length,
	for length in lengths:
		# reverse the reversal region
		reverse(num_list, index, length)

		# update the current index, skip++
		index = (index + length + skip) % len(num_list)
		skip += 1
	
	return num_list, index, skip

# get hash, print out result (first two values multiplied)
hash = get_hash(get_data_as_ints(data), list(range(0,256)), 0, 0)[0]
print(hash[0] * hash[1])

#
#	Part 2
#

# returns a string as a list of ascii values
def get_data_as_ascii(data):
	ascii = []
	for c in data:
		ascii.append(ord(c))
	return ascii

# append extra ascii values as specified in day 10's docs
def add_extra_ascii(ascii):
	ascii.extend([17, 31, 73, 47, 23])

# returns 'dense hash' by XORing 16 sets of 16 ascii values
def get_dense_hash(num_list):
	dense_hash = []
	for i in range(0,16):
		dense_hash.append(num_list[i*16+0] ^ num_list[i*16+1])
		for j in range(0,14):
			dense_hash[i] = dense_hash[i] ^ num_list[i*16+2+j]
	return dense_hash

# returns full 'Knot Hash'
def get_knot_hash(data):
	# turn the string `data` into a list of ints (ascii values), next add extra ints
	lengths = get_data_as_ascii(data.replace('\n', ''))
	add_extra_ascii(lengths)

	# create other needed variables
	num_list = list(range(0,256))
	index = skip = 0

	# create the 'sparse hash' by running the 'knot hash' 64 times
	for i in range(0,64):
		num_list, index, skip = get_hash(lengths, num_list, index, skip)

	# create dense hash
	dense_hash = get_dense_hash(num_list)

	# create final hash, convert each int/ascii to hex, combine into one string
	hex_list = list(map(hex, dense_hash))
	hash = ""
	for h in hex_list:
		h = h.replace('0x', '')
		if len(h) < 2:
			h = '0' + h
		hash += h

	# please work
	return hash

knot_hash = get_knot_hash(data)
print(knot_hash)
