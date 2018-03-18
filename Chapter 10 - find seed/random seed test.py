import random

random.seed(1.0) # set the random "seed" to a static value
#random.seed(1) # set the random "seed" to a static value

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
			# From pdf file on Page 183
			# It might not be clear that
			# 1349411356.892 is Thursday, October 4th, 2012 around 9:30 pm.
	#			print('Seed founded: ' + str(whatIsTheSeed))
			
	print(message[:50])


# The result is that seed 1 and 1.0 are all the same