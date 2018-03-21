# Makes the wordPatterns.py File
# http://inventwithpython.com/hacking (BSD Licensed)

# Creates wordPatterns.py based on the words in our dictionary
# text file, dictionary.txt. (Download this file from
# http://invpy.com/dictionary.txt)

import pprint


def getWordPattern(word):
	# Returns a string of the pattern form of the given word.
	# e.g. '0.1.2.3.4.1.2.3.5.6' for 'DUSTBUSTER'