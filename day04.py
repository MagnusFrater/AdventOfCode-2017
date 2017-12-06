#read in the data
with open("04") as f:
	data = f.read()

#
#	Part 1
#

# returns True if passphrase is valid, false otherwise
def areDuplicates (passphrase):
	# container for used up space-separated strings
	usedWords = []

	# separate passphrase by spaces
	for word in passphrase.split(' '):
		# if word used, return not valid, else track new word
		if word in usedWords:
			return False
		
		usedWords.append(word)

	# all individual space-separated strings were unique
	return True

def part1 (data):
	validPassphraseCount = 0

	# check data line by line
	for line in data.split('\n'):
		if len(line) > 0:
			validPassphraseCount += 1 if areDuplicates(line) else 0
	
	print(validPassphraseCount)

part1(data)

#
#	Part 2
#

# returns True if given passphrase contains anagrams, false otherwise
def hasAnagrams (passphrase):
	# container for used up sorted words
	usedSortedWords = []

	# split the passphrase on spaces
	for word in passphrase.split(' '):
		# sort all the letters in the word alphabetically
		sortedWord = ''.join(sorted(word))

		# return True if the sorted word has been used already
		if sortedWord in usedSortedWords:
			return True

		# else, track new sorted word
		usedSortedWords.append(sortedWord)

	# no sorted word duplicates were found
	return False

def part2 (data):
	validPassphraseCount = 0

	# check data line by line
	for line in data.split('\n'):
		if len(line) > 0:
			validPassphraseCount += 0 if hasAnagrams(line) else 1
	
	print(validPassphraseCount)

part2(data)
