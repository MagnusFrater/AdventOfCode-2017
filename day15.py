# read in the data
with open("PuzzleInputs/15", "r") as f:
	data = f.read()
	gen_a = int(data.split()[4])
	gen_b = int(data.split()[9])

FACTOR_A = 16807
FACTOR_B = 48271
DIVISOR = 2147483647

#
#	Part 1
#

# returns the bit string of an int (long)
def get_bit_string(n):
	return bin(n)[2:].zfill(32)

# returns the number of times the last 16 bits of `gen_a` && `gen_b` match
# `gen_a` prefers numbers that are multiples of `picky_a`; same for `gen_b` and `picky_b`
def get_final_count(gen_a, gen_b, picky_a, picky_b, FACTOR_A, FACTOR_B, DIVISOR, simulations):
	count = 0

	# simulate `simulations` number of times
	for i in range(0, simulations):
		# get `gen_a`s next value
		gen_a = (gen_a * FACTOR_A) % DIVISOR
	
		# make sure `gen_a` is a multiple of `picky_a`
		if picky_a > 0:
			while gen_a % picky_a != 0:
				gen_a = (gen_a * FACTOR_A) % DIVISOR

		# get `gen_b`s next value
		gen_b = (gen_b * FACTOR_B) % DIVISOR

		# make sure `gen_b` is a multiple of `picky_b`
		if picky_b > 0:
			while gen_b % picky_b != 0:
				gen_b = (gen_b * FACTOR_B) % DIVISOR

		# generate their bit strings
		bit_a = get_bit_string(gen_a)
		bit_b = get_bit_string(gen_b)

		count += 1 if bit_a[-16:] == bit_b[-16:] else 0

	return count

final_count = get_final_count(gen_a, gen_b, 0, 0, FACTOR_A, FACTOR_B, DIVISOR, 40000000)
print(final_count)

#
#	Part 2
#

picky_final_count = get_final_count(gen_a, gen_b, 4, 8, FACTOR_A, FACTOR_B, DIVISOR, 5000000)
print(picky_final_count)
