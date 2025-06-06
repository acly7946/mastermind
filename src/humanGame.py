from util import *

def game(args):
	pegs = args.pegs
	colors = args.colors
	guesses = args.guesses
	board = initBoard(pegs, guesses)
	hints = initHints(pegs, guesses)

	for guessNum in range(guesses):
		guess = inputGuess(pegs, colors)
		hint = inputHint(pegs)
		board[guessNum] = guess
		hints[guessNum] = hint
		printBoard(board, hints)
		if hint == ['X', 'X', 'X', 'X']:
			win = True
			break

	if win:
		print("You win!")
	else:
		print("You lose.")
