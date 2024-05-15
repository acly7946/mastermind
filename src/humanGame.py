from util import *

def game(args):
	pegs = args.pegs
	colors = args.colors
	guesses = args.guesses
	board = initBoard(pegs, guesses)
	hints = initHints(pegs, guesses)

	for guessNum in range(guesses):
		guess = inputGuess(pegs, colors)
		hint = inputHint(pegs, guess)
		board[guessNum] = guess
		hints[guessNum] = hint
		printBoard(board, hints)
		if hint == ['X', 'X', 'X', 'X']:
			print("You win!")
			quit()

	print("You lose.")