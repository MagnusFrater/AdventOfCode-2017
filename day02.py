import re

#
#	Part 1
#

# read in data
with open("two") as f:
	data = f.read()

sum = 0

# parse the nums line by line
for line in data.split('\n'):
	nums = re.findall('\d+', line)

	# make sure the array isn't empty
	if len(nums) > 0:
		smallest = largest = int(nums[0])

		# get the largest and smllest values in each line
		for num in nums:
			if int(num) < smallest:
				smallest = int(num)
			if int(num) > largest:
				largest = int(num)

		# sum largest/smallest difference
		sum += largest - smallest

# print results
print(sum)

#
#	Part 2
#

sum = 0

# parse the nums line by line
for line in data.split('\n'):
	nums = re.findall('\d+', line)

	# make sure the array isn't empty
	if len(nums) > 0:
		# cycle through all relevant pairs of nums
		i = 0
		while i < len(nums):
			quotient = None

			j = i + 1
			while j < len(nums):
				# get each int
				n1 = int(nums[i])
				n2 = int(nums[j])

				# always modulus/divide largest->smallest
				if n1 > n2 and n1 % n2 == 0:
					quotient = int(n1 / n2)
					break
				if n2 % n1 == 0:
					quotient = int(n2 / n1)
					break

				j += 1
			i += 1

			# sum quotient, if one found (always should be the case)
			if quotient != None:
				sum += quotient

# print result
print(sum)
