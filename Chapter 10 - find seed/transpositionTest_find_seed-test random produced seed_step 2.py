# Transposition Cipher Test
# http://inventwithpython.com/hacking (BSD Licensed)
#numpy.arange(1, 5, .5)

import numpy, time, random, sys, transpositionEncrypt, transpositionDecrypt

#startTime = time.time()
#print(startTime)


def main():
	#for whatIsTheSeed in range(100):
	
	# 1 day == 3600 * 24 = 86,400 seconds
	# 1 year == 86,400 * 365 = 31,536,000 seconds
	# 0.5 year == 15,768,000 seconds
	# 13 4941 1356.892



	#for whatIsTheSeed in range(1000000):
	for whatIsTheSeed in numpy.arange(1521332945.739081, 1521332945.754707, 0.000001):
		random.seed(whatIsTheSeed) # set the random "seed" to a static value

		for i in range(1): # run the first test
			# Generate random message to test
			
			# The message will have a random length:
			message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

			# Convert the message string to a list to shuffle it.
			message = list(message)
			random.shuffle(message)
			message = ''.join(message) # convert list to string

			#print('Test #%s: "%s..."' % (i+1, message[:50]))

			#if message[:50] == 'JEQLDFKJZWALCOYACUPLTRRMLWHOBXQNEAWSLGWAGQQSRSIUIQ':
	#		if message[:50] == 'KQDXSFQDBPMMRGXFKCGIQUGWFFLAJIJKFJGSYOSAWGYBGUNTQX':
			if message[:50] == 'NECASAQBRMPEKQQNJJLMMLHPODBSJJYXWMRSGAFODKOECYFIZH':
			# From pdf file on Page 183
			# It might not be clear that
			# 1349411356.892 is Thursday, October 4th, 2012 around 9:30 pm.
				print('Seed founded: ' + str(whatIsTheSeed))
			
			#print(message[:50])		



#			# check all possible keys for each message.
#			for key in range(1, len(message)):
#				encrypted = transpositionEncrypt.encryptMessage(key, message)
#				decrypted = transpositionDecrypt.decryptMessage(key, encrypted)
#
#				# If the decryption doesn't match the original message, display
#				# an error message and quit.
#				if message != decrypted:
#					print('Mismatch with key %s and message %s.' % (key, message))
#					print(decrypted)
#					sys.exit()
#
#		print('Transposition cipher test passed.')


# If transpositionTest.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
	main()

#endTime = time.time()
#print(endTime)


# the output for step 1:
# 1521332945.739081
# NECASAQBRMPEKQQNJJLMMLHPODBSJJYXWMRSGAFODKOECYFIZHKAVVZGVUAXWDMZWHTRYDZTTZCEYBXGSRPJVPFBLQWSKLPHZOCHJFTENYTYGIIHQONWGUMFUXIRAVNVOUUEDRFKLKLGBBXWDPNCIUXISQCT
# 1521332945.754707
# 
# 
# 
# result for step 2:
# nothing found
# program produced seed is not related to time