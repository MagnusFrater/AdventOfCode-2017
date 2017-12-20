from collections import deque

INPUT = 366

#
#	Part 1
#

# returns a buffer built with `max` value that `steps` a specified amount
def build_buffer(step, max):
	buffer = [0]
	index = 0
	for i in range(1, max+1):
		index = (index + step) % len(buffer)
		buffer.insert(index + 1, i)
		index += 1
	return buffer, index

# get first value after `max` value in the buffer
def get_value_after_completed_buffer(step, max):
	buffer, index = build_buffer(step, max)
	return buffer[index + 1]

value = get_value_after_completed_buffer(INPUT, 2017)
print(value)

#
#	Part 2
#

# I stole **ahem** 'learned' this method from the subreddit
spinlock = deque([0])

for i in range(1, 50000001):
    spinlock.rotate(-INPUT)
    spinlock.append(i)

print(spinlock[spinlock.index(0) + 1])
