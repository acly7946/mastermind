import json
from util import *

def game(args):
	data = loadLevel(1)
	pegs = data.get("pegs")
	colors = data.get("colors")
	guesses = data.get("guesses")
	code = data.get("code")
	board = initBoard(pegs, guesses)
	hints = initHints(pegs, guesses)

	printLevelInfo(data)
	for guessNum in range(guesses):
		guess = inputGuess(pegs, colors)
		board[guessNum] = guess
		hints[guessNum] = evaluateGuess(pegs, code, guess)
		printBoard(board, hints)
		if guess == code:
			print("You win!")
			quit()

	print(f"You lose. The code was: {str(code).strip('[]').replace(' ', '')}")

def loadLevel(level):
	"""
	Load level
	"""
	with open(f"data/{level}.json", 'r') as f:
		data = json.load(f)
	return data

def printLevelInfo(data):
	"""
	Print level information
	"""
	print(f"Level: {data.get('level')}")
	print(f"Colors: {data.get('colors')}")
	print(f"Pegs: {data.get('pegs')}")
	print(f"Guesses: {data.get('guesses')}")
	print()