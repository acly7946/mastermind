import random

# Initialisation
def generateCode(pegs, colors):
	"""
	Generate random list of pegs integers 1(inclusive) to colors(inclusive)

	0 represents empty peg
	"""
	return [random.choice(range(1, colors + 1)) for _ in range(pegs)]

def initBoard(pegs, guesses):
	"""
	Generate 2D list of size guesses * pegs

	Array is initialized to 0
	"""
	return [[0]*pegs for _ in range(guesses)]

def initHints(pegs, guesses):
	"""
	Generate 2D list of size guesses * pegs

	Array is initialized to -
	"""
	return [['-']*pegs for _ in range(guesses)]


# Input Handling
def inputGuess(pegs, colors):
	"""
	Prompt user until valid guess

	Returns list of integers
	"""
	userInput = input("Guess: ")

	while not isValidGuess(userInput, pegs, colors):
		userInput = input("Invalid guess. Try again: ")
	guess = parseInput(userInput)

	return guess

def isValidGuess(input, pegs, colors):
	"""
	Check if guess is valid

	Example: 1,5,3,7

	Each integer is in the range 1 to colors (inclusive)
	"""
	guess = input.replace(',', '')
	if not guess.isnumeric():
		return False
	if not len(guess) == pegs:
		return False
	if not all([1 <= int(peg) <= colors for peg in guess]):
		return False
	return True

def parseInput(input):
	"""
	Parse input string

	Returns list of integers
	"""
	return [int(peg) for peg in input.replace(',', '')]

def inputHint(pegs, guess):
	"""
	Prompt user until valid hint

	Returns list of characters
	"""
	userInput = input("Hint: ")

	while not isValidHint(userInput, pegs, guess):
		userInput = input("Invalid hint. Try again: ")
	hint = parseHint(userInput)

	return hint

def isValidHint(input, pegs):
	"""
	Check if hint is valid

	Example: X,O,-,-

	Each character is X, O, or -
	"""
	hint = input.replace(',', '')
	if not len(hint) == pegs:
		return False
	if not all([peg in ['X', 'O', '-'] for peg in hint]):
		return False
	return True

def parseHint(input):
	"""
	Parse input string

	Returns list of characters
	"""
	return [peg for peg in input.replace(',', '')]


def evaluateGuess(pegs, code, guess):
	"""
	Check guess against code

	Returns a hint in the form O,X,-,O

	X is correct
	O is correct color wrong position
	- is incorrect
	"""
	hint = []
	for i in range(pegs):
		if guess[i] == code[i]:
			hint.append('X')
		elif guess[i] in code:
			hint.append('O')
		else:
			hint.append('-')
	return hint

def printBoard(board, hints):
	"""
	Print board

	Example:
	1,2,3,4 | -,-,O,-
	2,3,4,5 | -,X,-,-
	"""
	for row in board:
		print(','.join(map(str, row)), end=' | ')
		print(','.join(hints[board.index(row)]))
	print()
