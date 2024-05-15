import json
from util import *

def game(args):
	level = 1
	while(True):
		data = loadLevel(level)
		pegs = data.get("pegs")
		colors = data.get("colors")
		guesses = data.get("guesses")
		code = data.get("code")
		board = initBoard(pegs, guesses)
		hints = initHints(pegs, guesses)
		win = False

		printLevelInfo(data)
		for guessNum in range(guesses):
			guess = inputGuess(pegs, colors)
			board[guessNum] = guess
			hints[guessNum] = evaluateGuess(pegs, code, guess)
			printBoard(board, hints)
			if guess == code:
				win = True
				break

		if win:
			print("You win! Next Level! \n")
			level += 1
		else:
			print(f"You lose. The code was: {str(code).strip('[]').replace(' ', '')}")

def loadLevel(level):
	"""
	Load level
	"""
	with open(f"data/{level}.json", 'r') as f:
		data = json.load(f)
	validateLevel(data)
	return data

def validateLevel(data):
	"""
	Validate level data

	Example:
	{
		"level": int,
		"colors": int,
		"pegs": int,
		"guesses": int,
		"code": list(int)
	}

	Order of keys does not matter
	"""
	if not data.get("level"):
		raise ValueError("Level data must have a level key")
	if not data.get("colors"):
		raise ValueError("Level data must have a colors key")
	if not data.get("pegs"):
		raise ValueError("Level data must have a pegs key")
	if not data.get("guesses"):
		raise ValueError("Level data must have a guesses key")
	if not data.get("code"):
		raise ValueError("Level data must have a code key")
	if len(data.get("code")) != data.get("pegs"):
		raise ValueError("Code must have the same number of pegs as the level")

def printLevelInfo(data):
	"""
	Print level information
	"""
	print(f"Level: {data.get('level')}")
	print(f"Colors: {data.get('colors')}")
	print(f"Pegs: {data.get('pegs')}")
	print(f"Guesses: {data.get('guesses')}")
	print()