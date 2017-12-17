# read in the data
with open("PuzzleInputs/13", "r") as f:
	data = f.read()

# turn the raw data into layers (depth : range)
layers = {}
for line in data.replace(':', '').split('\n'):
	if len(line) > 0:
		layers[int(line.split()[0])] = int(line.split()[1])

#
#	Part 1
#

# returns the layers caught on when travelling through the 'friewall', with given delay
def get_caught_layers(layers, delay):
	# find the last layer
	max_layer = max(layers)

	# start in origin state
	picosecond = -1 + delay

	# container for leyrs caught on
	caught_layers = {}

	# move through the firewall
	while picosecond - delay <= max_layer:
		picosecond += 1

		# check if there is a scanner at this layer
		if picosecond - delay in layers:
			length = layers[picosecond - delay] * 2 - 2

			# check if caught
			if picosecond % length == 0:
				caught_layers[picosecond - delay] = layers[picosecond - delay]
	
	return caught_layers

# returns the severity from a given set of layers that you were caught on
def get_severity(caught_layers):
	severity = 0
	for depth in caught_layers:
		severity += depth * caught_layers[depth]
	return severity

severity = get_severity(get_caught_layers(layers, 0))
print(severity)

#
#	Part 2
#

# returns True if the specified delay amount gets you caught, False otherwise
def gets_caught(layers, delay):
	return len(get_caught_layers(layers, delay)) > 0

# returns the smallest number of picoseconds to delay before
# entering the firewall to make it through without getting caught
def get_smallest_delay(layers):
	delay = 0
	while gets_caught(layers, delay):
		delay += 1
	return delay

smallest_delay = get_smallest_delay(layers)
print(smallest_delay)
