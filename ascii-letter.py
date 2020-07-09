letter = 'A'
numLetter = ord(letter)
x = 1
while x < 27:
	print(letter, '==', numLetter)
	letter = chr(ord(letter) + 1)
	numLetter = ord(letter)
	x = x + 1

lowLetter = 'a'
lowNumLetter = ord(lowLetter)
x = 1
while x < 27:
	print(lowLetter, '==', lowNumLetter)
	lowLetter = chr(ord(lowLetter) + 1)
	lowNumLetter = ord(lowLetter)
	x = x + 1
